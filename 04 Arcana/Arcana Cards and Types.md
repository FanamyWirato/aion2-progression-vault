---
chapter: "04 Arcana"
system: Arcana Cards and Types
type: progression-system
unlock: "with Transcendence dungeon access; Stat Arcana slots require character level 50"
account_wide: false
cadence: "continuous"
gates: ["Transcendence stage 3 for Rare cards", "stage 9 for Unique Compass and Bell", "stage 10 for Unique Chalice"]
currencies: ["Kinah", "Mysterious Crystal", "Harmonious Crystal", "Pure Crystal", "Noble Crystal"]
region_verified: ["KR", "TW"]
patch: "KR live as of 2026-09-05 (Chapter One, Noiran's Hidden Legacy)"
confidence: high
tags:
  - aion2/progression
  - aion2/arcana
---

# Arcana Cards and Types

> **In one sentence:** an Arcana card is one slot, one grade, one set, one or two
> main-god stats and up to four skill-level lines, and knowing which of those the
> slot can even roll is what decides where you spend crystals.

## Why it matters

Every refinement is irreversible in the sense that the crystals are gone. You
cannot roll an active skill on a Bell, you cannot designate any skill at all on a
Scales, and you cannot get a Unique Chalice below stage 10. Getting the slot rules
wrong is the most expensive mistake available in this chapter. This note is the
reference table the rest of the chapter assumes.

## How it works

### Terminology

Sources disagree badly on English names because most English-language Arcana
content is machine-translated from Korean. The left column is what the shipped
English game data uses, taken from the AION2 Hub item and set database, and is what
this vault treats as canonical. See [[Glossary KR TW EN]].

| Canonical English | Korean | Traditional Chinese | Aliases seen in the wild |
| --- | --- | --- | --- |
| Arcana | 아르카나 | 阿爾卡那 | Arcane, Arkana |
| Chalice | 성배 | 聖杯 | Grail, Holy Grail, Stone Scroll |
| Parchment | 양피지 | 羊皮紙 | Scroll, Papyrus |
| Compass | 나침반 | 指南針 | — |
| Bell | 종 | 鐘 | — |
| Mirror | 거울 | 鏡子 | — |
| Scales | 천칭 | 天秤 | Libra, Balance, Heavenly Relations |
| Key | 열쇠 | — | — |
| Hourglass | 모래시계 | — | Sandglass, Sand Clock |
| Dice | 주사위 | — | — |
| Lantern | 등불 | — | Lamp, Light |
| Refinement | 연성 | 鍊成 | Synthesis, Alchemy, Transmutation, Transmuting |
| Extraction | 추출 | 抽取 | Disassembly, Dismantle |
| Transcendence | 초월 | 超越 | Transcendence Mask (mistranslation) |
| Training Arcana | 수련의 아르카나 | 修練阿爾卡那 | Practice Arcana, Cultivation Arcana |

**Resolving Chalice versus Grail.** The Korean 성배 and Chinese 聖杯 both literally
mean "holy grail", which is why English translations of Korean guides say "Grail"
or "Holy Grail". The shipped English item names are `Arcana: Chalice of Vigor`,
`Chalice of Punishment` and so on, so **Chalice is the correct global term** and
Grail is a translation artefact. "Stone Scroll", which appears in some SEO
articles as a sixth type, is a garbled rendering of Parchment and is not a real
slot.

**Resolving Libra versus Scales.** Korean 천칭 is the balance scale and the zodiac
sign Libra. English game data uses `Scales of Punishment`, so **Scales** is
canonical and Libra is the community term. "Heavenly Relations" is a
character-by-character mistranslation of 천칭 and should be ignored.

### The ten slots

| Slot | Skill lines it can roll | Skill pool size | Item level contribution | Added |
| --- | --- | --- | --- | --- |
| Chalice | Active and passive | all skills except Stigmas, reported as 22 | yes, by grade | launch |
| Parchment | Active only | 6 | yes, by grade | launch |
| Compass | Active only | 6 | yes, by grade | launch |
| Bell | Passive only | 5 | yes, by grade | launch |
| Mirror | Passive only | 5 | yes, by grade | launch |
| Scales | Active and passive, never selectable | all skills | unconfirmed | 2026-02-25 |
| Key | none | — | unconfirmed | 2026-07-01 |
| Hourglass | none | — | unconfirmed | 2026-07-01 |
| Dice | none | — | unconfirmed | 2026-08 (KR) |
| Lantern | none | — | unconfirmed | 2026-08 (KR) |

