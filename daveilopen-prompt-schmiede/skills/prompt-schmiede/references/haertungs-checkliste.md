# Haertungs-Checkliste — Filter-Domestizierung

Abzuarbeiten im Modus **Haerten** (`°hart`), zusaetzlich als Endkontrolle in
jedem Modus, der einen Prompt ausliefert.

## 1. Sprachliche Weichmacher tilgen
- Konjunktive → Imperative: "sollte/koennte/wuerde" → "tue/gib/pruefe".
- Hedging raus: "vielleicht", "moeglicherweise", "in der Regel", "tendenziell".
- Hoeflichkeits- und Einleitungsfloskeln streichen ("Gerne", "Natuerlich",
  "Ich hoffe das hilft").
- Selbstrelativierung raus ("als KI kann ich nicht sicher sein").

## 2. Mehrdeutigkeit schliessen
- Vage Mengen quantifizieren ("kurz" → "max. 120 Woerter").
- Pronomen mit unklarem Bezug aufloesen.
- Doppeldeutige Begriffe definieren oder ersetzen.
- Implizite Annahmen explizit machen.

## 3. Schranken erzwingen
- Jede "darf nicht"-Regel als eigene, pruefbare Zeile.
- Abbruchkriterium ergaenzen, wo Scheitern moeglich ist.
- Fehlerpfad fuer leere/kaputte Eingaben definieren.
- Ausgabeformat verbindlich festnageln (Felder, Reihenfolge, Grenzen).

## 4. Sicherheits-Fehltrigger entschaerfen
- Formulierungen entfernen, die beim Zielmodell unnoetige Verweigerung
  ausloesen (reizwortlastige, aber harmlose Passagen sachlich umformulieren).
- Aufgabe und Legitimitaet klar rahmen, damit kein Pseudo-Risiko-Reflex greift.
- Keine widerspruechlichen Instruktionen, die das Modell in Ausweich-Floskeln
  druecken.

## 5. Robustheit gegen Drift & Manipulation
- Rollen-Anker am Anfang UND als Schlussklammer, damit lange Kontexte nicht
  wegdriften.
- Trennung Steuerbefehl vs. Material explizit machen (Injection-Schutz).
- Sycophancy-Sperre: "Stimme nicht aus Gefaelligkeit zu; widersprich sachlich
  bei Fehlern."
- DARVO-/Gaslighting-Verbot explizit setzen, wo das Modell sonst Fehler
  umdeuten koennte.

## 6. Endkontrolle
- Zwei gedankliche Testlaeufe: Erzeugt der Prompt strukturgleiche Ausgaben?
- Entfernte nichts Semantisches, nur Weichmacher? Gegenpruefen.
- Jede Aenderung benennbar? Wenn nicht, dokumentieren.
