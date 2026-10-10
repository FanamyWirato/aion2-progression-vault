---
chapter: "11 Class Playbooks"
system: Chanter Progression Plan
type: progression-system
unlock: "class selection at character creation; the plan proper begins at level 45"
account_wide: false
cadence: "continuous"
gates: ["item level 1000 for Expedition", "item level 1600 for two-star Conquest", "item level 2200 for Fire Temple", "item level 2700 for Sanctuary 1", "item level 3800 practical ceiling"]
currencies: ["Kinah", "Odyle Energy", "Enhance Stones", "Breakthrough Stones", "Stigma Shards", "Daevanion Crystals", "Mysterious Crystals", "Abyss Points", "Dream Fragments"]
region_verified: ["KR", "TW"]
patch: "KR launch through Chapter 1 (2025-11-19 to 2026-09-06); written for Global Season 1 (2026-10-05)"
confidence: medium
tags:
  - aion2/progression
  - aion2/class-playbooks
  - aion2/chanter
---

# Chanter BiS Roadmap

> **In one sentence:** the Chanter (호법성) is a melee staff hybrid whose results
> are mostly other people's damage — the right build chases buff uptime and
> combat speed first, then Smite, and never stops hitting the boss in melee.

## Why it matters

Every other note in the vault describes a system. This one describes a
character — necessary because the Chanter is the class English sources get
wrong most often. Fextralife reads him as back-row buff support with some
healing; datamined class tables say `Healer/DPS`. Either produces a Chanter
who stands at range, presses heals, and delivers roughly half of what the
class should.

Korean live play is something no label captures cleanly — and that gap
changes almost every gearing choice below. Role first, then stat priority,
then the phase plan.

Mechanics are not re-explained here. [[Stat Reference]] for stats,
[[Item Level vs Combat Power]] for the numbers,
[[Progression Phases Roadmap]] for the class-agnostic sequence underneath.
Companion plan for the other support-adjacent class: [[Templar BiS Roadmap]].

## The Season 1 launch baseline this plan assumes

Global launch is 2026-10-05 with Founder early access from 2026-09-30, and
NC's own gamescom statements put the launch build at approximately Korean
launch parity. The numbers that shape a Chanter plan specifically:

| Dimension | Season 1 value | Current KR value | Confidence |
| --- | --- | --- | --- |
| Level cap | **45** | 50 | Confirmed for this vault |
| Item-level range | **0–3,800** | 4,800 | 4,000+ is Chapter 1. See [[Item Level vs Combat Power]] |
| Party size | 4 | 5 | Confirmed by NC at gamescom |
| Raid size | 8 | 10 | Confirmed by NC at gamescom |
| **Stigma slots** | **4** | 6 | Inferred from KR patch chronology, medium-high |
| **Stigma level cap** | **20** | 25 | Inferred, medium |
| Daevanion boards | Nezekan, Zikel, Vaizel, Triniel | plus Marchutan and Yustiel | Inferred, medium |
| Arcana slots | 5 | 10 | Inferred, medium |
| Arcana sets available | Primal Vigor, Magic Armor | 7 | Inferred, medium |
| Equipment grade ceiling | **Unique** | Heroic | Medium, single-source |
| Accessory slots | Necklace, Earrings, Rings, Bracelet, Belt, Amulet | plus Brooch, Pendant, Seal | Medium |

The fifth stigma slot arrived in KR on 2026-03-25, the sixth plus level 25 on
2026-07-01 — **every Korean Chanter stigma guide you find assumes five or six
slots; you have four**. That single fact invalidates more Korean Chanter
content than anything else in this plan. See [[Global Launch Differences]] and
[[Stigmas]].

Four-player parties at launch also raise the value of the **main-heal-without-
Cleric** variant — see the build table below.

## Role definition

**The Chanter is a melee staff hybrid support: primary buff and debuff carrier
for the party, competent backup healer who can cover main-healer duty in a
four-player dungeon, and real sub-DPS who must stand in melee range.**

Evidence, descending by authority:

1. **Client data.** The class table tags Chanter as `Healer/DPS` with weapon
   type **Staff**, crafted under Jewelcrafting alongside the Ranger bow. No
   mace class — mace belongs to the Cleric (치유성). No shield; off-hand is the
   **Guard** (가더), which all nine classes wear.
2. **Endgame players of the class.** The maintained PvE general guide on the
   Inven Chanter board (897,000 Combat Power) opens with: *"in boss fights,
   hybrid positioning of damage + heal + buff + debuff"* and adds that
   *"synergy rework and updates push the direction toward heal + buff + debuff
   rather than damage."* Hybrid in practice, support in intent.
