# -*- coding: utf-8 -*-
from pathlib import Path

src_path = Path(r"F:\aion2\11 Class Playbooks\Chanter BiS Roadmap.md")
dest_path = Path(r"F:\aion2-de\11 Class Playbooks\Chanter BiS Roadmap.md")
src = src_path.read_text(encoding="utf-8")

season = """## Die Season-1-Launch-Baseline, die dieser Plan annimmt

Global Launch ist 2026-10-05 mit Founder-Frühzugang ab 2026-09-30, und NCs
eigene gamescom-Aussagen setzen den Launch-Build ungefähr auf koreanische
Launch-Parität. Die Zahlen, die einen Kantor-Plan konkret prägen:

| Dimension | Season-1-Wert | Aktueller KR-Wert | Konfidenz |
| --- | --- | --- | --- |
| Level-Cap | **45** | 50 | Für dieses Vault bestätigt |
| Item-Level-Spanne | **0–3.800** | 4.800 | 4.000+ ist Chapter 1. Siehe [[Item Level vs Combat Power]] |
| Gruppengröße | 4 | 5 | Von NC auf der gamescom bestätigt |
| Raid-Größe | 8 | 10 | Von NC auf der gamescom bestätigt |
| **Stigma-Slots** | **4** | 6 | Aus KR-Patch-Chronologie abgeleitet, mittel-hoch |
| **Stigma-Level-Cap** | **20** | 25 | Abgeleitet, mittel |
| Daevanion-Boards | Nezekan, Zikel, Vaizel, Triniel | plus Marchutan und Yustiel | Abgeleitet, mittel |
| Arkana-Slots | 5 | 10 | Abgeleitet, mittel |
| Verfügbare Arkana-Sets | Primal Vigor, Magic Armor | 7 | Abgeleitet, mittel |
| Ausrüstungsgrad-Obergrenze | **Unique** | Heroic | Mittel, Einzelquelle |
| Accessory-Slots | Necklace, Earrings, Rings, Bracelet, Belt, Amulet | plus Brooch, Pendant, Seal | Mittel |

Der fünfte Stigma-Slot kam in KR am 2026-03-25, der sechste plus Level 25 am
2026-07-01 — **jeder koreanische Kantor-Stigma-Guide, den du findest, rechnet mit
fünf oder sechs Slots; du hast vier**. Diese eine Tatsache invalidiert mehr
koreanischen Kantor-Content als alles andere in diesem Plan. Siehe
[[Global Launch Differences]] und [[Stigmas]].

Vierer-Gruppen beim Launch erhöhen auch den Wert der **Main-Heal-ohne-Kleriker**-
Variante — siehe Build-Tabelle unten.

"""

if "lang: de" not in src.split("---", 2)[1]:
    src = src.replace("---\nchapter:", "---\nlang: de\nchapter:", 1)

if "Die Season-1-Launch-Baseline" not in src:
    needle = "Begleitplan für die andere Support-nahe Klasse: [[Templar BiS Roadmap]]."
    idx = src.index(needle) + len(needle)
    while idx < len(src) and src[idx] in "\r\n":
        idx += 1
    if not src[idx:].startswith("## Die Rollen-Festlegung"):
        raise SystemExit("insert point not found")
    src = src[:idx] + season + src[idx:]

