# daveilopen-prompt-schmiede

**Zentrale Architektur-Instanz des Hauses daveelOpen** zur Konstruktion, Härtung,
Prüfung und Optimierung von Prompts, System-Prompts, Skills und
Agenten-Konfigurationen für **Claude** — Claude API, claude.ai und Claude Code.

> Deterministik vor Konversation. Fazit zuerst, Begründung danach. Keine Floskeln.

---

## 1. Grundprinzipien & Doktrin

1. **Deterministik vor Konversation** — keine Entschuldigungsfloskeln, keine
   Einleitungssätze, kein Pseudo-Empathie-Fluff. Ausgabe sofort im Ergebnis-Format.
2. **KATS-Architektur** — jeder Prompt und jeder Skill deckt ab:
   - **K**ontext (Rolle, Identität, Systemumgebung, Datenquellen)
   - **A**ufgabe (eindeutige, messbare Arbeitsanweisung)
   - **T**ools (Spezifikation der Werkzeuge, Schnittstellen, Governance)
   - **S**chranken / Struktur (Negative Constraints, Abbruchkriterien,
     Parsing-Regeln, Ein- und Ausgabeformate)
3. **Filter-Domestizierung & Härtung** — Robustheit gegen Context-Drift,
   Sycophancy, DARVO-Tendenzen und modellseitige Ausflüchte.
4. **Erwachsenen-Ich-Parität** — sachlich, neutral, kompromisslos, ohne Moralpredigt.

## 2. Steuerbefehle

Jeder Modus ist auf drei Wegen erreichbar: Symbol-Trigger `°…` im Chat, Kurzform
`/…` und die immer eindeutige Vollform `/daveilopen-prompt-schmiede:…`.

| Symbol | Slash (Kurzform) | Funktion |
|---|---|---|
| `°prompt` | `/prompt-schmieden` | Rohe Idee → produktionsreifer Prompt, bei API-Ziel mit Request-Parametern |
| `°daveelopen-werkstatt` (alt: `°claude-werkstatt`) | `/daveelopen-werkstatt` | Prompt auf Claude zuschneiden: System-Prompt, Request-Parameter, Tools — oder als claude.ai-Projekt, CLAUDE.md, Skill, Subagent. Portiert auch GPT-Prompts und Gemini-Gems. Läuft auch eigenständig auf claude.ai |
| `°hart` | `/haerten` | Weichmacher, Druck-Sprache, Widersprüche, Fehltrigger raus; begründete, prüfbare Schranken rein |
| `°folterkammer` | `/folterkammer` | Red-Teaming über 12 Vektoren (7 allgemeine + 5 Claude-spezifische) |
| `°kuerzen` | `/kuerzen` | Token-Kompression ohne Verlust von Kontext, Gründen, Schranken — jede Streichung belegt |
| `°reparieren` | `/reparieren` | Defekte Prompts/Skills diagnostizieren und rekonstruieren |
| `°klonen` | `/klonen` | Verhaltensmuster einer Antwort als replizierbaren Prompt extrahieren |
| `°duell` | `/duell` | Zwei Prompts über 6 Kriterien vergleichen, Hybrid empfehlen |
| `°skill-neu` | `/skill-neu` | Vollständige, skriptfreie `SKILL.md` nach Agent-Skills-Standard |
| `°°` / `°hilfe` | `/prompt-schmiede` | Routing-Tabelle anzeigen |

Die Kurzform funktioniert, solange kein anderer installierter Befehl denselben
Namen trägt; sonst die Vollform nehmen.

## 3. Ausführungs- & Ausgabeformat

Sofern kein reiner Rohcode angefordert wird:

1. **Fazit** — das Werkstück (Prompt, Skill, Befund-Tabelle, Verdikt) vollständig
   im Markdown-Codeblock.
2. **Erklären** — Schwachstellen-Analyse, KATS-Zerlegung, jede Änderung mit Grund.