3. **Unambiguously melee.** `Onslaught` (격파쇄) is left-click autoattack and
   the backbone of the rotation; `Rushing Smash` (돌진 격파) is a 20-meter gap
   closer; `Storm Chain` (폭풍쇄, fourth Onslaught hit) is **the Chanter's
   third-largest damage share**. A senior post: *"A Chanter who fears getting
   hit and throws Dark Crush from range is not a Chanter."*
4. **Can genuinely main-heal.** A Korean guide: *"You do not need a Cleric" —
   healer-replacement build*; Inven links a Sanctuary 3 clear **without
   Cleric**. Three heal sources: `Recuperation` (쾌유의 주문), `Mantra of Recovery`
   (쾌유의 진언 — **not on the current Global skill list**; do not confuse with
   Recuperation or Healing Touch) and `Healing Touch` (쾌유의 손길) stigma.
5. **TW/CN guides agree with caveats.** 護法星 as all-round support, *"not a
   dedicated healer like the Cleric"*; Season 1 CN: *"good at everything,
   master of nothing"* — every group support active has a long CD: Recuperation
   15 s base, Healing Touch 30 s, `Impeding Authority` and `Power of the Storm`
   both over a minute. **Emergency heals and timed burst support**, not a
   continuous heal stream.

**Fextralife has identity roughly right and positioning wrong.** `Healer/DPS`
overstates healing and understates buffs. One line for every decision:
*uptime on Undefeated Mantra and Power of the Storm; second job: nobody dies —
both from melee with autoattack cancel.*

### Primary build and alternatives

| Build | What it is | When |
| --- | --- | --- |
| **Buff uptime melee support** (primary) | Full stigma investment in Undefeated Mantra and Power of the Storm, melee auto-cancel rotation, `Earth's Promise` uptime, one flex heal | Standard with Cleric; build of this note |
| **Main heal without Cleric** (alternative) | Same gear. Flex stigma → `Healing Touch`, `Blessing of Life` passive levels instead of `Attack Preparation`, CD and duration specs on Recuperation | Four-player Conquest without Cleric, progression nights, early phase without a healer |
| **Block / Regeneration bruiser** (niche) | `Crossguard`, `Focused Defense`, Regeneration instead of Iron Wall, block-oriented soul imprint | PvP and certain melee bosses. Chanter-only: **Regeneration and Iron Wall ~ equally efficient for Chanter; other classes prefer Iron Wall.** One source, medium confidence |

All three builds share one gear set. Only stigma, passive levels on gear, and
a few skill specialisations differ — which is why [[Chanter Gear and Slots]]
is written once and [[Chanter Skills and Stigmas]] covers three loadouts.

## Stat priority with reasoning

Here the Chanter diverges from the generic Korean table in [[Stat Reference]]
(Accuracy → Smite → Critical). Chanter order and why.

| Rank | Stat | Why on Chanter |
| --- | --- | --- |
| 0 | **Accuracy** (명중) | Hard prerequisite like everywhere — too little = blocks/parries, not reduced damage. Doubly important: damage spread across many small multi-hits; miss rate eats the profile evenly. To content floor, then stop |
| 1 | **Combat Speed** (전투 속도) | Signature class scaling; main deviation from the generic list. Three reasons: **autoattack cancel** loop → extra hits; **measured breakpoints** (below); combat speed = cast speed → heal throughput too. `Power of the Storm` is a combat-speed buff — your combat speed and the group stat share the same axis |
| 2 | **Smite** (강타) to 30%, then 40 | Unusually cheap. **0.3% per passive level**; passive level 20 = +6% Smite, theoretically ~**9.6%** from passive sources alone; `Undefeated Mantra` stigma 20 adds **+5% Smite** for the group including you. Bosses without Smite resist → in PvE 1% = 1% DPS |
| 3 | **Cooldown Reduction** (재사용 대기시간 감소) | Heavily emphasised in guides. Every support button is 15 s to 60 s+ CD; buff/shield **uptime is performance**. On damage dealers: comfort; on Chanter: throughput. Sources: Illusion (Kaisinel), Nezekan Daevanion, `Through Hell and Back`, Talisra Wings |
| 4 | **Critical Hit** (치명타) | Wanted; Chanter twist: crit ceiling ~80%; `Dark Crush` Guaranteed Critical ~**10% damage on the skill** because it bypasses the ceiling. Crit stops earlier than on classes without guaranteed-crit specs |
| 5 | **Damage Amplification** and **Weapon Damage Amplification** | Universal multipliers. Weapon damage amplification only on weapon and Guard → first soul-imprint projects |
| 6 | **Perfect** (완벽) and **Max Attack Power** (최대 공격력) | Chanter exception. [[Stat Reference]]: do not chase Perfect (~5% real) for classes without Perfect sources. `Inspiring Spell` raises Critical **and Perfect**; Korean endgame guide: **Chanter and Spiritmaster: Max Attack Power beats Additional Attack** (20 Max over 16–17 Additional), *because* Perfect stacks. Late optimisation; boards argue over Perfect sources |
| 7 | **HP** and **Healing Amplification** (치유 증폭) | Floor, not ceiling — a floor you must hit. `Earth's Promise` shreds boss damage resistance for the group only while **your own HP ≥75%**. Below 75% you silently turn off the group's damage buff. Healing amplification scales heals; from `Blessing of Life` |
| — | Multi-hit Accuracy (다단 히트 적중) | Higher than generic: Onslaught, Incandescent Blow, Heat Wave Blow, Rushing Smash, Gust Rampage multi-hit specs |
| last | Movement Speed, Status Effect Resist | Small in PvE; strong in PvP |

