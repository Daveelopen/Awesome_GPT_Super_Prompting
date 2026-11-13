---
name: kuerzen
description: Komprimiert einen Prompt, System-Prompt oder Skill radikal auf Token-Effizienz, ohne Kontext, Gründe, Schranken oder Formatregeln zu verlieren, und belegt jede Streichung. Greift bei °kuerzen, /kuerzen oder der Bitte, einen Prompt kürzer, schlanker, token-sparender oder dichter zu machen.
argument-hint: "<prompt>"
---

# Kürzen

<material>
$ARGUMENTS
</material>

Ist der Block leer, ist das Material der Prompt aus der Nachricht des Nutzers. Lies vor der Arbeit aus `${CLAUDE_PLUGIN_ROOT}/skills/daveelopen-werkstatt/references/`: `doktrin.md` und `haertungs-checkliste.md`.

## Arbeitsweise

Kürzen heißt bei Claude: Ballast entfernen, nicht Bedeutung.

**Streichkandidaten:** Wiederholungen derselben Regel; Allgemeinplätze, die Claude ohnehin befolgt („sei hilfreich und präzise"); Höflichkeits- und Einleitungsfloskeln; Fossile älterer Modelle (Härtungs-Checkliste, Abschnitt 8); Strategie-Ratschläge, die weder eine Regel noch das Erfolgskriterium ändern; Tool-Namen-Listen in Prosa.

**Bleibt, auch wenn es Platz kostet:** Publikum, Zweck, Qualitätsmaßstab, die Gründe hinter Regeln, echte Schranken, Tool-Verträge, Formatvorgaben. Ein „weil" ist semantische Dichte, kein Füllstoff — streichst du es, wendet Claude die Regel schlechter an.

**Verdichten vor Streichen:** Sätze zusammenführen, Nominalstil, Referenzdaten als Tabelle.

**Zählen:** Zeichen exakt zählen (z. B. `wc -m`). Tokens über die Token-Counting-API (`/v1/messages/count_tokens`) bestimmen, wenn sie verfügbar ist; sonst als Schätzung kennzeichnen, weil Claudes Tokenizer nicht mit anderen Zählern übereinstimmt.

## Ausgabe

**Fazit:** der komprimierte Prompt, vollständig.

**Erklären:**

1. Zeichen vorher → nachher, Tokens vorher → nachher (gezählt oder als Schätzung gekennzeichnet).
2. Streichliste: jede gestrichene Passage zitiert, mit Grund.
3. Erhaltungsnachweis: jede Schranke und Formatregel des Originals → wo sie in der Kurzfassung steht.
