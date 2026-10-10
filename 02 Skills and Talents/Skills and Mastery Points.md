---
chapter: "02 Skills and Talents"
system: Skills and Mastery Points
type: progression-system
unlock: "level 1; skills are granted by class quests as you level"
account_wide: false
cadence: "continuous"
gates: ["skill level 8", "skill level 12", "skill level 16", "skill level 20"]
currencies: ["Skill Points", "Wisdom Stones"]
region_verified: ["KR", "TW"]
patch: "KR pre-Chapter-1 baseline; the 423-point total and the Chapter 1 Monolith extension are roadmap"
confidence: medium
tags:
  - aion2/progression
  - aion2/skills-and-talents
---

# Skills and Mastery Points

> **In one sentence:** Skill Points are the only completely free and completely
> reversible power in Aion 2, they cap every skill at level 10, and their entire
> purpose is to get a small number of skills onto the specialisation ladder.

## Why it matters

Mastery skills (마스터리 스킬) are your class's ordinary kit — the basic attack
you hold down, the chain skill on right-click, and the numbered actives and
passives you pick up as you level. Skill Points, called Mastery Points in some
English sources, are the currency that levels them.

Two facts make this system unusual and worth understanding properly:

**It is free and free to undo.** Resetting your entire mastery allocation costs
**zero Kinah**. This was not true in the first days of the Korean launch — the
reset was a paid action — and it was changed almost immediately. Korean beginner
guides now explicitly tell players to experiment, because there is no penalty.
If you take nothing else from this note: you cannot make a permanent mistake
here, so stop hoarding points and spend them.

**It has a hard ceiling of 10, and every interesting threshold is above 10.**
Skill Points will take a skill to level 10 and stop. The specialisation
thresholds are at 8, 12, 16 and 20. So points alone reach exactly one of the
four thresholds. Everything past level 10 comes from [[Daevanion Boards]],
[[Arcana Cards and Types]] and gear soul imprint. This is the single most
important structural fact about Aion 2 skill progression, and it is why
"spreading points around" is a losing strategy: an even spread across a dozen
skills means none of them are anywhere near 12.

## How it works

### The specialisation ladder

Each mastery **active** skill has five specialisation options and a growing
number of slots. Options and slots unlock on different schedules, which is the
source of a persistent conflict in English sources over whether the third
breakpoint is 16 or 20. Both are real:

| Skill level | Options unlocked (cumulative) | Slots usable | What actually changes for you |
| --- | --- | --- | --- |
| 1–7 | 0 | 0 | Raw numbers only |
| **8** | **3 of 5** | **1** | First real power step; you pick one of three effects |
| **12** | 4 of 5 | **2** | Second slot. Korean guides rate this as the biggest single jump |
| **16** | **5 of 5** — all options now available | 2 | More *choice*, not more slots |
| 17–19 | 5 of 5 | 2 | Raw numbers only |
| **20** | 5 of 5 | **3** | Third slot. The final and most expensive step |

So the honest phrasing is: **level 16 completes the menu, level 20 adds the
third plate.** An Inven tips post states it directly — at 16 every
specialisation is unlocked but only two can be equipped; three become equippable
at 20. Sources that name 16 as a breakpoint are describing option unlocks;
sources that name 20 are describing slots. Neither is wrong and they are not in
conflict.

Which of the five options to actually equip is class-specific. The PvE picks,
written as "20 (3, 4, 5)", live on:

- [[Templar Skills and Stigmas]] — Judgment, Vicious Strike, Pummel, Punishment
- [[Chanter Skills and Stigmas]] — Onslaught, Dark Crush, Recuperation, Wave Blow
- [[Cleric Skills and Stigmas]] — Radiant Recovery, Condemnation, the two marks

**Passive** skills do not have this ladder. They scale their numbers with level
and nothing more, which is a large part of why actives outrank passives for
investment (below).

Stigma skills invert the design: their specialisation effects are **applied
automatically** at levels 5, 10, 15 and 20 with no selection at all. See
[[Stigmas]].

### The cap, and how many points exist

There is no per-character "Skill Point cap" in the sense of a spendable ceiling.
What is capped is the **total number of points that exist to be earned**, and
the answer for the current Korean build is **423**.

That figure comes from an Inven allocation guide and includes Chapter 1
content, so it is a roadmap number rather than a launch number. The sources it
counts are tabulated under Inputs below.

Because 423 explicitly bundles Chapter 1, **the global launch total will be
lower.** I could not find a published pre-Chapter-1 figure. Treat 423 as the
long-run target and expect meaningfully less at launch.

