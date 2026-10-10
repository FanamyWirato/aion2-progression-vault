---
chapter: "01 Foundations"
system: Item Level and Combat Power
type: progression-system
unlock: "item level from character creation; Combat Power display added KR 2026-03-18"
account_wide: false
cadence: "continuous"
gates: ["item level 200", "item level 1000", "item level 1600", "item level 2200", "item level 2400", "item level 2700", "item level 3800 Season 1 ceiling"]
currencies: ["Odd Energy", "Kinah", "Enhance Stones"]
region_verified: ["KR", "TW"]
patch: "KR 2026-03-18 (Combat Power introduced), 2026-07-01 (Chapter 1 gates)"
confidence: high
tags:
  - aion2/progression
  - aion2/foundations
---

# Item Level vs Combat Power

> **Season 1 power range: 0–3,800.** That is the full unlock slider at global
> launch. Korean guides that list 4,000, 4,100, 4,500, 4,800 or 4,950 are
> describing Chapter 1 and later, after the level-50 rescale. They are not
> launch numbers. See the gate table below.

> **In one sentence:** Item level (아이템 레벨, also Gear Score) is the number
> the game checks to let you into a dungeon, and Combat Power (전투력) is the
> number other players check to let you into their party.

## Why it matters

These two numbers move at different speeds and for different reasons, and
almost every "why am I doing no damage at the required item level" complaint is
the gap between them. Item level is close to a plain sum of the item levels
printed on your gear. It does not read your stat rolls, your manastones, your
soul imprint, your stigma levels or your pet collection. Combat Power reads all
of that and nothing else. You can therefore be simultaneously qualified for a
dungeon and useless in it, which is exactly the situation the Combat Power
system was introduced to expose.

There is also a terminology hazard that costs people real resources. Before
2026-03-18 the KR community used the word 전투력 ("combat power") as its
everyday name for item level, because item level was the only aggregate number
the game displayed. Korean guides from that era with targets like "전투력
1,600" or "전투력 2,000까지" mean **item level** 1,600 and 2,000. Guides from
after 2026-03-18 with targets like "710k" mean **Combat Power**. Machine
translation flattens both to "Combat Power". Use the magnitude to tell them
apart: four digits is item level, five or six digits is Combat Power.

## How it works

### Item level

The formula, verified against extracted client data by aion2hub, is a sum:

```
Item level = Σ base item level of each equipped piece
           + Σ enchant levels
           + Σ breakthrough levels
           + Daevanion crystal points spent on the boards
```

Every +1 in any of those terms is exactly +1 item level. The in-game total
reads a little higher than this because the game also folds in soul-bind
sub-stats, manastones, pets and titles, which are not itemised per gear piece
and so cannot be modelled exactly by third-party planners.

Practical consequences of the formula:

- **Spread enchants evenly** rather than pushing one piece. Ten pieces at +5
  and one piece at +50 give the same item level, but the even spread is far
  cheaper because enchant costs and failure risk climb with level.
- **Empty slots are pure loss.** A missing earring is its entire base item
  level plus every enchant you could have put on it. Filling empty accessory
  slots from the market is the cheapest item level in the game.
- **Daevanion points are item level.** Each crystal point spent is +1. The
  Marchutan board added on 2026-02-25 has over 150 nodes and needs over 230
  points in total; completing it is worth over 150 item level on its own.
- **Belt and Amulet are gear slots.** The Belt of Nobility and Revelation
  Amulet are easy to forget because they upgrade through stronghold scrolls and
  world feathers rather than dungeon drops, and leaving them at +0 is free item
  level thrown away. Chapter 1 allowed both to be promoted to Hero grade.

### Combat Power

Introduced in KR on 2026-03-18 as a toggle in the character information UI, so
you can display either item level or Combat Power. The developers stated the
intent explicitly: to replace the third-party stat aggregator sites the
community had been using as a party-entry standard with a number the game
itself computes. Key properties:

- It is computed **server-side** and the formula is not in the client data. No
  third-party tool publishes a CP value, and aion2hub deliberately refuses to
  because NCSoft adjusts the weights.
- It reflects **both offence and defence**. This was a design decision: high
  attack with no survivability produces no damage in higher-tier dungeons
  because you are dead, so defence carries weight.
- **Consumable and skill buffs are excluded** by design. In practice a bug at
  introduction caused some buff skills to be counted, and CP was observed to
  rise when buffs were active. This was slated for a fix.
