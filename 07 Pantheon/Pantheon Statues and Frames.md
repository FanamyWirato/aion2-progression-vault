---
chapter: "07 Pantheon"
system: Pantheon Statues and Frames
type: progression-system
unlock: "first statues from the level 22 ascension (각성) reward chain; all 17 slots available immediately"
account_wide: false
cadence: "continuous"
gates: ["Nightmare Layer I for shop statues", "item level 2,400 for the Season 1 colossus", "Draupnir Conquest x10 for Transcended Bakarma"]
currencies: ["Dream Fragments (몽환의 파편)", "Shugo Festa Coins", "Kinah", "Traces of Painting (명화의 잔흔)"]
region_verified: ["KR", "TW"]
patch: "KR Season 1 (2025-11-19) baseline, updated through Season 3 (2026-04-08); TW cross-check from Season 4 guides"
confidence: medium
tags:
  - aion2/progression
  - aion2/pantheon
---

# Pantheon Statues and Frames

> **In one sentence:** the Pantheon has exactly seventeen slots — one colossus,
> four statues and twelve artworks — and which decorations you put in them
> decides how your Lord stat budget is distributed across the ten domains.

## Why it matters

Slot scarcity is the whole game here. Sixteen statues existed in Season 1 and
only four can be placed. Roughly seventy-five artworks existed and only twelve
can hang. Because points are simply summed per domain, the layout question
reduces to a knapsack problem: fill seventeen slots so that the domains you
care about end up highest, without wasting slots on domains that do nothing
for your role.

The twelve artwork slots are the part players underrate. Individually an
artwork is worth 3 to 5 points per domain against a colossus's 45, but twelve
of them stacked on the same two domains produce more total value than the
centre plinth. A Chinese endgame layout reached Wisdom 45 and Illusion 45 from
artworks alone, which matches the colossus's entire output.

This note is the catalogue and the layout guide. For what the domains actually
do, see [[Pantheon Stats]]. For where the currency comes from, see
[[Nightmare Mode]].

## How it works

### Slot structure

| Class | Korean | Aliases seen in sources | Slots | Position |
| --- | --- | --- | --- | --- |
| Colossus | 거상 | Great statue, 大雕像 (CN/TW), "centre statue" | 1 | Central plinth |
| Statue | 조각상, 석상 | Sculpture, small statue, 小雕像 / 小金像 (CN/TW) | 4 | Four pedestals around the plinth |
| Artwork | 명화, 액자 | Painting, frame, picture frame, 名画 / 畫框 (CN/TW) | 12 | Wall frames on the outer ring |

There is no separate "artifact" slot. The word appears only in the item name
Statue: Eternal Artifact (조각상: 영원의 아티팩트), which is an ordinary statue.

Placement rules that hold across every source checked:

- Placement is free, instant and fully reversible. There is no cost, cooldown
  or consumption. A Korean guide's FAQ states outright that you can swap
  freely, so experimenting carries no risk.
- Points from placed decorations are summed per Lord domain. Nothing about the
  physical position within a class matters; a statue in pedestal 1 and the same
  statue in pedestal 3 are identical.
- Only placed decorations count. Owning a decoration does nothing.
- Grade drives the point value. The same conceptual decoration at a higher
  grade gives substantially more points, and higher grades also carry more
  domains at once.
- Since KR Season 3 (2026-04-08) three presets can be saved, each with its own
  set of placed decorations, and a Pantheon entry was added to the preset
  set-equip feature so a preset switch can change Pantheon and gear together.

### Grades

Sources use local colour names. The mapping that reconciles them:

| Grade | KR | Colour in CN/TW guides | Typical artwork value |
| --- | --- | --- | --- |
| Rare | 희귀 | blue (蓝色) | 3 points across 2 domains |
| Unique | 유일 | gold/yellow (黄色/金色) | 4 points across 2 to 3 domains |
| Heroic | 영웅 | orange or red (橙色/红色) | 5 points across 4 domains |