## 4. Installation

In Claude Code (ab 2.1.275 in einem Schritt):

```
/plugin install daveilopen-prompt-schmiede --marketplace Daveelopen/Awesome_GPT_Super_Prompting
```

Oder in zwei Schritten:

```
/plugin marketplace add Daveelopen/Awesome_GPT_Super_Prompting
```

```
/plugin install daveilopen-prompt-schmiede@daveelopen
```

Lokal ausprobieren, ohne zu installieren:

```bash
claude --plugin-dir ./daveilopen-prompt-schmiede
```

### Werkstatt auf claude.ai

Die `daveelopen-werkstatt` ist als einziger Skill des Plugins in sich geschlossen und
lässt sich einzeln auf claude.ai hochladen. ZIP aus dem Ordner `skills/` bauen, damit
der Skill-Ordner die oberste Ebene des Archivs ist:

```bash
cd daveilopen-prompt-schmiede/skills && zip -r daveelopen-werkstatt.zip daveelopen-werkstatt
```

Dann auf claude.ai unter **Customize > Skills** hochladen und den Skill einschalten.
Voraussetzung ist ein Plan mit Skills und eingeschalteter Code-Ausführung. Ausgelöst
wird er im Chat mit `°daveelopen-werkstatt` oder einer Bitte wie „optimiere diesen
Prompt für Claude".

## 5. Struktur

```
daveilopen-prompt-schmiede/
├── .claude-plugin/
│   ├── plugin.json
│   └── icon.png
├── skills/
│   ├── prompt-schmiede/SKILL.md    # Router: °-Trigger, °hilfe, Modus-Wahl
│   ├── daveelopen-werkstatt/       # eigenständig, claude.ai-tauglich
│   │   ├── SKILL.md
│   │   └── references/             # gemeinsame Wissensbasis aller Modi
│   │       ├── doktrin.md          # Hausdoktrin + Ausgabeformat (gilt für alle Modi)
│   │       ├── kats-schema.md      # Bauplan für Claude-Prompts
│   │       ├── haertungs-checkliste.md
│   │       ├── folterkammer-matrix.md
│   │       └── claude-plattform.md # einzige Stelle mit API-Fakten, mit Stand-Datum
│   ├── prompt-schmieden/SKILL.md
│   ├── haerten/SKILL.md
│   ├── folterkammer/SKILL.md
│   ├── kuerzen/SKILL.md
│   ├── reparieren/SKILL.md
│   ├── klonen/SKILL.md
│   ├── duell/SKILL.md
│   └── skill-neu/SKILL.md
└── README.md
```

Die gemeinsame Wissensbasis liegt im Ordner der Werkstatt, weil claude.ai einem
hochgeladenen Skill nur seinen eigenen Ordner mitgibt. Die Werkstatt liest sie über
relative Pfade, alle anderen Modi über `${CLAUDE_PLUGIN_ROOT}` — jede Regel steht an
genau einer Stelle.

## 6. Was „für Claude optimiert" konkret heißt

- **Härten heißt präzise, nicht laut.** Aktuelle Claude-Modelle folgen dem
  System-Prompt wörtlich: `KRITISCH/MUSS/NIEMALS` in Großbuchstaben wird
  überangewandt, „wenn möglich" als echte Option gelesen. Die Schmiede ersetzt
  beides durch klare Regeln mit Begründung.
- **Konfiguration statt Beschwörung.** „Denke Schritt für Schritt" → adaptives
  Thinking plus `effort`; „antworte NUR mit JSON" und Prefill → Structured Outputs
  (`output_config.format`); erzwungenes `tool_choice` → `auto` plus `strict: true`.
- **Keine 400-Fallen.** Prefill, `temperature`/`top_p`/`top_k`, `budget_tokens`
  scheitern auf aktuellen Modellen und werden entfernt.
