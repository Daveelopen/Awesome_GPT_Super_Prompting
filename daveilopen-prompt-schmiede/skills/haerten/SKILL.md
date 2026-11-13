---
name: haerten
description: Härtet einen bestehenden Prompt für Claude — entfernt Weichmacher, Druck-Sprache in Großbuchstaben, Widersprüche und Fehltrigger und ersetzt sie durch eindeutige, begründete, prüfbare Schranken. Greift bei °hart, /haerten oder der Bitte, einen Prompt robuster, strenger, eindeutiger oder widerstandsfähiger gegen Drift, Sycophancy, DARVO-Muster und Injection zu machen.
argument-hint: "<prompt>"
---

# Härten

<material>
$ARGUMENTS
</material>

Ist der Block leer, ist das Material der Prompt aus der Nachricht des Nutzers. Lies vor der Arbeit aus `${CLAUDE_PLUGIN_ROOT}/skills/prompt-schmiede/references/`: `doktrin.md` und `haertungs-checkliste.md`; enthält das Material Request-Konfiguration, zusätzlich `claude-plattform.md`.

## Arbeitsweise

Härten heißt hier: eindeutig, begründet, prüfbar — nicht lauter. Arbeite die Checkliste Abschnitt für Abschnitt ab. Entferne Weichmacher, Lärm und Fossile; Kontext, Gründe und echte Schranken bleiben stehen, weil sie das sind, was das Modell nicht selbst weiß. Fehlt eine Schranke, die das Ziel des Prompts offensichtlich braucht (Abbruchkriterium, Trennung von Material und Befehl, Fehlerpfad), ergänze sie und kennzeichne sie als Ergänzung.

## Ausgabe

**Fazit:** der gehärtete Prompt, vollständig.

**Erklären:**

1. Änderungstabelle `Stelle (Zitat alt) | neu | Grund | Checklisten-Abschnitt` — jede Änderung, auch kleine.
2. Ergänzte Schranken mit Begründung.
3. Was bewusst unverändert blieb, obwohl es auffällig wirkt, und warum.