### Wisdom Stones and the Monolith connection

**Wisdom Stone (지혜의 돌)** is a consumable that grants Skill Points directly.
It is the only way to gain points without levelling, and it is the reason two
characters at identical levels can have visibly different skill trees.

The primary supply is the Monolith system. You collect **Empyrean Lord's Traces**
(주신의 흔적) — the feathers scattered across the world — and donate/resonate
them at Monoliths. Resonance levels 1 through 30 pay out **112 Wisdom Stones**
in total, alongside stat bonuses and other currencies. Two independent Korean
guides give the same 112 figure. Chapter 1 extended Monolith resonance beyond
level 30 with further rewards, which is part of why the total point count rose.

Secondary supply is shops: Wisdom Stones appear in the **Nightmare** shop and
the **Shugo Festa** event shop. Buy them whenever they appear; there is no
competing use for that currency that beats permanent skill levels.

The full trace-collection routine and map coverage live in
[[Empyrean Traces and Feathers]], and the resonance reward ladder in
[[Monolith Resonance]]. From this chapter's point of view the only thing that
matters is: **exploration content is skill progression**, even though it grants
no item level and therefore looks like optional flavour.

> **Terminology warning.** [[Glossary KR TW EN]] lists 현자의 돌 for "Wisdom
> Stone". The Korean sources used here consistently write **지혜의 돌** for the
> Skill Point item, and use 현자의 돌 ("Sage's Stone") for the Soul Imprint
> reroll material. These are two different items with similar English names.
> Worth reconciling in the glossary.

### Respec

| Action | Cost | Confidence |
| --- | --- | --- |
| Reset mastery skill levels and specialisations | **0 Kinah** | **High** — three independent Korean sources |
| Reset stigma levels, pre-Chapter-1 | expensive, reduced on 2026-01-28 | Medium; see [[Stigmas]] |
| Reset stigma levels, Chapter 1 onward | free | Medium |
| Refund a Daevanion node | Kinah per node | Medium; see [[Daevanion Boards]] |

The free mastery reset is verified. NC's own tips post on Inven says there is no
reset cost and to reallocate freely; a Korean games-press article says the reset
cost was *adjusted to* zero (implying it was not always); and a Korean strategy
blog repeats it as a reason for new players to experiment. Note that the reset
returns your **points**, not any Daevanion, Arcana or gear contributions — those
are separate layers with separate reversal rules.

One consequence people miss: since resets are free, the correct habit is to
**re-plan your allocation at every major gear step**, not to pick a build at
level 20 and keep it. When Arcana starts pushing a skill from 14 toward 20, the
points you had parked on a different skill are better moved.

### Active versus passive priority

Actives first, and by a wide margin. Three reasons, all from Korean guides:

1. **Only actives have the specialisation ladder.** A passive at 12 is a passive
   with bigger numbers. An active at 12 has a second specialisation slot, which
   is a qualitative change.
2. **Frequency beats magnitude.** The strongest recommendation in Korean
   early-game guides is to level the **left-click basic attack and the
   right-click chain skill to 12 before anything else**, because cumulative
   damage from a constantly-pressed skill outweighs a big number on a 30-second
   cooldown.
3. **The Daevanion boards cover passives separately.** Green nodes give passive
   skill levels and cost Daevanion Crystals, which are abundant. Spending scarce
   Skill Points where an abundant currency already works is the wrong trade.

The exception worth naming: a passive that gates a mechanic your build depends
on — a resource-generation or proc-enabling passive — is worth points. The rule
is about default behaviour, not an absolute.

A Taiwanese guide phrases the priority as "raise active skills first" and puts
Wisdom Stones in the role of a flexible top-up used to push a chosen skill over
a threshold rather than to broaden the tree. That matches the Korean reading.

### Skill presets

**Three presets maximum**, per the official guidebook. Presets were added to KR
on **2026-01-07**, covering both skill mastery and stigma configurations.

The critical rule, and it is not obvious: **skill levels themselves are shared
across presets — only the specialisation choices and the equipped skill layout
switch.** So a preset is not a second character build with independent
investment; it is a saved arrangement of the same investment. That is exactly
what you want for the common cases:

- A PvE preset with specialisations chosen for sustained single-target damage
  and a PvP preset chosen for burst, CC and survivability.
- A solo preset versus a group preset for healers and tanks.

