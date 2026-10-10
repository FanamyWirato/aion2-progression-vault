---
chapter: "04 Arcana"
system: Arcana Set Effects and Build Meta
type: progression-system
unlock: "two matching cards of one set"
account_wide: false
cadence: "continuous"
gates: ["two slots for a 2-piece bonus", "four slots for a 4-piece bonus", "eight slots for a 4+4 configuration"]
currencies: ["Mysterious Crystal", "Harmonious Crystal", "Noble Crystal", "Splendent Noble Crystal", "Pure Crystal", "Kinah"]
region_verified: ["KR", "TW"]
patch: "KR live as of 2026-09-05 (Chapter One, Noiran's Hidden Legacy)"
confidence: high
tags:
  - aion2/progression
  - aion2/arcana
---

# Arcana Sets and Meta

> **In one sentence:** seven Arcana sets exist, they stack in 2-piece and 4-piece
> tiers, and the entire history of the Arcana meta is the story of how many slots
> the game gave you to split between them.

## Why it matters

Set effects are the part of Arcana that is not just raw item level. A 4-piece
bonus like +150 PvE Attack or +5% Boss Damage Boost is a real multiplier on your
output, and unlike skill lines it is deterministic: you choose it, you do not roll
for it. Because the number of Arcana slots grew from five to six to ten over ten
months, the correct split changed three times, and most English-language guides
describe whichever split was current when they were written. This note separates
the current answer from the archaeology.

## How it works

A set bonus fires when you have the required number of cards from the same set
equipped. Only two tiers exist, at 2 and 4 pieces. Where the two tiers grant
different stats they stack; where they grant the same stat the 4-piece figure
appears to replace the 2-piece figure rather than add to it, which is the reading
KR guides use when they quote 4-Vigor as "+150 PvE Attack" rather than "+210".

### The seven sets

| Set (canonical) | Korean | 2-piece | 4-piece |
| --- | --- | --- | --- |
| Primal Vigor | 태초의 활력 | +60 PvE Attack when HP is 70% or more | +150 PvE Attack when HP is 70% or more |
| Magic Armor | 마력 갑옷 | Restores 1,500 MP when MP is 20% or less, 30s cooldown | +1,000 PvE Defence when MP is 50% or more |
| Frenzy | 광분 | +50 PvE Attack | +5% Boss Damage Boost, and +10% Boss Damage Tolerance when HP is 70% or less |
| Pure Blood | 순수한 피 | +500 PvE Defence | +5% Critical Damage Boost, and +1,000 Defence when HP is 70% or less |
| Punishing Overture | 징벌의 서곡 | +5% Boss Damage Tolerance | +60 PvE Attack, and +10% PvE Damage Boost when HP is 70% or more |
| Protected Soul | 수호받는 영혼 | +5% Restoration | +5% Weapon Damage Boost, and a shield absorbing 10,000 damage for 5s when HP is 30% or less, 2 minute cooldown |
| Indomitable Dedication | 불굴의 집념 | +5% Weapon Damage Tolerance | +5% Critical Damage Tolerance, and +50% PvP Damage Tolerance for 5s when afflicted with Stun, Knockdown, Airborne, Grab, Frost or Fear |

All fourteen figures above come from the shipped game data via the AION2 Hub set
database, and the Frenzy, Pure Blood and Punishing Overture lines are
independently corroborated by the KR and TW patch notes of 2026-02-25 and the KR
community summary of the May update. Note that the TW patch note renders the
Frenzy 2-piece as "PvE 攻擊力增加50%" with a percent sign; the KR note, the KR
community summary and the game data all say a flat +50, so the TW percent is a
typo.

### Which slots each set covers

This is the constraint that drives everything. Sets do not cover all ten slots.

| Set | Chalice | Parchment | Compass | Bell | Mirror | Scales | Key | Hourglass | Dice | Lantern | Max pieces |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Primal Vigor | yes | yes | yes | yes | yes | no | no | no | no | no | 5 |
| Magic Armor | yes | yes | yes | yes | yes | no | no | no | no | no | 5 |
| Frenzy | yes | yes | yes | yes | yes | yes | no | no | no | no | 6 |
| Pure Blood | yes | yes | yes | yes | yes | yes | no | no | no | no | 6 |
| Punishing Overture | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | 10 |
| Protected Soul | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | 10 |
| Indomitable Dedication | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | 10 |