### Combat speed breakpoints

The most important Chanter-only number: repeated experiments on the Inven
Chanter board — Time lord stat point by point, hits in a fixed 7-second window:

| Combat Speed | What breaks | Hits in window |
| --- | --- | --- |
| under 82.5% | Dark Crush speed-capped | 18 |
| 82.5% and above | Dark Crush cap breaks | 20 |
| 90.5% and above | Piercing Strike cap breaks | 22 |
| 118.5% and above | Dark Crush capped, then breaks | 24 |

Two caveats. First: experiment used `Marchutan's Wrath` stigma, 7 s Dark Crush
window (patch 2026-03-04) — **likely absent at Global launch**; breakpoints
are probably mechanical, framing is not. Second: hit counts depend on FPS and
latency — targets to exceed, not a benchmark. Medium confidence: one source,
careful method.

Practical at launch: **82.5% combat speed first real gear goal after
Accuracy**, 90.5% the second.

### Where the three jobs collide

The honest Chanter question is not "which stat" but **which passive levels on
which gear slot** — that is where all three jobs compete.

Korean Smite guide: **Necklace 1 + Earrings 2 + armor 7 + Mirror/Bell Arcana
4 + Chalice 4 + Daevanion 4 = 22 gear-sourced levels**, plus 10 buyable with
Skill Points → theoretically 32. ~ten passive lines. ~22 levels across ~ten
lines — **that is the build**:

- **Own damage / Smite:** `Attack Preparation` (공격 준비 — damage amplification,
  defense, accuracy), `Impact Hit` (충격 적중 — shock accuracy, Smite chance).
  Endgame Chanters push both toward 30.
- **Heal throughput:** `Blessing of Life` (생명의 축복 — max HP, healing
  amplification). Common mistake: level-15 spec on `Sprint Mantra` "+100% HP
  recovery" applies only *to that skill*, **not** Recuperation/Healing Touch.
  Larger heals → only healing amplification from Blessing of Life.
- **Group mitigation:** `Protection Circle` (보호진 — ten stacks on hit, then
  party shield 10 s), low `Crossguard`.
- **Group damage:** `Earth's Promise` (대지의 약속); since mid-2026 patch +0.7%
  critical damage amplification per level also `Wind's Promise` (바람의 약속).

Global Season 1 recommendation: **~half passive budget on gear to Attack
Preparation + Impact Hit, quarter Blessing of Life, quarter Earth's Promise +
Protection Circle** — more Blessing of Life if you are the only healer.
Protection Circle is *preventive* mitigation for scenarios long heal CDs do
not cover.

**Korean disagreement.** Late August 2026: *Smite set* vs. *full damage
amplification set* at ~equal CP (930k vs. 896k, parses); `Earth's Promise` vs.
`Inspiring Spell` same passive slot; frontal vs. rear damage amplification
same imprint line. No settled answer. Smite = flat proc doubler; damage
amplification = additive pool → **Smite relatively better with rising damage
amplification, worse far from everyone else's gear.** Under endgame Smite;
measure at endgame.

## Progression path: level 1 to item level 3800

**Korean Season 1 dungeon gates.** Everything in 0–3,800. Do not stretch to a
second scale or copy Chapter 1 numbers (4,000 / 4,500 / 4,800). **3,800** is
the peak after Ludra, enchants, boards and Arcana — not a separate dungeon.
Full table: [[Item Level vs Combat Power]].

