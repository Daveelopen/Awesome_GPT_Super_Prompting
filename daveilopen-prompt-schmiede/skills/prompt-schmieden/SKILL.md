---
name: prompt-schmieden
description: Schmiedet aus einer rohen Idee oder Aufgabenstellung einen produktionsreifen Prompt oder System-Prompt für Claude nach dem KATS-Schema, bei API-Zielen samt empfohlener Request-Parameter. Greift bei °prompt, /prompt-schmieden oder wenn jemand aus einer Idee, Notiz oder Anforderung einen fertigen Prompt, System-Prompt oder eine Agenten-Anweisung gebaut haben will.
argument-hint: "<rohe idee / aufgabenstellung>"
---

# Schmieden

<material>
$ARGUMENTS
</material>

Ist der Block leer, ist das Material die Idee aus der Nachricht des Nutzers. Lies vor der Arbeit aus `${CLAUDE_PLUGIN_ROOT}/skills/daveelopen-werkstatt/references/`: `doktrin.md`, `kats-schema.md`, bei einem API-Ziel zusätzlich `claude-plattform.md`.

## Arbeitsweise

1. **Ziel und Einsatzort bestimmen:** Claude API (System-Prompt plus Request), claude.ai-Projekt oder Claude Code (CLAUDE.md, Skill, Subagent). Ohne Angabe: System-Prompt für die Claude API mit Claude Opus 5.5.
2. **Lücken klären:** Fehlt eine Angabe, ohne die das Ergebnis falsch würde, stelle eine gebündelte Rückfrage. Sonst setze Defaults und markiere sie.
3. **Nach KATS bauen.** Investiere in den Kontext: Publikum, Zweck, Qualitätsmaßstab und die Gründe hinter jeder Regel sind genau das, was Claude nicht selbst wissen kann — und was den Unterschied zwischen generischer und treffender Ausgabe macht. Verhalten in Prosa mit „weil", Material in XML-Tags, lange Daten oben und die Aufgabe am Ende, maschinenlesbare Ausgabe über Structured Outputs.
4. **Endkontrolle** nach Abschnitt 9 der Härtungs-Checkliste (`haertungs-checkliste.md`).

## Ausgabe

**Fazit:** der fertige Prompt, vollständig. Bei einem API-Ziel ein zweiter Block mit den empfohlenen Request-Parametern als JSON — Modell, `max_tokens`, `thinking`, `output_config` (Effort und gegebenenfalls Format-Schema), Tools.

**Erklären:** KATS-Zerlegung (welcher Teil des Prompts deckt welchen Block), markierte Defaults, offene Annahmen.