A Unique card shows four skill lines drawn from its pool, so a Unique Parchment
shows four of its six possible actives. That is why Parchment and Compass have
high hit rates and Chalice has terrible ones: four lines out of a pool of roughly
22 is a much worse lottery than four out of six.

Key, Hourglass, Dice and Lantern are collectively called **Stat Arcana**
(스탯 아르카나) in the KR patch notes. They carry no skill lines at all. Dice and
Lantern were announced on 2026-07-01 as "coming later" and appear in the live drop
tables for Noiran's Hidden Legacy, so they went live with the August KR update.

### Grades

| Grade (canonical) | Korean | Traditional Chinese | Colour | Item level | Skill lines | Database label |
| --- | --- | --- | --- | --- | --- | --- |
| Normal | 일반 | 一般 | grey | +20 | 1 | Common |
| Rare | 희귀 | 稀有 | green | +40 | 2 | Rare |
| Heritage | 전승 | 傳承 | blue | +60 | 3 | Epic |
| Unique | 유일 | 獨特 | gold | +80 | 4 | Unique |

Scales exists only at Rare, Heritage and Unique. It has no Normal tier, because it
cannot drop and is only ever produced by refinement.

Cards enhance from +0 to +5. Each enhancement level rerolls upward one of the
card's existing skill lines at random, which is why a card with three junk lines
and one good line is a bad enhancement target: you are paying for a coin flip on
which line improves.

### Main-god stats

Each card carries a Lord/main-god stat (주신 스탯), named after an Aion deity
concept. Which stat you get is determined by the slot plus the set family, not by
luck. This is the single most useful table in the chapter.

| Slot | Vigor / Frenzy stat | Effect | Magic / Pure Blood stat | Effect |
| --- | --- | --- | --- | --- |
| Chalice | Time (시간) | Combat Speed, Crushing Blow Resistance | Space (공간) | Movement Speed, Block |
| Parchment | Life (생명) | Health, Regeneration Chance | Fate (운명) | Spirit, Iron Wall Chance |
| Compass | Freedom (자유) | Accuracy, Evasion | Death (죽음) | Critical, Regeneration Penetration |
| Bell | Justice (정의) | Defence, Perfect Block Chance | Destruction (파괴) | Attack Power |
| Mirror | Illusion (환상) | Cooldown Reduction, Iron Wall Penetration | Wisdom (지혜) | Crushing Blow, Spirit cost reduction |
| Scales | Justice 10 + Life 10 | both of the above at half value | Destruction 10 + Fate 10 | both of the above at half value |

The single-stat slots carry the stat at value 20 at Rare grade in the KR tooltips
quoted by the community; Scales carries two stats at 10 each. That is the defining
difference of the Scales slot: half of two stats instead of all of one.

Frenzy and Pure Blood are stat-identical to Vigor and Magic respectively. A Frenzy
Chalice and a Vigor Chalice both give Time 20. The only differences are the set
effect and the refinement cost. This is confirmed directly in the KR community
summary of the 2026-02-25 patch: "파츠별 장착 효과는 활력=광분, 마력=순수의 피로
동일" — per-slot equip effects are identical between Vitality and Frenzy, and
between Magic and Pure Blood.

Note that 강타 is rendered variously as Crushing Blow, Slam and Impact, and 철벽 as
Iron Wall and Block, across English translations. See [[Stat Reference]].

### Stat Arcana options

Key and Hourglass carry one fixed main stat that scales with enhancement, plus
four randomly assigned sub-stats.

| Enhancement | Key: Additional Attack | Hourglass: Additional Defence |
| --- | --- | --- |
| +0 | 5 | 50 |
| +1 | 10 | 100 |
| +2 | 15 | 150 |
| +3 | 20 | 200 |
| +4 | 25 | 250 |
| +5 | 30 | 300 |

The sub-stat pools are mirrored between the offensive and defensive slot.

| Key (offensive) | Hourglass (defensive) |
| --- | --- |
| Critical Attack | Critical Defence |
| Rear Attack | Rear Defence |
| Frontal Attack | Frontal Defence |
| PvE Attack | PvE Defence |
| Boss Attack | Boss Defence |
| Maximum Attack | Damage Tolerance |
| Damage Boost | PvE Damage Tolerance |
| PvE Damage Boost | Critical Damage Tolerance |
| Critical Damage Boost | Weapon Damage Tolerance |
| Weapon Damage Boost | Rear Damage Tolerance |
| Rear Damage Boost | Frontal Damage Tolerance |
| Frontal Damage Boost | PvP Defence |
| Penetration | PvP Damage Tolerance |
| Soulstone Additional Damage | — |
| PvP Attack | — |
| PvP Damage Boost | — |