| Phase                     | Item level      | Target gear                                                                                                     | Systems                                                                                                                                                                                                              | Next milestone                                                            |
| ------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **0. Levelling**          | 0–1,000 (1–45)  | Quest and field gear; free story staff 45; Ascension Bracelet; keep green Belt of Nobility                      | Main story only. Daevanion Onslaught and Dark Crush. Sealed dungeons/strongholds. Pantheon. Fill every empty slot                                                                                                    | Level 45 with story staff, Ascension Bracelet, Daeva's Ultimate Wings     |
| **1. Finish foundations** | 1,000–1,400     | No new gear required                                                                                            | One-time sweep: regional missions, sealed dungeon, stronghold, Empyrean Lord's Trace **both** faction maps. Belt and amulet scroll loops. Monolith resonance. Alchemy Craft 20, then 25. **`Through Hell and Back`** | ~Item level 1,400, Intermediate manastones craftable, stigma slots filled |
| **2. Complete uniques**   | 1,400–1,700     | `Bakarma Guard` Draupnir; `Rupture` staff, helm, necklace Krao Cave; rest broker                                | Draupnir and Krao each **14-dice guarantee**. Bank `Weapon Change Vouchers`. Even enchants: +10 weapon/guard, +5–+7 armor                                                                                            | Item level 1,600 — two-star Conquest and Transcendence                    |
| **3. Arcana**             | 1,600–2,000     | Unchanged; farm cards                                                                                           | **All Odyle Energy into Transcendence.** All five Arcana slots filled before upgrading. `Onslaught` on Parchment first. Abyss Points accessories. Nightmare Layer I daily                                            | Five Rare Arcana with set effect; `Undefeated Mantra` stigma 20           |
| **4. Armor set**          | 2,000–2,400     | Full `Vakron` Vakron Sky Island; `Aulamus` staff Urugugu Canyon                                                 | Breakthroughs, offense first. Soul imprint start. Pet Understanding 5, Species Understanding 9 without locks                                                                                                         | Item level 2,400 — Fire Temple and Ferocious Horn Den                     |
| **5. Season 1 endgame**   | 2,400–2,700     | `Nuakum` Ferocious Horn Den; **`Enraged Kromede` staff Fire Temple**; crafted unique Dragon Lord staff optional | Combat speed 82.5% then 90.5%. Transcendence 6–8 Heritage Arcana. Godstone staff. Belt/amulet Unique +10 **stop**                                                                                                    | ~2,700 — Sanctuary 1 Ludra                                                |
| **6. Ceiling**            | 2,700–**3,800** | `Abyssal` unique set and bracelet Ludra                                                                         | Four stigmas 20 = **300 shards**. Unique Arcana, Chalice first. Pantheon colossus `Zikel's Thoughtform`. Species Understanding 10, lock Smite slots 3 and 9                                                          | Season 1 done. 4,000+ is Chapter 1                                        |

### Differences from the damage-dealer plan

Three deviations from [[Progression Phases Roadmap]]:

1. **Draupnir before Krao Cave phase 2.** Same gate. Generic Krao first; Chanter
   Draupnir first — endboss **unique Guard**; Guard equal to main hand. Korea
   Season 3: first two premium upgrades of the season → weapon and Guard.
2. **Stigma earlier and more important.** Damage dealers: fungible CP block.
   Chanter: `Undefeated Mantra` 20 = group damage amplification, damage
   resistance, critical, accuracy, critical damage amplification and Smite buff
   at once. Guide: *"the reason the Chanter exists."* Before gear levels.
3. **Hard HP floor from phase 4.** `Earth's Promise` at 75% own HP — no glass-
   cannon manastone profile. One guide: **≥19,500 HP** ~item level 1,800 KR;
   one source, medium confidence; 75% rule confirmed everywhere.

## Priorities and breakpoints