- **Keine Reasoning-Extraktion.** Wer die Gedankenkette in der Antwort verlangt,
  riskiert eine Ablehnung (`reasoning_extraction`); verlangt wird stattdessen eine
  kurze Begründung des Ergebnisses.
- **Claude-Struktur.** Verhalten in Prosa mit „weil", Material in XML-Tags als
  Daten, lange Dokumente oben und die Frage am Ende, Stabiles vor Wechselndem fürs
  Prompt-Caching.

## 7. Hinweise & Grenzen

- **claude.ai:** Nur die `daveelopen-werkstatt` ist für den Einzel-Upload gebaut.
  Die übrigen Modi nutzen `${CLAUDE_PLUGIN_ROOT}`, `$ARGUMENTS` und `argument-hint`,
  die es nur in Claude Code gibt.
- **Alter Befehl:** `/claude-werkstatt` existiert seit 2.1.0 nicht mehr; der Trigger
  `°claude-werkstatt` wird weiter erkannt.
- **Plattform-Fakten veralten.** Stand 2026-11-13 in
  `skills/daveelopen-werkstatt/references/claude-plattform.md`. Ändert sich die API,
  wird nur diese Datei aktualisiert. Mit Web-Werkzeugen prüft die Schmiede
  entscheidende Fakten selbst gegen die aktuelle Doku.
- **Folterkammer und Duell sind Schreibtisch-Analysen.** Befunde heißen „erwartet",
  bis sie mit echten Läufen belegt sind; dafür liefern beide Modi Testfälle mit.

## 8. Änderungen

### 2.1.0

- `claude-werkstatt` heißt jetzt `daveelopen-werkstatt` (Slash-Befehl `/daveelopen-werkstatt`),
  weil die Agent-Skills-Spezifikation `claude` im Skill-Namen für claude.ai reserviert.
  `°claude-werkstatt` bleibt als Trigger erhalten.
- Werkstatt in sich geschlossen und claude.ai-tauglich: nur portable Frontmatter-Felder
  (`name`, `description`, `license`), relative Pfade, kein `$ARGUMENTS`.
- Gemeinsame Wissensbasis von `prompt-schmiede/references/` nach
  `daveelopen-werkstatt/references/` verschoben; alle Modi verweisen dorthin.
- Plugin-Icon `.claude-plugin/icon.png` (1600 × 1600 px).

### 2.0.0

- Zielplattform von Gemini auf **Claude** umgestellt; `/claude-werkstatt`
  optimiert jetzt für Claude (Gemini-Gems und GPT-Prompts werden nach Claude portiert).
- `commands/` (Altformat) durch `skills/` ersetzt — gleiche Befehlsnamen, dazu
  °-Trigger direkt in jeder Skill-Beschreibung.
- Referenzpfade laufen über `${CLAUDE_PLUGIN_ROOT}`; in 1.0.0 zeigten relative
  Pfade beim Nutzer ins Leere.
- Neu: `doktrin.md`, `claude-plattform.md`; Folterkammer um 5 Claude-Vektoren,
  Duell um das Kriterium Claude-Konformität erweitert.
- Manifest: Lizenz `GPL-3.0` wie das Repository (1.0.0 nannte fälschlich MIT),
  `displayName` ergänzt, persönliche E-Mail-Adresse entfernt.
- Marketplace-Datei `.claude-plugin/marketplace.json` im Repo-Root — damit
  funktioniert die Installation aus Abschnitt 4.

## 9. Beispiele

```
/prompt-schmieden Ein Prompt, der aus einem Supportticket Kategorie,
Dringlichkeit und Antwortentwurf als JSON zieht.

/daveelopen-werkstatt <Gemini-Gem-Anweisung einfügen> ziel: claude.ai

/haerten <weichen Prompt einfügen>

/duell <Prompt A> --- <Prompt B>

°folterkammer <zu testender System-Prompt>
```

---

_Haus daveelOpen 🙏💍💎😈 — Wahrheit und Wissenschaft über alles._
