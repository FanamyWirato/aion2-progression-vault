---
chapter: "11 Class Playbooks"
system: Templar Progression Plan
type: progression-system
unlock: "class selection at character creation; the plan proper begins at level 45"
account_wide: false
cadence: "continuous"
gates: ["accuracy about 1100 for Expedition Conquest Hard and Transcendence stage 10", "item level 1000 / 1600 / 2400 / 2700 / 3800", "4 stigma slots and stigma level 20 at Season 1"]
currencies: ["Kinah", "Abyss Points", "Odd Energy", "Enhance Stones", "Breakthrough Stones", "Mysterious Crystal", "Daevanion Crystals"]
region_verified: ["KR"]
patch: "KR Season 1 baseline (2025-11-19) read forward from KR live 2026-09-06; global launch 2026-10-05"
confidence: medium
tags:
  - aion2/progression
  - aion2/class-playbooks
  - aion2/templar
---

# Templar BiS Roadmap

> **In one sentence:** the Season 1 Templar is a main tank whose damage kit is
> gated on two thresholds rather than on stat curves — Accuracy to beat boss
> parry and Block to keep the Fury passive running — so the whole plan is
> "pay those two thresholds as cheaply as possible, then stack percentage
> mitigation and cooldown reduction on top".

## Why it matters

The Templar (수호성, sometimes localised Guardian) is the only class in the
Season 1 roster built for main-tanking, and in four-player parties there is
exactly one of you. That gives the class an unusual property: nobody can carry
your gaps. A damage dealer who is 15% behind is a slower clear. A tank who is
below the accuracy threshold loses aggro, and a tank who cannot hold the boss
wipes the party.

The second thing that makes this class's plan different is that its damage
kit runs on a *defensive* stat. The **Fury** passive (격앙) triggers off
blocking, and the Korean Guardian community builds around keeping it up
permanently. That collapses the usual tank tension between "survive" and
"contribute": Block buys both at once, and it is the one stat where a Templar
should outbid every other class in the party for the same manastone.

Everything mechanical below lives in other notes. This note is the ordering.
See [[Stat Reference]], [[Item Level vs Combat Power]] and
[[Progression Phases Roadmap]] for the machinery, and
[[Chanter BiS Roadmap]] for the companion plan on the support side.

## The Season 1 launch baseline this plan assumes

Global launch is 2026-10-05 with Founder early access from 2026-09-30, and NC's
own gamescom statements put the launch build at approximately Korean launch
parity. The numbers that shape a Templar plan specifically:

| Dimension | Season 1 value | Current KR value | Confidence |
| --- | --- | --- | --- |
| Level cap | **45** | 50 | Confirmed for this vault |
| Item-level range | **0–3,800** | 4,800 | 4,000+ is Chapter 1. See [[Item Level vs Combat Power]] |
| Party size | 4 | 5 | Confirmed by NC at gamescom |
| Raid size | 8 | 10 | Confirmed by NC at gamescom |
| **Stigma slots** | **4** | 6 | Inferred from the KR patch chronology, medium-high |
| **Stigma level cap** | **20** | 25 | Inferred, medium |
| Daevanion boards | Nezekan, Zikel, Vaizel, Triniel | plus Marchutan and Yustiel | Inferred, medium |
| Arcana slots | 5 | 10 | Inferred, medium |
| Arcana sets available | Primal Vigor, Magic Armor | 7 | Inferred, medium |
| Equipment grade ceiling | **Unique** | Heroic | Medium, single-source |
| Perfect Block (완벽 막기) | **absent** | present | KR patch dated 2026-03-25 |
| Accessory slots | Necklace, Earrings, Rings, Bracelet, Belt, Amulet | plus Brooch, Pendant, Seal | Medium |

The fifth stigma slot arrived in KR on 2026-03-25 and the sixth plus level 25
on 2026-07-01, so **every Korean Templar stigma guide you will find describes
five or six slots and you have four**. That single fact invalidates more
Korean Templar content than anything else in this plan. See
[[Global Launch Differences]] and [[Stigmas]].