- **PvP stats are not reflected.** A PvP-focused title or set contributes
  nothing to your displayed CP.
- **The wardrobe contributes**, which surprises people.

Reported CP value per stat point, from a Korean video guide translated by Vortex
Gaming shortly after introduction. Treat as confidence medium: these are one
source's measurements, and the developers announced they would retune them.

| Stat | CP per point |
| --- | --- |
| Damage Increase, Damage Reduction, Critical Damage Increase or Reduction, Boss Damage Increase or Reduction, PvP Damage Increase or Reduction, Healing Increase or Reduction — each 1% | 100 |
| Movement Speed, Attack Speed, Cast Speed — each 1% | 100 |
| Attack Power (1 point) | 1.25 |
| Main attribute (1 point) | 1.25 |
| Defense (1 point) | 1 |
| Accuracy (1 point) | 0.25 |
| Critical Hit (1 point) | 0.25 |
| Sub-attribute (1 point) | 0.25 |
| HP, MP (1 point) | 0.05 |
| Penetration (1 point) | 10, acknowledged as a bug; intended 1 to 1.25 |

Combat Power from stigma levels, same source:

| Stigma level range | CP gained |
| --- | --- |
| 1 to 5 | about 900 |
| 5 to 10 | about 2,000 |
| 10 to 15 | about 3,500 |
| 15 to 20 | about 6,000 |

Individual upgrade magnitudes measured by an Inven community member on patch
day, useful for calibrating what a CP number means:

| Change | CP gained |
| --- | --- |
| One pet-understanding option slot rerolled to a useful stat | 500 to 800 |
| One active or passive skill from level 1 to level 10 | 1,000 to 3,000 |
| Armour piece from 3 breakthroughs to 4 | about 450 |
| One Clash Rune from unequipped to +6 | about 5,000 |
| One armour piece from unequipped to equipped at +0 | 3,000 to 12,000, depending on which stats it carries |
| One stigma skill from level 1 to level 20 | 10,000 to 15,000 |
| One dungeon accessory swapped for a 5-breakthrough crafted accessory | about 20,000 |
| Weapon upgrade one tier and breakthrough | about 25,000 |
| Bracelet from unequipped to a 4-breakthrough Abyssal bracelet | about 30,000 |

### The Combat Power scale

Because there is no published formula, the only way to read a CP number is
against anchors. All of these are KR, and CP inflated with Chapter 1, so every
figure needs a date attached.

| Anchor | CP | Date and source |
| --- | --- | --- |
| Freshly capped level 45, item level about 1,000 | over 46,000 | pre-Chapter 1, mein-mmo |
| Target of the Chapter 1 "New Ascent" growth support for new and returning players | 300,000 | 2026-07-01, KR press |
| Alt clearing Sanctuary "Muspel's Chalice" Normal | 460,000 to 490,000; author recommends 520,000 to 550,000 minimum | post-Chapter 1, Inven |
| Well-equipped endgame character | about 500,000 | 2026-03, Korean analysis |
| Fixed raid group running Sanctuaries 1, 2 and 3 | 680,000 to 710,000 | pre-Chapter 1 recruitment posts |
| The same group's post-Chapter 1 equivalent | 800,000 to 850,000 | post-Chapter 1 recruitment posts |

Before the official system existed, KR parties recruited on a third-party
aggregate called Atull (아툴). The mapping between the two, from the Vortex
breakdown, is the most useful single translation table for reading older
recruitment posts:

| Atull value | Equivalent Combat Power |
| --- | --- |
| 250K to 300K | 500K or higher |
| 200K to 250K | 450K or higher |
| 170K to 200K | 350K or higher |
| 70K to 90K | 300K or higher |
| 20K to 30K | 200K or higher |

## Unlock and gates

**The Season 1 range is 0–3,800.** That is the full unlock slider at global
launch (level cap 45, Unique ceiling). 3,800 is the *top of the bar*, not a
dungeon you walk into on day one. Filling 2,700→3,800 is enchant, breakthrough,
Daevanion and Arcana on Season 1 gear — not Chapter 1 raids.

Korean Chapter 1 (2026-07-01) **rescaled** the same bar. After that patch,
Expedition Normal starts at 3,800 and Hard at 4,500, Transcendence goes to
4,800, and Doom Trial sits at 4,000. Those numbers describe a later game. Do
not copy them onto a launch character. Source for the rescale: the live KR
gate list in this note's own earlier drafts, Inven 2026-07-01, and
[[Gear Tiers and Sources]].

