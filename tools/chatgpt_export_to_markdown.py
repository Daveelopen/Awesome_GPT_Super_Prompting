#!/usr/bin/env python3
"""Convert a ChatGPT/OpenAI conversations export to readable Markdown files.

Accepts either:
  * a ChatGPT export ZIP containing conversations.json, or
  * conversations.json directly.

Output:
  * 000_INDEX.md with a chronological overview
  * one Markdown file per conversation
  * optional ZIP archive of the Markdown output
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


@dataclass(frozen=True)
class Message:
    create_time: float | None
    role: str
    author_name: str | None
    content: str


@dataclass(frozen=True)
class Conversation:
    title: str
    create_time: float | None
    update_time: float | None
    messages: list[Message]


def load_conversations(source: Path) -> list[dict[str, Any]]:
    if source.is_dir():
        candidate = source / "conversations.json"
        if not candidate.exists():
            raise FileNotFoundError(f"No conversations.json found in directory: {source}")
        return read_json(candidate)

    if source.suffix.lower() == ".zip":
        with zipfile.ZipFile(source) as archive:
            names = archive.namelist()
            matches = [name for name in names if name.endswith("conversations.json")]
            if not matches:
                raise FileNotFoundError("No conversations.json found inside ZIP export")
            with archive.open(matches[0]) as handle:
                return json.load(handle)

    return read_json(source)


def read_json(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, list):
        raise ValueError("Expected conversations.json to contain a JSON list")
    return data


def parse_conversation(raw: dict[str, Any]) -> Conversation:
    title = str(raw.get("title") or "Untitled conversation").strip() or "Untitled conversation"
    mapping = raw.get("mapping") or {}
    if not isinstance(mapping, dict):
        mapping = {}
    messages = extract_messages(mapping)
    create_time = raw.get("create_time") or first_timestamp(messages)
    update_time = raw.get("update_time") or last_timestamp(messages)
    return Conversation(
        title=title,
        create_time=as_float(create_time),
        update_time=as_float(update_time),
        messages=messages,
    )


def extract_messages(mapping: dict[str, Any]) -> list[Message]:
    messages: list[Message] = []
    for node in mapping.values():
        if not isinstance(node, dict):
            continue
        raw_message = node.get("message")
        if not isinstance(raw_message, dict):
            continue
        message = parse_message(raw_message)
        if message is not None:
            messages.append(message)

    return sorted(messages, key=lambda item: (item.create_time is None, item.create_time or 0.0))


def parse_message(raw: dict[str, Any]) -> Message | None:
    author = raw.get("author") or {}
    role = str(author.get("role") or "unknown")
    author_name = author.get("name")
    content = raw.get("content") or {}
    if not isinstance(content, dict):
        content = {"text": str(content)}
    text = content_to_markdown(content)

    if not text.strip():
        return None

    return Message(
        create_time=as_float(raw.get("create_time")),
        role=role,
        author_name=str(author_name) if author_name else None,
        content=text.strip(),
    )


def content_to_markdown(content: dict[str, Any]) -> str:
    content_type = content.get("content_type")
    parts = content.get("parts")

    if content_type in {"text", "multimodal_text"} and isinstance(parts, list):
        rendered = [part_to_markdown(part) for part in parts]
        return "\n\n".join(part for part in rendered if part)

    if content_type == "code" and isinstance(content.get("text"), str):
        language = content.get("language") or ""
        return f"```{language}\n{content['text']}\n```"

    if content_type == "execution_output":
        text = content.get("text") or content.get("stdout") or content.get("stderr") or ""
        return f"```text\n{text}\n```" if text else ""

    if isinstance(parts, list):
        rendered = [part_to_markdown(part) for part in parts]
        return "\n\n".join(part for part in rendered if part)

    text = content.get("text")
    if isinstance(text, str):
        return text

    return ""


def part_to_markdown(part: Any) -> str:
    if isinstance(part, str):
        return part
    if not isinstance(part, dict):
        return str(part)

    if "text" in part and isinstance(part["text"], str):
        return part["text"]

    asset_pointer = part.get("asset_pointer") or part.get("file_id")
    if asset_pointer:
        return f"[Attachment: {asset_pointer}]"

    return json.dumps(part, ensure_ascii=False, indent=2)


def write_output(conversations: list[Conversation], output_dir: Path, make_zip: bool) -> Path | None:
    output_dir.mkdir(parents=True, exist_ok=True)
    ordered = sorted(
        conversations,
        key=lambda item: (item.create_time is None, item.create_time or 0.0, item.title.lower()),
    )

    index_lines = [
        "# ChatGPT conversations export",
        "",
        f"Generated conversations: {len(ordered)}",
        "",
        "| # | Date | Title | Messages | File |",
        "|---:|---|---|---:|---|",
    ]

    filenames: list[Path] = []
    for number, conversation in enumerate(ordered, start=1):
        stem = f"{number:04d}_{slugify(conversation.title)}"
        filename = (stem[:180] or f"{number:04d}_untitled") + ".md"
        path = output_dir / filename
        write_conversation(path, conversation, number)
        filenames.append(path)
        index_lines.append(
            "| {number} | {date} | {title} | {count} | [{filename}]({filename}) |".format(
                number=number,
                date=escape_table(format_timestamp(conversation.create_time, date_only=True)),
                title=escape_table(conversation.title),
                count=len(conversation.messages),
                filename=escape_table(filename),
            )
        )

    index_path = output_dir / "000_INDEX.md"
    index_path.write_text("\n".join(index_lines) + "\n", encoding="utf-8")

    if not make_zip:
        return None

    archive_path = output_dir.with_suffix(".zip")
    with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.write(index_path, index_path.name)
        for path in filenames:
            archive.write(path, path.name)
    return archive_path


def write_conversation(path: Path, conversation: Conversation, number: int) -> None:
    lines = [
        f"# {conversation.title}",
        "",
        f"- Number: {number}",
        f"- Created: {format_timestamp(conversation.create_time)}",
        f"- Updated: {format_timestamp(conversation.update_time)}",
        f"- Messages: {len(conversation.messages)}",
        "",
        "---",
        "",
    ]

    for message in conversation.messages:
        role = role_label(message.role, message.author_name)
        lines.extend(
            [
                f"## {role} · {format_timestamp(message.create_time)}",
                "",
                message.content,
                "",
            ]
        )

    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def role_label(role: str, author_name: str | None) -> str:
    labels = {
        "user": "User",
        "assistant": "Assistant",
        "system": "System",
        "tool": "Tool",
    }
    base = labels.get(role, role.title() if role else "Unknown")
    return f"{base} ({author_name})" if author_name else base


def as_float(value: Any) -> float | None:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def first_timestamp(messages: Iterable[Message]) -> float | None:
    values = [message.create_time for message in messages if message.create_time is not None]
    return min(values) if values else None


def last_timestamp(messages: Iterable[Message]) -> float | None:
    values = [message.create_time for message in messages if message.create_time is not None]
    return max(values) if values else None


def format_timestamp(value: float | None, *, date_only: bool = False) -> str:
    if value is None:
        return "unknown"
    dt = datetime.fromtimestamp(value, tz=timezone.utc)
    return dt.strftime("%Y-%m-%d") if date_only else dt.strftime("%Y-%m-%d %H:%M:%S UTC")


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9äöüß._ -]+", "", value)
    value = value.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    value = re.sub(r"[\s._-]+", "-", value).strip("-")
    return value or "untitled"


def escape_table(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert a ChatGPT/OpenAI conversations.json export into readable Markdown files."
    )
    parser.add_argument("source", type=Path, help="Path to ChatGPT export ZIP, export directory, or conversations.json")
    parser.add_argument("-o", "--output", type=Path, default=Path("chatgpt_markdown_export"), help="Output directory")
    parser.add_argument("--no-zip", action="store_true", help="Do not create a ZIP archive next to the output directory")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    raw_conversations = load_conversations(args.source)
    conversations = [parse_conversation(item) for item in raw_conversations]
    archive_path = write_output(conversations, args.output, make_zip=not args.no_zip)

    print(f"Converted {len(conversations)} conversations to {args.output}")
    if archive_path:
        print(f"Created archive: {archive_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # argparse has already handled user input errors before this point.
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