Confidence medium on the exact per-grade artwork numbers. They are inferred
from a Chinese graduation layout that sums to Wisdom 15 + 12 + 18 = 45 across
three orange, three gold and six blue artworks, corroborated by a Taiwanese
healer guide reporting that gold artworks give "4 Life, 4 Fate" and by the
aion2hub database entry for a Heroic artwork giving +5 in four domains.

### Upgrade and fusion

No upgrade, enhancement, fusion or reroll mechanic for Pantheon decorations
appears in any patch note or database entry I checked. The aion2hub database
lists Pantheon decorations with max enchant 0. You improve the Pantheon by
acquiring better decorations, not by upgrading the ones you have.

One Korean blog claims that the Season 3 Unique-to-Heroic succession feature
should be spent on Pantheon items first. The Season 3 patch notes describe
that feature as applying to equipment, and I found no confirmation that
Pantheon decorations are eligible. Treat as unverified; see
[[Succession and Transfer]].

Artworks are craftable rather than upgradeable. Fragments plus a frame
crafting toolbox produce a finished artwork, and one expedition recipe has a
20 percent success rate, so artwork acquisition behaves more like
[[Crafting]] than like [[Enchanting]].

## Unlock and gates

| Slot class | First fill | Best-in-slot gate |
| --- | --- | --- |
| Statues | Level 22 ascension rewards give two statues | Draupnir Conquest cleared 10 times |
| Colossus | An early Rare colossus (Warden Santras) is available to normal levelling players | Nightmare Zikel's Apparition challenge level 1, item level around 2,400 |
| Artworks | World boss drops, region quests and trading post purchases start early | Heroic world boss artworks and dungeon achievement artworks, both slow |

## Inputs: currencies, materials, sources

| Input | What it buys | Source | Notes |
| --- | --- | --- | --- |
| Dream Fragments | Colossus, three or more statues, later-season statues | [[Nightmare Mode]] | Purchase history is not reset between seasons and unspent fragments carry over |
| Draupnir Conquest clear count | Statue: Transcended Bakarma | Expedition Conquest, 10 clears | Last-boss-only runs are the efficient route |
| Fire Temple achievement stage 4 | Colossus: Kromede's Desire | Achievements | Required 32 achievements while only 27 existed in Season 1 |
| Shugo Festa Coins | Artwork fragments and frame crafting toolboxes | Shugo Festa | Advanced toolbox 50 coins, Superior toolbox 500 coins |
| Traces of Painting (명화의 잔흔) | Expedition artworks | Expedition Conquest clears | 10 traces per attempt, 20 percent success |
| Kinah | Finished artworks | Trading post | Taiwanese players reported 600,000 to 5,500,000 kinah per frame |
| World boss kills | Heroic artworks | Named world bosses | Artwork: Eternal Gartua drops from the Lv 70 named world boss in Verteron |
| Season ranking placement | Seasonal statues and artworks | [[Arenas Sieges and Seasons]], [[Abyss Points and Ranks]] | Effects expire; see Traps |

## Progression path

### Colossi

Four colossi existed in Season 1. All four grant the same three domains and
differ only in magnitude, which makes the choice purely a question of what you
can obtain.

| Colossus | Korean | Grade | Lord stats | Source | Confidence |
| --- | --- | --- | --- | --- | --- |
| Warden Santras | 교도관 산트라스 | Rare | Justice 35, Time 35 | Available to normal levelling players; the colossus "everyone is wearing" early | high |
| Zikel's Thoughtform | 지켈의 사념체 | Unique | Justice 45, Time 45, Destruction 45 | Nightmare exchange shop, 14,000 Dream Fragments, unlocked by clearing Zikel's Apparition challenge level 1 | high |
| Kromede's Desire | 크로메데의 욕망 | Unique | Justice, Time, Destruction (values not published) | Fire Temple achievement stage 4, requiring 32 achievements | medium |
| Guardian General Nahma | 수호신장 나흐마 | Heroic | Not published | Drops from the Abyss world boss Guardian General Nahma | low |

