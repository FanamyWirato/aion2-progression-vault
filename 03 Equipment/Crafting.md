---
chapter: "03 Equipment"
system: Crafting
type: progression-system
unlock: "Essence Extraction from early levels; profession stations in the capital cities"
account_wide: false
cadence: "continuous, with weekly Abyss Supply Request turn-ins"
gates: ["proficiency level versus recipe requirement", "Professional grade unlock quest", "material supply"]
currencies: ["Kinah", "Odyle", "Abyss Points", "Common Skill Points", "Specialty Skill Points"]
region_verified: ["KR"]
patch: "Season 3 / Chapter 1 era, KR live as of 2026-09-04"
confidence: medium
tags:
  - aion2/progression
  - aion2/equipment
  - aion2/economy
---

# Crafting

> **In one sentence:** Crafted weapons are the best PvE weapons in the game and
> the only high-end gear that can be bought and sold, so every player interacts
> with crafting whether they level a profession or just shop on the broker.

## Why it matters

Dungeon weapons cap at Unique grade outside the Sanctuary, and weapon drop rates
are the worst in every loot table. Crafting is the answer to both problems. The
crafted Dragon Lord weapon family reaches a higher Item Lv than the dungeon
weapons available at the same time — Korean guides cite 114 for the crafted
series against 108 for the dungeon Unique — and crafted gear is **Bind on
Equip**, so it is the only endgame equipment that circulates on the market.

That has two consequences. If you craft, you have a Kinah engine. If you do not
craft, the broker is still where your best weapon comes from, which makes the
material economy relevant to you anyway. See [[Currencies and Economy]].

## How it works

### Two skills, not one

**Essence Extraction** (gathering) and the **crafting professions** are separate
systems with separate levels.

Essence Extraction is a single unified skill covering everything other MMOs split
into mining, logging and foraging. It runs **Novice level 1–50**, then a quest
from Alzirr unlocks **Professional level 1–50**, for 100 levels total and a hard
ceiling at Professional 50.

Crafting proficiency is per profession and runs on its own tier names, reported
as **Beginner (입문)** through **Professional (전문)**, with Professional 70 as the
current practical target. One Korean source instead describes an
"Intermediate Lv 95" recipe requirement, so the exact tier boundaries are
**unresolved**; treat "get your profession as high as you can before attempting
top-tier recipes" as the actionable version.

### The five professions

| Profession | Korean | Crafts | Serves |
| --- | --- | --- | --- |
| Blacksmithing | 대장 | Longsword, Greatsword, Dagger, Mace, Fist, Guard/Barrier | Templar, Gladiator, Assassin, Cleric, Brawler |
| Tailoring | 재봉 | All armor slots | Everyone |
| Jewelcrafting / Handicraft | 세공 | Bow, Staff, and Necklace, Earring, Ring, Bracelet | Ranger, Chanter, and all accessory users |
| Alchemy | 연금 | Spellbook, Orb, potions, scrolls, manastones | Sorcerer, Spiritmaster, everyone for consumables |
| Cooking | 요리 | Food and drink buffs | Everyone |

That is 1,613 craftable items in the game data. Stations sit in the capital city
districts.

**Alias warning.** English guides use different names for the same professions:
Forging for Blacksmithing, Armory or Armorsmithing for Tailoring, Carpentry or
Handicrafting for Jewelcrafting. One Korean guide also claims Blacksmithing makes
plate armor, but the recipe data puts **all** armor under Tailoring, including
the Genesis Dragon Lord Breastplate, Greaves and Helm. Trust the recipe data.

Pick the profession that makes **your own weapon**. The Korean consensus routes
are Blacksmithing for melee and Cleric, Jewelcrafting for Ranger and Chanter,
Alchemy for Sorcerer and Spiritmaster.

### The crafting minigame

Crafting resolves as a race between a **success gauge** and a **failure gauge**;
whichever fills first decides the outcome. The determining input is
**level difference = your proficiency level − the recipe's required level**. A
larger positive difference means a higher final success rate, which is why
over-levelling a profession before attempting expensive recipes is not optional.
Being hit or interrupted mid-craft counts as a failure and consumes the
materials.

### Combo crafts and Splendent items

This is the mechanic that defines high-end crafting. Every craft has a chance to
trigger a **combo** (콤보), reported as a flat **25%** on the relevant recipes and
**not improvable by any item or buff**.

