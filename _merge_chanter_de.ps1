$ErrorActionPreference = 'Stop'
$srcPath = 'F:\aion2\11 Class Playbooks\Chanter BiS Roadmap.md'
$destPath = 'F:\aion2-de\11 Class Playbooks\Chanter BiS Roadmap.md'
$src = [IO.File]::ReadAllText($srcPath, [System.Text.UTF8Encoding]::new($false))

$season = @'
## Die Season-1-Launch-Baseline, die dieser Plan annimmt

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


'@

if ($src -notmatch 'lang:\s*de') {
  $src = $src -replace '---\r?\nchapter:', "---`r`nlang: de`r`nchapter:"
}
if ($src -notmatch 'Die Season-1-Launch-Baseline') {
  $lineMatch = [regex]::Match($src, 'Begleitplan[^\r\n]+\.')
  if (-not $lineMatch.Success) { throw 'insert point not found' }
  $needle = $lineMatch.Value
  $idx = $src.IndexOf($needle)
  $after = $idx + $needle.Length
  while ($after -lt $src.Length -and ($src[$after] -eq [char]13 -or $src[$after] -eq [char]10)) { $after++ }
  if (-not $src.Substring($after).StartsWith('## Die Rollen-Festlegung')) { throw 'insert point not found' }
  $src = $src.Substring(0, $after) + $season + $src.Substring($after)
}

$replacements = @{
  'Every other note' = 'Jede andere Notiz'
  '## The Season 1 launch baseline' = '## Die Season-1-Launch-Baseline, die dieser Plan annimmt'
  'dessen Output' = 'dessen Ergebnis'
  'Buff-Uptime' = 'Buff-Verfügbarkeit'
  'Gear-Entscheidung' = 'Ausrüstungsentscheidung'
  '[[Stat Reference]] für Stats,' = '[[Stat Reference]] für Werte,'
  'Die drei Builds teilen ein Gear-Set.' = 'Die drei Builds teilen ein Ausrüstungsset.'
  'Gleiches Gear.' = 'Gleiche Ausrüstung.'
  'Vor Gear-Graden.' = 'Vor Ausrüstungsstufen.'
  '| **1. Foundation Sweep** |' = '| **1. Grundlagen abschließen** |'
  '| **2. Unique Fill** |' = '| **2. Uniques vervollständigen** |'
  'Stark promoted.' = 'In Guides stark betont.'
  'Damage Dealer:' = 'Schadensdealer:'
  'Zwei Caveats.' = 'Zwei Einschränkungen.'
  'Kein settled Answer.' = 'Keine festgelegte Antwort.'
  'frontal vs. rear' = 'frontal vs. von hinten'
  '= flat Proc-Double;' = '= flacher Proc-Doppelter;'
  'weit vom Gear der anderen.' = 'weit von der Ausrüstung der anderen.'
  'Praxis Launch:' = 'Praxis beim Launch:'
  '22 Gear-Stufen' = '22 Ausrüstungsstufen'
  '~Hälfte Gear-Passiv-Budget' = '~Hälfte Passiv-Budget auf Ausrüstung'
  'Low-trust SEO' = 'SEO mit geringer Verlässlichkeit'
  'Kiting verliert' = 'Abstandhalten verliert'
  'Glass-Cannon' = 'Glaskanone'
  'Early Game ohne Heiler' = 'Frühe Phase ohne Heiler'
  'main-healen kann' = 'Hauptheiler-Rolle übernehmen kann'
  'Passiv-Stufen auf Gear und' = 'Passiv-Stufen auf Ausrüstung und'
  'Kein neues Gear nötig' = 'Keine neue Ausrüstung nötig'
  'Backline-Buff-Support' = 'Buff-Support aus der zweiten Reihe'
  'Kann wirklich main-healen.**' = 'Kann wirklich als Hauptheiler fungieren.**'
  'Damage Dealer: fungibler' = 'Schadensdealer: austauschbarer'
  '### Unterschiede zum Damage-Dealer-Plan' = '### Unterschiede zum Schadensdealer-Plan'
  'Convenience; Kantor' = 'Komfort; Kantor'
  'Buff-/Schild-**Uptime ist Output**' = 'Buff-/Schild-**Verfügbarkeit ist Leistung**'
  'welchem Gear-Slot**' = 'welchem Ausrüstungsslot**'
  'echtes Gear-Ziel' = 'echtes Ausrüstungsziel'
  'CP-Optimierung strippt' = 'CP-Optimierung entfernt'
  'Einmal-Layer:' = 'Einmaliger Durchlauf:'
  '**No-Cleric Main Heal**' = '**Main-Heal ohne Kleriker**'
  'No-Cleric Main Heal wertvoller' = 'Main-Heal ohne Kleriker wertvoller'
}
foreach ($k in $replacements.Keys) { $src = $src.Replace($k, $replacements[$k]) }

$dir = Split-Path $destPath
if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }
[IO.File]::WriteAllText($destPath, $src, [System.Text.UTF8Encoding]::new($false))
$count = ([regex]::Matches($src, 'Every other note')).Count
Write-Output "Wrote $destPath"
Write-Output "Every other note matches: $count"