The other quietly important row is Perfect Block. The "auto-Fury" builds that
dominate the current Korean Guardian board are a Chapter 1 artifact built on
top of Perfect Block and Chapter 1 gear scaling. The *direction* of that build
— Block is your damage stat — holds at Season 1. The *numbers* do not. Flagged
again wherever they appear below.

## Why a party wants a Templar

Concretely, in Season 1 four-player content:

- **Aggro control.** Taunt (도발) is the class's non-negotiable stigma and the
  Korean Guardian board treats its fourth specialisation as mandatory because
  that is what makes uptime continuous rather than periodic.
- **A damage floor, not zero damage.** This is the point English tank
  intuition gets wrong in AION 2. Aggro is damage-derived, so a Templar who
  cannot damage the boss also cannot hold it. The current KR endgame Guardian
  parses in the same order of magnitude as a damage dealer — around 1.05
  million dummy DPS on the mid-2026 patch — and even at Season 1 scale the
  class is expected to contribute to the clear timer.
- **Party damage amplification.** Debilitating Smash (쇠약의 맹타) is quoted by
  the Korean board as a large party damage boost, and the Guard-side Defense
  Reduction godstone lowers the boss's defence for everyone. A Templar's real
  contribution is partly on other people's damage meters.
- **Crowd control and groggy.** Empyrean Lord's Punishment (주신의 징벌) shaves 50
  groggy and stuns at range; Capture (나포) is a 100% stun against NPCs at
  specialisation 5, which makes it a mob-pull tool as well as a PvP skill.

## Stat priority

### The three positions the community actually holds

This is the most contested question about the class and the sources genuinely
disagree, so all three positions are given with their reasoning.

**Position A — Accuracy first, then percentage mitigation.** This is the
mainstream Korean stat-priority position and it is what [[Stat Reference]]
records for every class, Guardian included: Accuracy → Damage Resistance →
HP %. The reasoning is that high-tier bosses have very high parry and block
rates, and an under-accuracy character does not deal reduced damage, it deals
*no* damage on a large fraction of its swings. The Korean Guardian board puts
the Season 1–2 era working figure at roughly **1,100 Accuracy** for
Expedition Conquest Hard and Transcendence stage 10, and describes boss parry
as cutting damage by about half when you are under it.

**Position B — Accuracy last, because a tank does not need damage.** This is
the position taken by several Chinese-language tank guides: stack Defense,
Damage Resistance and HP, and let the damage dealers care about Accuracy. It
is internally coherent and it is wrong for AION 2, for two specific reasons.
First, aggro is damage-derived, so an accuracy-starved Templar loses the boss
to the party's actual damage dealer. Second, Accuracy is a *threshold*, not a
curve — you pay roughly 1,100 once and then stop, so the opportunity cost of
paying it is small and bounded. Recorded here because you will meet it, not
because I recommend it.

**Position C — Block first, because Block is the damage kit.** This is the
Korean Guardian board's own position and it is the class-specific one. Fury
(격앙) procs on block, so Block uptime is damage uptime, and the board treats
a Block figure sufficient to keep Fury permanently active as the single
defining number of the build. Korean figures quoted are roughly **1,700–1,800
Block** in the Season 2 era and **2,400+ town Block** in the Chapter 1 meta.
Both are post-launch numbers on post-launch gear scaling — treat them as the
shape of the target, not the target.

### Where I settle, and why

**PvE tanking, Season 1:**

| Rank | Stat | Why, in one line |
| --- | --- | --- |
| 1 | **Accuracy**, to about 1,100 | Cheapest threshold in the plan, and below it your aggro and your damage both fail |
| 2 | **Block**, as high as Season 1 gear allows | The only stat that is simultaneously your mitigation and your damage engine, via Fury |
| 3 | **Damage Resistance** (피해 내성) | Percentage mitigation; the KR Guardian board argues explicitly that flat Defense is nearly meaningless in PvE next to this |
| 4 | **Cooldown Reduction** | The Season 1 rotation is cooldown-gated: Warding Strike must come off cooldown to enable Judgment, and Flash Rampage shaves 3s off everything |
| 5 | **Combat Speed** | More skill presses per window, which is more Judgment activations and more block rolls |
| 6 | **Smite**, toward 30% | The flat damage doubler; comes from Wisdom, which for a tank is a late purchase |
| 7 | **Critical Hit**, then **Damage Amplification** | Real but unthresholded; they scale with everything else once 1–5 are in place |
| 8 | Flat Defense, HP % | Not worthless, but the worst value per Kinah of anything on this list |