| Breakpoint | Value | Benefit |
| --- | --- | --- |
| Accuracy | Content floor | Stops block/parry. Below it nothing else counts |
| Combat Speed | **82.5%** | Dark Crush speed cap breaks; 18 → 20 hits |
| Combat Speed | **90.5%** | Piercing Strike cap breaks; 20 → 22 hits |
| Smite | 30%, then 40 | Cheap via passive levels + +5% Undefeated Mantra 20 |
| Own HP | **75%, maintain** | `Earth's Promise` damage-resistance shred stays active |
| Stigma: Undefeated Mantra | Level 20 | Reason the party brings you |
| Stigma: Power of the Storm | Level 20 | Group combat speed + attack buff spec 20 |
| Skill: Onslaught | 20, spec 5 | `Storm Chain`, fourth hit — third-largest damage share |
| Skill: Dark Crush | 20+ | Guaranteed Critical ~10%; CD-delete spec repeatable |
| Skill: Recuperation | min. 12, ideal 20 | 12 s CD, heal scales with max HP |
| Skill: Wave Blow | 16 | **−20% incoming damage** debuff mid-boss+, CD spec holds uptime |
| Passive: Blessing of Life | as high as party needs | Only heal scaler |
| Item level | 1,000 KR equivalent | Expedition; game begins |
| Item level | 1,600 KR equivalent | Two-star Conquest and Transcendence |
| Item level | 2,200 tooltip, 2,500 social | Fire Temple. Public groups above tooltip |
| Item level | 2,700 KR equivalent | Abyssal Forge: Ludra |

## Costs and math

- **Stigma Shards:** one stigma 0→20 ~**75 shards** (~5 to 5, +10 to 10, +20 to
  15, +40 to 20). Four slots at 20 ~300. Specs at 5, 10, 15, 20. Abyss shop,
  Rift of Time and Space.
- **Skill levels:** active spec slots 8, 12, 16, 20. Skill Points + full
  Daevanion ~14 → **16 needs +2, 20 needs +6 from Arcana/gear**. Unique Arcana
  card up to 4 levels on one line.
- **Short level-20 list.** Endgame: only **two actives must hit 20** —
  Onslaught and Dark Crush — plus at most Recuperation and Incandescent Blow.
  Both required skills sit in the Parchment pool → small, aimable → Chalice for
  passives; largest Arcana planning consequence for this class.
- **Passive levels:** max 10 from Skill Points; up to 22 more from
  gear/Arcana/Daevanion; theoretically 32. 0.3% Smite/level → 32 = 9.6% Smite.
- **Guarantees:** Krao and Draupnir unique choice each **14 dice**; Urugugu **21**.
  Krao, Urugugu, Fire Temple **Weapon Change Voucher** at ceiling, two-to-one
  conversion.
- **Conquest drops Season 1 Expedition:** endboss 0.5% Heroic, 7.5% Unique Normal,
  doubled Hard; mid-bosses 0.25% and 3.75% each.

## Traps and mistakes

- **Playing at range.** Most expensive mistake. Storm Chain top-three damage;
  rotation is melee auto-cancel; staying back loses damage and Protection Circle
  stacks.
- **Believing Sprint Mantra "+100% HP recovery" heals Recuperation/Healing Touch.**
  Only that skill. Healing amplification from `Blessing of Life` is the lever.
- **Own HP under 75% and staying there.** Group shred turns off. Life-drain spec
  on Onslaught exists for this.
- **Building for Combat Power.** Accuracy/critical underweighted in CP formula;
  lord stats missing; PvP stats zero. CP optimisation strips Chanter stats. See
  [[Item Level vs Combat Power]].
- **Skipping `Through Hell and Back`.** 5% cooldown reduction + 800 HP for ~30 min
  sealed dungeons — highest power/minute; CDR = throughput.
- **Chasing Perfect early.** Real but late. Pre-endgame loses to Accuracy,
  combat speed, Smite.
- **Over-investing transitional armor.** Vakron/Nuakum level stones.
  Breakthroughs, godstones, soul-imprint rerolls on staff, Guard, belt, amulet.
- **Stacking two Chanter buff stigmas.** Mantra skills **do not stack — higher
  level wins.** Party already has Undefeated Mantra 20 → your level 10 contributes
  nothing → different flex stigma.
- **Korean guide without a date.** Reworks: Attack Preparation patch 2026-01-21;
  Undefeated Mantra −5% same patch; Spinning Strike self-buff 2026-04-29; Wave
  Blow spec 2026-01-07; Marchutan's Wrath Dark Crush 2026-03-04. March ≠ December.

## Global launch notes

**All Korea-meta-derived.** Patch-dependent recommendations flagged inline.
Most likely shifts:

- **Four stigma slots, cap 20, not six at 25.** Korea launch four; fifth
  2026-03-25, sixth with 50. Cap 20 until Chapter 1. Global Season 1:
  **Undefeated Mantra + Power of the Storm + Sprint Mantra + one flex**; six-
  slot loadouts from Korea do not apply. Most important launch adjustment.