The two launch sets predate Scales and cannot use it. This is the mechanical
reason the launch-era meta was capped at "4 of one plus 1 of the other": with five
slots and two sets that reach five slots each, 4+1 was the only way to take a
4-piece bonus at all.

Note that in the game-data set lists, Key, Hourglass, Dice and Lantern appear at a
single grade only, which suggests Stat Arcana exist exclusively at Unique grade.
That is an inference from the piece counts and the drop tables rather than a
stated rule, so treat it as medium confidence.

### Vitality versus Magic Power, and their reskins

The Vitality/Magic Power split is the oldest axis in the system and the most
misunderstood. Two things are true at once:

1. **The set effects are genuinely different.** Primal Vigor is an offensive HP-gated
   set. Magic Armor is a defensive and sustain set gated on MP.
2. **The main-god stats are attached to the slot, not to the set family's
   philosophy.** A Vigor Bell gives Justice (Defence). A Magic Bell gives
   Destruction (Attack Power). So the "offensive" set gives you the defensive stat
   on the Bell slot, and vice versa. This inversion is why the classic build is
   *not* five Vigor cards.

Frenzy and Pure Blood, added 2026-02-25, are stat-identical reskins: a Frenzy card
gives exactly the same main-god stat as the Vigor card in the same slot, and a
Pure Blood card matches the Magic card. Only the set bonus and the refinement cost
differ. In practice they made Vigor and Magic obsolete for new crafting, because a
Frenzy or Pure Blood Chalice costs a small fraction of the Kinah of a Vigor
Chalice for the same stat.

The full slot-to-stat table is in [[Arcana Cards and Types]].

## Unlock and gates

Set effects have no unlock of their own. They gate purely on how many matching
cards you can equip, which in turn gates on how many slots the build has and
which dungeon generation you can farm.

| What you need | Requirement |
| --- | --- |
| Any 2-piece bonus | two cards of the same set, so effectively immediate |
| Any 4-piece bonus | four cards of the same set, and a set that covers four slots you can fill |
| A 4+2 configuration | six slots, which means Scales, which means Harmonious Crystal from Submerged Life Temple |
| A 4+4 configuration | eight slots, which means Key and Hourglass from Abyssal Horn Den at character level 50 and entry item level 3,800 or more |
| Frenzy or Pure Blood at all | refinement only; these two sets never drop |
| Punishing Overture, Protected Soul or Indomitable Dedication | Mirror of Scarlet Desire drops, or refinement with Noble Crystal |

## Inputs: currencies, materials, sources

| Resource | What it buys in set terms |
| --- | --- |
| Mysterious Crystal | Vigor, Magic, Frenzy and Pure Blood cards in the five original skill slots |
| Harmonious Crystal | the Scales that makes 4+2 possible |
| Noble and Splendent Noble Crystal | the three Season 3 sets, including their Chalice and Scales |
| Pure Crystal | Key and Hourglass, which are what make 4+4 possible |
| Kinah | every refinement, and the reason Frenzy and Pure Blood displaced Vigor and Magic |

Every one of these comes out of the Transcendence loop described in
[[Arcana Refinement and Farming]].

## Progression path

1. Equip whatever you have and take whichever 2-piece bonus falls out. Do not plan
   around sets at all while you are still upgrading grades.
2. Once four cards of one set are realistic, commit to a single 4-piece. On five
   slots that is 4 Primal Vigor with a Magic Bell in the fifth.
3. When you unlock Scales, rebuild toward 4+2. Craft new Chalices as Frenzy or
   Pure Blood from this point onward and never as Vigor or Magic.
4. When Season 3 dungeons open, move the whole build onto Punishing Overture,
   Protected Soul and Indomitable Dedication, since only those three reach all ten
   slots.
5. When Key and Hourglass are farmable, complete a 4+4. Farm the Key first if you
   are a damage role and the Hourglass first if you are a tank.
6. Only after the sets are settled should you optimise which skill lines sit on
   the Chalice and Scales, because a set change can force a re-craft.

## The meta, in order

### Launch era, five slots, two sets: 4 Vigor + 1 Magic Bell

With five slots and two five-slot sets, the only 4-piece bonus available was
4 Vigor, worth +150 PvE Attack when above 70% HP. The fifth slot went to a Magic
Bell because the Bell inverts: the Magic version carries Destruction, which is
flat Attack Power, while the Vigor version carries Justice, which is Defence.

The consensus assignment was:

| Slot | Family | Main-god stat | Why |
| --- | --- | --- | --- |
| Chalice | Vigor | Time | Combat Speed, which raises both attack and skill speed |
| Parchment | Vigor | Life | Health is the useful half; Fate gives Spirit, which is near-worthless |
| Compass | Vigor | Freedom | Accuracy, which matters up to the 1,200 accuracy threshold |
| Mirror | Vigor | Illusion | Cooldown Reduction |
| Bell | Magic | Destruction | flat Attack Power |

The standing rules of thumb from that era, which still hold: Vigor Chalice, Vigor
Parchment and Magic Bell are locked in; Magic Chalice, Magic Parchment and Vigor
Bell are inefficient; Compass and Mirror are the flexible slots, with Vigor
Compass useful in PvP for the Accuracy and Evasion.

### Transitional: 3 Vigor + 2 Magic, or 2 Vigor + 3 Magic

Before Scales arrived, guides began recommending giving up the 4-piece Vigor bonus
in exchange for two Magic 2-piece effects plus better main-god stats. The
reasoning was that Bell (Destruction, Attack Power) and Mirror (Wisdom, Crushing
Blow) are both better on the Magic side, and that two 2-piece bonuses plus two
better stats beat one 4-piece bonus plus two worse stats. Chalice stayed Vigor for
Combat Speed; Parchment flexed depending on which skill you needed.

This period is the source of most of the contradictory advice in circulation. Both
"4 Vigor + 1 Magic is 0-tier" and "3+2 or 2+3 is current" were written within
weeks of each other, and both were correct at the time.

### Scales era, six slots: 4 + 2

Scales made six slots available and Frenzy and Pure Blood made two more sets
available, so a genuine 4+2 became possible for the first time. Two configurations
dominated.

**4 Pure Blood + 2 Vigor** — the defensive-leaning split:

| Slot | Family | Main-god stat |
| --- | --- | --- |
| Chalice | Vigor | Time |
| Parchment | Vigor | Life |
| Compass | Pure Blood | Death |
| Mirror | Pure Blood | Wisdom |
| Bell | Pure Blood | Destruction |
| Scales | Pure Blood | Destruction + Fate |

**4 Frenzy + 2 Pure Blood** — the boss-damage split, giving +50 PvE Attack,
+5% Boss Damage Boost, +10% Boss Damage Tolerance below 70% HP and +500 PvE
Defence:

| Slot | Family | Main-god stat |
| --- | --- | --- |
| Chalice | Frenzy | Time |
| Parchment | Frenzy | Life |
| Compass | Frenzy | Freedom |
| Mirror | Frenzy | Illusion |
| Bell | Pure Blood | Destruction |
| Scales | Pure Blood | Destruction + Fate |

The tradeoff between the two is Crushing Blow. Putting Frenzy on the Mirror forces
Illusion instead of Wisdom, which costs you Crushing Blow. Classes that already
have a six-piece Crushing Blow gear configuration can absorb that; classes that
are naturally short on Crushing Blow should keep Pure Blood on the Mirror and move
the Parchment instead.

A third variant, **4 Frenzy + 2 Magic**, swapped the Pure Blood pair for the Magic
Armor 2-piece MP restore, taking Frenzy Scales as Justice + Life.

### Chapter One era, ten slots: 4 + 4

The May 2026 update added Punishing Overture, Protected Soul and Indomitable
Dedication, all of which reach the Scales slot. The July 2026 Chapter One update
added Key and Hourglass, and the August update added Dice and Lantern. Because all
three new sets cover all ten slots, a true 4+4 became possible.

NC's own recommended configuration is **4 Punishing Overture + 4 Protected Soul**,
keeping an existing 4-piece Punishing Overture and using the new Stat Arcana plus
adjusted Parchment and Chalice to complete Protected Soul. That combination buys
+5% Weapon Damage Boost and the 10,000-damage shield alongside Punishing Overture's
+60 PvE Attack and +10% PvE Damage Boost. The investment priority NC gives is to
farm and refine the Key first, because it is the offensive slot.

An independently circulated alternative is **4 Punishing Overture + 4 Indomitable
Dedication**, which trades the shield and Weapon Damage Boost for Critical Damage
Tolerance and the crowd-control-triggered +50% PvP Damage Tolerance. That is a PvP
configuration, not a PvE one.

## Recommendations by role and mode

These are directional rather than authoritative, because no source publishes
per-class set simulations. Treat them as a starting point and verify against your
own numbers using the [[Stat Reference]] conversions.