### Season 1 doors (use these)

All of these sit inside 0–3,800. Confidence high for the Expedition and Krao
figures (repeated across KR launch guides); medium for Sanctuary 1 as a
community convention rather than a tooltip.

| Item level | What it opens at Season 1 |
| --- | --- |
| 200 | Krao Cave Exploration |
| 1,000 | Krao Cave and Draupnir Conquest; Abyss Lower; Nightmare Layer I; Ascension Trial Easy |
| 1,500 | Ascension Trial Normal; Transcendence stages 1–2 (recommended) |
| 1,600 | Two-star Conquest: Urugugu Canyon, Vakron Sky Island |
| 2,000 | Ascension Trial Hard |
| 2,200 | Three-star Conquest tooltip: Fire Temple, Ferocious Horn Den. Groups often want ~2,500 |
| 2,400 | Krao Cave Hard; Draupnir Hard; practical Fire Temple Conquest |
| 2,500 | Ascension Trial Extreme |
| ~2,700 | Sanctuary 1 — Abyssal Forge: Ludra / Rudra (8 players at launch). Community number |
| **3,800** | **Ceiling of the Season 1 unlock bar.** Not a separate dungeon |

Krao Cave (level 45, 1 to 4 players):

| Difficulty | Item level | Season 1 |
| --- | --- | --- |
| Exploration | 200 | In |
| Normal | 1,000 | In |
| Hard | 2,400 | In |

Expedition Conquest, Season 1 roster:

| Dungeon | Star | Conquest entry |
| --- | --- | --- |
| Krao Cave | 1 | 1,000 |
| Draupnir | 1 | 1,000 (Hard 2,400) |
| Urugugu Canyon | 2 | 1,600 |
| Vakron Sky Island | 2 | 1,600 |
| Fire Temple | 3 | 2,200 |
| Ferocious Horn Den | 3 | 2,200 |

Transcendence at Season 1 is the two launch dungeons (Deus Research Base,
Fragmented Arcanis) with ten stages. Recommended bands from a Korean guide,
not hard gates: stages 1–2 at 1,500–1,700, 3–5 at 1,800–2,300, 6–8 at
2,400–2,700, 9–10 at 2,800–2,900. All inside 3,800.

Ascension Trial at Season 1: Easy 1,000 / Normal 1,500 / Hard 2,000 /
Extreme 2,500. **Doom at 4,000 is out.**

Nightmare at Season 1 is Layer I from ~1,000, climbing through the launch
boss list. Layers whose recommended item level exceeds 3,800 (Tyrant Tashin
4,050, Layer IV up to 4,950) are later seasons. See [[Nightmare Mode]].

### Inside 3,800 but not Korean Season 1 launch

These numbers are *smaller* than 3,800 so they look like launch gates. They
are not. They arrived in later Korean seasons on the pre-rescale bar.

| Gate | Content | KR introduced | Season 1 verdict |
| --- | --- | --- | --- |
| 3,000 | Abyss Middle Layer; some Season 3 Expeditions | Season 2+ | Out for week-one planning |
| 3,500 | Sanctuary 2, Erosion Purification Plant (was 3,700, cut 2026-03-18) | Season 2 | Out. Still below 3,800, still not launch |
| 3,200–3,800 | Later Transcendence (Sunken Temple, Mirror of Red Passion) | Season 3 | Out. Stage 4 of Mirror at **4,000** is already above the cap |

### Above 3,800 — Chapter 1 rescale, ignore at launch

| Gate | Content | Why it is out |
| --- | --- | --- |
| 3,800 as a *floor* | Castle of the Fallen Daeva Normal; Abyssal Horn Den stage 1 | Level 50 Chapter 1 dungeon, not the Season 1 ceiling |
| 4,000 | Ascension Trial Doom; Mirror of Red Passion stage 4 | Above the bar |
| 4,100 / 4,500 / 4,800 | Abyssal Horn Den stages 2–4; Fallen Daeva Hard; Muspel's Chalice | Chapter 1 / Sanctuary 3 |
| 4,300 | Abyss Surface (entry *cap*, not a floor) | Chapter 1 |
| 4,050–4,950 | Nightmare Layer III/IV recommendations | Later seasons |