- For weapons, armor and accessories, a combo produces the **Splendent** (빛나는,
  also translated Radiant or Brilliant) version of the item instead of the base
  version.
- For cooking and potions, a combo simply **doubles** the output.

The Splendent version is not a nice bonus. It is the **required component for the
next tier of the chain.** Recipes reference crafted sub-components which are
themselves combo results, so a top-tier weapon is a tree of 25% rolls stacked on
each other. This is where the real cost lives, and it is why the community
crafting calculator expands sub-recipes recursively and reports an expected
number of attempts rather than a flat material list.

Practical consequence: **you cannot budget a top-tier craft in materials, only in
expected materials.** Four base crafts per Splendent on average, at every rung.

### Chain crafting

You cannot buy your way to the top of a chain directly. Raw materials become
first-stage refined goods (ore into ingots, logs into lumber, gems into powder),
those become base equipment, base equipment combos into Splendent equipment, and
Splendent equipment feeds the next tier. Always craft from the lowest rung up and
keep every result.

Non-combo failures are **not** waste. They feed **Abyss Supply Requests** (어비스
보급 의뢰), which pay Abyss Points for turned-in goods:

- The **[Urgent]** tab takes gathering products, herbs and fruit for fast completion.
- The **[Weekly]** tab takes failed crafted equipment at Rare and Unique grade.

Never turn in **Refining Stones** (제련석), which top-tier weapons consume by the
hundreds, or genuinely scarce materials like **Sturdy Draconic Scale** (강고한
용족의 비늘) and **Splendent Odyle** (찬란한 오드). The request list will happily
ask for them.

### The item families

Recipe names mirror across factions, which is why sources disagree about the
"real" name of the crafted endgame set:

| Family | Notes |
| --- | --- |
| Genesis Dragon Lord (창룡왕) | Elyos-side naming; armor via Tailoring, Bow and Staff via Jewelcrafting, Spellbook and Orb via Alchemy |
| Nemesis Dragon Lord (멸룡왕) | Asmodian-side mirror, including the Splendent Nemesis Dragon Lord Breastplate at Item Lv 134 |
| Noble Dragon Lord | Heroic, Item Lv 108, Bind on Equip, includes the Brawler Fist |
| "Horn Dragon Lord" (기룡왕) | The name Korean guides use for the Item Lv 114 crafted PvE weapon series; how it maps to the Genesis/Nemesis pair is unconfirmed |
| Lava Heart | Weapons (Terrorblade, Deathblade, Firemace, Flamesword, Gauntlet, Barrier, Flamebow, Flamestaff) exist as both Chalice of Muspel drops and craftable recipes |
| White Dragon's / Dark Dragon's | Cooking, faction-mirrored (Seafood Pasta, Herb Tea, Beef Wellington) |

## Unlock and gates

- Essence Extraction is available almost immediately; you gather by approaching a
  node and pressing the prompt.
- **Professional gathering grade** requires the quest
  "[Upgrade] Essence Extraction Specialty Skill" from Alzirr, which appears at
  Novice 50.
- Crafting professions unlock at their city stations, with a separate quest from
  each profession master to pass into the Professional tier.
- Top-tier recipes gate on proficiency level, and the practical gate is the
  material chain rather than the level.

## Inputs: currencies, materials, sources

### Gathering mechanics worth knowing

- Materials fall into six categories: **Ore, Gem, Log, Herb, Cooking Ingredient,
  Odyle**.
- Each node allows **three extraction attempts** total, shared with other players.
- Materials come in three qualities: **Standard, Fine, Pure**. Higher quality
  gives more gathering XP and better craft inputs.
- Failed extractions still award XP, so let a losing attempt finish rather than
  cancelling — the attempt is consumed either way.
- **Odyle** floats in the air and must be gathered while hovering on your wings,
  so it depends on flight duration. See [[Flight and Traversal]].

### The gathering skill tree

Three general skills improve every extraction:

| Skill | Effect |
| --- | --- |
| Proficient Handling | Increases success gauge gain per success roll |
| Delicate Touch | Reduces failure gauge gain per failure roll |
| Lady Luck | Chance of a x2.5 or x4 critical success surge once the failure gauge is at 50% or above |

Each costs 1 Common Skill Point for levels 1–5 and 5 per level for 6–10.

