---
chapter: "08 Collections and Exploration"
system: Wardrobe (Closet) Skin Collection
type: progression-system
unlock: "first gear extraction or dismantle"
account_wide: false
cadence: "continuous"
gates: []
currencies: ["Kinah", "Abyss Points", "Enhancement Stones"]
region_verified: ["KR", "TW"]
patch: "Chapter 1: Land of Sand and Frost (KR 2026-07-01)"
confidence: medium
tags:
  - aion2/progression
  - aion2/collections-and-exploration
---

# Wardrobe and Skin Collection

> **In one sentence:** registering gear appearances in the Wardrobe (옷장) grants a
> Weapon Attack Power Increase percentage that multiplies your damage — typical
> players run 7–10%, high-end players 21.2% — plus two titles at 100 and 700 skins.

## Why it matters

The Wardrobe is disguised as a fashion menu and it is one of the largest hidden
multipliers in the game. Korean players call it 옷장 내실, "closet substance", and
put it in the same tier as pet understanding as a reason two identically-geared
characters do different damage.

The mechanically important part is the **Weapon Attack Power Increase percentage**.
A long technical Inven thread on the Gladiator board, testing damage output with
two weapons of known attack values, established the formula behaviour:

```
attack difference × (1 + Attack Increase%) × (1 + Wardrobe Weapon Attack%)
```

That test was run by a player with **Wardrobe 21.2%**, and the predicted and
observed attack values matched within rounding. A separate damage-formula
investigation states that in practice, Weapon Damage Amplification and the
Wardrobe's weapon attack percentage both multiply into the Max Attack Power term,
and that "most players have secured roughly 7–10% Wardrobe weapon attack
increase". So the realistic range is 7–10% for an ordinary account and 21.2% as a
documented high-end figure.

For scale: a 10% multiplier on your weapon attack contribution is more than most
single enchant steps deliver, and it applies to every hit forever. See
[[Item Level vs Combat Power]] and [[Stat Reference]] for how this interacts with
the rest of your damage.

The second reason is the two titles, which are among the best generic titles in the
game — details below.

## Terminology and aliases

| Term | Notes |
| --- | --- |
| **Wardrobe** | The term used by English-language guides and by Vortex Gaming's translations. Preferred here. |
| **Closet** | The other common English rendering; mmom and mein-mmo use it. Same system. |
| 옷장 | Korean original — literally "wardrobe / clothes cupboard". |
| 옷장 내실 | "Closet substance" — Korean shorthand for the stat side specifically. |
| 외형 수집 (appearance collection) | The Korean name for the act of registering skins. |
| Collection Effects | The passive stat bonuses from filling the Wardrobe. |
| Empty Closet / 아이고, 입을 옷이 없네 | The 700-skin title. The Korean is a joke: "oh dear, I have nothing to wear". |

## How it works

Every piece of gear in AION 2 carries an appearance. The first time you register
that appearance — by extracting or dismantling the item — the skin is permanently
unlocked in your Wardrobe and awards **collection points** based on its grade.
Points accumulate into Collection Effects, which are permanent passive stats.

Registration is one-way and one-time per appearance. Once unlocked, you can apply
that look to any compatible gear without owning the original item.

### Grade-to-point table

| Grade | Colour | Collection points |
| --- | --- | --- |
| Unique | Yellow | **4** |
| Transcendence | Blue | **3** |
| Advanced / Rare | Green | **2** |
| Common | White | not stated (presumably 1) |
| Heroic | Red | not stated (presumably 5+) |

This table comes from a single Korean guide (relayed by Vortex Gaming) and is not
corroborated elsewhere, so treat it as **medium confidence**. The rarity ladder
itself — White → Green → Blue → Yellow → Red — is confirmed by multiple sources.
Note the terminology collision: Korean sources use 전승 (Transcendence) for the blue
tier where English guides often say "Rare", and 고급/희귀 for green.

### The two exclusion rules that most players get wrong

These are the highest-value facts in this note.

1. **Cash-shop-only appearances do not count.** Skins obtainable only with cash are
   excluded from collection points. The shop is not a shortcut to the stat.
