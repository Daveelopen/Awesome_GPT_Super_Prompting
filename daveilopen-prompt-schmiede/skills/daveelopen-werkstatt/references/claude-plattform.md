# Claude-Plattform — Hebel und Fallstricke

Stand: 2026-11-13. Quellen: platform.claude.com, code.claude.com. Diese Datei ist die einzige Stelle im Plugin mit versionsabhängigen Fakten. Ist ein Punkt für ein Ergebnis entscheidend und sind Web-Werkzeuge verfügbar, prüfe ihn gegen die aktuelle Doku.

## Inhalt

- Modelle
- Thinking und Effort
- Was auf aktuellen Modellen fehlschlägt
- Ausgabeformat
- Tools
- Caching und Platzierung
- Ablehnungen
- Lange Eingaben
- claude.ai und Claude Code
- Skill-Format

## Modelle

| Modell | ID | Einsatz |
|---|---|---|
| Claude Opus 5.5 | `claude-opus-5-5` | Standardziel |
| Claude Sonnet 5.5 | `claude-sonnet-5-5` | schnell; Alltags-Coding, Agenten |
| Claude Haiku 5.5 | `claude-haiku-5-5` | günstig; Klassifikation, Extraktion |
| Claude Fable 5.2 | `claude-fable-5-2` | leistungsstärkstes allgemein verfügbares Modell |

Modell-IDs ohne Datums-Suffix verwenden.

## Thinking und Effort

- Denktiefe steuerst du über Konfiguration, nicht über Prosa: `thinking: {type: "adaptive"}` und `output_config: {effort: "low" | "medium" | "high" | "xhigh" | "max"}`.
- Opus 5.5: Thinking ist immer an und lässt sich nicht abschalten; Effort-Default ist `medium` — explizit setzen. Sonnet 5.5: Default `high`; Thinking aus nur über `{type: "between_tools"}`.
- Weniger Denken → Effort senken, nicht „denke weniger" schreiben; das wirkt kaum.
- `max_tokens` muss Thinking plus Antwort fassen (Richtwert: 16K ohne, 64K mit Streaming).

## Was auf aktuellen Modellen fehlschlägt (HTTP 400)

- **Assistant-Prefill** (letzter Turn vom Assistenten) — ersetzt durch Structured Outputs oder eine Anweisung im System-Prompt.
- **`temperature`, `top_p`, `top_k`** — auf aktuellen Modellen entfernt; ab API-Version `2026-10-21` auf jedem Modell ein Fehler.
- **`budget_tokens`** — ersetzt durch adaptives Thinking plus Effort.
- **Erzwungenes `tool_choice`** (`any` / `tool`) auf Opus 5.5, Sonnet 5.5, Fable 5.1/5.2 — ersetzt durch `auto` plus Prompt-Satz plus `strict: true`, oder durch Structured Outputs.
- **`thinking: {type: "disabled"}`** auf Opus 5.5 und Sonnet 5.5.

## Ausgabeformat

- Maschinenlesbar: `output_config: {format: {type: "json_schema", schema: {...}}}`; jedes Objekt mit `additionalProperties: false`. Nicht kombinierbar mit Citations und Prefill.
- Präambel unterdrücken: Anweisung im System-Prompt („Antworte direkt ohne Einleitung") oder Ausgabe in XML-Tags.

## Tools

- Beschreibung als Vertrag, drei bis vier Sätze aufwärts; `strict: true` für schemagültige Argumente (verlangt `additionalProperties: false` und `required`).
- Parallele Tool-Aufrufe: alle `tool_result`-Blöcke in einer einzigen Nutzer-Nachricht zurückgeben; Fehler mit `is_error: true` melden statt weglassen.
- Tool-Entmutigung („nur wenn unbedingt nötig", „minimiere Tool-Aufrufe") wird wörtlich befolgt — streichen und stattdessen sagen, wann nachzusehen ist.

## Caching und Platzierung

- Reihenfolge `tools` → `system` → `messages`; Stabiles zuerst, Wechselndes (Zeitstempel, IDs, Nutzerfrage) nach dem letzten Cache-Breakpoint. Jede Byte-Änderung im Präfix macht den Cache dahinter ungültig.
- Betreiber-Anweisungen mitten im Gespräch: System-Nachricht in `messages` (`{"role": "system", ...}`) statt den Top-Level-`system` zu ändern — hält den Cache und ist der injektionssichere Kanal (Opus 5.5, Sonnet 5.5, Haiku 5.5, Fable).
- Nutzertext nie in einen `tool_result`-Block legen.

## Ablehnungen

- Klassifikator-Ablehnung kommt als HTTP 200 mit `stop_reason: "refusal"` und `stop_details.category`. Vor dem Lesen von `content` prüfen.
- Server-seitige Fallbacks: Beta `server-side-fallback-2026-07-01` mit `fallbacks: "default"`. `reasoning_extraction`-Ablehnungen werden nicht per Fallback wiederholt.
- Klassifikator-Ablehnungen lassen sich nicht wegprompten; prompt-seitig hilft nur klarer, legitimer Kontext gegen modellseitige Übervorsicht.

## Lange Eingaben

- Lange Dokumente oben, Frage und Anweisungen am Ende (laut Anthropic bis zu 30 % bessere Antworten bei komplexen Mehrdokument-Eingaben).
- Mehrere Dokumente: je `<document>` mit `<document_content>` und `<source>`; deutsche Tag-Namen funktionieren genauso, solange sie konsistent sind.
- Bei langen Dokumenten zuerst relevante Stellen zitieren lassen, dann die Aufgabe lösen.

## claude.ai und Claude Code

- claude.ai: Projektanweisungen plus Projektwissen sind das Gegenstück zu Gemini-Gems; Skills für wiederkehrende Abläufe.
- Claude Code: `CLAUDE.md` (Projektkontext, lädt in jeder Sitzung — knapp halten), Skills (`skills/<name>/SKILL.md`, laden bei Bedarf), Subagenten (`agents/*.md`).

## Skill-Format

- Frontmatter portabel (claude.ai, Skills-API): nur `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`; andere Schlüssel sind dort ein harter Fehler.
- `name`: max. 64 Zeichen, Kleinbuchstaben, Ziffern, Bindestriche; keine XML-Tags; nicht die reservierten Wörter `anthropic` oder `claude`.
- `description`: nicht leer, max. 1024 Zeichen (Claude Code kürzt `description` plus `when_to_use` in der Liste bei 1536), keine XML-Tags, dritte Person; was der Skill tut und wann er greift, wichtigster Anwendungsfall zuerst.
- Nur in Claude Code: `when_to_use`, `argument-hint`, `arguments`, `disable-model-invocation`, `user-invocable`, `disallowed-tools`, `model`, `effort`, `context: fork`, `agent`, `paths`.
- Platzhalter: `$ARGUMENTS`, `$ARGUMENTS[N]` bzw. `$N`, benannte `$name`; Pfade über `${CLAUDE_SKILL_DIR}`, in Plugins `${CLAUDE_PLUGIN_ROOT}`.
- Körper unter 500 Zeilen; Details in Referenzdateien, die direkt aus `SKILL.md` verlinkt sind (eine Ebene tief); Referenzdateien über 100 Zeilen mit Inhaltsverzeichnis.
- Plugin-Skills heißen `/plugin-name:skill-name`; setzt ein Skill `name` selbst, funktioniert auch die Kurzform `/name`, solange kein anderer Befehl so heißt.