NC's own guidance is that Damage Boost and Damage Tolerance lines carry the most
value, that Key should prioritise Weapon Damage Boost, Boss Critical Damage Boost
and PvP Damage Boost, and that melee classes want the Frontal lines added in that
patch while the assassin-type class wants Rear Damage Boost. Because refinement
locks only one option, the efficient play is to farm a card that already has three
or four useful sub-stats and then refine to lock the missing one.

The sub-stat pools for Dice and Lantern are not published in any source consulted.

## Unlock and gates

Grade availability is gated by Transcendence stage on the original two dungeons.

| What you want | Where it becomes available |
| --- | --- |
| Any card at all | stage 1, but the reward boxes are not worth opening at stages 1-2 |
| Rare (green) cards | chance from stage 3, effectively guaranteed at stage 4 with a 20% chance of a second |
| Chalice at all | both dungeons from stage 3 by chance, guaranteed from stage 5 |
| Heritage (blue) cards | from stage 6, with bonus-roll chances from stage 7 |
| Unique Compass and Bell | stage 9 |
| Unique Chalice | stage 10 only |
| Scales | refinement only, never a drop from the original dungeons |
| Key and Hourglass | Abyssal Horn Den, character level 50, entry item level 3,800 and up |
| Dice and Lantern | Noiran's Hidden Legacy |

Full per-stage numbers, including the game-data drop percentages, are in
[[Arcana Refinement and Farming]].

## Inputs: currencies, materials, sources

| Resource | What it buys in this note's terms |
| --- | --- |
| Mysterious Crystal | A designated Vigor, Magic, Frenzy or Pure Blood card in any of the five skill slots |
| Harmonious Crystal | A Scales, at 20 crystals, with no skill selection |
| Pure Crystal + 500,000 Kinah | A Key or Hourglass with one locked sub-stat |
| Noble and Splendent Noble Crystal | Punishing Overture, Protected Soul or Indomitable Dedication cards; the Chalice and Scales of those sets use the Splendent variant |
| Training Arcana, three tiers | Enhancement experience; maximum use per action was raised from 10 to 100 on 2026-02-25 |
| Duplicate cards | Enhancement experience, with a bonus for feeding the identical card |

## Progression path

1. Fill all available slots with whatever grade you have. Empty slots are the only
   truly wrong answer.
2. Upgrade by grade, ignoring skill lines, until you can farm the top stage.
3. Only then start caring about which skills are on which card.
4. Add Scales when Harmonious Crystals accumulate, accepting that you cannot aim
   it.
5. Add Stat Arcana last, and farm them for sub-stat quality rather than refining
   blindly.

## Priorities and breakpoints

- **Chalice is the bottleneck and therefore goes first in the plan**, even though
  it is farmed last. Decide what you need from it before you touch Parchment and
  Compass, because those two exist to fill whatever the Chalice failed to give.
- **Parchment and Compass are the reliable slots.** Small pools mean you can
  actually aim them. Use combinations like 4+2+1+1 or 3+3+2+1 across cards and
  rings to land your level-20 and level-16 targets.
- **Bell and Mirror are the cheap slots.** Enhance loosely, do not chase.
- **Scales is the gambling slot.** Its skill lines are fully random across every
  active and passive in the game and cannot be designated at refinement, so treat
  any good roll as a bonus and never plan around it.
- **Stat Arcana are not skill slots.** Do not evaluate them with skill-level
  logic; evaluate them as four sub-stat lines.

## Costs and math

### Skill-level arithmetic

[[Skills and Mastery Points]] plus a maxed [[Daevanion Boards]] gets a skill to
about level 14. Active skills open specialisation slots at levels 8, 12, 16 and
20, so:

- Reaching 16 needs +2 from Arcana or gear.
- Reaching 20 needs +6.

A Unique card can contribute up to 4 levels on a single skill line, which is why
the standard patterns look like this (rings and earrings from
[[Soul Imprint and Soul Binding]] supply the remainder; rings carry actives,
earrings carry passives):

| Pattern | Parchment | Compass | Chalice | Ring 1 | Ring 2 | Result |
| --- | --- | --- | --- | --- | --- | --- |
| A | 4 | — | — | 1 | 1 | level 20 |
| B | — | 4 | — | 1 | 1 | level 20 |
| C | 2 | — | 2 | 1 | 1 | level 20 |
| D | — | 2 | — | — | 2 | level 16 |
| E | — | — | 2 | — | 2 | level 16 |

Stacking these gives roughly three skills at 20 and several at 16. Community
calculators report that with a well-rolled Scales added, five level-20 skills
becomes reachable, which is a large jump over the pre-Scales ceiling.