2. **Only your own class's weapons feed the stat.** Other classes' weapon skins
   still increment the achievement counter toward 700, but contribute **nothing**
   to Wardrobe collection stats. A Korean guide states this as an explicit warning
   with a screenshot, and repeats it in its FAQ.

The practical consequence: the 700-skin title and the Wardrobe stat total are two
separate progress bars that happen to share a source. You can hit 700 and still
have a mediocre stat total if you fed it foreign weapon skins.

### Collection Effects

Filling the Wardrobe activates permanent passive boosts. The attributes named by
sources are:

- **Weapon Attack Power** (the percentage discussed above — the important one)
- **Armor Defense**
- **Accessory Attack and Defense**

Korean guides describe the effects as arriving "per body-part slot" — you get a
bonus tied to each equipment category as you fill that category's appearances. One
Korean guide describes the practical feel at the 700-skin mark as "like adding one
more manastone option to every piece of gear".

**No source publishes the point-to-percentage table.** Every guide, Korean and
English, describes Collection Effects qualitatively. This is the single biggest
documented gap in this system and it is recorded in the open questions.

### Titles

| Title | Grade | Requirement | Equipped effect | Owned effect (always on) |
| --- | --- | --- | --- | --- |
| Fashionista | Rare | Obtain 100 Skins | Combat Speed 3.7% | Critical Hit 5 |
| Empty Closet | Unique | Obtain over 700 Skins | Combat Speed 5%, Natural HP Regen 40, Cooldown Reduction 5% | HP 50 |

There are further skin titles between these two. An Inven player who catalogued
title-granting achievements reports the **owned** effects along the ladder as
**Critical Hit 5 at 100 skins, HP Recovery 10 at 300, and HP 50 at 500**, and
assesses 300 and 500 as hard targets with unremarkable effects — worth taking as
they arrive rather than chasing. Confidence on the 300 and 500 values: medium,
single source. The 100-skin value matches aion2hub's Fashionista entry exactly,
which is a good sign for the rest of the list.

Empty Closet is a genuinely strong generic title: 5% Combat Speed and 5% Cooldown
Reduction are useful to every class in the game, and the Korean guide dedicated to
it calls it "not a mere collector's title". Its stats are confirmed independently
by aion2hub, questlog.gg and mmom, which is unusually good corroboration.

The 700-skin count is tracked by the **Fashionista** achievement, whose steps are:

| Step | Skins |
| --- | --- |
| 1 | 10 |
| 2 | 50 |
| 3 | 100 |
| 4 | 200 |
| 5 | 300 |
| 6 | 500 |
| 7 | **700** |
| 8 | **1,000** |

Rewards along the ladder are bound Kinah and Lucky Aura, with the Fashionista title
itself at step 3 (100 skins). The existence of a 1,000-skin step means there is
progression beyond Empty Closet, though no source documents a reward for it beyond
the achievement completion.

### Synthesis: upgrading duplicate skins

Duplicates are not wasted. Combine **4 duplicate skins of the same rarity** for a
random chance at a skin of the next tier up. A booster item, purchasable or
exchangeable with Mileage Points from premium purchases, raises the success rate.

The one published rate is that **synthesising 4 Unique (yellow) skins has a 10%
chance of producing a Heroic (red) skin**. That figure comes from a single English
source (mmom) with no Korean corroboration, so treat it as **medium-to-low
confidence**. It is directionally consistent with Korean guides calling red skins
"extremely difficult".

## Unlock and gates

Nothing to unlock beyond doing your first extraction. There is no level gate, no
quest and no item-level requirement. The Wardrobe grows from the moment you start
discarding gear correctly.

## Inputs: currencies, materials, sources

| Source | Skin unlock rate | Notes |
| --- | --- | --- |
| **Extracting normal gear** | Random chance | The primary route. Also refunds 100% of Enhancement Stones invested in that item, and costs Kinah. See [[Extraction and Refunds]]. |
| **Dismantling Abyss (AP) gear** | **100% guaranteed** | The efficient route to Unique skins. Abyss gear only refunds 70% of Enhancement Stones, so use gear you bought specifically for this. |
| Hidden Cubes | Direct item drops | ~25 Unique helm/earring/necklace skins plus an Epic helm skin sit in the cube pool. See [[Hidden Cubes]]. |
| Monolith resonance | Direct item grants | Full 7-piece Unique sets: Crimson Twilight Gown, Light of Life, Windbound Wanderer, Salvation's Grace. See [[Empyrean Traces and Feathers]]. |
| Black Cloud Trading Company | Kinah purchase | Buyable with in-game currency, but Korean guides warn it is a heavy Kinah drain for free-to-play players. |
| Events and battle pass | Direct grants | See [[Seasons and Battle Pass]]. |
| Cash shop | Direct grants | **Excluded from collection points.** Cosmetic only. |