| Role | PvE | PvP |
| --- | --- | --- |
| Melee damage | 4 Punishing Overture + 4 Protected Soul. Take the Frontal Damage Boost sub-stats on Key, which were added specifically for melee classes. | Swap Protected Soul for Indomitable Dedication for the crowd-control tolerance window. |
| Assassin-type | Same as melee damage, but take Rear Damage Boost on the Key rather than Frontal. | 4 Punishing Overture + 4 Indomitable Dedication; the +50% PvP Damage Tolerance on being stunned or knocked down is the single most relevant line in the game for a class that dies to opening burst. |
| Ranged and caster damage | 4 Punishing Overture + 4 Protected Soul, with Pure Blood or Magic main-god stats on Compass and Mirror for Critical and Crushing Blow. | Vigor Compass for the Accuracy and Evasion. |
| Main tank | 4 Punishing Overture for the Boss Damage Tolerance, plus 4 Indomitable Dedication. Hourglass over Key on investment priority. | 4 Indomitable Dedication + 4 Protected Soul. |
| Healer and support | 4 Protected Soul for the +5% Restoration and the shield. | 4 Protected Soul + 4 Indomitable Dedication. |

If you are still on six slots, the honest answer is 4 Frenzy + 2 Pure Blood for
PvE boss content and 4 Pure Blood + 2 Vigor if you are dying. If you are still on
five slots, 4 Vigor + 1 Magic Bell.

Because [[Arcana Cards and Types]] confirms that saved Arcana presets exist and
that quick-equip was improved, maintaining a separate PvP preset is cheap in time
even if it is expensive in cards. See [[PvP Progression]] and
[[Arenas Sieges and Seasons]].

## Priorities and breakpoints: the skill-levelling argument

The most important meta shift in this chapter is not about sets at all. It is
about what you put on the Chalice and Scales.

**The old rule** was to cram your main active skill onto the Chalice by any means
necessary, so that it reached level 20 and unlocked its final specialisation slot.

**The current rule** is that this is usually wrong, for three reasons:

1. **Skill levels got easy.** With Chalice and Scales both able to roll any skill,
   and with rings and earrings supplying skill levels, hitting level 20 on your
   genuine main skills is no longer the hard part.
2. **Most actives do not matter.** A skill that contributes 1-2% of your damage
   gains almost nothing real from 19 to 20. What it does gain is Combat Power,
   which inflates the number on your character sheet without improving your
   output. KR guides describe this bluntly as inflating your rating for show.
3. **Tier-one passives scale everything.** A class's top passives multiply all of
   your damage or survivability, so a level on one of them is worth more than the
   final specialisation slot on a minor active.

The practical formulation, from the KR cleric board and echoed by the guide
community:

- Use Parchment and Compass, which have small fixed skill pools, to take your two
  or three genuine main actives to level 20.
- Use the Chalice and Scales, which can roll anything, to fill the one or two
  levels those cards are short *and* to pick up **three or more passive lines**.
- Do not spend Chalice or Scales lines on low-contribution actives that need three
  specialisation slots to be worth anything.
- Skills that will finish at level 16 should be matched to level 2 on a card, not
  higher. A level-3 or level-4 line on a skill that stops at 16 is wasted budget.

The corollary for refinement is that when you designate skills on a Chalice, at
least some of those designations should be passives. See [[Skills and Talents]]
and [[Daevanion Boards]] for which passives are tier one for your class.

## Costs and math

- Frenzy and Pure Blood Chalice refinement costs roughly 100,000 to 600,000 Kinah,
  against roughly 5,000,000 for a Vigor Chalice, for an identical main-god stat.
  Two KR sources give different figures within that range, so treat the exact
  number as medium confidence, but the order-of-magnitude saving is not in dispute
  and is the reason nobody crafts Vigor or Magic Chalices any more.
- The 4-piece thresholds are what make partial progress worthless: three matching
  cards give you only the 2-piece bonus. Plan set changes as blocks of four, not
  card by card.
- Full refinement material and Kinah tables are in
  [[Arcana Refinement and Farming]].

## Traps and mistakes

- **Crafting a Vigor or Magic Chalice.** Frenzy or Pure Blood gives the same stat
  for a fraction of the cost.
- **Reading a guide without checking how many slots it assumes.** A "4+1 is
  0-tier" guide and a "4+4 is best" guide can both be current-sounding and ten
  months apart.
- **Assuming Frenzy and Pure Blood are stat upgrades.** They are cost and
  set-effect changes only.
- **Chasing 4-piece Primal Vigor after Scales exists.** Primal Vigor cannot reach
  the Scales slot, so it competes for the same five slots that the newer sets use
  better.