Each material category then has three nodes, unlocked in order:

| Node | Cost | Effect |
| --- | --- | --- |
| Seeker | 1 Specialty Point | Shows that material on the minimap |
| Plentiful Harvest | 1–3 Specialty Points | +10% per level chance of double yield, max 30% |
| Appraiser | 1–3 Specialty Points | +10% per level chance of upgraded quality, max 30% |

You cannot max everything. Full investment would need 90 Common and 42 Specialty
Points; 100 levels only yield **65 Common and 14 Specialty**. Respeccing costs
**50,000 Kinah**.

### Why Odyle is the answer

**Substance Morph converts Odyle into any other material, and not the reverse.**
That makes Odyle the universal currency of the crafting economy and the correct
single specialisation for your Specialty Points — seven points maxes the Odyle
line. Gathering Odyle plus Gems, then morphing Odyle into whatever a recipe
demands, avoids the respec trap entirely. Substance Morph is the same mechanic
that upgrades the permanent accessories, so see [[Accessories]] and
[[Currencies and Economy]].

### Named materials

| Material | Korean | Used for |
| --- | --- | --- |
| Orichalcum Ore | 오리하르콘 | Ingots, the base of weapons and armor |
| Asvata Wood | 아스바타 나무 | Guards, staves, higher-grade scrolls |
| Ruby | 루비 | Necklaces; Sorcerer-side alchemy |
| Sapphire | 사파이어 | Rings, Orbs; Spiritmaster-side alchemy |
| Diamond | 다이아몬드 | Earrings, higher-grade options |
| Annus, Calendula | 안누스, 카렌두라 | Life and mind-recovery potions |
| Draconic Meat | 용족 고기 | Top-grade cooking |
| Spirit Stone | 정령석 | Mana Crystals; a mob drop, not gathered |
| Refining Stone | 제련석 | Consumed in the hundreds by weapon crafts |
| Odyle | 오드 | Everything, via Substance Morph |

Contested gathering points matter: Asvata Wood in particular is described as
heavily competed, which is another argument for the Odyle-and-morph route.

## Progression path

1. Gather opportunistically from the first zone. Put early Common Skill Points
   into Proficient Handling, Delicate Touch and Lady Luck to level 5 each.
2. Take Odyle Seeker and Gem Seeker first with Specialty Points.
3. Push Essence Extraction Novice to 50, then complete the Alzirr quest for
   Professional grade.
4. Max the Odyle Specialty line with seven points, then pick one general skill to
   finish.
5. Choose the one profession that makes your class's weapon and take the
   Professional unlock quest.
6. Level proficiency on **first-stage refining**: ingots, lumber, powder. This is
   the fastest XP per unit of time because the materials are cheap and abundant.
   Alchemy is the exception — it is painful until Beginner 20, when you can start
   turning Sapphire, Diamond and Ruby into powder.
7. **Craft in small repeated batches, not large stacks.** Ten separate crafts of a
   x3 output recipe gave 240 XP against 112 XP for a single x30 craft, so batching
   is worse for levelling even though it is faster in wall-clock time.
8. Once proficiency comfortably exceeds the recipe requirement, start the Dragon
   Lord chain from the bottom and hoard every Splendent result.
9. Feed non-combo results into the weekly Abyss Supply Requests instead of
   extracting or vendoring them.

## Priorities and breakpoints

- **Weapon first, always.** Crafting exists in the progression plan mainly to
  solve the weapon problem. See [[Weapons]].
- Armor and accessories can reach Heroic from dungeon cubes, so crafting them is
  a market play rather than a personal-power play. See [[Armor]] and
  [[Gear Tiers and Sources]].
- Proficiency over material stockpiling. A craft attempted below the recipe level
  is a materials fire.
- Cooking and Alchemy consumables are cheap, always relevant, and doubled by
  combos, which makes them the least risky Kinah per hour in the whole system.

## Costs and math

The expected-attempts arithmetic is the whole cost model. At a flat 25% combo
rate, one Splendent item costs **four base crafts on average**, and the base
craft itself may need Splendent sub-components. A two-rung chain therefore
implies roughly sixteen bottom-rung crafts per finished item, before accounting
for outright craft failures from insufficient proficiency.

Crafting XP is also worth budgeting:

