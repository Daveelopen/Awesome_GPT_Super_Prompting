---
name: prompt-schmiede
description: Zentrale Prompt-Schmiede des Hauses daveelOpen. Baut, härtet, prüft und optimiert Prompts, System-Prompts, Skills und Agenten-Konfigurationen für Claude nach dem KATS-Schema und routet die °-Steuerbefehle (°prompt, °claude-werkstatt, °hart, °folterkammer, °kuerzen, °reparieren, °klonen, °duell, °skill-neu) in den passenden Modus. Greift bei °°, °hilfe oder °? sowie bei jeder Prompt-Engineering-Anfrage, die keinem einzelnen Modus eindeutig zuzuordnen ist.
argument-hint: "[°befehl] <material>"
---

# Prompt-Schmiede — daveelOpen

<material>
$ARGUMENTS
</material>

Ist der Block leer, ist das Material der Text des Nutzers nach dem Trigger. Lies zuerst die Hausdoktrin `${CLAUDE_PLUGIN_ROOT}/skills/prompt-schmiede/references/doktrin.md`; sie gilt für jeden Modus.

## Routing

Erkenne den Modus am führenden Trigger — Symbol `°…`, Slash-Befehl oder eine gleichbedeutende Bitte in eigenen Worten. Alles danach ist Material.

| Symbol | Slash | Modus | Leistung |
|---|---|---|---|
| `°prompt` | `/prompt-schmieden` | Schmieden | rohe Idee → produktionsreifer Prompt |
| `°claude-werkstatt` | `/claude-werkstatt` | Claude-Werkstatt | Prompt auf Claude zuschneiden: System-Prompt, Request-Parameter, Tools, claude.ai-Projekt, Claude Code |
| `°hart` | `/haerten` | Härten | Weichmacher, Druck-Sprache, Widersprüche, Fehltrigger raus; begründete Schranken rein |
| `°folterkammer` | `/folterkammer` | Folterkammer | Red-Teaming: Drift, Injection, Jailbreak, Halluzination, Claude-Fallstricke |
| `°kuerzen` | `/kuerzen` | Kürzen | Token-Kompression ohne Verlust von Kontext, Gründen und Schranken |
| `°reparieren` | `/reparieren` | Reparieren | Logikbrüche diagnostizieren, korrekten Ablauf rekonstruieren |
| `°klonen` | `/klonen` | Klonen | Verhaltensmuster einer Antwort als replizierbaren Prompt extrahieren |
| `°duell` | `/duell` | Duell | zwei Prompts messbar vergleichen, Hybrid empfehlen |
| `°skill-neu` | `/skill-neu` | Skill-Neu | vollständige, skriptfreie SKILL.md nach aktuellem Standard |

Ist der Modus erkannt, lade den Skill `daveilopen-prompt-schmiede:<name>` (Name = Slash-Spalte ohne `/`) und arbeite nach ihm. Als Slash-Befehl heißen die Modi vollständig `/daveilopen-prompt-schmiede:<name>`; die Kurzform `/<name>` funktioniert, solange kein anderer Befehl denselben Namen trägt.

- Nur `°°`, `°hilfe` oder `°?` → gib die Routing-Tabelle aus, sonst nichts.
- Prompt-Arbeit ohne erkennbaren Modus → Schmieden, wenn Rohmaterial (Idee, Notiz) vorliegt; Härten, wenn ein fertiger Prompt verbessert werden soll. Nenne die Wahl in einem Satz im Erklären-Teil.
- Mehrere Trigger in einer Nachricht → die Modi in der genannten Reihenfolge nacheinander, jeder mit eigenem Fazit und Erklären; das Werkstück des einen ist das Material des nächsten.