The logic is that ranks 1 and 2 are thresholds and ranks 3 onward are curves.
Thresholds first, cheapest threshold before expensive threshold, then curves.
Accuracy is cheap because manastones, the Precise weapon option, Freedom
(Vaizel) and two titles all supply it. Block is expensive because it comes
from the Guard, Dexterity, Space (Israphel), pet understanding and a small
number of specific titles and wings — which is exactly the list in
[[Templar Support Systems]].

**Off-damage tanking (you are the tank, but the party is comfortable and you
are pushing the clear timer):** same list, two swaps. Damage Resistance drops
below Cooldown Reduction and Combat Speed, and Smite and Critical Hit move up
above Damage Resistance. Accuracy and Block do not move. That is the whole
difference — which is the useful insight, because it means a Templar does not
maintain two gear sets in Season 1, only two manastone and Arcana presets.

**PvP:** Accuracy stays first because opposing players stack Evasion and
Block. Critical Damage Resistance replaces Damage Resistance at rank 3
because it is the key PvP defensive stat. Status Effect Resist becomes real
where it was ignorable in PvE. Note that PvP-specific stats contribute
**nothing** to your displayed Combat Power, so a PvP-configured Templar reads
as weaker than they are.

**Korean-meta caveat, applying to this whole section.** Every number above is
derived from KR live data on a patch later than the launch build, and the
PvE/PvP damage coefficient split (2026-03-25) and the abolished attack power
and PvP resistance caps (2026-07-01) are all post-launch changes. The
*ordering* follows from the threshold-versus-curve argument and should
survive; the figures should be re-measured on day one.

## Phase table, level 1 to the 3,800 ceiling

The bands are item level, because after 45 character level does almost
nothing. Each phase gives the gear, the systems, and the single next
milestone. Detail per slot is in [[Templar Gear and Slots]]; skills and
stigmas in [[Templar Skills and Stigmas]]; everything else in
[[Templar Support Systems]].

### Where 3,800 comes from

Worth stating up front, because it changes how you read the last two phases.
Season 1's *content* tops out around item level 2,400 to 2,700 — Krao Cave
Hard, Fire Temple Conquest, and the Rudra Sanctuary at a community-recommended
2,700. There is no Season 1 gear tier above Unique. So the band from roughly
2,700 to 3,800 is not a gear band at all: it is the rest of the item level
formula being filled in.

Item level is a sum of base item levels, enchant levels, breakthrough levels
and Daevanion points spent. Modelling a finished Season 1 Templar:

| Term | Estimate |
| --- | --- |
| ~16–18 slots of Unique gear at base item level 67–78 | 1,100–1,300 |
| Every slot to +20 | 320–360 |
| Every slot to 5 breakthroughs | 80–90 |
| Four launch Daevanion boards at roughly 210 points each | ~840 |
| Five Unique Arcana at +80 each | 400 |
| **Modelled total** | **~2,750–3,000** |

The in-game figure reads higher than any third-party model because the client
also folds in soul-bind sub-stats, manastones, pets and titles, none of which
are itemised per gear piece. A 3,800 in-game reading on a fully finished
Season 1 Unique set is therefore consistent with this arithmetic, but I cannot
reproduce it exactly. **Treat the 2,750–3,000 figure as my derived estimate
(medium confidence) and 3,800 as the in-game display it corresponds to.** The
practical consequence is the important part: past about 2,700, a Templar stops
acquiring and starts finishing.

### The phases