- **Building a single set for both PvE and PvP.** Indomitable Dedication's
  4-piece is almost entirely a PvP effect; Protected Soul's is almost entirely a
  PvE one.
- **Believing set-effect numbers from kinah-selling sites.** Several circulate
  paraphrased effects with the conditions dropped, for example quoting Frenzy's
  4-piece Boss Damage Tolerance without the "below 70% HP" gate, which inverts
  when it is useful.

## Global launch notes

Which sets exist at global launch determines the entire answer here. The three
plausible snapshots:

- **Launch snapshot**: Primal Vigor and Magic Armor only, five slots, so 4 Vigor
  + 1 Magic Bell.
- **February snapshot**: adds Frenzy, Pure Blood and Scales, so 4+2.
- **Current KR snapshot**: adds Punishing Overture, Protected Soul, Indomitable
  Dedication and the four Stat Arcana, so 4+4.

Check the set list in the Arcana UI before spending anything on day one. NC has
publicly said dungeons and PvP were reworked for global, which makes it plausible
that the Transcendence roster differs and therefore that the crystal economy
behind these sets differs too. Record what you find in
[[Global Launch Differences]].

## Open questions

- [ ] Do the 2-piece and 4-piece tiers stack when they grant the same stat? Frenzy
      and Pure Blood clearly stack because the stats differ, but Primal Vigor's
      +60 and +150 PvE Attack are the same stat. Settle by equipping 2 and then 4
      and reading the stat panel.
- [ ] Do Dice and Lantern appear in the Punishing Overture, Protected Soul and
      Indomitable Dedication set piece lists in the live client? The database
      snapshot lists 26 pieces per set, which accounts for Key and Hourglass but
      not Dice and Lantern.
- [ ] Do Stat Arcana exist below Unique grade? Inferred as Unique-only from piece
      counts and drop tables; not stated anywhere.
- [ ] Is a 4+4+2 configuration possible with ten slots, and is any 2-piece worth
      the two spare slots? No source discusses the last two slots.
- [ ] Which passives are tier one per class? No consolidated list exists; the KR
      community post on passive efficiency by class is the closest thing.
- [ ] Are there per-class set simulations anywhere? Nothing found; all
      per-role advice above is directional.
- [ ] Exact Kinah cost of Frenzy and Pure Blood Chalice refinement at one, two,
      three and four designated skills. Two sources give 100,000 and 600,000 for
      the same operation.

## Sources

