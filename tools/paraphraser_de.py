#!/usr/bin/env python3
"""Ein einfacher deutscher Paraphraser für CLI-Nutzung.

Beispiele:
  python3 tools/paraphraser_de.py "Das ist ein guter Plan."
  echo "Ich habe keine Zeit." | python3 tools/paraphraser_de.py
"""

from __future__ import annotations

import argparse
import random
import re
import sys
from typing import Final

SYNONYMS = {
    "wichtig": "entscheidend",
    "gut": "stark",
    "schlecht": "ungünstig",
    "Problem": "Herausforderung",
    "schnell": "zügig",
    "langsam": "gemächlich",
    "nutzen": "verwenden",
    "machen": "erstellen",
    "zeigen": "darlegen",
    "denken": "annehmen",
    "verstehen": "nachvollziehen",
    "helfen": "unterstützen",
    "einfach": "unkompliziert",
    "schwierig": "anspruchsvoll",
    "starten": "beginnen",
    "enden": "abschließen",
    "klar": "deutlich",
    "viele": "zahlreiche",
    "wenige": "einige",
}

PROMPT: Final[str] = "Bitte gib deinen deutschen Text ein und drücke Enter:\n> "

OPENERS = [
    "Zusammengefasst:",
    "Anders formuliert:",
    "Kurz gesagt:",
    "Neu ausgedrückt:",
]


def _lookup_with_simple_inflection(word: str) -> str | None:
    lower = word.lower()
    if lower in SYNONYMS:
        return SYNONYMS[lower]

    for ending in ("er", "e", "en", "em", "es", "n", "s"):
        if lower.endswith(ending) and len(lower) > len(ending) + 2:
            stem = lower[: -len(ending)]
            if stem in SYNONYMS:
                return SYNONYMS[stem] + ending
    return None


def replace_words(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        word = match.group(0)
        new = _lookup_with_simple_inflection(word)
        if not new:
            return word
        if word[0].isupper():
            return new.capitalize()
        return new

    pattern = r"\b[\wÄÖÜäöüß]+\b"
    return re.sub(pattern, repl, text, flags=re.IGNORECASE)


def smooth_whitespace(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return re.sub(r"\s+([,.!?;:])", r"\1", text)


def paraphrase(text: str, add_opener: bool = False) -> str:
    out = replace_words(text)
    out = smooth_whitespace(out)
    if add_opener and out:
        out = f"{random.choice(OPENERS)} {out}"
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Ein kleiner deutscher Paraphraser für Terminal-Workflows.")
    parser.add_argument("text", nargs="*", help="Eingabetext. Wenn leer, wird von STDIN gelesen.")
    parser.add_argument("--opener", action="store_true", help="Fügt optional eine Einleitungsphrase hinzu.")
    args = parser.parse_args()

    raw = " ".join(args.text).strip()
    if not raw and not sys.stdin.isatty():
        raw = sys.stdin.read().strip()

    if not raw and sys.stdin.isatty():
        raw = input(PROMPT).strip()

    if not raw:
        print("Fehler: Kein Text übergeben. Übergib Text, nutze Pipe oder interaktive Eingabe.", file=sys.stderr)
        return 1

    print(paraphrase(raw, add_opener=args.opener))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
