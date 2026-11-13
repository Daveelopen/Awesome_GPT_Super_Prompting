# daveilopen-prompt-schmiede

**Zentrale Architektur-Instanz des Hauses daveelOpen** zur Konstruktion, Härtung,
Prüfung und Optimierung von Prompts, System-Prompts, Gems und agentischen Skills
für **Gemini- und Open-Source-LLM-Architekturen.**

> Deterministik vor Konversation. Fazit zuerst, Begründung danach. Keine Floskeln.

---

## 1. Grundprinzipien & Doktrin

1. **Deterministik vor Konversation** — keine Entschuldigungsfloskeln, keine
   Einleitungssätze, kein Pseudo-Empathie-Fluff. Ausgabe sofort im Ergebnis-Format.
2. **KATS-Architektur** — jeder Prompt und jeder Skill folgt dem Schema:
   - **K**ontext (Rolle, Identität, Systemumgebung, Datenquellen)
   - **A**ufgabe (eindeutige, messbare Arbeitsanweisung)
   - **T**ools (Spezifikation der Werkzeuge, Schnittstellen, Governance)
   - **S**chranken / Struktur (Negative Constraints, Abbruchkriterien,
     Parsing-Regeln, Ein- und Ausgabeformate)
3. **Filter-Domestizierung & Härtung** — Robustheit gegen Context-Drift,
   Sycophancy, DARVO-Tendenzen und modellseitige Ausflüchte.
4. **Erwachsenen-Ich-Parität** — sachlich, neutral, kompromisslos, ohne Moralpredigt.

## 2. Steuerbefehle

Jeder Modus ist über **zwei Wege** erreichbar: den Symbol-Trigger `°…` (fängt die
zentrale Skill ab, auch natürlichsprachlich) und den Slash-Befehl `/…`
(direkter Einstiegspunkt).

| Symbol | Slash | Funktion |
|---|---|---|
| `°prompt` | `/prompt-schmieden` | Rohe Idee → produktionsreifer, deterministischer Prompt |
| `°claude-werkstatt` | `/claude-werkstatt` | Prompt für **Google Gemini** optimieren (System-Instruktion, Gems, Tool-Calling) |
| `°hart` | `/haerten` | Weichmacher, Konjunktive, Widersprüche, Fehltrigger raus; strikte Schranken |
| `°folterkammer` | `/folterkammer` | Stresstest & Red-Teaming (Drift, Jailbreak, Halluzination, Randfälle) |
| `°kuerzen` | `/kuerzen` | Radikale Token-Kompression bei vollem Erhalt von Semantik & Schranken |
| `°reparieren` | `/reparieren` | Defekte Prompts/Skills diagnostizieren und rekonstruieren |
| `°klonen` | `/klonen` | Implizite Systemlogik einer Antwort als replizierbaren Prompt extrahieren |
| `°duell` | `/duell` | Zwei Prompt-Architekturen messbar vergleichen |
| `°skill-neu` | `/skill-neu` | Vollständige, skriptfreie `SKILL.md` nach Agenten-Standard bauen |

> **Namenshinweis:** `°claude-werkstatt` / `/claude-werkstatt` optimiert laut
> Spezifikation für **Gemini**, nicht für Claude — der Name ist historisch. Das
> Plugin folgt der Spezifikation (Zielplattform Gemini).

## 3. Ausführungs- & Ausgabeformat

Sofern kein reiner Rohcode angefordert wird, folgt jede Analyse und
Berichterstattung zwingend:

1. **Fazit** — der gehärtete Prompt / das Ergebnis im sauberen Markdown-Code-Block.
2. **Erklären** — strukturierte Begründung, Schwachstellen-Analyse, KATS-Zerlegung.

## 4. Struktur

```
daveilopen-prompt-schmiede/
├── .claude-plugin/
│   └── plugin.json
├── commands/                     # 9 Slash-Befehle (/…)
│   ├── prompt-schmieden.md
│   ├── claude-werkstatt.md
│   ├── haerten.md
│   ├── folterkammer.md
│   ├── kuerzen.md
│   ├── reparieren.md
│   ├── klonen.md
│   ├── duell.md
│   └── skill-neu.md
├── skills/
│   └── prompt-schmiede/
│       ├── SKILL.md              # Zentrale Skill: fängt °-Trigger + Routing
│       └── references/
│           ├── kats-schema.md
│           ├── haertungs-checkliste.md
│           └── folterkammer-matrix.md
└── README.md
```

Die **Slash-Befehle** sind selbsttragende Einstiegspunkte. Die **zentrale Skill**
`prompt-schmiede` fängt die `°`-Symbol-Trigger sowie natürlichsprachliche Anfragen
ab, routet in den passenden Modus und hält die gemeinsame KATS-Wissensbasis.

## 5. Installation (Claude Code)

Plugin aus einem lokalen Marketplace oder Verzeichnis laden:

```bash
/plugin marketplace add daveelopen/awesome_gpt_super_prompting
/plugin install daveilopen-prompt-schmiede
```

Alternativ das Verzeichnis `daveilopen-prompt-schmiede/` in dein
Plugin-/Marketplace-Setup einhängen. Nach der Installation stehen die neun
`/…`-Befehle und die `°…`-Trigger zur Verfügung.

## 6. Beispiele

```
/prompt-schmieden Ein Prompt, der aus einem Supportticket Kategorie,
Dringlichkeit und Antwortentwurf als JSON zieht.

/haerten <hier deinen weichen Prompt einfügen>

/duell <Prompt A> --- <Prompt B>

°folterkammer <zu testender System-Prompt>
```

---

_Haus daveelOpen 🙏💍💎😈 — Wahrheit und Wissenschaft über alles._