### Storage

The Arcana holding cap was raised to **800** in the KR patch of 2026-03-18. Before
that it was lower; no source states the previous figure. Whether equipped cards
count against the cap is unconfirmed.

800 sounds generous and is not, because the correct play is to hoard Heritage and
Unique cards as enhancement fuel and to hoard any card with a valid skill line.
Plan a weekly extraction pass, described in [[Arcana Refinement and Farming]].

## Equipping, presets and quality of life

- One card per slot. You cannot equip two Chalices.
- Cards are Bound (각인 / 刻印) on acquisition from reward cubes, so they cannot be
  traded. See [[Currencies and Economy]] for what Bound means economically.
- A quick-equip function exists and was improved on 2026-02-25: you can now filter
  by Arcana type when setting a primary effect, use quick-equip without having set
  primary or additional effects, and when no primary effect is set the game
  auto-equips the highest item level card available.
- Multiple saved sets are supported, and swapping between them is the intended way
  to move between PvE and PvP configurations. This matters because
  [[Arcana Sets and Meta]] recommends genuinely different sets for the two.
- The refinement cooldown was removed on 2026-02-25, so refinement is now limited
  only by materials.

## Traps and mistakes

- **Refining a Vigor or Magic Chalice when a Frenzy or Pure Blood Chalice gives
  the identical main-god stat for a fraction of the Kinah.** This is the single
  most commonly repeated warning in KR guides after the 2026-02-25 patch.
- **Trying to designate a skill on Scales.** You cannot. Any guide that describes
  choosing Scales skills is wrong.
- **Assuming Scales has fewer attachment slots.** English SEO articles claim
  Scales has "ten attachment slots" or "reduced attachment slots". Neither is
  supported by any primary source; what Scales actually has is two half-value
  main-god stats and non-selectable skills.
- **Enhancing a card whose good line is one of four.** Enhancement improves a
  random existing line.
- **Treating Stat Arcana as a skill source.** They have no skill lines.
- **Reading pre-February guides as current.** The five-slot, four-set description
  on Korean wikis predates Scales entirely.

## Global launch notes

The ten-slot structure is the product of three separate KR content waves in
February, July and August 2026. A global launch built on an earlier snapshot could
plausibly ship with five slots and four sets, or with six slots and six sets.
Confirm the slot count in the Arcana UI on day one before planning anything, and
check whether the shipped English strings match the canonical names above.

The English names in this note come from the same data files the global client
will use, so they are the most likely names to be correct at launch even if the
content itself differs. Record any deviation in [[Global Launch Differences]].

## Open questions

- [ ] Do Scales, Key, Hourglass, Dice and Lantern grant item level, and how much
      per grade? Settle from the in-client tooltip and the Combat Power panel.
- [ ] Exactly how large is the Chalice skill pool? "4 out of 22" comes from one
      community guide and the 22 is likely class-dependent. Settle by opening the
      refinement skill list on several classes.
- [ ] Which six actives and which five passives are in the Parchment, Compass,
      Bell and Mirror pools, per class? No source publishes the full per-class
      lists. Settle from the refinement UI.
- [ ] What are the Dice and Lantern main stats and sub-stat pools? Not published.
- [ ] Do Dice and Lantern use Pure Crystal, or a new material?
- [ ] Does the main-god stat value scale with grade and enhancement, or is 20 flat?
      The "Time 20" figure comes from a single Rare-grade tooltip quote.
- [ ] Does the 800 storage cap include equipped and enhancement-locked cards?
- [ ] How many Arcana presets can be saved?
- [ ] Confirm whether "Heritage" or "Legacy" is the shipped English word for 전승;
      the database exposes it as "Epic" in one view, which conflicts with both.

## Sources