| Phase | Item level | What to equip | What to invest in | The single next milestone |
| --- | --- | --- | --- | --- |
| **P0 — Ascend** | 0 → ~1,000 (levels 1–45) | Highest item level piece in every slot from quests and vendors. At 45: the free Unique-grade Longsword from the main story, the Ascension Bracelet, Daeva's Supreme Wings | Daevanion points on Vicious Strike, Pummel and Judgment. Pantheon placement as collectibles drop. Every sealed dungeon and stronghold the moment it unlocks. Start the Noble Belt scroll loop | Level 45 holding the story Longsword |
| **P1 — Foundation** | 1,000 → 1,400 | Same gear. Belt and Amulet pushed to Unique +0 minimum | The one-time sweep: all regional missions, all remaining sealed dungeons and strongholds on **both** faction maps, Empyrean Traces, Monolith resonance. **Through Hell and Back** title. Alchemy to 20 then 25 for Intermediate manastones. Blacksmithing started | Item level 1,400 with Intermediate manastones craftable |
| **P2 — Fill** | 1,400 → 1,700 | Conquest Krao Cave and Draupnir Unique armor; market fill-in for empty slots; any Guard at all | Even enchanting: +10 on weapon and Guard, +5 to +7 on armor. Intermediate manastones, Accuracy first | **Accuracy at 1,100.** Transcendence and Expedition Conquest open |
| **P3 — Arcana** | 1,700 → 2,000 | Decurion accessories bought with Abyss Points, rings first at 31,600 AP each | Essentially all Odd Energy into Transcendence. Five Rare Arcana as **4 Primal Vigor + 1 Magic Bell**. Skill levels toward 16. Nightmare Mode as tickets accumulate. Ascension Trial Normal weekly | Five filled Arcana slots with a set effect live, and Judgment at 16 |
| **P4 — Vakron** | 2,000 → 2,400 | The **Vakron** armor set from Vakron's Sky Island Conquest, plus the Vakron or Decurion Guard. Decurion armor for whatever Vakron does not cover | **Guard to 2 breakthroughs first**, and tune every spare Unique into it. Soul imprint order: Guard → weapon → gloves and chest → pauldrons and boots → ring. Pet collection and race understanding. Arcana refinement toward Unique | Guard at 2 breakthroughs with imprint lines up, weapon at +15 |
| **P5 — Craft and raid** | 2,400 → ~2,700 | Crafted Unique **Dragon Lord** Longsword and Guard at 3 breakthroughs. Enraged Kromede from Fire Temple Conquest as the drop-route alternative. Nuakum from Ferocious Horn Den for remaining gaps | Weapon to 3 breakthroughs. **Godstones now**, not earlier — Extra Damage on the weapon, Defense Reduction on the Guard. Heritage Arcana from Transcendence stage 6. Titles chosen for stats. Block pushed toward the Fury threshold | A Rudra Sanctuary clear at ~2,700 |
| **P6 — Finish** | ~2,700 → 3,800 | No new gear tier exists. This band is enchants, breakthroughs, Daevanion and Arcana | **Stigmas to 20** — the densest Combat Power in the game at 10,000–15,000 each. All four Daevanion boards toward completion. Unique Arcana at +5. Belt and Amulet to Unique +10 and **stop**. Every slot to +20 and 5 breakthroughs. Pet understanding to level 10. Monolith 30 for the **Saint of Verteron / Altgard** title and its Block 110 | The Season 1 ceiling — after which you are waiting on content, not gear |

### What to deliberately ignore, by phase

The single skill that separates fast Templars from slow ones is knowing what
to skip. Phase-specific:

- **P0:** enchanting anything below Heritage grade, manastones, Arcana, soul
  imprint, crafting beyond gathering, PvP, alts. All of it gets replaced at
  45 or is not yet available.
- **P1–P2:** Superior manastones. Intermediate stones roll a higher per-option
  value (13 against 10) and cost roughly a fifth as much to reach the same
  total. Also: soul imprint rerolling, because you are not holding gear you
  intend to keep.
- **P3:** spending Odd Energy on Expeditions. Arcana return more power per
  point, and Vakron waits for P4 without penalty.
- **P4:** deep breakthroughs on the Vakron armor set, which is transitional.
  Godstone imprinting, which is destroyed on removal.
- **P5–P6:** chasing the Combat Power number. The formula values Accuracy at
  0.25 CP per point, which is far below its real worth to a Templar who is
  still under the threshold. Build to the thresholds and let CP follow.

