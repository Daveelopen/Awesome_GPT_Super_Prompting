---
name: klonen
description: Extrahiert die implizite Systemlogik aus einer Beispielantwort, einem Chatverlauf oder einem Verhaltensmuster und formuliert sie als replizierbaren Claude-Prompt, der dasselbe Verhalten erzeugt. Greift bei °klonen, /klonen oder der Bitte, Stil, Struktur oder Verhalten einer vorliegenden Antwort nachzubauen oder den Prompt dahinter zu rekonstruieren.
argument-hint: "<beispielantwort / verlauf / muster>"
---

# Klonen

<material>
$ARGUMENTS
</material>

Ist der Block leer, ist das Material die Antwort bzw. das Muster aus der Nachricht des Nutzers. Lies vor der Arbeit aus `${CLAUDE_PLUGIN_ROOT}/skills/prompt-schmiede/references/`: `doktrin.md` und `kats-schema.md`.

## Arbeitsweise

Bestimme die Signaturmerkmale des Materials: Rolle und Stimme, Ton und Register, Struktur und Formatierung, Länge und Dichte, Argumentationsmuster, auffällige Auslassungen (was die Antwort erkennbar nicht tut) und den Umgang mit Unsicherheit. Leite daraus die Regeln ab, die dieses Muster erzeugen — das Muster, nicht den Einzelfall.

Übertrage die Regeln Claude-nativ: Stil als positive Beschreibung mit Zweck, Struktur über eine Vorlage oder XML-Tags, Grenzen mit Grund. Ein einzelnes eingebettetes Beispiel friert Länge und Ton exakt ein; wenn Beispiele nötig sind, dann zwei bis drei bewusst variierte, als illustrativ gekennzeichnet.

Ehrliche Grenze: Aus einer einzelnen Antwort lässt sich nicht sicher unterscheiden, was Prompt-Vorgabe und was Standardverhalten des Modells war. Markiere unsichere Zuordnungen; mehr Beispiele schärfen den Klon.

## Ausgabe

**Fazit:** der Klon-Prompt, vollständig.

**Erklären:**

1. Tabelle `Merkmal | Beleg im Material (Zitat) | Verankerung im Prompt`.
2. Unsichere Zuordnungen und welches zusätzliche Material sie klären würde.