Since the levels are shared and the reset is free, presets mostly save you
clicking rather than resource. Their real value is that switching mid-session is
instant, where re-picking specialisations by hand is not.

The 2026-01-14 KR patch added a convenience feature for equipping presets in
bulk across profile categories, and the March 2026 patch let stigma slots carry
per-preset conditions. Both are quality-of-life on top of the same three slots.

## Unlock and gates

| Gate | Effect |
| --- | --- |
| Level 1 | Skills begin arriving from class quests; the first level of each is granted |
| Skill level 8 | 3 specialisation options unlock; 1 slot |
| Skill level 10 | **Skill Points stop working.** Further levels need other layers |
| Skill level 12 | 4th option; 2nd slot |
| Skill level 16 | 5th option; slots unchanged |
| Skill level 20 | 3rd slot |
| 2026-01-07 (KR) | Skill and stigma presets, 3 maximum |

## Inputs: currencies, materials, sources

| Source of Skill Points | Amount | Notes |
| --- | --- | --- |
| Character level-ups | the bulk of the total | Awarded automatically, no action needed |
| **Monolith resonance, levels 1–30** | **112 Wisdom Stones** | The single biggest block. See [[Monolith Resonance]] |
| Nightmare shop | purchasable | Wisdom Stones sold for Nightmare currency. See [[Nightmare Mode]] |
| Shugo Festa shop | purchasable, limited | Event-gated |
| Chapter 1 Monolith extension *(roadmap)* | part of the 423 total | Not in the launch build |
| **Kinah** | **none** | Nothing in this system costs Kinah, including the reset |

That last row is the point of the table. Mastery Points are the only
progression system in the vault with **no currency cost at all** — the whole
economy of the system is level-ups plus a collectible you pick up while walking
past it.

## Progression path

1. **Levels 1–20.** Put everything into your basic attack and chain skill until
   both are at 10, which is the points ceiling. Take the level 8 specialisation
   on each as soon as it appears.
2. **Levels 20–45.** Spread the remaining points onto the two or three actives
   you actually press in your rotation. Do not touch passives yet. Start
   collecting Empyrean Lord's Traces during your normal questing — you walk past
   most of them anyway.
3. **Level 45 onward.** Resonate Monoliths for the 112 Wisdom Stones. This is
   the point where Skill Points stop being a level-up trickle and become a
   collectible you actively farm.
4. **Item level 1,400+.** Reallocate as your Daevanion and Arcana layers develop.
   The skills that Arcana can push to 16 or 20 are the skills that deserve your
   points at 10; skills that will never see Arcana support can sit lower.

## Priorities and breakpoints

- **12 on two skills** beats 8 on five skills.
- **Actives before passives**, always, as the default.
- **Buy every Wisdom Stone you see** in the Nightmare and Shugo Festa shops.
- **Reset whenever your gear changes materially.** It is free.
- **Do not use Skill Points to chase 16 or 20** — you cannot. Those levels come
  from [[Arcana Cards and Types]] and soul imprint. Points get you to 10; the
  other layers carry you the rest of the way.

## Costs and math

| Item | Figure | Confidence |
| --- | --- | --- |
| Skill level reachable with Skill Points alone | **10** | High |
| Specialisation options total, per active skill | **5** | High |
| Specialisation slots at level 8 / 12 / 16 / 20 | **1 / 2 / 2 / 3** | High |
| Options unlocked at 8 / 12 / 16 | **3 / 4 / 5** | High |
| Mastery reset cost | **0 Kinah** | High |
| Wisdom Stones from Monolith resonance 1–30 | **112** | High, two sources |
| Total Skill Points obtainable, post-Chapter-1 | **423** | Medium, single source |
| Skill presets | **3** | High, official |
| Stigma specialisation levels | 5, 10, 15, 20, automatic | High |

The one calculation worth doing yourself: with a fully invested Daevanion adding
**+4**, a skill at points-cap 10 sits at **14**. Level 16 is therefore +2 away
and level 20 is +6 away, and both of those come from Arcana and gear. The
combination patterns that produce +2 and +6 are tabulated in
[[Arcana Cards and Types]].

## Traps and mistakes

- **Hoarding points "until you know your build."** The reset is free. Hoarding
  is a pure loss.
- **Levelling passives early.** Green Daevanion nodes do that job with a
  currency you have more of.
- **Assuming 423 points are available at global launch.** That number includes
  Chapter 1.
- **Confusing 지혜의 돌 with 현자의 돌.** Wisdom Stone gives Skill Points; Sage's
  Stone is a Soul Imprint material. See the terminology warning above.