## Priorities and breakpoints

The breakpoints that actually gate something, in the order you meet them:

| Breakpoint | Why it matters |
| --- | --- |
| Level 45, story Longsword in hand | First weapon worth enhancing at all |
| Item level 1,000 | Krao Cave Normal, Draupnir and the Abyss open — the real start of the game |
| Accuracy ~1,100 | Boss parry stops eating roughly half your damage, so your aggro becomes reliable |
| Item level 1,600 | Transcendence opens, which is the Arcana engine |
| Skill level 16 on Judgment, Pummel, Vicious Strike | The third specialisation slot, which is where each skill's kit actually closes |
| Item level 2,000 | Five Arcana filled; Vakron becomes the priority |
| Guard at 2 breakthroughs | The Korean gearing order's first hard target, ahead of the weapon |
| Item level 2,400 | Krao Hard, Fire Temple Conquest, Sanctuary range |
| Weapon at 3 breakthroughs plus Guard at 2, both tuned | The Korean board's stated gate for Transcendence stage 9 |
| Item level 2,700 | Rudra Sanctuary by community convention |
| Skill level 20 on the three core actives | Final specialisation slots; this is where the rotation becomes the endgame rotation |
| Stigma level 20 across four slots | The Season 1 stigma ceiling and the largest CP block available |

## Costs and math

- Accuracy about 1,100 for Expedition Conquest Hard and Transcendence stage 10
  in the Season 1–2 era. Single Korean source, **medium confidence**. The
  2,350 figure in [[Stat Reference]] belongs to Sanctuary 2, which is Season 2
  content.
- Block roughly 1,700–1,800 to sustain Fury in the Season 2 era, 2,400+ in the
  Chapter 1 meta. Both **medium confidence** and both above Season 1 gear
  scaling. Treat "as much Block as the Guard, Dexterity, Space and pet
  understanding will give you" as the Season 1 instruction.
- Attack speed breakpoint quoted at 116.7 for the Judgment cast, **low
  confidence** — single Korean board post, and the mechanism behind the number
  is not explained.
- Decurion accessories by Abyss Points: rings 31,600 each, earrings and cloak
  and gloves 42,100 each, necklace and boots and pauldrons 52,600 each, chest
  and legs and weapon 60,000 to 120,000+. Abyss Point income is roughly 10,000
  from the daily supply request, 30,000 weekly, 10,000 per Abyss Corridor
  during an artifact hold, and 2,500 from five daily missions.
- One stigma from level 1 to 20 is 10,000 to 15,000 Combat Power. Four
  stigmas at 20 is therefore the single largest CP block in a Season 1
  Templar's plan.
- A full Vakron set swap was measured at about +150 item level.
- Four Daevanion boards at roughly 210 points each is roughly 840 item level,
  and every point is also the board node's stats.

## Traps and mistakes

- **Reading a Korean stigma guide without checking the slot count.** Almost
  all of them assume five or six slots. You have four. This is the single
  most consequential misreading available to a global Templar.
- **Building toward the 2,400 town Block figure at launch.** It is a Chapter 1
  number resting on Perfect Block, which the launch build does not have.
- **Stacking flat Defense.** A detailed Korean Guardian write-up argues
  Defense is nearly meaningless in PvE next to Damage Resistance, and that a
  Defense-oriented armor set is not worth taking. Damage Resistance caps
  around 80% and that is the ceiling worth approaching.
- **Treating yourself as a zero-damage tank.** Aggro is damage-derived. The
  Chinese-guide position that a tank should skip Accuracy costs you the boss.
- **Breaking through the Vakron armor set.** It is a P4 transitional set;
  breakthroughs belong on the Guard and the weapon.
- **Buying an expensive crafted weapon instead of one more breakthrough.** The
  Korean gearing thread is explicit: a 3-breakthrough lower crafted tier beats
  a 2-breakthrough higher one, so do not overpay for the tier.
- **Dismantling spare Unique drops.** They are the tuning fodder that puts
  imprint lines on your Guard. The Korean instruction is to funnel every
  spare Unique into the Guard first.