If a guide's next goal is any of those numbers, stop and check
[[Season 1 System Availability]].

## Inputs: currencies, materials, sources

| Resource | Feeds | Note |
| --- | --- | --- |
| Odd Energy | Both, indirectly | Required to open Expedition and Transcendence reward cubes. Chapter 1 raised Expedition cost from 40 to 60 points |
| Enhance Stones | Item level directly | Each enchant level is +1 item level and +1 to +2 CP |
| Daevanion Crystals | Item level directly | +1 item level per point, plus the node's stats feed CP |
| Manastones and Spirit Stones | CP only | Not counted in third-party item level, counted in the in-game figure |
| Kinah | Both | Manastone rerolling is the main Kinah sink for CP |

## Progression path

1. **Item level 0 to 1,000.** Levelling. Equip the highest item level piece in
   every slot and do not enchant common gear. Item level 1,000 opens Krao Cave
   Normal, Draupnir and the Abyss, and is the real start of the game.
2. **1,000 to 1,400.** Almost entirely one-time content: every remaining
   regional mission, sealed dungeon, stronghold and Empyrean Lord's Trace, plus
   the belt and amulet. No dungeon farming required.
3. **1,400 to 1,700.** Conquest Krao Cave and Draupnir for Unique gear, using
   cubes for the guaranteed rewards. Fill remaining slots from the market —
   item level 55 Unique armour and accessories are cheap. Compromise at +10 on
   the weapon and +5 to +7 on armour.
4. **1,700 to 2,000.** Transcendence for Arcana, and Abyss Points for Decurion
   accessories. This is the fastest CP-per-hour stretch in the game.
5. **2,000 to 2,400.** Vakron's Sky Island for the armour set, Arcana
   refinement toward Unique grade.
6. **2,400 and up.** Fire Temple Conquest, breakthroughs, soul imprint tuning,
   Sanctuary raids. From here item level growth slows and CP growth comes from
   optimisation rather than acquisition.

## Priorities and breakpoints

- **Below the gate you need, push item level. Above it, push Combat Power.**
  This is the whole decision rule.
- Arcana are the highest item level per unit of effort in the mid game. A plain
  Arcana card is worth 20 item level and a green one 40, across five slots,
  which is why the KR consensus is to spend nearly all Odd Energy on
  Transcendence between item level 1,600 and 2,000.
- Grade upgrades beat enchant levels. Replacing a whole gear tier is the single
  largest item level jump available; a full Vakron set swap was measured at
  about +150 item level over what it replaced.
- Weapon before off-hand before armour before accessories for CP, because
  attack-side stats carry more CP weight than defensive ones — but the
  offence-first rule inverts in the highest-tier dungeons where you die without
  defence.
- Do not chase CP as a score. Accuracy at 0.25 CP per point and Critical Hit at
  0.25 are both badly undervalued relative to their real damage contribution,
  because the weights were tuned for endgame characters that are already above
  the useful accuracy and crit thresholds. A player below those thresholds who
  strips accuracy to raise CP will do dramatically less damage. See
  [[Stat Reference]].

## Costs and math

- Each enchant level: +1 item level, and +1 CP up to +10, then +2 CP from +11.
  Single-sourced, confidence medium.
- Arcana item level by grade, across five slots: Common +20 each (+100 total),
  Rare/green +40 (+200), Heritage/blue +60 (+300), Unique +80 (+400). Two
  Korean sources agree on Common and Rare; only one covers Heritage and Unique.
- Marchutan Daevanion board fully completed: over +150 item level for over 230
  points.
- Belt and Amulet at +10: about +8 CP. Rudra Sanctuary bracelet: about +21 CP
  each over the Ascension Bracelet. Abyss feather Aspel collection: about +25
  CP. These are small numbers because they are pre-Chapter 1, when the whole CP
  scale was compressed — do not compare them against the post-Chapter 1
  anchors above.

## Traps and mistakes

- **Copying 4,000 / 4,500 / 4,800 from a current Korean guide.** Those are
  Chapter 1 numbers after the scale changed. Season 1 stops at 3,800.
- **Reading old Korean four-digit "Combat Power" targets as CP.** They are item
  level. This is the single most consequential misreading available.
- **Over-enchanting one piece to hit a gate.** Same item level, several times
  the cost, and you lose the material buffer you need when the next tier drops.
- **Entering content you meet the item level for but not the CP for.** The gate
  is generous relative to what the encounter demands, deliberately, so that
  parties rather than the game do the filtering.