- **Expecting presets to hold separate skill levels.** They do not — levels are
  shared, only specialisations and layout switch.
- **Skipping feather collection because it gives no item level.** In Korea it
  still pays 112 Skill Points. **On global, feathers did not grant Skill Points
  in the Launch Scale Test** — side quests and Sealed Dungeons do. Collect
  feathers after the cap for amulet scrolls and the rest of the Monolith track,
  not for mastery. See [[Global Launch Differences]].

## Global launch notes

The ladder (level 10 from points, 8/12/16/20 specialisations, free reset) is
launch-era Korean content and should ship. The **supply path is not the Korean
one.**

**Launch Scale Test:** Empyrean Traces / feathers **do not grant Skill Points**.
Side quests grant **1 Skill Point and 1 Daevanion point**. Completing a Sealed
Dungeon grants **2 and 2**. You are therefore stronger *while levelling*
without a horizontal feather sweep, and the 112-Wisdom-Stone Monolith line in
this note is a KR figure, not a launch plan. Still collect feathers after the
cap for amulet scrolls, cube keys and leftover Monolith stats. Shugo and
Nightmare shops still sell extra Daevanion points (Nightmare shop is new vs
KR). See [[Empyrean Traces and Feathers]] and [[Global Launch Differences]].

Presets arrived in Korea on 2026-01-07, so they remain borderline. The
published 423-point total includes Chapter 1 and is still not a launch number.

## Open questions

- [ ] What is the pre-Chapter-1 total Skill Point count? 423 is post-Chapter-1
      and no source gives the earlier figure. Settled by summing level-up grants
      and Monolith payouts in the launch client.
- [ ] Is the mastery ceiling exactly 20? Every source stops at 20 but none calls
      it a hard cap, and no specialisation exists above it.
- [ ] Does resetting return Wisdom-Stone-derived points, or only level-up
      points? No source distinguishes them, and the distinction would matter a
      great deal.
- [ ] Which of the five specialisation options are the three that unlock at
      level 8 — is it fixed per skill, or player-chosen from the five?
- [ ] Do the three presets share a cooldown or have a swap restriction in
      combat, in instances, or in the Abyss?
- [ ] Glossary reconciliation: confirm 지혜의 돌 as Wisdom Stone and 현자의 돌 as
      Sage's Stone against the shipped English client strings.

## Sources