- **Pushing the Belt or Amulet past Unique +10.** With no Heroic conversion in
  the launch build, Unique +10 is the genuine endgame on both, and beyond it
  the stones-per-level cost climbs while the stat gain does not.
- **Wearing Abyss gear in PvE.** Every tier of the Abyss sets carries a −5%
  PvE Damage Boost penalty. It is a PvP set, full stop.

## Global launch notes

The whole of this note is a Korean-meta extrapolation onto an inferred launch
build, so the things most likely to be wrong on day one, in order:

1. **The stigma slot count.** If global ships with five slots rather than
   four, the PvE stigma set in [[Templar Skills and Stigmas]] gains its
   flexible fifth pick immediately and the whole "four-slot tension" framing
   softens.
2. **Whether Fury behaves at launch as the Korean board describes.** The
   passive's existence at launch is inferred, not confirmed, and the block
   thresholds are certainly different.
3. **The Accuracy figure.** 1,100 is attached to specific Season 1–2
   encounters. If global's dungeon roster was reworked — NC has said dungeons
   and PvP were reworked for global — the number moves.
4. **Whether crafted Unique Dragon Lord weapons are craftable at launch.**
   [[Weapons]] places the family in the KR Season 2–3 window while also
   arguing it becomes the launch-era ceiling under a no-Heroic build. Which
   specific tiers ship is unresolved; see the open questions.

## Open questions

- [ ] Does the Fury (격앙) passive exist in the launch build, and does it
      trigger on ordinary block or only on Perfect Block? Settled by the
      skill tooltip on day one. This is the load-bearing uncertainty in the
      entire plan.
- [ ] The Season 1 Accuracy requirement per dungeon. Only the ~1,100 figure
      for Conquest Hard and Transcendence 10 is documented, single-source.
- [ ] The Block value at which Fury is actually continuous on Season 1 gear.
      No source addresses launch-era scaling.
- [ ] Confirmed stigma slot count and level cap in the global launch client.
- [ ] Which Unique crafted Dragon Lord tiers are craftable at Season 1, and
      whether the Longsword and Guard recipes are both under Blacksmithing at
      launch.
- [ ] Whether the Templar has one or two Bracelet slots at launch. The
      aion2hub build planner shows two; [[Accessories]] records the question
      as open.
- [ ] Whether Debilitating Smash's party damage boost is the ~40% figure the
      Korean board quotes, and whether it is Damage Amplification or a
      defence debuff. The distinction changes whether it stacks.

## Sources