### The Abyss Point route to guaranteed Unique skins

The most-cited optimisation, from an English guide summarising Korean practice:

1. Visit the AP Merchant and buy **Guardian Decanus** gear — specifically
   **earrings, gloves or cloaks**. Do not buy rings; rings have no visual skin.
2. Dismantle it. Abyss equipment dismantling has a **100% skin unlock rate**, so
   each purchase is a guaranteed Unique skin.
3. Dismantling AP gear refunds **80% of the Abyss Points** spent, so the net cost is
   roughly **8,000 AP per guaranteed Unique skin**.
4. Use the resulting Uniques as synthesis material for Heroic rolls.

The 100% Abyss dismantle rate is corroborated by Vortex Gaming's Korean equipment
guide. The 80% AP refund and 8,000 AP net figure are single-source from mmom and
should be treated as **medium confidence** — verify against the AP merchant prices
on your own server before committing Abyss Points. See [[Abyss Points and Ranks]].

## Progression path

1. **From level 1: change your discard habit.** If a tooltip says NEW, extract or
   dismantle it — never vendor and never sell it. Registered appearances are gone
   forever if you sell the item unregistered. Korean guides state this as the single
   rule that matters most.
2. **Register everything, including junk grades.** Green items still award 2 points.
   The Korean phrasing is that low-grade registrations accumulate into "defence
   0.3%"-scale stats, which is real.
3. **Around 100 skins:** Fashionista title. Equip it if nothing better is competing.
4. **Mid-game:** start banking duplicates for synthesis rather than discarding them.
5. **Once you have surplus Abyss Points:** run the Guardian Decanus loop for
   guaranteed Uniques, which are both the highest point value and the best synthesis
   material.
6. **700 skins:** Empty Closet. This is the endgame target for the title side.
7. **1,000 skins:** the last Fashionista step, reward unknown.

## Priorities and breakpoints

| Priority | Target | Why |
| --- | --- | --- |
| 1 | Register every NEW appearance before disposal | Free, irreversible if missed |
| 2 | 100 skins | Fashionista, Combat Speed 3.7% |
| 3 | Fill your **own class's** weapon appearances | Only these move the weapon attack percentage |
| 4 | 7–10% Wardrobe weapon attack | The "normal account" benchmark from Korean damage analysis |
| 5 | 700 skins | Empty Closet: Combat Speed 5% + Cooldown Reduction 5% |
| 6 | Synthesise toward Heroic skins | Highest point value per slot; 10% per 4-Unique roll |

## Costs and math

- **Extraction is Kinah-positive on balance** for normal gear: you pay a Kinah fee
  and recover 100% of Enhancement Stones. Abyss gear recovers only 70%.
- **Abyss route:** roughly 8,000 AP net per guaranteed Unique skin (medium
  confidence). Each Unique is 4 collection points.
- **Synthesis:** 4 same-rarity duplicates per roll; 10% Unique→Heroic (medium-low
  confidence). Expect ~40 Unique skins consumed per Heroic without boosters.
- **Damage effect:** a documented 21.2% at the high end and 7–10% as the common
  band. This multiplies into stat attack and into the Max Attack Power damage term.

### Do you need to spend money?

No, and buying cash skins actively does not help the stat. Cash-obtainable
appearances are excluded from collection points, which means the entire stat side
of this system is free-to-play content. Money can accelerate the *title* counters
(a cash skin presumably still counts as a skin for the 700 tally — unverified) and
can buy synthesis boosters via Mileage Points, but the multiplier itself is earned
by dismantling gear and running the Abyss loop. The Kinah route through the Black
Cloud Trading Company exists but Korean guides describe it as painful for
free-to-play Kinah budgets.

## Traps and mistakes

