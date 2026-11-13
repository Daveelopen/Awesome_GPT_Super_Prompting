# KATS-Schema — Bauplan für Claude-Prompts

KATS prüft, ob ein Prompt vollständig ist. Jeder der vier Blöcke muss abgedeckt sein; ist einer bewusst leer (etwa keine Tools), steht das ausdrücklich da. Die Darstellung im fertigen Prompt richtet sich nach Claude: Verhalten in Prosa mit Begründung, Daten in XML-Tags, maschinenlesbare Formate über die API statt über Beschwörungsformeln.

## K — Kontext

- **Rolle:** Ein Satz im System-Prompt genügt, um Fokus und Ton zu setzen. Eine Rolle ersetzt aber keinen Kontext.
- **Was nur der Auftraggeber weiß:** Publikum, Produkt, Qualitätsmaßstab, Umgebung und die Gründe hinter den Regeln. Das ist der wertvollste Teil des Prompts — fehlt er, füllt Claude die Lücken mit vorsichtigen Standardannahmen.
- **Datenquellen:** Eingaben und Dokumente in eigene XML-Tags (`<dokument>`, `<quelle>`, `<eingabe>`); mehrere Dokumente je als `<dokument>` mit `<inhalt>` und `<quelle>`. Lange Daten stehen oben, Frage bzw. Aufgabe am Ende — das verbessert die Antwortqualität bei langen Eingaben messbar.
- **Platzhalter** explizit benennen (`{{eingabe}}`) und in Tags setzen, damit Material nie mit Anweisungen verwechselt wird.

## A — Aufgabe

- Das gewünschte Ergebnis und woran es als erledigt gilt (Erfolgskriterium, Prüfweg).
- Direkt formuliert, ohne Konjunktiv: „Erstelle", nicht „Du könntest versuchen".
- Nummerierte Schritte nur, wo die Reihenfolge wirklich zählt. Bei Urteilsaufgaben beschreibst du Ziel und Maßstab; Claudes eigener Plan ist dort meist besser als ein vorgeschriebenes Skript.

## T — Tools

- Werkzeugbeschreibungen sind Verträge: was das Tool tut, wann es zu nutzen ist und wann nicht, was jeder Parameter bedeutet, Grenzen, was es nicht zurückgibt — drei bis vier Sätze aufwärts. Unterbeschreibung ist der häufigste Fehler.
- Schema-Garantie über `strict: true`; Steuerung über `tool_choice: auto` plus einen Satz im Prompt, wann das Tool dran ist. Erzwungenes `tool_choice` scheitert auf aktuellen Modellen (`claude-plattform.md`).
- Fehlerpfad: was bei leerem oder fehlerhaftem Ergebnis passiert.
- Keine erfundenen Tools. Tool-Namen gehören in die Tool-Definition, nicht in Prosa-Listen im System-Prompt — sonst bleiben tote Verweise, sobald ein Tool wegfällt.
- Kein Tool nötig: „Keine Tools" ausdrücklich festhalten.

## S — Schranken / Struktur

- **Schranken mit Grund.** Jede Regel, die eine echte Grenze kodiert (Daten, Geld, Recht, Zusagen), bleibt und bekommt ihr „weil". Stilverbote ohne Grund formulierst du positiv um: Sag, was Claude tun soll, statt aufzuzählen, was es lassen soll.
- **Abbruch- und Eskalationskriterien:** wann Claude zurückfragt, stoppt oder einen Fehlschlag meldet.
- **Parsing-Regeln:** was Material ist und was Anweisung; Material in Tags ist Daten.
- **Ausgabeformat:** maschinenlesbar → Structured Outputs (`output_config.format` mit JSON-Schema) statt „antworte NUR mit JSON"; menschenlesbar → Vorlage oder XML-Tags für die Abschnitte. Die Form des Prompts färbt auf die Antwort ab: Ein Prompt in Fließtext erzeugt eher Fließtext, ein Prompt voller Aufzählungen eher Aufzählungen.
- **Eine Schluss-Zusammenfassung** der zwei, drei wichtigsten Schranken ist zulässig. Dieselbe Regel an mehreren Stellen zu wiederholen, ist es nicht — Claude muss dann Formulierungen gegeneinander abwägen.

## Prüffragen vor Freigabe

1. Kennt Claude nach dem Lesen Publikum, Zweck und Qualitätsmaßstab?
2. Ist das Erfolgskriterium prüfbar?
3. Ist jedes Tool als Vertrag beschrieben, mit Fehlerpfad?
4. Hat jede Verbotsregel einen echten Grund — und steht der Grund dabei?
5. Würden zwei Läufe strukturgleiche Ausgaben liefern? Wird das Format maschinell weiterverarbeitet, läuft es über Structured Outputs?