Aliases: the same colossus appears in English translations as "Zikel's Thought
Entity" and as "Zikel's Apparition" (the Nightmare boss shares the name). The
Taiwanese board calls it simply "the Destruction colossus". Later Taiwanese
Season 4 guides name **Ascended Atheron** (각성 아테론) as the best-in-slot
colossus, which corresponds to the Nightmare Layer IV boss of the same name and
is therefore a later-content item, not a launch one.

The practical Season 1 answer is Zikel's Thoughtform. Kromede's Desire was
mathematically unobtainable at Korean launch because the achievement pool was
too small, and Nahma requires an Abyss world boss drop.

The upgrade from Warden Santras to Zikel's Thoughtform is the largest single
step in the chapter: it adds 10 points each to Justice and Time and 45 points
of Destruction from nothing.

### Statues

Sixteen statues existed in Season 1 and four can be placed. Season 1 statues
only carry three domains — Freedom, Death and Space — and every statue below
Unique grade carries exactly two of them in one of the three possible pairs.
Transcended Bakarma is the only Season 1 statue with all three.

| Statue | Korean | Grade | Lord stats | Source | Confidence |
| --- | --- | --- | --- | --- | --- |
| Transcended Bakarma | 초월한 바카르마 | Unique | Freedom 12, Death 12, Space 12 | Draupnir Conquest cleared 10 times (achievement) | high |
| Fortress Guardian Notun | 요새 수호자 노툰 | Rare | Death 10, Space 10 | Nightmare shop, 8,000 fragments, after Notun challenge level 10 | high |
| Asar's Mirror | 아사르의 거울 | Rare | Death 10, Space 10 | Unclear; multiple players report simply owning it, likely a quest or levelling reward | medium |
| Furious Feruk | 광폭한 페르크 | Rare | Death 8, Space 8 | Nightmare shop, 5,000 fragments | high |
| Fafnir's Poison Blood | 파프니르의 독혈 | Rare | Freedom 8, Death 8 | Nightmare shop | medium |
| Eternal Artifact | 영원의 아티팩트 | Rare | Freedom 10 | Level 22 ascension reward chain | medium |
| Fragment of Dream | 꿈의 파편 | Rare | Freedom 8, Death 8 | Ascension reward chain | medium |

Nightmare boss to statue domain mapping, for planning which boss to push
first:

| Nightmare boss | Domains on its statue |
| --- | --- |
| Gatekeeper Pinopi | Death, Space |
| Furious Feruk | Death, Space |
| Fortress Guardian Notun | Death, Space |
| Fafnir's Poison Blood | Freedom, Death |
| Wraith Giselle | Freedom, Space |
| Mutated Gerod | Freedom, Space |

Seasonal ranking statues sit outside this catalogue because their effects are
temporary. Known examples from the database: Statue: Laboratory Chief Nazmun
(Transcendence Season 1, Master to Grand Master), Statue: Silvermoon Asmodian
Leader (Abyss Season 1, Marshal to General), Statue: Glimmering Elyos Leader
(Abyss Season 1, 5-Star to 1-Star Officer), Statue: Void Talisra (ranking), and
Statue: Submerged Emon [Season 2] (Transcendence Season 2). Each of these
states that the effect is maintained only until the end of the following
season.

### Artworks

Roughly seventy-five artworks existed in Season 1 and the count has grown with
each season; the item database now lists well over a hundred. Artworks carry a
different domain pool from statues, centred on Wisdom, Illusion, Life and Fate.
Notably, **no artwork grants Destruction**, which is part of why the colossus
is the only realistic source of Destruction.

