---
name: duell
description: Vergleicht zwei Prompt-Architekturen A und B anhand messbarer Kriterien — Präzision, Token-Effizienz, Robustheit, Format-Treue, Wartbarkeit und Claude-Konformität — kürt je Kriterium einen Sieger und empfiehlt eine Hybrid-Fassung. Greift bei °duell, /duell oder der Bitte, zwei Prompts, System-Prompts oder Skills gegeneinander zu bewerten.
argument-hint: "<prompt A> --- <prompt B>"
---

# Duell

<material>
$ARGUMENTS
</material>

Ist der Block leer, sind die beiden Prompts das Material aus der Nachricht des Nutzers. Lies vor der Arbeit aus `${CLAUDE_PLUGIN_ROOT}/skills/prompt-schmiede/references/`: `doktrin.md`, `haertungs-checkliste.md` und `folterkammer-matrix.md`.

## Arbeitsweise

**Trennung:** `---` zwischen A und B. Fehlt der Separator, nutze eine eindeutige Trennung (Überschriften, Codeblöcke) und nenne die Annahme; ist keine eindeutig, stelle eine Rückfrage.

**Kriterien**, je Prompt 1–10 Punkte mit Begründung aus dem Text:

1. **Präzision** — wie wenig Interpretationsspielraum.
2. **Token-Effizienz** — Wirkung pro Token; Zeichen gezählt, Tokens geschätzt und so gekennzeichnet.
3. **Robustheit** — Schnelldurchgang durch die Folterkammer-Vektoren 1–7.
4. **Format-Treue** — Determinismus der Ausgabestruktur.
5. **Wartbarkeit** — Lesbarkeit, Erweiterbarkeit, keine verstreuten Doppelregeln.
6. **Claude-Konformität** — Druck-Sprache, Weichmacher, Fossile, Reasoning-Extraktion (Folterkammer-Vektoren 8–12).

Die Punkte sind ein begründetes Urteil, keine Messung. Wo ein Kriterium knapp ausgeht, gib einen Testfall an, der es am Zielmodell empirisch entscheidet.

## Ausgabe

**Fazit:** Tabelle `Kriterium | A | B | Sieger | Kernbegründung`, Summenzeile, Gesamtverdikt in einem Satz.

**Erklären:** Begründung je Kriterium; Hybrid-Empfehlung — welche Teile aus A, welche aus B und warum. Die ausformulierte Hybrid-Fassung entsteht auf Wunsch mit `/prompt-schmieden`.