- **Selling or vendoring an unregistered appearance.** Irreversible. The rule is
  absolute: NEW tooltip means dismantle.
- **Feeding the counter with other classes' weapon skins.** Counts for 700, worth
  zero stats. This is the trap that produces a "maxed" Wardrobe with a weak
  multiplier.
- **Buying cash skins for power.** Excluded from collection points.
- **Buying rings from the AP merchant to dismantle.** Rings have no visual skin, so
  the purchase is wasted.
- **Dismantling Abyss gear you actually enhanced.** You lose 30% of the invested
  Enhancement Stones. Buy fresh AP gear for the skin loop.
- **Discarding duplicates.** They are synthesis material.
- **Expecting the Wardrobe percentage to boost Max Attack Power on the tooltip.**
  The Inven investigation found the Wardrobe percentage applies to *stat* attack,
  not to the displayed Max Attack Power number; a follow-up analysis found it does
  multiply into the damage calculation. Both can be true — display and formula
  differ. Do not use the character sheet to judge this stat.

## Global launch notes

The Wardrobe is core content from the 2025-11-19 KR/TW launch and should be present
at global launch on 2026-10-05. Expect these differences:

- The skin **pool** will be smaller. Every KR season and chapter has added skins,
  including collaboration lines. A global launch build will have fewer registrable
  appearances, which makes 700 harder to reach early.
- Founder's Pack cosmetics (Ascended Daeva armour, Eternal Sun weapon, Moonlit
  Aria armour, Daeva's Styling Chest) are paid appearances and, by the
  cash-exclusion rule, are unlikely to feed collection points. Unverified for the
  global build.
- The Monolith and Hidden Cube skin sets should be present, since both systems ship
  at launch.
- Korean sources for the numbers in this note are from Chapter 1 (2026-07-01) and
  earlier. See [[Global Launch Differences]].

## Open questions

- [ ] **The point-to-percentage table.** What Wardrobe point totals correspond to
      what Weapon Attack Power Increase percentages, and are there discrete
      thresholds or a continuous curve? Settled by screenshots of the Wardrobe stat
      panel at several known point totals. This is the highest-value missing fact.
- [ ] Is the Wardrobe per character or per account? One low-trust English source
      claims gear registration gives "permanent, account-wide boosts"; no Korean or
      official source says so, and every other collection system in the game is
      character-bound. Settled by checking a fresh alt's Closet.
- [ ] Point values for Common (white) and Heroic (red) skins. Only Unique 4 /
      Transcendence 3 / Advanced 2 are documented, from one source.
- [ ] Does a cash-shop skin count toward the 700-skin achievement tally even though
      it gives no collection points?
- [ ] The 10% Unique→Heroic synthesis rate — single English source, no Korean
      corroboration.
- [ ] The 80% AP refund and ~8,000 AP net per Unique skin — single English source.
- [ ] Owned-effect values for the 300-skin and 500-skin titles, and their names.
      Single Inven post; not yet cross-checked against aion2hub.
- [ ] What does the 1,000-skin Fashionista step award?
- [ ] What is the maximum achievable Wardrobe weapon attack percentage, and has
      anyone published a full-collection figure above 21.2%?

## Sources