- [AION 2 Set Bonuses — Equipment & Arcana Set Effects](https://aion2hub.com/database/sets) — game data, English, current. All seven set names and the exact 2-piece and 4-piece wording, plus the piece lists that establish the slot coverage table.
- [AION 2 Drop Rates — Where to Farm Every Item](https://aion2hub.com/database/drop-rates) — game data, English, current. Confirms that Frenzy and Pure Blood cards never drop, and that Key, Hourglass, Dice and Lantern appear only at Unique grade.
- [Primal Vigor - Item Set](https://questlog.gg/aion-2/en/db/item-set/Arcana_A_set_001) and [Magic Armor - Item Set](https://questlog.gg/aion-2/en/db/item-set/Arcana_A_set_002) — game data, English. Independent corroboration of the Primal Vigor and Magic Armor effect wording and of Primal Vigor's five-slot piece list.
- [아이온2 인벤 : 천칭 등장 이후의 아르카나 추천 세팅](https://www.inven.co.kr/board/aion2/6444/1408) — KR community, 2026-02/03. The three post-Scales 4+2 configurations reproduced above with per-slot main-god stats, the Crushing Blow tradeoff on the Mirror, and the Frenzy and Pure Blood Chalice Kinah saving.
- [아이온2 인벤 : 신규 초월 '가라앉은 생명의 신전' 핵심 사전정보 (+천칭, 마르쿠탄)](https://www.inven.co.kr/board/aion2/6444/1393) — KR community summary of official pre-patch information, 2026-02. Frenzy and Pure Blood 2-piece and 4-piece wording, the statement that per-slot equip effects are identical between Vitality and Frenzy and between Magic and Pure Blood, and the Scales main-god stat pairs.
- [【討論】2/25更新公告內容](https://forum.gamer.com.tw/C.php?bsn=82913&snA=4240) — TW patch notes, 2026-02-25. Frenzy and Pure Blood set effects as published by NC, including the percent-sign typo on the Frenzy 2-piece noted above.
- [\[안내\] 2/25(수) 업데이트 노트](https://arca.live/b/aion2/163280518) — KR patch notes, 2026-02-25. Confirms the flat +50 PvE Attack Frenzy 2-piece and that Frenzy and Pure Blood are obtainable only by refinement with Mysterious Crystal.
- [Aion 2 Arcana Perfect Guide: Card Types, Meta Analysis, Skill Level 20 Achievement Strategy](https://vortexgaming.io/en/postdetail/635384) — KR via English translation, 2026. The 4 Vigor + 1 Magic launch meta with its +150 PvE Attack figure, the shift to 3+2 and 2+3, and the per-slot reasoning for Chalice, Bell, Mirror, Compass and Parchment.
- [\[Aion 2\] Guide to Efficiently Crafting Arcana Cards](https://vortexgaming.io/en/postdetail/623253) — KR via English translation, 2026. The "Vigor Chalice, Vigor Parchment and Magic Bell are locked in, Magic Chalice, Magic Parchment and Vigor Bell are inefficient, Compass and Mirror are variable" rule set, and the guidance that level-16 skills should be matched at 2 rather than higher.
- [\[Aion 2\] Arcana Guide: Perfect Summary of Basic Concepts, Farming Methods, and Advanced Choices](https://vortexgaming.io/en/postdetail/615162) — KR via English translation, 2026 Q1. Primal Vigor and Magic Armor trigger conditions in plain language, the recommendation to mix 2-piece and 2-piece for damage, and the launch-era stat assignment of Life on Parchment, Death on Compass, Destruction on Bell and Illusion on Mirror.
- [\[아이온2 공략\] 신규 아르카나 완벽 가이드! 광분/순수 세트 조합 추천 및 천칭 활용법](https://gamenewb.tistory.com/53) — KR community blog, 2026. The clearest statement that Frenzy equals Vigor and Pure Blood equals Magic in main-god stats, the Vigor Chalice at roughly 5,000,000 Kinah versus Frenzy and Pure Blood at roughly 600,000, and the tier-one-passive argument against pushing minor actives to 20.
- [아이온2 인벤 : 아르카나 액티브가 아니라 패시브](https://www.inven.co.kr/board/aion2/6452/21640) — KR cleric class board, 2026. The practical formulation of the passive-first rule: use Parchment and Compass for two or three main actives at 20, and use Chalice or Scales to close the gap and add three or more passive lines.
- [\[AION2\] 챕터원 업데이트 신규 아르카나 '열쇠'와 '모래시계'](https://lounge.plaync.com/feed/74514?country=KR&locale=ko-KR) — official NC Purple Lounge, KR, 2026-07-07. The recommended 4 Punishing Overture + 4 Protected Soul configuration, the reasoning that it captures +5% Weapon Damage Boost and the shield simultaneously, and the Key-first investment priority with class-specific sub-stat advice.
- ["확장팩급 규모" 아이온2 챕터1 프리뷰 방송 요약](https://www.inven.co.kr/webzine/news/?news=317991) — KR games press, 2026-06-30. Confirms Stat Arcana share the Punishing Overture, Protected Soul and Indomitable Dedication sets and that this is what makes 4-piece configurations newly possible.
- [《AION 2》新超越「緋紅羈絆之鏡」登場 新增 3 種阿爾卡那套裝效果](https://gnn.gamer.com.tw/detail.php?sn=304877) — TW games press, 2026-05-13. Confirms the Mirror of Scarlet Desire update introduced exactly three new Arcana set effects and expanded the crystal extraction types.
- [Aion 2 Comprehensive New Arcana Setup Guide](https://www.u4gm.com/aion-2/blog-aion-2-comprehensive-new-arcana-setup-guide) — English SEO aggregator, low trust, used for leads only. Source of the "Frenzy 4 / Pure Blood 2" beginner label and the "Vigor 4 / Purity 4" long-term label; the set effects it lists are paraphrased and drop trigger conditions, so none of its numbers are used above.
- [Aion 2 Punishing Overture, Protected Soul, and Indomitable Dedication Arcana Sets](https://www.u4n.com/news/aion-2-punishing-overture-protected-soul-and-indomitable-dedication-arcana-sets.html) — English SEO aggregator, low trust, used for leads only. Correctly names the three May sets and the Season 1/2 to Mysterious Crystal and Season 3 to Noble Crystal extraction split, which is corroborated by the KR patch notes; its item level entry figures are not corroborated and are not used.