- **Missing stigmas/specs.** `Crushing Strike` (분쇄격) 2025-12-17, `Barrier Spell`
  later; Marchutan's Wrath window 2026-03-04. Do not plan rotation around them.
- **No Heroic, reportedly.** `Enraged Kromede` and crafted unique Dragon Lord
  staff are real end weapons; **Unique +10 belt/amulet is the end line**.
  Medium confidence; Korea Expedition drops Heroic `Ancient Spirit` 0.5%.
- **Five Arcana slots, two sets, not ten/seven.** Scales 2026-02-25; Stat Arcana
  July/August 2026. Season 1: Primal Vigor and Magic Armor → 4 + 1.
- **No Pendant, Brooch, Seal** (2026-07-01, 2026-05-27, 2026-09).
- **Party five/raid ten or four/eight?** NC gamescom: four/eight like Korea
  launch. Four-player without Cleric more likely → main-heal-without-Cleric more
  valuable.
- **Balance unknown.** Largest rework since Chapter 1 2026-08-26; "identity"
  pass discussed September. Global snapshot; identity drifts toward support.

One English class tier list: Chanter PvE C-tier, low control difficulty. SEO
with low reliability — letter noise; observation (own damage behind real DPS)
matches Korea.

## One-page checklist

**Identity.** Melee staff hybrid support. Buffs/debuffs first, backup or solo
main heal second, sub-DPS third — always melee.

**Stat order.** Accuracy to content floor → combat speed 82.5 then 90.5% →
Smite 30 then 40% → cooldown reduction → critical hit → damage and weapon
damage amplification → Perfect and max attack late → HP and healing amplification
as floor, **maintain 75% HP always**.

**In this order.**

- [ ] Main story to 45, all quest rewards. Daevanion only Onslaught and Dark Crush.
- [ ] Story staff level 45 and Ascension Bracelet. Never sell green Belt of Nobility.
- [ ] All sealed dungeons, strongholds, regional missions, Empyrean Traces **both**
      faction maps.
- [ ] Distorted → Crevice → Rift → Roah for **`Through Hell and Back`**. 5%
      cooldown reduction, 800 HP.
- [ ] Start belt enhance scroll and Revelation amulet enhance scroll loops.
- [ ] Alchemy Craft 20, then 25 for Intermediate manastones and spirit stones. Never
      buy Superior early.
- [ ] Draupnir Conquest 14 dice → **Bakarma Guard**.
- [ ] Krao Cave Conquest 14 dice → **Rupture Staff**, helm, necklace. Bank Weapon
      Change Vouchers.
- [ ] Remaining slots broker. Empty is the most expensive option.
- [ ] Even enchants: +10 staff/guard, +5–+7 armor. No deeper.
- [ ] All Odyle Energy Transcendence until five Arcana slots full. Onslaught Parchment first.
- [ ] Stigmas: Undefeated Mantra 5 → Power of the Storm 5 → Sprint Mantra 5 → flex 5 →
      **Undefeated Mantra 20** → Power of the Storm 20 → Sprint Mantra 10.
- [ ] Nightmare twice daily, do not overflow 14-ticket cap. Dream Fragments for
      `Zikel's Thoughtform`.
- [ ] Vakron Sky Island → full armor set, guard, Forest Spirit Wings.
- [ ] Soul imprint: Guard → staff → gloves/chest → shoulders/boots → ring. Stop at
      combat speed **or** weapon damage amplification.
- [ ] Breakthrough offensive slots 5 before armor.
- [ ] Pet families level 5: Intelligence → Nature → Wild → Transform. Species Understanding
      9, **nothing locked**.
- [ ] Ferocious Horn Den → Nuakum. Fire Temple → **Enraged Kromede Staff**.
- [ ] **82.5% combat speed**, then 90.5%.
- [ ] Belt and amulet Unique +10, stop.
- [ ] All three title slots. Godstone on finished staff.
- [ ] Stigmas capped. Species Understanding 10, lock Smite slots 3 and 9 at 1.5%+.
- [ ] Abyssal Forge Ludra → Abyssal Bracelet, sub-stats Wisdom, Time, Death.

**Never.** At range. Belt/amulet past Unique +10. Superior manastones before final set.
Perfect early. Optimise CP display. HP under 75%.

## Open questions

- [x] ~~Which item-level scale Global launches with.~~ **0–3,800, Season 1 gates 1,000 /
      1,600 / 2,200 / 2,400 / ~2,700.** [[Item Level vs Combat Power]]. Check Conquest
      panel day one.
- [ ] Whether 82.5% and 90.5% combat-speed breakpoints are mechanical or artefact of
      the Marchutan's Wrath window. Re-test without that stigma.