- **Believing a higher CP player is a better player.** Multiple Korean
  post-mortems make the same point: a 500K character who executes mechanics
  out-damages a higher-CP character who dies to them, and Sanctuary clears are
  gated on mechanics, not on the number.
- **Optimising against the current CP weights.** They are explicitly
  provisional. Penetration is overvalued by roughly eight times and is slated
  for correction; anyone who built into Penetration to inflate CP will lose it.

## Global launch notes

**The unlock bar is 0–3,800.** That is settled for this vault. Combat Power
*display* is still an open question: KR launched without it and only added it
on 2026-03-18.

**Launch Scale Test doors are lower than the KR table above.** Until Advance
Access, use these Conquest floors instead of 1,000 / 1,600 / 2,200:

| Star | Live KR | Global test (plan) |
| --- | --- | --- |
| 1 — Krao, Draupnir | 1,000 | **700** (last NC stream was 800) |
| 2 — Urugugu, Vakron | 1,600 | **1,400–1,500** |
| 3 — Fire Temple, Horn Den | 2,200 | **2,100–2,200** |

Welps' reading: the T1 cut is last-minute compensation for deleting the Ariel
board (Ariel points were item level). Hard Conquest at 2,400 is unverified in
the test (level cap 37). Ludra ~2,700 is unchanged as a community number.
Full table and sources: [[Global Launch Differences]].

Do not use the Inven 2026-07-01 compilation as a launch shopping list. That
table is Chapter 1. See [[Season 1 System Availability]].

## Open questions

- [ ] The actual Combat Power formula. Settled only if NCSoft publishes it;
      otherwise it can be approximated by regression against the per-stat table.
- [ ] Post-fix Penetration CP weight, and whether Accuracy and Critical Hit were
      revalued. Settled by a KR patch note after 2026-03.
- [x] ~~Which item-level range does global launch with?~~ **0–3,800.**
      Numbers above that are Chapter 1. See the Season 1 door table above.
- [ ] The "Hell" Ascension Trial difficulty gate and how its rewards differ
      from Doom. A KR forum thread asks exactly this and gets no answer.
- [ ] Whether the in-game item level figure counts manastones and pets at a
      known rate, which would let third-party planners match the in-game number.
- [ ] Tier 1 Transcendence hard entry gates, as opposed to the recommended
      values quoted here.

## Sources