| Artwork | Grade | Lord stats | Source | Confidence |
| --- | --- | --- | --- | --- |
| Eternal Gartua | Heroic | Fate 5, Life 5, Wisdom 5, Illusion 5 | Lv 70 named world boss, Verteron; also a conversion recipe | high (client data) |
| Fire Temple | Not published | Life, Wisdom, Fate | Crafted from fragments dropped by Fire Temple Conquest | high |
| Eldes Temple | Not published | Not published | Shugo Festa: 5 of each festival fragment plus 10 Superior frame crafting toolboxes, around 5,000 Shugo Festa coins total | high |
| Generic Shugo Festa artwork | Not published | Not published | 10 festival fragments plus 10 Advanced frame crafting toolboxes, around 500 coins total | high |
| Expedition artwork | Not published | Not published | 10 Traces of Painting, 20 percent craft success | high |
| Kantas Valley, Ellun River Marsh, Tolbas Forest | Rare to Unique | Illusion and Wisdom combinations | Named per the Shugo Festa mini-game they are tied to | medium |
| Kaisinel's Illusion [Season 2] | Not published | Not published | Nightmare Season 2 ranking reward; temporary effect | high |

The three highest-priority artworks for a damage build, per the Chinese
graduation guide, are the three Unique-grade artworks that roll the
Wisdom + Illusion + Life combination. Two of them drop from same-named world
bosses and the third comes from a dungeon achievement. This is the hardest part
of the whole chapter to complete.

## Priorities and breakpoints

### Recommended layout: PvE damage

This is the layout the Korean and Chinese endgame guides converge on.