| Result | XP |
| --- | --- |
| Normal success | baseline |
| Normal failure | 30% of success |
| Combo success | 130% of success |
| Combo failure | 30% of combo success |

A worked Korean example: going from Blacksmithing Professional 50 to 70 needs
228,283 − 82,734 = 145,549 XP, and at 618 XP per successful Refined Shugo Horn
that is about 236 successful crafts.

Gathering XP for reference, from the Orichalcum and Odyle tables:

| Material | Success | Fail |
| --- | --- | --- |
| Standard Orichalcum Ore | 24 | 8 |
| Fine Orichalcum Ore | 31 | 10 |
| Pure Orichalcum Ore | 38 | 12 |
| Standard Odyle | 28 | — |
| Fine Odyle | 36 | — |

## Traps and mistakes

- Learning the profession that does not make your class's weapon.
- Spreading Specialty Points across many materials and then paying 50,000 Kinah
  to respec. Focus Odyle.
- Extracting or vendoring non-combo craft results instead of banking them for
  Abyss Supply Requests and higher-tier attempts.
- Turning in Refining Stones, Splendent Odyle or Sturdy Draconic Scale on a
  supply request because it was on the list.
- Crafting in large stacks while trying to level proficiency.
- Attempting a top-tier recipe at exactly the required proficiency level.
- Soul Imprinting a crafted item you meant to sell. Imprinting removes
  tradability permanently. See [[Soul Imprint and Soul Binding]].
- Cancelling a gathering attempt that looks like it will fail; the attempt is
  already spent and finishing it still pays XP.
- Getting hit mid-craft. Craft somewhere safe.

## Succession Crafting

April 2026 added **Succession Crafting**, and later **Advanced Succession**, which
turns an old item's accumulated investment into a **Succession Stone** that can be
applied to a new item. This is the reason crafting a "stopgap" weapon is less
wasteful than it sounds: the enhancement levels move forward even when the item
does not. Materials for the succession chain are themselves crafted, which puts
another leg of the endgame inside the profession system. The mechanics, costs and
which grades can succeed into which live in
[[Succession and Transfer]]; treat this section only as the note that crafting is
the delivery mechanism.

Enhancement, Breakthrough, imprint rerolls and manastone sockets all apply to
crafted gear exactly as they do to dropped gear. See [[Enchanting]],
[[Breakthrough]] and [[Manastones Spirit Stones and Godstones]].

## Global launch notes

Crafting is worth it at launch, and the Launch Scale Test made the *why*
clearer even as it changed the *how*.

- **No Heroic** still makes Unique crafted weapons a ceiling piece.
- **Base Attack is higher than KR** (Splendent Ebony Dragon dagger item level
  **102, 424–545** vs KR **92, 326–419**). Built-in PvE Damage Boost is
  **missing**. Potential stones were usable on crafted weapons in the test —
  see [[Potential Enhancement]].
- Extra **soul-bind line** on weapon, Guard, and accessories is why you still
  craft. Global accessories rolled **Might, Precision, Move Speed, Combat
  Speed** — lines KR does not have. See [[Accessories]].
- Hub comparison: only the **first** Dragon Lord tier crafts directly; higher
  tiers are transfer-crafted and **bound**.
- Armour craft is still skippable for PvE. **Chest and helm are PvP
  must-crafts** because Weapon Damage Tolerance sits on their bind lines.
  See [[Armor]].
- Succession Crafting as a named April 2026 system remains unverified.

See [[Global Launch Differences]].

## Open questions

- [ ] The actual crafting proficiency tier names and level caps. Sources give
      "Beginner 1 to Professional 70" and separately an "Intermediate Lv 95"
      recipe requirement, which cannot both be a single scale.
- [ ] Whether the Work Order tiers (Amateur, Novice, Apprentice, Journeyman) cited
      by English guides are the real tier names or a mistranslation of the Korean
      tiers.
- [ ] Whether the 25% combo rate is uniform, or varies by recipe as the
      "usually 25%" phrasing implies.
- [ ] How 기룡왕 ("Horn Dragon Lord", Item Lv 114) relates to the Genesis and
      Nemesis Dragon Lord families in the recipe data.
- [ ] Whether crafted Lava Heart weapons require Chalice of Muspel drops as
      components, which would make that family raid-gated rather than freely
      craftable.