- [AION 2 Hub — Templar](https://aion2hub.com/classes/templar) — live global client skill list, retrieved 2026-09-17. Source of the English skill names used in this note.
- [수호성 스킬 정리(PVE)](https://www.inven.co.kr/board/aion2/6438/6625) — KR, Inven Guardian board, revised 2026-04-09, read 2026-09-06. The per-skill specialisation picks and target levels that underpin the phase table's skill milestones, and the sub-20 fallback picks.
- [수호성pvp/pve 스티그마 선택가이드](https://www.inven.co.kr/board/aion2/6438/7621) — KR, Inven Guardian board, read 2026-09-06. The stigma evaluations and, critically, the **four-stigma** point layouts that match the Season 1 slot count.
- [(스압)개인적인 pve 수호성 스킬 특화 및 스티그마 세팅](https://www.inven.co.kr/board/aion2/6438/12045) — KR, Inven Guardian board, read 2026-09-06. The 80% Damage Resistance cap measurement and the argument that flat Defense is nearly meaningless in PvE for a Guardian — the basis of Position A's rank 3 and of the flat-Defense trap.
- [수호성 세팅 / 스탯 우선순위 thread](https://www.inven.co.kr/board/aion2/6438/22782) — KR, Inven Guardian board, 2026, read 2026-09-06 **via search-result extract only** (direct fetch returned 404, so the board URL may have shifted). Source of the ~1,100 Accuracy figure, the boss-parry-halves-damage claim, the Fury block-threshold framing, the 116.7 attack speed figure, and the pet understanding Block placement. Treated as **medium confidence** throughout because it could not be re-fetched.
- [부캐 수호 연(맹)심 vs 맹(연)심 비교](https://www.inven.co.kr/board/aion2/6438/25720) — KR, Inven Guardian board, 2026-09-04. The 1,054,534 versus 1,051,644 dummy DPS measurement used for the "a Templar parses like a damage dealer" claim, and the MP-sustain caveat.
- [현재 수호 최고점 연(맹)심 셋팅 공유](https://www.inven.co.kr/board/aion2/6438/25722) — KR, Inven Guardian board, 2026-09-04. The 7.5–7.8 million dummy DPS ceiling figure and the skill-queue requirement.
- [25.11.22 수호성 세팅 공유](https://www.inven.co.kr/board/aion2/6438/166) — KR, Inven Guardian board, 2025-11-22 — one of the few genuinely **Season 1-dated** Templar posts. Capture's 100% NPC stun at specialisation 5, and Empyrean Lord's Punishment as a 50-groggy ranged stun.
- [현시점 효율적으로 장비맞추는 순서(근딜/원딜)](https://www.inven.co.kr/board/aion2/6444/839) — KR, Inven, read 2026-09-06. The gearing order that P4 and P5 are built from: Vakron armor, Decurion for the gaps, Guard to 2 breakthroughs first, all spare Uniques tuned into the Guard, crafted weapon to 3 breakthroughs, and the "3 breakthroughs on a lower tier beats 2 on a higher tier" rule.
- [아이온2 십부장 공략 십부장 순서와 어비스 포인트 수급처](https://jason-movie.tistory.com/4307) — KR blog, read 2026-09-06. Decurion item level 67, the per-slot Abyss Point costs, and the AP income figures. Medium confidence — blog aggregation of in-game shop prices.
- [아이온2, 전투력 1000에서 2000 구간 돌파를 위한 핵심 가이드](https://www.playforum.net/news/articleView.html?idxno=633300) — KR press, read 2026-09-06. The +10-on-weapon-and-Guard versus +5-on-transitional-armor enchant split, the Decurion purchase order, the Intermediate-versus-Superior manastone split by gear grade, and the instruction not to dismantle spare Uniques.
- [아이온2 바크론 공략! 패턴 및 보상 완벽 정리](https://jason-movie.tistory.com/4358) and [아이온2 바크론의 공중섬 공략](https://game.savetip.co.kr/aion2-bacron-floating-island-guide/) — KR blogs, 2025-12-27 and read 2026-09-06. Vakron entry at item level 1,600, armor being class-agnostic, three to four Vakron pieces carrying you to 2,400, and Vakron dropping both the Guard and the Forest Spirit wing feather.
- [Guided.news — AION 2: NC wants to do a lot better with the Western release](https://guided.news/en/opinion/aion-2-nc-wants-to-do-a-lot-better-with-the-western-release/) — EN gamescom hands-on, 2026-09-06. The eight-classes / four-player-party / eight-player-raid statements that fix the Season 1 baseline table.
- [AION2 Hub — patch note archive](https://aion2hub.com/updates) — KR notes in translation, read 2026-09-06. The dates that produce the stigma slot chronology (fifth slot 2026-03-25, sixth slot and level 25 on 2026-07-01) and the 2026-03-25 introduction of Perfect Block.

## Related notes

[[Templar Gear and Slots]] · [[Templar Skills and Stigmas]] ·
[[Templar Support Systems]] · [[Chanter BiS Roadmap]] · [[Stat Reference]] ·
[[Item Level vs Combat Power]] · [[Progression Phases Roadmap]] ·
[[Gear Tiers and Sources]] · [[Weapons]] · [[Armor]] · [[Accessories]] ·
[[Crafting]] · [[Enchanting]] · [[Breakthrough]] ·
[[Soul Imprint and Soul Binding]] ·
[[Manastones Spirit Stones and Godstones]] · [[Stigmas]] ·
[[Daevanion Boards]] · [[Arcana Sets and Meta]] · [[Pantheon Stats]] ·
[[Species Understanding]] · [[Wings Acquisition]] · [[Dungeons and Raids]] ·
[[Global Launch Differences]] · [[Home]]

---

## One-page summary checklist

Print this. Everything above is the reasoning.

**Levels 1–45 (item level 0 → 1,000)**

- [ ] Main story, exclusively, until it stalls; fill the Ascension gauge when it does
- [ ] Every sealed dungeon and stronghold the moment it unlocks — both faction maps
- [ ] Daevanion points into Vicious Strike, Pummel, Judgment
- [ ] Do not sell the green Noble Belt; start the Belt scroll loop on your first Stronghold
- [ ] Place every Pantheon collectible as it drops
- [ ] Enchant nothing below Heritage grade
- [ ] At 45: claim the story Longsword and the Ascension Bracelet

**Item level 1,000 → 1,400 — the foundation sweep**

- [ ] All regional missions to 100%, both maps
- [ ] Empyrean Traces, then Monolith resonance
- [ ] **Through Hell and Back** title: Distorted → Crevice → Rift Cave, then Roah in 15 minutes. Cooldown Reduction 5%, HP 800, and Block 10 owned
- [ ] Belt and Amulet to Unique +0 minimum
- [ ] Alchemy to 25 (Intermediate manastones and spirit stones)
- [ ] Blacksmithing started — it makes your Longsword *and* your Guard

**Item level 1,400 → 1,700 — fill every slot**

- [ ] Conquest Krao Cave and Draupnir; take the guaranteed cube rewards and stop
- [ ] Market-fill every empty slot; empty slots are the most expensive mistake in the game
- [ ] Weapon and Guard to +10, armor to +5–7, evenly
- [ ] Intermediate manastones, **Accuracy first**
- [ ] **Accuracy 1,100** — the first hard threshold

**Item level 1,700 → 2,000 — Arcana**

- [ ] All Odd Energy into Transcendence; farm stage 3 S-rank
- [ ] Fill all five Arcana slots before upgrading any: **4 Primal Vigor + 1 Magic Bell**
- [ ] Abyss Points → Decurion rings (31,600 each), then earrings, then necklace
- [ ] Judgment, Pummel and Vicious Strike to level 16
- [ ] Nightmare tickets — never let them cap at 14

**Item level 2,000 → 2,400 — Vakron**

- [ ] Vakron's Sky Island Conquest for the armor set and the Guard
- [ ] Decurion armor for whatever Vakron does not cover
- [ ] **Guard to 2 breakthroughs before anything else**
- [ ] Tune every spare Unique drop into the Guard
- [ ] Soul imprint order: Guard → weapon → gloves and chest → pauldrons and boots → ring
- [ ] Start pet collection and race understanding
- [ ] Arcana refinement toward Unique, Chalice first

**Item level 2,400 → 2,700 — craft and raid**

- [ ] Crafted Unique Dragon Lord Longsword and Guard, or Enraged Kromede from Fire Temple
- [ ] Weapon to 3 breakthroughs
- [ ] **Godstones now**: Extra Damage on the weapon, Defense Reduction on the Guard
- [ ] Heritage Arcana from Transcendence stage 6
- [ ] Titles: Saint of Verteron/Altgard for the Defense slot (Block 110), Teleportation Specialist for Attack
- [ ] Rudra Sanctuary at ~2,700

**Item level 2,700 → 3,800 — finish**

- [ ] **Four stigmas to level 20** — 10,000–15,000 CP each, the largest block left
- [ ] All four Daevanion boards toward completion
- [ ] Unique Arcana at +5
- [ ] Belt and Amulet to Unique +10, then **stop**
- [ ] Every slot to +20 and 5 breakthroughs, spread evenly
- [ ] Pet understanding to level 10; lock nothing before level 9
- [ ] Monolith 30 for Saint of Verteron / Altgard
- [ ] Block as high as Season 1 gear allows, for Fury uptime

**Never, at any phase**

- [ ] Leave a gear slot or a socket empty
- [ ] Buy Superior manastones before the set is final
- [ ] Wear Abyss gear in a dungeon (−5% PvE Damage Boost on every tier)
- [ ] Push the Belt or Amulet past Unique +10
- [ ] Trade Accuracy for a higher Combat Power number
