# KATS-Schema — Konstruktionsraster der Prompt-Schmiede

Jeder produktionsreife Prompt und jeder Skill wird in vier Bloecken konstruiert.
Reihenfolge ist verbindlich; kein Block darf leer bleiben.

## K — Kontext
- **Rolle & Identitaet:** Wer ist das Modell? Scharf abgegrenzt, kein generisches
  "du bist ein hilfreicher Assistent".
- **Systemumgebung:** Zielplattform (Gemini / OSS-LLM), Laufzeit, Aufrufkontext.
- **Datenquellen:** Welche Eingaben, Dokumente, Variablen stehen zur Verfuegung?
  Platzhalter explizit benennen (`{{input}}`, `{{dokument}}`).
- **Wissensgrenzen:** Was darf angenommen, was muss erfragt oder recherchiert
  werden?

## A — Aufgabe
- **Eine** eindeutige, messbare Arbeitsanweisung als Imperativ.
- Erfolgskriterium nennen: Woran ist die Aufgabe nachweislich erledigt?
- Mehrschrittige Aufgaben als nummerierte, abhaengigkeitsgeordnete Schritte.
- Keine Mehrdeutigkeit, kein Konjunktiv ("sollte", "koennte", "idealerweise").

## T — Tools
- Spezifikation der Werkzeuge, Funktionen, Schnittstellen (Function-Calling,
  Retrieval, Code-Ausfuehrung).
- Governance: Wann welches Tool, in welcher Reihenfolge, mit welchen Limits.
- Fehlerpfad je Tool: Was tun bei leerem/fehlerhaftem Rueckgabewert?
- Verbot erfundener Tools. Nur real verfuegbare Schnittstellen deklarieren.
- Kein Tool noetig → Block explizit mit "Keine Tools" fuellen, nicht weglassen.

## S — Schranken / Struktur
- **Negative Constraints:** Was ist strikt verboten (Floskeln, Disclaimer,
  Formatbruch, Erfindung von Fakten)?
- **Abbruchkriterien:** Wann stoppt das Modell und fragt zurueck oder meldet
  Fehlschlag?
- **Parsing-Regeln:** Wie wird die Eingabe gelesen, was ist Material vs.
  Steuerbefehl?
- **Eingabeformat / Ausgabeformat:** Exakte Struktur, Reihenfolge, Felder,
  Codeblock-Grenzen. Bei strukturierter Ausgabe: Schema angeben.

## Prueffragen vor Freigabe
1. Ist die Rolle so scharf, dass sie das Verhalten wirklich steuert?
2. Ist die Aufgabe messbar und einschrittig interpretierbar?
3. Ist jeder Tool-Aufruf mit Governance und Fehlerpfad versehen?
4. Deckt jede Schranke einen realen Fehlweg ab (nicht nur Dekoration)?
5. Ist das Ausgabeformat so eng, dass zwei Laeufe strukturgleich sind?