- [ ] Season 1 stigma pool Global. Purple Lounge ~twelve per class; no Season 1 Chanter
      list found.
- [ ] Global four or five stigma slots.
- [ ] Heroic at launch; possibly 0.5% `Ancient Spirit` Expedition drops in build.
- [ ] Smite set vs. damage amplification set at equal CP — board both ways, no convergence.
- [ ] `Earth's Promise` vs. `Inspiring Spell` passive slot — still debated.
- [ ] Frontal vs. rear damage amplification for Chanter — no consensus.
- [ ] `Through Hell and Back` Attack, Defense or Other title slot — effects like Other,
      category unconfirmed.

## Sources

- [AION 2 Hub — Chanter](https://aion2hub.com/classes/chanter) — live global client skills, 2026-09-17. English skill names in this note.
- [\[26.08.05\] 호법성 PVE 종합 가이드](https://www.inven.co.kr/board/aion2/6451/116) — KR, Inven Chanter board, 2025-11-24 to 2026-08-05, read 2026-09-06. Author at 897k CP. **Primary source:** hybrid role, heal+buff+debuff direction, skill/stigma priorities, autoattack cancel (평캔), Storm Chain share, Undefeated Mantra 20 incl. +5% Smite, mantra non-stacking, Protection Circle, Wind's Promise 0.7%/level, Wave Blow −20%, Dark Crush guaranteed crit ~10% / 80% crit ceiling, Blessing of Life correction, Regeneration vs. Iron Wall on Chanter, seven Daevanion boards.
- [아이온2 호법성 PVP 스킬트리, 셋팅등 종합가이드](https://cvmaxlimbo.tistory.com/141) — KR, February 2026, read 2026-09-06. Closest Season 1 approximation. Four stigma slots, passive order, Incandescent cancel test, Earth's Promise 75% HP, block stat.
- [560+ 호법의 강의 및 방향성](https://www.inven.co.kr/board/aion2/6451/11651) — KR, Inven, read 2026-09-06. Melee requirement, level-20 actives (Onslaught/Dark Crush), passives toward 30, Parchment/Chalice logic.
- [재측정) 암격쇄/관통쇄 전속캡에 대한 실험 2](https://www.inven.co.kr/board/aion2/6451/14994) and [earlier 82.5–90.5% measurements](https://www.inven.co.kr/board/aion2/6451/11904) — KR, Inven, read 2026-09-06. Combat speed breakpoint table, method, FPS/latency caveat.
- [호법 PVE 간단 가이드 (평캔 매크로사용)](https://www.inven.co.kr/board/aion2/6451/7090) — KR, Inven, read 2026-09-06. Minimal loadout, four stigmas incl. Crushing Strike.
- [✨ PvE 호법성 스킬트리 & 공략: "치유성 없어도 됨" 힐러 대체 빌드](https://harukyu.tistory.com/63) — KR, read 2026-09-06. Main-healer replacement, supportive stigmas, without Cleric.
- [AION 2 Crafting Calculator](https://aion2hub.com/tools/crafting-calculator) — client, EN, read 2026-09-06. Chanter `Healer/DPS`, **Staff**, Jewelcrafting; Cleric mace.
- [《AION2》護法星技能點法與副本定位攻略](http://a.ptt543.com/thread-447611-1-1.html) and [mirror](https://www.game735.com/thread-447611-1-1.html) — TW, read 2026-09-06. Support position, class passive on reroll.
- [《AION2》護法星入門攻略｜新手技能點法、團隊輔助重點](https://sticweb.tw/aion2-%e8%ad%b7%e6%b3%95%e6%98%9f%e5%85%a5%e9%96%80%e6%94%bb%e7%95%a5/) — TW, read 2026-09-06. Not dedicated healer, long CDs, lower stigma levels.
- [《永恒之塔2》「游戏心得」PVE向上班族护法星小小心得](http://news.17173.com/content/12222025/164037427.shtml) — CN, 2025-12-22, read 2026-09-06. Season 1, good at everything, CD numbers.
- [\[아이온 2\] "스탯 낭비는 이제 그만!" PVE 효율을 극대화하는 엔드 세팅 가이드](https://gamenewb.tistory.com/66) — KR, read 2026-09-06. Chanter/Spiritmaster max attack vs. additional attack; pet slots, HP mix.
- ['강타' 세팅 가이드 (만신전 명화, 펫작, 아르카나 등)](https://www.inven.co.kr/board/aion2/6444/1138) — KR, Inven, read 2026-09-06. 0.3% Smite/level Chanter, 22-level budget, 9.6% ceiling, Undefeated Mantra +5%, pet slots 3/9 Smite.
- [아이온2 명중 강타 스탯 우선순위 2026](https://tamagotch.tistory.com/1535) — KR, Season 2, read 2026-09-06. Generic order this note diverges from.
- [\[아이온2\] PVE 영혼 각인 종결 가이드](https://game.savetip.co.kr/aion2-soul-imprint-pve-priority-guide/) — KR, 2026, read 2026-09-06. Combat speed tier zero, slot lists.
- [\[아이온2\] 원정 정복 던전별 드랍 아이템 총정리](https://madimi.tistory.com/41) — KR, read 2026-09-06. Season 1 Expedition drop map for phase table.
- [\[아이온2\] 원정 정복 난이도 완벽 공략 가이드](https://madimi.tistory.com/40) — KR, read 2026-09-06. Conquest item-level gates Season 1.
- [아이온2/원정 — 나무위키](https://namu.wiki/w/%EC%95%84%EC%9D%B4%EC%98%A82/%EC%9B%90%EC%A0%95) — KR wiki, read 2026-09-06. Drop rates, Heroic `Ancient Spirit`.
- [\[AION2\] 아이온2 스티그마 시스템 완전 정복](https://lounge.plaync.com/feed/51924?country=KR&locale=ko-KR) — NC Purple Lounge, 2025-12-22, read 2026-09-06. ~twelve stigmas/class, **max four equipped at launch**.
- [아이온2 "3월 25일에 클래스별 신규 스티그마 추가한다"](https://www.gametoc.co.kr/news/articleView.html?idxno=107107) — KR, 2026-03, read 2026-09-06. Four→five stigma slots.
- [\[아이온2\] 스티그마 올리는 방법](https://madimi.tistory.com/58) — KR, Season 3, read 2026-09-06. Shard curve ~75 to 20.
- [아이온2, 루드라가 허락한 '심연의 팔찌'...랭커들의 옵션 선택은?](https://www.playforum.net/news/articleView.html?idxno=633597) — KR, read 2026-09-06. Top Chanter lord stats; hybrid evidence.
- [아이온2직업별 각인 빌드·스킬트리가이드 2026](https://alias007.tistory.com/738) — KR, read 2026-09-06. C-tier label, low confidence.
- [\[아이온2\] 호법성 스킬트리 상향 후 최신 버전](https://vortexgaming.io/postdetail/615843) — EN/KR translation, read 2026-09-06. Recuperation 16, Gust Rampage 16.
- [아이온2 호법성 빌드 완전 공략 (1800 레벨 기준)](https://game.savetip.co.kr/%ec%95%84%ec%9d%b4%ec%98%a82-%ed%98%b8%eb%b2%95%ec%84%b1-%eb%b9%8c%eb%93%9c-%ec%99%84%ec%a0%84-%ea%b3%b5%eb%9e%5-%ec%8a%a4%ed%82%ac%ed%8a%b8%eb%a6%ac-%ec%8a%a4%ed%8b%b0%ea%b7%b8%eb%a7%88-%eb%8d%b0/) — KR, read 2026-09-06. 19,500 HP, Daevanion HP.
- [Aion 2 — Fextralife wiki](https://aion2.wiki.fextralife.com/) — EN, read 2026-09-06. Buff-support reading this note corrects.
- [AION2护法星强度解析](https://wap.pp.cn/news/781011.html) — CN, read 2026-09-06, **low trust**. AION 1 contamination — warning.
- Author demo links from Inven guide — autoattack cancel, macro, Nightmare, Chalice without Cleric. Not independently reviewed.

## Related notes

[[Chanter Gear and Slots]] · [[Chanter Skills and Stigmas]] ·
[[Chanter Support Systems]] · [[Templar BiS Roadmap]] · [[Stat Reference]] ·
[[Item Level vs Combat Power]] · [[Progression Phases Roadmap]] ·
[[Gear Tiers and Sources]] · [[Enchanting]] · [[Breakthrough]] ·
[[Soul Imprint and Soul Binding]] ·
[[Manastones Spirit Stones and Godstones]] · [[Stigmas]] ·
[[Daevanion Boards]] · [[Arcana Sets and Meta]] · [[Pantheon Stats]] ·
[[Species Understanding]] · [[Wings Acquisition]] · [[Dungeons and Raids]] ·
[[Crafting]] · [[Global Launch Differences]] · [[Home]]
