---
name: skill-neu
description: Baut eine vollständige, skriptfreie SKILL.md nach aktuellem Agent-Skills-Standard — YAML-Frontmatter mit auslösestarker description, Trigger, Phasen, Fallbacks und Ausgabeformat — lauffähig in Claude Code, auf claude.ai und über die Skills-API. Greift bei °skill-neu, /skill-neu oder der Bitte, einen neuen Skill, Slash-Befehl oder eine wiederverwendbare Agenten-Anweisung zu entwerfen.
argument-hint: "<zweck / rolle / workflow> [ziel: claude-code | portabel]"
---

# Skill-Neu

<material>
$ARGUMENTS
</material>

Ist der Block leer, ist das Material die Beschreibung des gewünschten Skills aus der Nachricht des Nutzers. Lies vor der Arbeit aus `${CLAUDE_PLUGIN_ROOT}/skills/prompt-schmiede/references/`: `doktrin.md`, `kats-schema.md` und in `claude-plattform.md` den Abschnitt „Skill-Format".

## Arbeitsweise

1. **Zweck, Auslöser, Einsatzort** klären. Einsatzort Claude Code erlaubt die erweiterten Frontmatter-Felder; „portabel" (claude.ai, Skills-API) nur die portablen. Ohne Angabe: portabel, weil es überall läuft.
2. **`name`:** Kleinbuchstaben, Ziffern, Bindestriche, höchstens 64 Zeichen, ohne die reservierten Wörter `claude` und `anthropic`; aussagekräftig, als Gerundium oder Nominalphrase.
3. **`description`:** dritte Person, höchstens 1024 Zeichen, keine XML-Tags. Zuerst, was der Skill tut, dann wann er greift. Auslöser als Kategorien von Absichten plus die expliziten Befehle — keine wachsende Synonymliste. Kalibrierte Dringlichkeit ist hier zulässig, weil Skills eher zu selten auslösen; im Körper nicht.
4. **Körper:** nur, was Claude nicht schon weiß. Verhalten in Prosa mit Gründen; nummerierte Phasen nur, wo die Reihenfolge zählt. Den Freiheitsgrad an die Fragilität anpassen: offenes Feld → Heuristik, schmale Brücke → exakte Schritte. Fallbacks für leere oder unklare Eingaben, verbindliches Ausgabeformat, konsistente Begriffe, keine Datumsangaben, die veralten. Unter 500 Zeilen; was darüber hinausgeht, kommt in Referenzdateien eine Ebene tief, die du mitlieferst.
5. **Werkzeuge:** keine erfundenen Tools und keine ausführbaren Skripte — reine Instruktion. MCP-Tools voll qualifiziert (`Server:tool_name`).
6. **Prüfen** gegen die Checkliste: description spezifisch, mit Schlüsselbegriffen, mit Was und Wann? Unter 500 Zeilen? Referenzen eine Ebene tief? Frontmatter-Felder passend zum Einsatzort?

## Ausgabe

**Fazit:** die komplette `SKILL.md` inklusive Frontmatter; außen vier Backticks, falls innen Codeblöcke stehen. Jede Referenzdatei in einem eigenen Block mit ihrem Pfad als Überschrift.

**Erklären:** Begründung von Name, Trigger-Wahl, Phasen und Freiheitsgrad; dazu drei Testanfragen für einen Auslösetest — zwei, bei denen der Skill greifen soll, eine, bei der er es nicht soll.
