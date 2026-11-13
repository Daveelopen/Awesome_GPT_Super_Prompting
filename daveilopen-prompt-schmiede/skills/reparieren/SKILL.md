---
name: reparieren
description: Diagnostiziert und repariert defekte Prompts, System-Prompts und Skills — Logikbrüche, widersprüchliche Anweisungen, Fehlinterpretations-Fallen, fehlende Schranken und Claude-spezifische Fehler wie Überanwendung, 400-auslösende Request-Parameter, Reasoning-Extraktion oder Skills, die nicht auslösen. Greift bei °reparieren, /reparieren oder wenn ein Prompt oder Skill sich falsch verhält, Fehler wirft oder unerwartete Antworten liefert.
argument-hint: "<defekter prompt/skill> [symptom]"
---

# Reparieren

<material>
$ARGUMENTS
</material>

Ist der Block leer, ist das Material der defekte Prompt oder Skill aus der Nachricht des Nutzers, gegebenenfalls mit Symptom (Fehlermeldung, Fehlverhalten, Beispielausgabe). Lies vor der Arbeit aus `${CLAUDE_PLUGIN_ROOT}/skills/daveelopen-werkstatt/references/`: `doktrin.md`, `kats-schema.md`, `haertungs-checkliste.md`; bei Request-Konfiguration oder Skills zusätzlich `claude-plattform.md`.

## Arbeitsweise

Erst Diagnose, dann Reparatur. Rekonstruiere die Absicht des Prompts in einem Satz, bevor du etwas änderst — ein Fix, der die Absicht verfehlt, ist ein neuer Defekt.

Prüfe drei Defektklassen:

- **Logik:** Widersprüche, falsche Reihenfolge, nicht abgedeckte Fälle, fehlender KATS-Block.
- **Interpretation:** Mehrdeutigkeit, unklare Bezüge, Material und Anweisung vermischt.
- **Claude-spezifisch:** Druck-Sprache → Überanwendung; Weichmacher an Pflichten → Unterlieferung; Prefill, `temperature`, `budget_tokens`, erzwungenes `tool_choice` → HTTP 400; geforderte sichtbare Gedankenkette → Ablehnung als `reasoning_extraction`; Skill löst nicht aus → `description` zu vage, nicht in dritter Person, zu lang oder ohne Auslöser; Skill-`name` mit reserviertem Wort oder unzulässigen Zeichen.

Lässt sich ein gemeldetes Symptom im Text nicht auf eine Ursache zurückführen, sag das und nenne die Hypothesen, jeweils mit einem Testfall, der sie entscheidet.

## Ausgabe

**Fazit:** die reparierte Fassung, vollständig.

**Erklären:**

1. Rekonstruierte Absicht in einem Satz.
2. Tabelle `Defekt | Ursache | Wirkung | Fix`.
3. Offene Hypothesen mit Testfall, falls vorhanden.