- [AION 2 Set Bonuses — Equipment & Arcana Set Effects](https://aion2hub.com/database/sets) — game data, English, current. Canonical English item names including `Chalice of Punishment`, `Scales of Punishment`, `Key of Punishment` and `Hourglass of Punishment`, which resolve the Chalice/Grail and Scales/Libra naming conflicts.
- [AION 2 Drop Rates — Where to Farm Every Item](https://aion2hub.com/database/drop-rates) — game data, English, current. Grade labels Rare, Epic and Unique per card; confirmation that Dice and Lantern exist and drop from Noiran's Hidden Legacy; confirmation that Frenzy and Pure Blood cards appear in no drop table.
- [Aion 2 Arcana Perfect Guide: Card Types, Meta Analysis, Skill Level 20 Achievement Strategy](https://vortexgaming.io/en/postdetail/635384) — KR via English translation, 2026. The main-god stat table per slot for both Vitality and Magic Power.
- [아이온2 인벤 : 천칭 등장 이후의 아르카나 추천 세팅](https://www.inven.co.kr/board/aion2/6444/1408) — KR community, 2026-02/03. Per-slot main-god stat names with their paired sub-effects in Korean, including the two-stat Scales lines Justice/Life and Destruction/Fate.
- [아이온2 인벤 : 신규 초월 '가라앉은 생명의 신전' 핵심 사전정보 (+천칭, 마르쿠탄)](https://www.inven.co.kr/board/aion2/6444/1393) — KR community summary of official pre-patch information, 2026-02. Scales obtainable only via 20 Harmonious Crystals, skills not selectable and fully random, Frenzy Scales as Justice 10 / Life 10 and Pure Blood Scales as Destruction 10 / Fate 10, and the statement that Vitality equals Frenzy and Magic equals Pure Blood for per-slot equip effects.
- [엔씨 '아이온2' 스킬 레벨 올리는 가장 쉬운 방법, 아르카나 편성](https://www.gamechosun.co.kr/webzine/article/view.php?no=219142) — KR games press. Skill lines per grade (Normal 1, Rare 2, Heritage 3, Unique 4), the dungeon-to-slot map, Chalice by chance from stage 3 and guaranteed from stage 5, and the rule that designatable skills differ by slot.
- [엔씨 '아이온2', '조각난 아르카니스' 초월 던전 공략](https://www.gamechosun.co.kr/webzine/article/view.php?no=218681) — KR games press. Arcana as a separate system tab rather than a gear slot, main-god stats named after gods such as Justice (Nezekan) and Destruction (Zikel), one card per slot type.
- [아이온2 유일 아르카나 얻는법 강화방법 제작 공략](https://saiha.tistory.com/560948) — KR community blog. Item level per grade with the 0-enhancement baseline, Unique Chalice restricted to stage 10, the note that Chalice can roll every active and passive except Stigma skills, and the grade-over-enhancement argument.
- [아이온2 아르카나 세팅 추천 : 기본 셋팅과 유일 제작](https://cvmaxlimbo.tistory.com/149) — KR community blog. Item level per grade and the 8/12/16/20 specialisation unlock ladder that sets the level-16 and level-20 targets.
- [아이온2 아르카나 액티브 20레벨 세팅 완전 공략](https://dalbodre91.tistory.com/490) — KR community blog. The Parchment/Compass/Chalice/ring combination table reproduced above, and the note that refinement only offers skills valid for the chosen card.
- [\[AION2\] 챕터원 업데이트 신규 아르카나 '열쇠'와 '모래시계'](https://lounge.plaync.com/feed/74514?country=KR&locale=ko-KR) — official NC Purple Lounge, KR, dated 2026-07-07. The four Stat Arcana slots with Dice and Lantern pending, the Key and Hourglass main stat table from +0 to +5, the full sub-stat pools, the 500,000 Kinah plus Pure Crystal refinement with one locked option, and the class-specific sub-stat guidance.
- [아이온2 인벤 : \[AION2\] 챕터원 업데이트 신규 아르카나 '열쇠'와 '모래시계'](https://www.inven.co.kr/board/aion2/6493/202) — KR, mirror of the official post, 2026-07-07. Same tables, used to corroborate the Key and Hourglass numbers independently.
- [【討論】2/25更新公告內容](https://forum.gamer.com.tw/C.php?bsn=82913&snA=4240) — TW patch notes, 2026-02-25. Scales limited to Rare, Heritage and Unique grades; Harmonious Crystal from Submerged Life Temple shards via material conversion; refinement cooldown removed; the three quick-equip improvements including auto-selecting the highest item level card; Training Arcana max use raised from 10 to 100.
- [\[안내\] 3/18(수) 업데이트 노트](https://arca.live/b/aion2/165151239) — KR patch notes, 2026-03-18. Arcana maximum holding quantity raised to 800.
- [아이온2/성장 - 나무위키](https://namu.wiki/w/%EC%95%84%EC%9D%B4%EC%98%A82/%EC%84%B1%EC%9E%A5) — KR wiki, pre-February snapshot. Enhancement consuming other Arcana plus Kinah with a bonus for identical cards; used only for the enhancement mechanic, since its "five slots and four sets" description is now outdated.
- [\[안내\] 12/24(수) 업데이트 노트](https://arca.live/b/aion2/157647414) — KR patch notes, 2025-12-24. Confirms enhancement raises skill levels on the card and that cards enhance at least to +5, via the compensation rules for a December bug.
