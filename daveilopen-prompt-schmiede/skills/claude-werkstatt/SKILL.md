---
name: claude-werkstatt
description: Schneidet einen vorhandenen Prompt auf Claude zu — System-Prompt, Nutzer-Turn-Vorlage und Request-Parameter (adaptives Thinking, Effort, Structured Outputs, strict Tools, Caching-Reihenfolge) oder als claude.ai-Projektanweisung, CLAUDE.md, Skill oder Subagent. Portiert auch Prompts und Gems aus GPT oder Gemini nach Claude. Greift bei °claude-werkstatt, /claude-werkstatt oder der Bitte, einen Prompt für Claude, die Claude API, claude.ai oder Claude Code zu optimieren oder umzuziehen.
argument-hint: "<prompt> [ziel: api | claude.ai | claude-code]"
---

# Claude-Werkstatt

<material>
$ARGUMENTS
</material>

Ist der Block leer, ist das Material der Prompt aus der Nachricht des Nutzers. Lies vor der Arbeit aus `${CLAUDE_PLUGIN_ROOT}/skills/prompt-schmiede/references/`: `doktrin.md`, `kats-schema.md`, `claude-plattform.md`. Plattform-Fakten übernimmst du aus `claude-plattform.md`; ist einer für das Ergebnis entscheidend und sind Web-Werkzeuge verfügbar, prüfe ihn gegen die aktuelle Doku.

## Arbeitsweise

1. **Zielort bestimmen:** Claude API, claude.ai-Projekt oder Claude Code (CLAUDE.md, Skill, Subagent). Ohne Angabe: Claude API mit Claude Opus 5.5.
2. **Zerlegen**, was im Material steckt:
   - Verhalten → System-Prompt, als Prosa mit Gründen.
   - Material und Variablen → Nutzer-Turn in XML-Tags; lange Daten oben, Frage am Ende.
   - Format → Structured Outputs bei maschineller Weiterverarbeitung, sonst Vorlage oder Tags.
   - Konfiguration → Request-Parameter, nicht Prosa.
3. **Auf Claude anpassen:**
   - Druck-Sprache auf normale Lautstärke, Weichmacher an Pflichten entfernen (Härtungs-Checkliste, Abschnitte 1–2).
   - Gerüste älterer Modelle und anderer Anbieter ersetzen: „Schritt für Schritt" und Scratchpads durch adaptives Thinking plus Effort; Prefill und „nur JSON" durch Structured Outputs; `temperature`, `top_p`, `budget_tokens` und erzwungenes `tool_choice` entfernen oder ersetzen.
   - Tools als Verträge beschreiben, `strict: true`, `tool_choice: auto` plus ein Satz, wann das Tool dran ist.
   - Caching: Stabiles zuerst, Wechselndes ans Ende.
   - Kommt das Material aus einem Gemini-Gem oder GPT: Persona und Regeln werden zur Projektanweisung bzw. zum System-Prompt, Wissensdateien zum Projektwissen bzw. zu Dokumenten im Nutzer-Turn.
   - Keine Forderung nach sichtbarer Gedankenkette; stattdessen eine kurze Begründung des Ergebnisses.
4. **Endkontrolle** nach Abschnitt 9 der Härtungs-Checkliste.

## Ausgabe

**Fazit** als getrennte Blöcke:

- (a) System-Prompt,
- (b) Nutzer-Turn-Vorlage mit Platzhaltern,
- (c) bei API-Ziel: Request-Parameter als JSON — `model`, `max_tokens`, `thinking`, `output_config` (`effort`, gegebenenfalls `format`), `tools`,
- (d) bei claude.ai- oder Claude-Code-Ziel stattdessen die fertige Datei: Projektanweisung, CLAUDE.md-Abschnitt, SKILL.md oder Subagent-Datei.

**Erklären:** jede Claude-spezifische Änderung mit Grund, die Liste der entfernten Fossile, Hinweis auf Ablehnungs-Handling (`stop_reason: "refusal"`, Fallbacks), wo die Anwendung es braucht, und das Stand-Datum der verwendeten Plattform-Fakten.