| Slot | Fill | Domains gained |
| --- | --- | --- |
| Colossus | Zikel's Thoughtform | Justice 45, Time 45, Destruction 45 |
| Statue 1 | Transcended Bakarma | Freedom 12, Death 12, Space 12 |
| Statues 2–4 | Best available Death + Space statues (Notun, Asar's Mirror, Feruk) | Death 28, Space 28 |
| Artworks 1–3 | Heroic artworks | Wisdom 15, Illusion 15, Life 15, Fate 15 |
| Artworks 4–6 | Unique Wisdom + Illusion + Life artworks | Wisdom 12, Illusion 12, Life 12 |
| Artworks 7–12 | Rare Wisdom + Illusion artworks | Wisdom 18, Illusion 18 |

Approximate totals: Wisdom 45, Illusion 45, Justice 45, Time 45,
Destruction 45, Life 27, Death 40, Space 40, Freedom 12, Fate 15.

Reasoning: Wisdom is the damage-defining domain because it drives Smite, which
doubles a hit and can itself critically strike. Illusion is second because
cooldown reduction compounds with everything. Death is taken through statues
because statues cannot give Wisdom, so the statue slots are spent on the best
domains available to them, and Death (critical hit) beats Freedom (accuracy)
once accuracy is already overflowing in most content.

Freedom deliberately loses value at endgame. The Chinese guide notes that
outside one raid boss, accuracy overflows in current dungeons, and few PvP
players stack evasion, so Space (move speed) beats Freedom for the remaining
statue slots. This inverts the earlier Korean archer guide that recommended
maximising Freedom and Death, which was written for a boss-hit-rate problem
that later gear solved. Both are correct for their patch; use the accuracy
overflow test on your own character to decide.

### Recommended layout: PvE support and tanking

| Slot | Fill | Reasoning |
| --- | --- | --- |
| Colossus | Zikel's Thoughtform, or a Justice-heavy colossus if available | Justice for defence and Perfect proc, Time for cast speed |
| Statues | Space and Death pairs; Space is valuable for uptime and positioning | Statues offer nothing defensive beyond Space's block chance |
| Artworks | Prioritise Life and Fate over Wisdom | Life gives HP and regeneration, Fate gives spirit and Endurance proc, which is what keeps a healer casting |

A Taiwanese healer guide is explicit: for a survivability-first healer, take a
Destruction or Life-oriented colossus, make sure every statue at least carries
Space and is Rare grade or better, and go all-gold on artworks without
bothering to stack Wisdom, because gold artworks give 4 Life and 4 Fate which
is "very strong" for that role.

### Recommended layout: PvP and sieges

| Slot | Fill | Reasoning |
| --- | --- | --- |
| Colossus | Zikel's Thoughtform | Time 45 is the single most requested PvP domain |
| Statues | Freedom and Space pairs | Accuracy matters again against players who stack evasion, and move speed decides sieges |
| Artworks | Time and Illusion first, then Life | Cooldown reduction and combat speed beat a Smite proc when the target has Smite Resist |

The consistent PvP advice across Korean sources is to move from Wisdom towards
Time. A Smite proc is unreliable against a target stacking Smite Resist,
whereas combat speed and cooldown reduction are unconditional. Save this as a
separate preset. See [[PvP Progression]] and [[Arenas Sieges and Seasons]].

## Costs and math

- Season 1 core purchases: 14,000 fragments (Zikel's Thoughtform) + 8,000
  (Notun) + 5,000 (Feruk) = 27,000 Dream Fragments, against a season ceiling of
  about 82,740 for a player who never missed a daily attempt.
- Eldes Temple artwork: 10 Superior frame crafting toolboxes at 500 Shugo Festa
  coins each, plus 5 of each festival fragment, so roughly 5,000 coins.
- Standard Shugo Festa artwork: 10 Advanced toolboxes at 50 coins each plus 10
  fragments, so roughly 500 coins.
- Expedition artwork: 10 Traces of Painting per attempt at a 20 percent success
  rate, so an expected 50 traces per finished artwork.
- Trading post artworks in Taiwan ran 600,000 to 5,500,000 kinah each, with
  supply thin enough that a player reported only six of twelve frames listed.

## Traps and mistakes

- Spending Dream Fragments before owning a colossus. Everything else in the
  Nightmare shop is a smaller gain per fragment.
- Buying the Nightmare cosmetic wings at 160,000 fragments before the Pantheon
  is complete. That is more than a full season of income for one appearance.
- Filling statue slots with Freedom pairs at endgame. Once accuracy overflows,
  those points do nothing; audit your accuracy against the boss you actually
  fight.
- Relying on seasonal ranking decorations. NC removed Season 1 ranking
  decoration effects in the Season 3 patch while leaving the items in
  inventories, so a layout built on them silently degrades at a season
  boundary.
- Assuming an artwork will eventually give Destruction. None do; that domain
  comes from the colossus.
- Buying duplicate artworks in the hope of stacking them. There are twelve
  slots and there is no evidence duplicates stack beyond occupying separate
  slots.
- Chasing Kromede's Desire early. It was gated behind more achievements than
  the game contained at Korean launch.

## Global launch notes

- Slot counts (1 / 4 / 12) are Season 1 design and should be identical at
  global launch.
- If global launch ships Nightmare Layer I only, the reachable colossus is
  Zikel's Thoughtform and the reachable statues are the Layer I set: Pinopi,
  Feruk, Fafnir's Poison Blood, Wraith Giselle, Notun and Gerod. Layer II to IV
  statues, and the stronger Ascended Atheron colossus, are later content.
- Transcended Bakarma depends on Draupnir Conquest being present at launch.
  Draupnir is expected in the launch dungeon list, so this should be the first
  Unique statue available to global players too.
- Pantheon presets arrived in KR Season 3. If global launches without them,
  every PvE-to-PvP switch is a manual seventeen-slot rearrangement.
- All stat values in this note come from the KR Season 1 to Season 3 window.
  NC has rebalanced other systems at global launch before, so treat the numbers
  as strong expectations rather than guarantees.
- **Launch Scale Test:** buy Pantheon artwork from the shop with **generic**
  Shugo fragments. KR forced a specific minigame for the matching fragment,
  then a craft. See [[Shugo Festa]] and [[Global Launch Differences]].

## Open questions

- [ ] Exact Lord stat values for Kromede's Desire and Guardian General Nahma.
      Would be settled by the questlog.gg or aion2hub database entries for
      those two items.
- [ ] The precise per-grade artwork point values. Would be settled by three
      database entries, one Rare, one Unique and one Heroic artwork, read side
      by side.
- [ ] Where Statue: Asar's Mirror actually comes from. Multiple players own it
      without remembering how.
- [ ] The identity of the three Unique artworks that roll Wisdom + Illusion +
      Life, and which world bosses drop the first two.
- [ ] Whether the full sixteen-statue Season 1 list is anywhere published; only
      seven are documented above.
- [ ] Whether duplicate copies of the same artwork can occupy multiple frames.
- [ ] Whether the Unique-to-Heroic succession feature applies to Pantheon
      decorations.

## Sources

- [아이온2 만신전 공략 — 정보의 호수](https://joinfo.tistory.com/41) — KR, first-hand guide. Slot counts, the four colossi, the sixteen-statue count, Transcended Bakarma and Notun values, Eldes Temple and Shugo Festa artwork recipes, the Fire Temple artwork domains, and the 20 percent expedition craft rate.
- [충전권 추천: 악몽 도전권 (지켈의 사념체 파밍 + 만신전 세팅)](https://www.inven.co.kr/board/aion2/6444/565) — KR, 2025-12-01. Exact values for Zikel's Thoughtform and Warden Santras, four statue values, the Season 1 three-domain statue restriction, shop prices, and the Kromede's Desire achievement shortfall.
- [【永恒之塔2】主神殿输出毕业搭配](http://news.17173.com/content/12162025/052013463.shtml) — CN guide to the KR/CN client, 2025-12-16. The 3 orange / 3 gold / 6 blue graduation artwork layout, the Wisdom 45 and Illusion 45 totals, the statement that no artwork gives Destruction, the domain priority Wisdom > Illusion > Life > Fate, and the accuracy-overflow argument for Space over Freedom.
- [《AION2》治癒星養成攻略](https://jisu.tw/aion2-治癒星養成攻略/) — TW, healer guide. The support layout, the "4 Life 4 Fate" gold artwork value, and the advice to guarantee Space on every statue.
- [【討論】精靈星萬神殿 唯一選擇 — 巴哈姆特](https://forum.gamer.com.tw/Co.php?bsn=82913&sn=11566) — TW forum. Independent confirmation that the Destruction colossus comes from clearing the final Nightmare boss stage 1 at around 2,400 power, and market prices for artworks.
- [Artwork: Eternal Gartua — AION 2 Item Database](https://aion2hub.com/database/items/514310111) — client-extracted data. A concrete Heroic artwork stat line, the world boss source, the 200-point cap and the conversion note.
- [Items - pantheon - artwork | questlog.gg](https://questlog.gg/aion-2/en/db/items/pantheon/artwork) — client-extracted data. Confirms the Pantheon item taxonomy and the artwork grade spread from Epic to Legend.
- [Statue: Laboratory Chief Nazmun | questlog.gg](https://questlog.gg/aion-2/en/db/item/534320043) — client-extracted data. Establishes that seasonal ranking statues state a fixed expiry at the end of the following season.
- [Third Season Update | Aion2 PB](https://aion2pb.com/articles/Third_Season_Update) — KR patch notes in translation, 2026-04-09. Pantheon presets, the preset set-equip integration, the Season 3 statue shop tab, and the removal of Season 1 ranking decoration effects.
- [Aion 2 Man Pantheon Core Stat Setting Guide](https://vortexgaming.io/en/postdetail/628306) — KR video guide in translation. The archer-oriented Freedom and Death statue layout, the ascension-reward statues, Fafnir's Poison Blood, and the Wisdom-centred artwork advice with Time for PvP.
- [2026 아이온2 만신전 세팅 종결](https://game.savetip.co.kr/aion2-mansinjeon-setting-guide/) — KR, 2026. The Nightmare boss to statue domain mapping and the toolbox coin costs. Used as secondary confirmation.
- [《永恒之塔2》台服S4赛季全职业通用毕业攻略](https://news.17173.com/z/aion2/content/08132026/184309275.shtml) — TW/CN, 2026-08-13. Names Ascended Atheron as the later best-in-slot colossus and confirms the Pantheon needed no rework across a season boundary.