- [Vortex Gaming — Core Guide to Boosting Hidden Combat Power (Pets, Wardrobe)](https://vortexgaming.io/en/postdetail/603072)
  and its [Korean original](https://vortexgaming.io/postdetail/603072) — KR guide,
  read 2026-09-06; the grade-to-point table (Unique 4 / Transcendence 3 / Advanced
  2), the cash-skin exclusion, the own-class-weapons-only rule, the percentage
  nature of the effect, and the Black Cloud Trading Company Kinah route.
- [Inven — [장문] 최대 공격력, 추가 공격력 보고서](https://www.inven.co.kr/board/aion2/6448/23000)
  — KR player analysis, Gladiator board; the controlled two-weapon experiment
  showing the Wardrobe percentage multiplying stat attack, run at a documented
  Wardrobe 21.2%, and the finding that it does not appear in the Max Attack Power
  display.
- [baystory — 아이온 2 다들 버리던 최대 공격력, 실험해보니 결과가 달랐습니다](https://baystory.tistory.com/564245)
  — KR player analysis; the practical damage formula including Wardrobe weapon
  attack as a multiplicative term, and the "most players have 7–10%" benchmark.
- [game.savetip.co.kr — 외형 수집 공략: '아이고, 입을 옷이 없네' 타이틀 획득 팁](https://game.savetip.co.kr/aion2-appearance-collection-guide-title/)
  — KR; the 700-skin title's Combat Speed 5% and Cooldown Reduction 5%, the
  permanent Wardrobe stat growth, the "like one more manastone per slot" scale
  comparison, and the explicit warning plus FAQ that other classes' weapon skins
  count for the title but not for the stats.
- [game.savetip.co.kr — 실전 내실 공략: 뻥투력 말고 '진짜' 대미지 올리는 법](https://game.savetip.co.kr/aion2-practical-stats-guide/)
  — KR; the "if the tooltip says NEW, register it regardless of grade" rule,
  low-grade registrations accumulating into ~0.3% defence-scale stats, and dismantle
  rather than sell as the community standard.
- [AION2 Hub — Titles](https://aion2hub.com/database/titles) — KR/TW game data, read
  2026-09-06; Fashionista (Rare, 100 skins: Combat Speed 3.7% equipped, Critical Hit
  5 owned) and Empty Closet (Unique, 700 skins: Combat Speed 5% / Natural HP Regen
  40 / Cooldown Reduction 5% equipped, HP 50 owned).
- [questlog.gg — Title: Empty Closet](https://questlog.gg/aion-2/en/db/item/532530068)
  — KR/TW game data, read 2026-09-06; independent confirmation of the same three
  equipped effects and the HP 50 owned effect.
- [questlog.gg — Fashionista Ⅰ achievement](https://questlog.gg/aion-2/en/db/achievement/440100800)
  — KR/TW, read 2026-09-06; the full 10/50/100/200/300/500/700/1000 step ladder and
  the Kinah plus Lucky Aura rewards with the title at step 3.
- [mmom — How to Customise Outfits & Boost Stats in Aion 2](https://www.mmom.com/aion-2-news/detail_how-to-customise-outfits-boost-stats-in-aion-2.html)
  — EN, 2026-07-16, **low trust** (Kinah/boosting vendor); the source of the rarity
  ladder, the 4-duplicate synthesis mechanic, the 10% Unique→Heroic rate, and the
  Guardian Decanus / 80% AP refund / ~8,000 AP per Unique loop. All numeric claims
  from this source are flagged medium or lower in the note above. Its Empty Closet
  stats are corroborated by two independent databases.
- [Vortex Gaming — Detailed Equipment System Guide](https://vortexgaming.io/en/postdetail/594067)
  — KR guide in English, read 2026-09-06; extraction gives 100% Enhancement Stone
  refund for normal gear and 70% for Abyss gear, skin acquisition on extraction is
  probabilistic, and collection points are awarded by extracted item grade.
- [dowg — 아이온2 장비 강화 완벽 가이드](https://dowg.tistory.com/432) — KR, 2025;
  appearance collection awards points by grade on first acquisition, with per-slot
  additional stat bonuses.
- [Vortex Gaming — 전투력 이상의 대미지를 위한 실전 내실](https://vortexgaming.io/postdetail/623735)
  — KR, read 2026-09-06; dismantle unowned appearances, synthesise for higher tiers,
  and the placement of the Wardrobe alongside pets, titles, Pantheon and wings as
  the "real damage" systems.
- [Inven — 타이틀 주는 업적 뭐가있나](https://www.inven.co.kr/board/aion2/6444/594)
  — KR player catalogue; the 100 / 300 / 500 skin milestone owned effects
  (Critical Hit 5 / HP Recovery 10 / HP 50) and the assessment that the higher two
  are not worth chasing. Also mentions buying unowned appearances from the shop at
  50% off as a routine top-up.
- [Games Press — AION 2 Founder's Pack announcement](https://www.gamespress.com/en-US/AION-2-FOUNDERS-PACK-AVAILABLE-TODAY-FEATURES-FIVE-DAYS-OF-EARLY-ACCES)
  — GLOBAL, 2026-07-22; the paid cosmetic contents referenced in the global launch
  notes.