- [Gear Score & Stat Score — How They're Calculated (FAQ)](https://aion2hub.com/tools/build-calculator/faq) — EN, datamined from live client, current; used for the exact item level formula, the note that the in-game figure is higher, and the explicit refusal to publish CP because it is server-side and frequently retuned.
- [Aion 2 Equipment Guide: How to Quickly Obtain the Best Gear in PvE](https://mein-mmo.de/en/aion-2-equipment-guide-how-to-quickly-obtain-the-best-gear-in-pve,1586095/) — EN/DE, KR live; used for the item level vs CP definitions, the "46,000 CP at fresh 45" anchor, the seven-phase item level ladder and the Arcana 20/40 item level values.
- [Aion 2 Combat Power System Complete Breakdown](https://vortexgaming.io/en/postdetail/717212) — EN translation of a KR video guide, shortly after 2026-03-18; used for the per-stat CP table, the stigma level CP table, the Atull to CP mapping, the Penetration bug, the buff-inclusion bug and the accuracy 2,350 Sanctuary 2 requirement.
- [엔씨 '아이온2', 전투력 시스템 도입](https://www.khgames.co.kr/news/articleView.html?idxno=302490) — KR, 2026-03-18; used to date the system and confirm the display toggle and buff exclusion.
- [아이온2, 전투력 체계 표시…아이템 레벨과 별개](https://www.dailygame.co.kr/view.php?ud=20260318130009330043da15d9d2_26) — KR, 2026-03-18; used for the developer's stated intent to replace external sites, and for the Erosion Sanctuary 3,700 to 3,500 reduction.
- [대략적으로 실험해본 전투력 수치 변화](https://www.inven.co.kr/board/aion2/6444/1529) — KR Inven, 2026-03-18; used for the measured per-upgrade CP deltas table.
- [[아이온2] 공식 전투력(CP) 업데이트 스탯 효율 심층 분석](https://gamenewb.tistory.com/71) — KR blog, 2026-03; used for the "500K endgame" anchor and the argument that Accuracy and Critical Hit are undervalued because endgame characters are already over cap.
- [초월,원정 입장조건, 키나 정리 (2026.7.1 기준)](https://www.inven.co.kr/board/aion2/6444/2064) — KR Inven community compilation, 2026-07-01; used for the Transcendence tier 2 to 4 and Expedition Conquest item level gates.
- [[아이온2] 시즌3 초월 '붉은 연심의 거울' 완벽 공략](https://www.gametoc.co.kr/news/articleView.html?idxno=108481) — KR gametoc; independently confirms Mirror of Red Passion at 3,200 for stage 1 through 4,000 for stage 4.
- [아이온2, 첫 대규모 업데이트 단행](https://www.koreaittimes.com/news/articleView.html?idxno=154854) — KR, 2026-07-01; used for the Chapter 1 dungeons at level 50 and item level 3,500 minimum, and the Ascension Trial Doom difficulty at item level 4,000.
- [[뉴스] "확장팩급 규모" 아이온2 챕터1 프리뷰 방송 요약](https://www.inven.co.kr/webzine/news/?news=317991) — KR Inven, 2026-06-30; used for the Castle of the Fallen Daeva 3,800/3,800/4,500 gates, the Sanctuary rework and the Expedition Odd Energy change from 40 to 60.
- [[AION2] 아이온2 45레벨 이후 주간 필수 루틴](https://www.inven.co.kr/board/aion2/6493/45) — KR Inven; used for the Ascension Trial difficulties Easy/Normal/Hard/Extreme at item level 1,000/1,500/2,000/2,500, level 45, three weekly uses.
- [성역4준비+성역1,2,3고정팟(패치전710k) 구인](https://www.inven.co.kr/board/aion2/6449/16622) — KR Inven recruitment post; used for the 680K to 710K pre-patch and 800K to 850K post-patch raid recruitment CP figures.
- [부캐 궁성460k 권성490k 무스펠 일반 클리어 후기](https://www.inven.co.kr/board/aion2/6449/17457) — KR Inven; used for the 460K/490K Muspel Normal clear and the 520K to 550K recommended minimum, and for the mechanics-over-CP argument.
- [성역 입장 권장 템렙 근거 포함](https://www.inven.co.kr/board/aion2/6444/977) — KR Inven; used for the Rudra Sanctuary recommended item level about 2,700 and the DPS-based reasoning behind it.
- [아이온2 초월 공략: 1~10단계](https://game.savetip.co.kr/aion2-transcendence-dungeon-guide-1-10/) — KR blog; used for tier 1 Transcendence recommended item levels per stage band. Single source, confidence medium.
- [[아이온2] 전투력 빠르게 올리는 방법](https://madimi.tistory.com/49) — KR blog; used for the enchant CP rate (+1 per level, +2 from +11), the Arcana grade item level table and the "+150 item level for a full Vakron set" figure. Single source, confidence medium.
- [신규 초월과 천칭 등장! 2/25(수) 패치 핵심 정리](https://www.inven.co.kr/webzine/news/?news=313897&site=aion2) — KR Inven, 2026-02-25; used for the Marchutan Daevanion board node count and its +150 item level value.
- [퍼플 라운지: 악몽 몽층Ⅲ '폭군 타신'](https://lounge.plaync.com/feed/66725) — KR official lounge, 2026-04-29; used for the Nightmare unlock chain, boss level 77 and recommended item level 4,050.
- [아이온2/콘텐츠 — 나무위키](https://namu.wiki/w/%EC%95%84%EC%9D%B4%EC%98%A82/%EC%BD%98%ED%85%90%EC%B8%A0) — KR wiki; used for the Nightmare two-per-day / 14-maximum attempt recharge and the Ascension Trial reward list.

## Related notes

[[Foundations]] · [[Progression Phases Roadmap]] · [[Level and Ascension]] ·
[[Stat Reference]] · [[Gear Tiers and Sources]] · [[Enchanting]] ·
[[Breakthrough]] · [[Manastones Spirit Stones and Godstones]] ·
[[Daevanion Boards]] · [[Arcana Cards and Types]] · [[Arcana Sets and Meta]] ·
[[Dungeons and Raids]] · [[Nightmare Mode]] · [[Abyss Points and Ranks]] ·
[[Currencies and Economy]] · [[Global Launch Differences]] · [[Glossary KR TW EN]]