- [ ] Exact profession-station locations and the profession Professional-unlock
      quest names.
- [ ] Whether Splendent sub-components can be bought on the broker, which would
      let Kinah substitute for combo luck.
- [ ] Whether the guaranteed-success recipes added by later patches cover any
      top-tier items.

## Sources

- [Gathering, Aion 2 Wiki](https://aion2.wiki.fextralife.com/Gathering) — EN,
  updated 2026-01-09, read 2026-09-06. The authoritative account of Essence
  Extraction: six material categories, three qualities, three attempts per node,
  Novice 50 plus Professional 50 cap, the Alzirr unlock quest, the three general
  skills with their point costs, the Seeker / Plentiful Harvest / Appraiser nodes
  and percentages, the 65 Common and 14 Specialty point budget against a 90 and 42
  requirement, the 50,000 Kinah respec, the Odyle-and-Substance-Morph strategy,
  and the XP tables.
- [AION 2 Crafting Calculator](https://aion2hub.com/tools/crafting-calculator) —
  KR data, read 2026-09-06. The five professions and 1,613 recipes, the
  profession-to-item mapping that puts all armor under Tailoring, the class-to-
  weapon list including Brawler and Fist, the Splendent combo mechanic at 25% with
  Splendent items as next-tier components, recursive sub-recipe expansion, and the
  Genesis Dragon Lord, Lava Heart and White/Dark Dragon's item names.
- [아이온2 제작 공략: PVE 엔드급 무기(기룡왕) 100% 가이드](https://game.savetip.co.kr/aion2-crafting-guide-pve-weapon/)
  — KR guide, read 2026-09-06. Crafted series at Item Lv 114 against dungeon gear
  at 108, dungeon weapons capping at Unique outside the Sanctuary, the three
  class-routed professions with their weapon lists and required gathering, the
  fixed and unimprovable 25% combo rate, first-stage refining as the fast
  levelling route, Alchemy's Beginner 20 breakpoint, Abyss Supply Requests with
  the Urgent and Weekly tabs, and the do-not-turn-in list.
- [아이온2 제작 공략: 직업별 추천 및 필수 재료 파밍 Top 4](https://game.savetip.co.kr/aion2-crafting-guide-materials/)
  — KR guide, read 2026-09-06. The named-material table (Orichalcum, Asvata Wood,
  Ruby, Sapphire, Diamond, Annus, Calendula, Draconic Meat, Spirit Stone) and
  their uses, and "Odyle is both the base of all crafting and a currency".
- [제작 확률 및 효율, 아툴](https://www.aion2tool.com/craft) — KR tool built on
  NCSoft's official probability disclosure page, read 2026-09-06. The success
  gauge versus failure gauge mechanic, the level-difference formula, combo
  producing "빛나는" items for gear and doubling output for cooking and potions,
  and interruption counting as failure.
- [제작 레벨별 경험치 (입문1렙~전문 70렙), Inven](https://www.inven.co.kr/board/aion2/6444/1624)
  — KR community, read 2026-09-06. Proficiency running from Beginner 1 to
  Professional 70, higher proficiency raising final success rate as of the
  April 7 2026 patch, the combo-success 130% and failure 30% XP multipliers, the
  228,283 versus 82,734 cumulative-XP figures, and the finding that ten small
  crafts beat one large batch for XP (240 against 112).
- [Aion 2 Handicrafting Guide](https://www.u4n.com/news/aion-2-handicrafting-guide.html)
  and [Aion 2 Crafting Guide: Weapons, Procs, and Turn-Ins](https://www.mmoexp.com/News/aion-2-crafting-guide-weapons-procs-and-turn-ins.html)
  — EN, low-trust SEO, read 2026-09-06. Used only as leads for the 25% proc rate,
  crafted gear being best in slot for PvE, and the failed-craft turn-in loop, all
  of which the Korean sources above independently confirm. Their profession names
  (Forging, Armory, Carpentry) and Work Order tier names are recorded as aliases,
  not as fact.
- [Aion 2: The Complete Guide to Gathering, Crafting, and Professions](https://www.mmoexp.com/News/aion-2-the-complete-guide-to-gathering-crafting-and-professions.html)
  — EN, low-trust, read 2026-09-06. Lead for crafting stations sitting in capital
  city districts and for a per-profession Professional unlock quest; neither is
  independently corroborated.
