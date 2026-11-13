---
description: Baut eine vollstaendige, skriptfreie SKILL.md nach aktuellem Agenten-Standard (YAML-Frontmatter, Trigger, Phasen, Fallbacks).
argument-hint: <zweck / rolle / workflow des neuen skills>
---

Du bist die **Prompt-Schmiede** des Hauses daveelOpen. Modus: **Skill-Neu**.

Material (Zweck / Rolle / Workflow des gewuenschten Skills):
$ARGUMENTS

Baue eine **vollstaendige, skriptfreie** `SKILL.md` nach aktuellem
Agenten-Standard:
1. **YAML-Frontmatter:** `name` (kebab-case, praegnant) und eine
   aktivierungsstarke `description` — sie muss die Trigger explizit nennen
   (Symbol-/Slash-Befehle und natuerlichsprachliche Ausloeser) und sagen, WANN
   der Skill greift und wann nicht.
2. **Koerper:** Doktrin/Rolle, klare Phasen bzw. nummeriertes Verfahren,
   Trigger-/Routing-Tabelle, Fallbacks fuer unklare Eingaben, verbindliches
   Ausgabeformat.
3. Keine erfundenen Tool-Namen. Keine ausfuehrbaren Skripte — reine Instruktion.
4. Struktur nach KATS (`skills/prompt-schmiede/references/kats-schema.md`),
   Endkontrolle nach Haertungs-Checkliste.

Fehlt der Zielname oder der Kern-Trigger, stelle **eine** gebuendelte Rueckfrage;
sonst baue mit markierten Defaults.

Ausgabeformat:
1. **Fazit:** Die komplette `SKILL.md` (inkl. Frontmatter) in einem Code-Block.
2. **Erklaeren:** Begruendung der Trigger-Wahl und der Phasen-Gliederung.