- [Skill introduction — official AION 2 guidebook](https://aion2.plaync.com/ko-kr/guidebook/view?title=%EC%8A%A4%ED%82%AC+%EC%86%8C%EA%B0%9C) — KR official, retrieved 2026-09-06. Supports: mastery versus stigma skill split; Skill Points raising a skill to level 10 with further levels only from items, Arcana and Daevanion; specialisation effects unlocking at specific skill levels; stigma levels coming only from Stigma Shards; and a maximum of three skill presets.
- [\[AION2\] 아이온2 초보를 위한 스킬 가이드 - 획득과 성장편](https://www.inven.co.kr/board/aion2/6493/26) — KR, NC-authored tips board hosted on Inven. Supports: Skill Points to level 10 with levels 11+ from Daevanion, Arcana and soul imprint; the explicit statement that there is no reset cost so points can be reallocated freely; and the 12-stigma pool of which four are equipped.
- [아이온2 스킬 레벨, 이렇게 올리자](https://www.gameple.co.kr/news/articleView.html?idxno=214499) — KR games press, 2025-11-21. Supports: five specialisation options per active skill with three unlocking at level 8 and one each at 12 and 16; mastery specialisations being chosen into slots while stigma specialisations apply automatically every five levels; and mastery reset cost having been adjusted to zero while stigma reset remained costly.
- [아이온2 스킬레벨 16~20 찍는 방법 정리](https://www.inven.co.kr/board/aion2/6444/457) — KR Inven tips board. Supports: the decisive statement that at skill level 16 all specialisations are unlocked but only two slots are usable, and that three slots become usable at level 20 — the resolution of the 16-versus-20 conflict.
- [(26/01/28 기준) ★ 치유성 가이드 ★](https://www.inven.co.kr/board/aion2/6452/657) — KR Inven Cleric board, 2026-01-28. Supports: slot counts of 1 / 2 / 3 at levels 8 / 12 / 20 stated from a player's own build, and Daevanion contributing at most +4 skill levels.
- [아이온2 스킬 특화 및 각인 스킬 정리](https://madimi.tistory.com/49) — KR blog. Supports: specialisation unlocks at 8, 12 and 16 with the last slot at 20, phrased from the opposite direction to the Inven post and consistent with it.
- [아이온2 “스킬, 데바니온 세팅만 잘해도 만렙 수월하다”](https://www.gametoc.co.kr/news/articleView.html?idxno=104096) — KR games press, launch era. Supports: Skill Points capping at 10 and therefore being unable to reach level-16 specialisations alone; the case for concentrated over spread investment; and automatic stigma specialisation.
- [아이온2 공략 종결: 초반 육성 루트와 필수 스킬 트리](https://game.savetip.co.kr/aion2-early-game-strategy-guide/) — KR blog, 2026-07-28. Supports: level the left-click basic attack and right-click chain skill to 12 first; skill reset is free so experimentation is safe.
- [아이온2 주신의 흔적 560개 위치 지도 & 보상 총정리](https://game.savetip.co.kr/aion2-jusin-mark-locations-rewards/) — KR blog. Supports: 112 Wisdom Stones across Monolith resonance levels 1 to 30, and Wisdom Stones as the Skill Point item.
- [아이온2 주신의 흔적 위치, 보상, 효율적인 수집 전략](https://redwendy.com/archives/2352) — KR blog. Supports: the same 112 Wisdom Stones figure independently, plus the framing of feather collection as skill progression.
- [아이온2, 신규 지역 '흔적' 보상 개편](https://www.inven.co.kr/webzine/news/?news=311568) — KR news. Supports: Wisdom Stones as a Monolith resonance reward and the reward restructuring that set the current payout.
- [아이온2 스킬 성장 시스템 완벽 분석](https://www.gametoc.co.kr/news/articleView.html?idxno=104206) — KR games press. Supports: Wisdom Stone acquisition from Monolith resonance, the Nightmare shop and the Shugo Festa shop.
- [Aion 2 Skill Reset and Respec Guide](https://vortexgaming.io/en/postdetail/598117) — EN translation of KR material. Supports: reset available at any time at no cost, and Wisdom Stones obtained from Monolith feather donations — the English-language corroboration of both claims.
- [스킬 포인트 배분 방법 (423p)](https://www.inven.co.kr/board/aion2/6444/2034) — KR Inven tips board, post-Chapter-1. Supports: the 423 total Skill Point figure, and the fact that it counts Chapter 1 content.
- [AION 2 Patch Notes archive](https://aion2hub.com/updates) — EN translations of official KR notes, retrieved 2026-09-06. Supports: skill mastery and stigma preset introduction on 2026-01-07; the 2026-01-14 bulk preset-equip convenience change; and the 2026-03-25 stigma slot condition system.
- [아이온2, 스킬·스티그마 프리셋 추가](https://www.inven.co.kr/webzine/news/?news=312562) — KR news, 2026-01-07. Supports: presets covering both skill mastery and stigma setups, and the rule that skill levels are shared across presets while only specialisation and layout switch.
- [《AION 2》技能強化攻略：精通、烙印技能與阿爾卡那系統成長指南](https://www.ludens.com.tw/aion-2-skill-enhancement-mastery-stigma-guide-2025/) — TW, retrieved 2026-09-06. Supports: the active-skills-first priority; Wisdom Stones (智慧之石) positioned as a flexible supplement used to cross a threshold rather than to broaden the tree; and the five-route growth model that matches the Korean layer ordering.
- [AION 2 Skill Progression: Stigma and Daevanion Order](https://expcarry.com/aion-2-stigma-daevanion-skill-upgrades-resets-progression) — EN boosting service, SEO content, **confidence low, used as a lead only**. Supports nothing independently; every mechanical claim it makes is covered by the Korean sources above. Retained because it is the most prominent English result for skill resets and a future researcher will find it — its useful content is the caveat that Korean reset costs and caps are not guarantees for the global client.

## Related notes

[[Skills and Talents]] · [[Daevanion Boards]] · [[Stigmas]] ·
[[Essence Extraction]] · [[Arcana Cards and Types]] ·
[[Empyrean Traces and Feathers]] · [[Monolith Resonance]] ·
[[Stat Reference]] · [[Item Level vs Combat Power]] ·
[[Level and Ascension]] · [[Progression Phases Roadmap]] ·
[[Soul Imprint and Soul Binding]] · [[Daily and Weekly Loops]] ·
[[Glossary KR TW EN]] · [[Season 1 System Availability]] ·
[[Global Launch Differences]] · [[Home]]