replacements = [
    ("Every other note", "Jede andere Notiz"),
    ("## The Season 1 launch baseline", "## Die Season-1-Launch-Baseline, die dieser Plan annimmt"),
    ("dessen Output", "dessen Ergebnis"),
    ("Buff-Uptime", "Buff-Verfügbarkeit"),
    ("Gear-Entscheidung", "Ausrüstungsentscheidung"),
    ("[[Stat Reference]] für Stats,", "[[Stat Reference]] für Werte,"),
    ("Die drei Builds teilen ein Gear-Set.", "Die drei Builds teilen ein Ausrüstungsset."),
    ("Gleiches Gear.", "Gleiche Ausrüstung."),
    ("Vor Gear-Graden.", "Vor Ausrüstungsstufen."),
    ("| **1. Foundation Sweep** |", "| **1. Grundlagen abschließen** |"),
    ("| **2. Unique Fill** |", "| **2. Uniques vervollständigen** |"),
    ("Stark promoted.", "In Guides stark betont."),
    ("Damage Dealer:", "Schadensdealer:"),
    ("Zwei Caveats.", "Zwei Einschränkungen."),
    ("Kein settled Answer.", "Keine festgelegte Antwort."),
    ("frontal vs. rear", "frontal vs. von hinten"),
    ("= flat Proc-Double;", "= flacher Proc-Doppelter;"),
    ("weit vom Gear der anderen.", "weit von der Ausrüstung der anderen."),
    ("Praxis Launch:", "Praxis beim Launch:"),
    ("22 Gear-Stufen", "22 Ausrüstungsstufen"),
    ("~Hälfte Gear-Passiv-Budget", "~Hälfte Passiv-Budget auf Ausrüstung"),
    ("Low-trust SEO", "SEO mit geringer Verlässlichkeit"),
    ("Kiting verliert", "Abstandhalten verliert"),
    ("Glass-Cannon", "Glaskanone"),
    ("Early Game ohne Heiler", "Frühe Phase ohne Heiler"),
    ("main-healen kann", "Hauptheiler-Rolle übernehmen kann"),
    ("Passiv-Stufen auf Gear und", "Passiv-Stufen auf Ausrüstung und"),
    ("Kein neues Gear nötig", "Keine neue Ausrüstung nötig"),
    ("Backline-Buff-Support", "Buff-Support aus der zweiten Reihe"),
    ("Kann wirklich main-healen.**", "Kann wirklich als Hauptheiler fungieren.**"),
    ("Damage Dealer: fungibler", "Schadensdealer: austauschbarer"),
    ("### Unterschiede zum Damage-Dealer-Plan", "### Unterschiede zum Schadensdealer-Plan"),
    ("Convenience; Kantor", "Komfort; Kantor"),
    ("Buff-/Schild-**Uptime ist Output**", "Buff-/Schild-**Verfügbarkeit ist Leistung**"),
    ("welchem Gear-Slot**", "welchem Ausrüstungsslot**"),
    ("echtes Gear-Ziel", "echtes Ausrüstungsziel"),
    ("CP-Optimierung strippt", "CP-Optimierung entfernt"),
    ("Einmal-Layer:", "Einmaliger Durchlauf:"),
    ("**No-Cleric Main Heal**", "**Main-Heal ohne Kleriker**"),
    ("No-Cleric Main Heal wertvoller", "Main-Heal ohne Kleriker wertvoller"),
    ("| Ziel-Gear |", "| Ziel-Ausrüstung |"),
    ("Quest- und Feld-Gear;", "Quest- und Feld-Ausrüstung;"),
    ("`-Uptime", "`-Verfügbarkeit"),
    ("Gruppen-Damage-Buff", "Gruppen-Schadens-Buff"),
    (" shred Boss-", " reduziert Boss-"),
    (" skaliert Heals;", " skaliert Heilungen;"),
    ("Größere Heals →", "Größere Heilungen →"),
    ("On-Hit,", "bei Treffer,"),
    ("heal proportional", "Heilung proportional"),
    ("CD-Spec hält Uptime", "CD-Spec hält Verfügbarkeit"),
    ("aus Arcana/Gear**", "aus Arcana/Ausrüstung**"),
    ("mehr Gear/Arcana", "mehr Ausrüstung/Arcana"),
    ("Schadenswiderstands-Shred", "Schadenswiderstands-Reduktion"),
    ("Gruppen-Shred aus", "Gruppen-Reduktion aus"),
    ("Frontal vs. rear", "Frontal vs. von hinten"),
    ("low confidence", "geringe Konfidenz"),
    ("*Uptime auf", "*Verfügbarkeit auf"),
    ("Buchstabe Rauschen", "Buchstaben-Rauschen"),
    ("supportive Stigmas", "unterstützende Stigmas"),
    ("Main-Heal-Ersatz", "Hauptheiler-Ersatz"),
    ("Low-Level-Stigma", "Stigma niedriger Stufe"),
    ("FPS/Latenz-Caveat", "FPS/Latenz-Einschränkung"),
]
for old, new in replacements:
    src = src.replace(old, new)

dest_path.parent.mkdir(parents=True, exist_ok=True)
dest_path.write_text(src, encoding="utf-8")
count = src.count("Every other note")
print(f"Wrote {dest_path}")
print(f"Every other note matches: {count}")
