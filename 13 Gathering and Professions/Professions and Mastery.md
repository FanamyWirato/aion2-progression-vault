---
chapter: "13 Gathering and Professions"
system: Crafting professions and mastery
type: progression-system
unlock: "learn each profession from its master NPC in a capital city crafting district; a promotion quest and a promotion item pass each profession into the Professional tier"
account_wide: false
cadence: "continuous"
gates: ["mastery level versus the recipe's required level", "Alchemy 5 / 20 / 25 for powder, mid manastones and mid spirit stones", "Blacksmithing mastery 1 / 10 / 20 / 30 for the ore conversions", "the promotion quest and promotion item for the Professional tier", "Jewelcrafting mastery 40 for the Brooch (post-launch, KR 2026-05-27)"]
currencies: ["Kinah", "Abyss Points"]
region_verified: ["KR", "TW"]
patch: "KR live as of 2026-09-06; mastery-gate values from the KR client conversion data. Brooch slot and recipe dated to the KR 2026-05-27 patch and treated as post-launch"
confidence: medium
tags:
  - aion2/progression
  - aion2/gathering-professions
---

# Professions and Mastery

> **In one sentence:** there are five crafting professions, not four; mastery
> levels come from **volume of cheap crafts** rather than from crafting anything
> good; and the correct order for a Season 1 player is **Cooking first, Alchemy
> second, your own weapon profession third.**

> **Season 1 verdict.** All five professions, the mastery ladders, the promotion
> quests and the combo mechanic are Korean-launch systems and should ship
> complete. **The Brooch is not.** The Brooch *slot* and its Jewelcrafting-40
> recipe both arrived on **2026-05-27**, ten months into the Korean service and
> behind an item level 4,500 raid — so at Season 1 the item that Jewelcrafting is
> famous for cannot be equipped, and Jewelcrafting drops to fourth priority.
> The Brooch case is preserved in [Later-season roadmap](#later-season-roadmap-the-jewelcrafting-40-brooch-gate) below, because it becomes correct in Season 3.

This note covers the professions as *progression systems*: how mastery levels,
what each rank unlocks, and where to invest. For the recipes themselves, the
success gauge, the 25% combo and the Splendent chain, see [[Crafting]].

## Why it matters

Mastery level is the input to the crafting success formula. The success chance
of any craft is driven by **level difference = your mastery − the recipe's
required level**, and the April 2026 patch made higher mastery raise the final
success rate outright. A craft attempted at exactly the required level burns
materials at a bad rate. So mastery is not a badge; it is the thing that
decides whether your expensive materials survive.

Mastery is also a gate in its own right. Several material conversions are locked
behind specific mastery ranks, which means profession level unlocks *progression
systems*, not just recipes. See [[Material Conversion]]. At Season 1 the gates
that actually bind are **Alchemy 5 / 20 / 25** for powder and mid-grade
manastones and spirit stones, and **Blacksmithing 1 / 10 / 20 / 30** for the ore
conversion ladder. Jewelcrafting 40 gates a slot that does not exist yet.

## How it works

### Five professions, and the four that matter

The user-facing framing of "four crafting professions" is nearly right and it is
worth being precise about why.

| Profession | Korean | TW | Crafts | Gates conversions? |
| --- | --- | --- | --- | --- |
| Blacksmithing | 대장 | 鐵匠 | Longsword, Greatsword, Dagger, Mace, Fist, Guard | **Yes** — the Ore conversions |
| Jewelcrafting | 세공 | 手工藝 | Bow, Staff, Necklace, Earring, Ring, Bracelet, and *post-launch* the Brooch | **Yes** |
| Alchemy | 연금 | 煉金 | Spellbook, Orb, potions, scrolls, manastones, spirit stones | **Yes** |
| Cooking | 요리 | 料理 | Food and drink buffs, cook's seasonings | No |
| Tailoring / Armor | 재봉 / 갑옷 | 盔甲 | **All armor slots** | No |

So: five professions exist, and the fifth is armor. The **three** that appear on
conversion lock badges in the client data are Blacksmithing, Jewelcrafting and
Alchemy; **Cooking** belongs in the shortlist anyway because it is the universal
consumable engine and the correct first pick. Tailoring/Armor is the one that
does nothing except make armor, which — given that dungeon and Abyss armor is
adequate and crafted armor is a market play rather than a personal-power play —
is why it drops off most recommendation lists.

**Alias warning.** English coverage is a mess here. Blacksmithing appears as
Forging; Tailoring as Armory or Armorsmithing; Jewelcrafting as Handicraft,
Handicrafting, Carpentry or Lapidary. The questlog database uses literal Korean
compounds: 갑옷제작 (armor crafting), 요리제작 (cooking crafting). Cross-check
against [[Glossary KR TW EN]] before trusting any English profession name.

### Mastery ranks

This is the least-settled part of the system, and the note is explicit about it.

What is solid: mastery runs on named tiers with a numeric level inside each
tier, it starts at **입문 (Beginner / Novice)**, it passes a promotion gate, and
the current top tier is **전문 (Professional)** with **70** as the practical
target level rather than 50.

What is not settled: how many tiers sit between, and their names. The sources
disagree in a way that cannot all be true at once:

| Source | What it says |
| --- | --- |
| Inven crafting-XP thread | A single continuous scale from 입문 1 to 전문 70 |
| questlog recipe pages | The Brooch requires "**초급 Lv 40**" (Beginner/Elementary 40) |
| Inven Brooch guide | The same Brooch requires "**수습 세공 40**" (Apprentice Jewelcrafting 40) |
| AION 2 Hub conversion data | Numeric only: "Blacksmithing Mastery 1 / 10 / 20 / 30" |
| One Korean guide | Cites an "Intermediate Lv 95" recipe requirement |
| English SEO guides | Work Order tiers of Amateur → Novice → Apprentice → Journeyman |

The two Brooch readings (초급 40 versus 수습 40) describing the same recipe
strongly suggest the client shows a tier name this vault has not pinned down
and that Korean writers paraphrase it inconsistently. **Treat mastery as a
single number and treat "get comfortably above the recipe requirement" as the
actionable rule.** Do not plan around a tier name.

### The promotion into Professional

Each profession has its own promotion, and it works like the gathering one:

- A **quest** from that profession's master, typed `gathercraftmastery` in the
  client data, e.g. `[Upgrade] Cooking Professional Technique`
  (`[升級]料理專業技術`), recommended level 10.
- The quest awards a **promotion item** — a consumable of item type
  `craftmastery`, named `<profession>제작 승급: 전문`, e.g. `요리제작 승급: 전문`
  ("Cooking Crafting Promotion: Professional") and `갑옷제작 승급: 전문`. Its
  description reads "unlocks the secret of promotion; your blocked mastery can
  now reach the Professional stage".
- The Cooking promotion quest also pays a **Pantheon artwork**,
  `명화: 요리 달인` ("Painting: Cooking Master"), which is permanent account-side
  stats. That makes the promotion worth doing on professions you do not intend
  to main. See [[Pantheon Statues and Frames]].

Promotion is level-cheap (recommended level 10) and gated on mastery, not on
character level.

### How mastery actually levels

Two rules, both counter-intuitive, both well documented.

**1. Craft the cheapest thing, in bulk.** Mastery XP scales with the recipe, not
with the value of the output, and first-stage refining is where the XP per unit
of material is best:

| Profession | The grind recipe |
| --- | --- |
| Blacksmithing | Orichalcum Ore → **Ingots** |
| Tailoring/Armor | Hide → cloth/leather intermediates |
| Jewelcrafting | Gem ore → **Powder**; Asvata Log → **Lumber** |
| Alchemy | Spirit Stone → **Spirit Stone Powder** (from Alchemy 5) |
| Cooking | The base-tier dishes, not the Master's or Dragon's versions |

Alchemy is the one painful start: it is rough until roughly **Beginner 20**,
where turning Sapphire, Diamond and Ruby into powder opens up. Spirit Stone
Powder from level 5 partly solves this, since one field-dropped Spirit Stone
becomes three Powder.

**2. Many small crafts beat one big batch.** Multi-output recipes do **not**
scale XP with output. Measured Korean results:

| Approach | XP |
| --- | --- |
| Spirit Stone Powder ×3, crafted 10 times | **240** |
| Spirit Stone Powder ×30, crafted once | 112 |
| Magic Crystal ×1, crafted 10 times | **200** |
| Magic Crystal ×10, crafted once | 112 |
| Orichalcum Ingot ×1, crafted 10 times | **200** |

Batching is faster in wall-clock time and roughly **half as efficient** in XP.
If you are levelling, click more.

### Mastery XP reference

Per-craft success XP, from a Korean community table:

| Craft | Success XP | Failure XP (30%) | Combo success (130%) | Combo failure |
| --- | --- | --- | --- | --- |
| Crystal (결정) | 20 | 6 | — | — |
| Powder (가루) | 24 | 7 | — | — |
| Manastone (마석) | 60 | 18 | 78 | 23 |
| Spirit Stone (영석) | 74 | 22 | 96 | 28 |
| Refined Shugo Horn | 618 | 185 | — | — |

Cumulative requirements: **Beginner 50 = 8,809 XP**, **Professional 50 =
82,734**, **Professional 70 = 228,283**. So the Professional 50→70 climb is
145,549 XP, or about **236 successful Refined Shugo Horn crafts**. Failures are
not zero-value — a failed craft still pays 30%.

### Work orders: what the English guides are talking about

English profession guides describe **Work Orders** as the main mastery-levelling
loop, with tiers Amateur → Novice → Apprentice → Journeyman, taken from a
profession master who supplies the materials. No Korean or Taiwanese source
checked describes such a system, and the tier names are the *Aion 1* work-order
tiers. What Korea actually has is two adjacent things:

- **Abyss Supply Requests** (어비스 보급 의뢰) — an [Urgent] daily tab that
  takes gathering products, herbs and fruit, and a [Weekly] tab that takes
  **failed crafted equipment** at Rare and Heritage grade, paying Abyss Points.
  This is the real "turn in your crafting output" loop, and it is what makes
  non-combo craft results valuable instead of waste. See [[Crafting]].
- **Duty / Mission Quests** (사명 퀘스트) — daily quests that pay guaranteed
  gathering materials including higher-quality Odyle and Orichalcum.

So the "work order proficiency loop" as described in English guides is
**unverified as a distinct system**. The functional equivalent is: craft cheap
things for mastery, and feed the failures into Supply Requests for Abyss
Points. **Confidence low** on Work Orders existing under that name.

### Catalysts

Most recipes want a **catalyst** bought from the vendor standing next to the
crafting station, paid for in Kinah. The documented example: two *gathered*
Orichalcum Ores plus a *vendor-bought* Orichalcum Ore make an Orichalcum Ingot.
Budget a small per-craft Kinah cost on every mastery grind — this is why "level
a profession" has a Kinah bill even when you gathered everything.

There is a conflict about **where** you craft. The wiki says visit one of five
crafting tables in the main cities; one English guide claims you can craft
anywhere from the crafting-management menu and that stations are decorative.
**Unresolved**; assume you need the station.

## What each rank unlocks

The concrete, verified gates:

### Blacksmithing

The **Ore conversion ladder** at `물질 변환 → 채집물 → 광석`, straight from the
client data:

| Conversion | Mastery required |
| --- | --- |
| Orichalcum Ore (base) | Blacksmithing 1 |
| Orichalcum Ore ×2 from 1 Fine | Blacksmithing 10 |
| Fine Orichalcum Ore ×2 from 1 Pure | Blacksmithing 20 |
| Fine, Pure and Radiant Orichalcum Ore | Blacksmithing 30 |
| Pure Orichalcum Ore ×3 from 1 Radiant | Blacksmithing 30 |

All at 100% success. Note the ladder runs **both ways** — you can break a
Radiant down into three Pure, or build Pure up out of Fine. Blacksmithing 30 is
therefore a real breakpoint: it makes you the person who can rebalance an ore
stockpile in either direction, for yourself or for sale.

### Jewelcrafting — what it actually is at Season 1

Strip the Brooch out and Jewelcrafting is a **narrow weapon profession with a
side business in accessories**:

| Output | Value at Season 1 |
| --- | --- |
| **Bow, Staff** | The weapon for Ranger and Chanter — two of the eight launch classes |
| Necklace, Earring, Ring | Real, but competing against dungeon and Abyss accessories that are adequate |
| Bracelet | **Borderline.** The bracelet blueprint arrived in the first post-launch KR update, 2025-12-17 |
| Gem powder | A mastery-grind intermediate, not a product |
| **Brooch** | **Absent at launch.** 2026-05-27. See the roadmap section below |

Two things worth being blunt about, because they are the reasons Jewelcrafting
looks stronger on paper than it is in a launch build:

1. **Selling gemstones does not require Jewelcrafting.** Ruby, Sapphire and
   Diamond ore are the best-selling gathered materials in the game and you sell
   them *raw*, straight off the node. That income belongs to
   [[Gathering Nodes and Plants]], not to this profession. Grinding Jewelcrafting
   mastery to profit from gems is a category error — grind the Gem Seeker
   instead.
2. **The Amulet and Belt are not crafted.** The Amulet of Revelation and Belt of
   Nobility are fixed personal items whose grades rise only on the conversion
   bench. Jewelcrafting has no route into them. See [[Accessories]].

So Jewelcrafting at Season 1 is correct if and only if you are a **Ranger or
Chanter** and want your own weapon. For everyone else it is fourth of five.

### Later-season roadmap: the Jewelcrafting 40 Brooch gate

**Not applicable at Season 1. This becomes the strongest argument in the chapter
around Korea's Season 3, and it is recorded here so it is ready when the slot
arrives.**

Confirmed dating: NC's own 2026-05-27 press release and Inven's summary of the
5/26 preview broadcast both describe the Brooch as **two entirely new equipment
slots** added in that patch — "기존의 장비와 별도로 브로치를 장착할 수 있는 신규
슬롯 2개가 추가된다" — with the Heritage grade obtainable from crafting and the
Unique grade from the new *Muspel's Chalice* Sanctuary. The slot did **not**
exist before the crafted Brooch; both shipped together. Korean guides file it
under Season 3.

When it does arrive:

- The **Heritage-grade Brooch** — *Pilgrim's Brooch* (순례자의 브로치, Elyos) /
  *Liberator's Brooch* (해방자의 브로치, Asmodian) — is crafted at
  `제작 → 세공 → 브로치` at **100% guaranteed success**, no combo gamble.
- The requirement is **Jewelcrafting mastery 40** (reported as both 초급 40 and
  수습 40; same recipe, see the tier-name problem above).
- Materials per Brooch: **Magic Crystal ×100**, **Master's Refining Stone
  ×200**, **Pure Sapphire Ore ×30**, **Pure Diamond Ore ×30**, **Pure Ruby Ore
  ×30**, **Pure Odyle ×30**, and **3,000,000 Kinah**.
- At KR market prices that is roughly **20,000,000 Kinah** per Brooch and
  **40,000,000** for both slots, dominated by the Pure Odyle line.
- Two Heritage Brooches are worth about **+200 item level**.

Why it matters when it lands: Brooch is a **paired slot**, so it is two pieces of
item level at once, and the alternatives are a Unique drop from an item level
**4,500** raid or a conversion recipe fed by that same raid's vouchers.
Jewelcrafting 40 is the cheapest route to a slot that otherwise needs top-tier
raid access — which is exactly why it is worth *nothing* in a build where
neither the slot nor the 4,500 raid exists.

**The practical read for a launch player:** do not level Jewelcrafting for the
Brooch now. If you are still playing when the slot ships, mastery 40 is a few
evenings of gem-powder crafting and the gemstones will be in your warehouse
already from gathering. Nothing is lost by waiting, and the materials keep.

See [[Brooch Pendant and Seal Slots]], [[Accessories]] and
[[Season 1 System Availability]].

### Alchemy

| Unlock | Mastery required |
| --- | --- |
| Spirit Stone Powder (정령석 가루) | Alchemy 5 |
| Mid manastone (중급 마석) | Alchemy 20 |
| Mid spirit stone (중급 영석) | Alchemy 25 |
| Gem-into-powder becomes practical | around Beginner 20 |

The manastone economy is Alchemy's real product. Low-grade manastones and
spirit stones come from monster drops, Expedition, Shugo Festa and the Deva
Pass; **mid grades exist only through Alchemy**; and **high grades come
overwhelmingly from a critical success (대성공) on a mid-grade craft.** That
makes Alchemy the only profession where the *upside* case is the business model
rather than an accident. A worked mid-manastone recipe: 5 low manastones + 3
Spirit Stone Powder + 5 of a Fine-grade component.

Note the asymmetry worth exploiting: the Deva Pass pays manastones but **not**
spirit stones, so spirit stones are structurally scarcer.
See [[Manastones Spirit Stones and Godstones]].

Alchemy also makes the **scrolls** (주문서) — the first update added Gale,
Critical and Shock Resistance scrolls — and the **potions**, including the
flight and mind potions that NC's own community post flags as high-demand.

### Cooking

Cooking has no conversion gates and does not need them. Its rank structure is a
**tier ladder inside the recipe list**, and lower tiers are ingredients for
higher ones:

| Tier | Naming | Grade |
| --- | --- | --- |
| Base | Curry Meat Stirfry, Fruit Salad, Steamed Pujery, Conide Pasta, Ohkra Fried Meat, Grilled Pujery, Raydam Juice, Morfa Tea | Common |
| Master's | 달인의 + the base dish name | Rare |
| Dragon's | 백룡의 (White Dragon's, Elyos) / 흑룡의 (Dark Dragon's, Asmodian) — Chopped Steak, Beef Wellington, Seafood Pasta, Herb Tea, Fruit Juice | Epic / Heritage |

Plus two consumables that are the closest thing to a rank marker:
`입문 요리사의 조미료` and `전문 요리사의 조미료` — Beginner's and
Professional's Cook's Seasoning, both Bound.

**Food buffs** are stat-block increases on a timer. Observed effects across the
dish list: max HP / MP / Action Points and their natural recovery, Attack,
Defense, Accuracy, Evasion, Critical and Block. Buff durations reported as
**300 seconds (5 minutes)** on a base dish, with English guides claiming 30 and
45 minutes for regular versus "Tasty" versions — the 300s figure comes from the
client item text and is the one to trust; the 30/45-minute claim is
**confidence low**.

Two things make Cooking the best first profession:

1. **Combos double the output** instead of producing an upgrade item. Every
   other profession's 25% combo produces a Splendent item you then need as a
   sub-component; Cooking's combo just gives you twice the food. Same for
   Alchemy potions. That means Cooking has no expected-attempts arithmetic and
   no compounding RNG.
2. **Everyone consumes it, forever.** Food is used in field hunting, dungeons,
   PvP, gathering and flying. It is a permanently liquid product.

See [[Consumables and Buffs]].

### Tailoring / Armor

All armor slots including the top-tier crafted breastplates, greaves and helms.
No conversion gates. One Korean guide claims Blacksmithing makes plate armor;
the recipe data puts **all** armor under Tailoring. Trust the recipe data.

## Which profession first, for a Season 1 player

**Cook first. Alchemy second. Your own weapon profession third. Tailoring and
Jewelcrafting only if you are a Ranger, Chanter or completionist.**

This is a revision. An earlier pass of this note ranked Jewelcrafting second
because of the Brooch; the Brooch is a 2026-05-27 addition and is not in the
Season 1 build, so that ranking would have sent a launch player up a mastery
ladder toward an item they cannot equip.

### First: Cooking

Unchanged, and the reasoning still holds without needing anything post-launch.

1. **It pays immediately and costs nothing.** Cooking-ingredient nodes are
   everywhere, the dishes are consumed by every activity, and you will be eating
   your own food from level 10 onward.
2. **Its combo doubles output instead of producing an upgrade component.** Every
   gear profession's 25% combo produces a Splendent item you then need as a
   sub-component, so a gear chain is a stack of compounding rolls. Cooking just
   gives you twice the food. No expected-attempts arithmetic, no RNG cliff.
3. **Consumables and buff food are confirmed launch content**, at pre-Chapter-1
   drop rates — which means everyone needs food and the supply is *worse* than
   in current Korea. Week one is the best cooking market the game will ever have.

Both Taiwanese beginner guides arrive here independently. See
[[Consumables and Buffs]].

### Second: Alchemy — and this is the pick that changed

**Alchemy wins the second slot at Season 1 for every class.** Four reasons, in
order of weight:

1. **It is the only faucet for mid-grade manastones and spirit stones, and the
   manastone layer is a larger share of a launch player's power than it is in
   current Korea.** Low grades drop; **mid grades exist only through Alchemy 20
   and 25**; high grades come overwhelmingly from a critical success on a
   mid-grade craft. Now count what a Season 1 player *cannot* use as a power
   sink: no Potential Enhancement (2026-03-04), no Soul Binding (2026-02-11), no
   Brooch, no Pendant, no Seal, no wing enhancement, no Succession, no Heroic
   tier. Manastones and Spirit Stones are marked **In** at launch. Strip out six
   competing systems and the cheap stat layer that remains gets proportionally
   more valuable, not less. See [[Manastones Spirit Stones and Godstones]].
2. **Its gates are low and inside the band.** Alchemy 5 for Spirit Stone Powder,
   20 for mid manastones, 25 for mid spirit stones. Compare Jewelcrafting 40 for
   an absent slot. Everything Alchemy unlocks is reachable and usable in the
   0–3,800 range.
3. **Its output is consumed by everyone, like Cooking's.** Potions and scrolls
   combo into *double output* rather than into a sub-component, so Alchemy shares
   Cooking's no-gamble economics. NC's own community post flags the **flight and
   mind potions** as high-demand goods, and the Wind Elixir is made from two
   herbs that grow on flat ground. Lowest-capital seller in the game.
4. **The scarcity asymmetry is exploitable.** The Deva Pass pays manastones but
   **not** spirit stones, so spirit stones are structurally scarcer than the
   thing everyone talks about.

Alchemy's known weakness is that it is the worst early-levelling experience —
rough until roughly Beginner 20. Spirit Stone Powder from level 5 blunts that,
since one field-dropped Spirit Stone becomes three Powder, and Spirit Stones are
field trash you were already walking over.

For **Sorcerer and Spiritmaster** this pick collapses into one: Alchemy is also
your weapon profession, so you get the Spellbook or Orb for free and you are
done at two professions.

### Third: the profession that makes your class's weapon

| Your class | Profession | Because |
| --- | --- | --- |
| Templar, Gladiator, Assassin, Cleric | **Blacksmithing** | Longsword, Greatsword, Dagger, Mace, Fist, Guard |
| Ranger, Chanter | **Jewelcrafting** | Bow, Staff |
| Sorcerer, Spiritmaster | **Alchemy** | Spellbook, Orb — already taken at step two |

Brawler is a Chapter 1 class and is not in the launch roster.

Weapon crafting is third rather than second on purpose. It is genuinely the
best thing you can eventually make — with Heroic absent, a **crafted Unique
weapon is the ceiling of the launch game**, and weapon drop rates are the worst
in every loot table. But it is a *top-of-band project*, not an early one: the
chain wants draconic materials from Conquest dungeons and the Ludra Sanctuary,
and Korean sources put solo Conquest Draupnir at roughly Combat Power
1,300–1,400. Until you are clearing that content, mastery in your weapon
profession has nothing to eat.

There is one class-independent argument for taking **Blacksmithing** early
anyway: **mastery 30 unlocks the bidirectional Orichalcum ladder**, which lets
you break a Radiant into three Pure or build Pure up out of Fine, at 100%
success. That makes you the person who can rebalance an ore stockpile in either
direction, for yourself or for sale, and it is the only conversion utility in
the game that a launch player can fully own. If you are a melee player who
intends to trade materials, Blacksmithing and Alchemy are close enough that
either order is defensible.

### Fourth and fifth: Jewelcrafting and Tailoring

- **Jewelcrafting** is fourth at Season 1 unless it is your weapon profession.
  Its headline product is absent, and selling gemstones is a *gathering* activity
  that needs no mastery at all. See the roadmap section above for when this
  reverses.
- **Tailoring is last.** Armour is the easiest slot family to fill from dungeon
  cubes and the Abyss shop, and it gates no conversions.

### The one-line version

With Heroic grade absent and no accessory slots to chase, a Season 1 player's
profession target is **buff food, mid-grade manastones and eventually a crafted
Unique weapon** — not a Heroic chase and not a Brooch.

## Costs and math

- A craft attempted at exactly the recipe's required level has the worst
  success rate the formula allows. Every level of headroom is materials saved.
- Failures still pay **30%** mastery XP, so a levelling grind at a slightly-too-
  hard recipe is not a total loss — but it is worse than an easy recipe at
  volume.
- Combo success pays **130%** XP; combo failure pays 30% of that.
- Ten small crafts beat one batched craft by roughly **2×** on XP.
- Budget catalyst Kinah on every craft. The Professional 50→70 climb is about
  **236 successful Refined Shugo Horn crafts**, so the levelling bill is mostly
  materials and catalysts rather than any single recipe.

## Traps and mistakes

- **Levelling Jewelcrafting to 40 at Season 1 for the Brooch.** The slot does
  not exist in the launch build. This is the specific mistake a Korean or
  Taiwanese guide will lead you into, because those guides are written for a
  service ten months further along.
- **Learning the profession that does not make your class's weapon**, then
  discovering the crafted weapon you can make is for someone else.
- **Grinding Jewelcrafting mastery in order to sell gemstones.** Gemstones sell
  raw. That is a Gem Seeker point, not a profession.
- Levelling on expensive recipes. Refine ore, powder and lumber.
- Batching x10 and x30 recipes while trying to level.
- Attempting a top-tier recipe at exactly the required mastery.
- Getting hit mid-craft; interruption counts as a failure and eats the
  materials.
- Vendoring or extracting non-combo craft results instead of banking them for
  the [Weekly] Abyss Supply Request tab.
- Handing Radiant Odyle, Sturdy Draconic Scale or Refining Stones to a Supply
  Request because it asked.
- Soul Imprinting a crafted item you meant to sell — imprinting removes
  tradability permanently. See [[Soul Imprint and Soul Binding]].
- Skipping the promotion quests on professions you do not main, and thereby
  skipping a free Pantheon artwork.
- Assuming an English profession name maps cleanly. Check
  [[Glossary KR TW EN]].

## Global launch notes

The professions, the promotion structure, the combo mechanic and the
volume-beats-value levelling rule all predate Season 1 and should ship as
described. What differs is which *outputs* exist to aim at.

| Profession output | KR introduced | Season 1 verdict |
| --- | --- | --- |
| Cooking dishes and seasonings | Launch | **In** |
| Alchemy manastones, spirit stones, potions | Launch | **In** |
| Alchemy scrolls: Gale, Critical, Shock Resistance | 2025-12-17 | Borderline, first post-launch update |
| Blacksmithing ore conversion ladder | Launch | **In** |
| Crafted weapons up to Unique | Launch | **In** — and the ceiling, since Heroic is out |
| Tailoring armour | Launch | **In** |
| Jewelcrafting bracelet blueprint | 2025-12-17 | Borderline, first post-launch update |
| **Brooch, slot and recipe** | **2026-05-27** | **Out** |
| Pendant | 2026-07-01 | **Out** |
| Sanctuary weapon succession recipes | 2026-05-27, on Succession Crafting from 2026-04-08 | **Out** |
| Heroic-grade anything | Later season | **Out for planning** |

The gate *numbers* are a separate risk from the gate *existence*: the Alchemy
20/25 manastone gates and the Blacksmithing 1/10/20/30 ore conversions come from
the current KR client and any of them can be tuned differently in a Season 1
build. Verify the one you are levelling toward before committing an evening.

Two things to expect at launch specifically:

- **Cooking will be disproportionately profitable in week one**, because
  everyone needs buff food, almost nobody has levelled a profession yet, and the
  vault records launch-era consumable drop rates as *worse* than current Korea's.
- **Selling raw and first-stage materials into the launch price spike** is
  better than trying to complete a top-tier chain. The top of the chain is a
  stack of 25% rolls and is not a week-one activity.

See [[Season 1 System Availability]], [[Global Launch Differences]] and
[[Progression Phases Roadmap]].

## Open questions

- [ ] The real mastery tier names and their level boundaries. 입문 / 초급 /
      수습 / 전문 are all attested; "Intermediate Lv 95" cannot fit the same
      scale as "Professional 70".
- [ ] Whether Work Orders exist in AION 2 as a distinct system, or whether
      English guides are importing *Aion 1* terminology onto Abyss Supply
      Requests. No Korean or Taiwanese source describes them.
- [ ] Whether you can craft anywhere from the management menu or must stand at
      a station. Two sources disagree.
- [ ] Exact profession-master NPC names and locations per faction.
- [ ] Whether the Professional 70 ceiling was 50 during the Season 1 era, which
      would change the whole XP budget for a launch player.
- [ ] Whether Tailoring or Cooking gate any conversion recipes not visible in
      the current client extract.
- [ ] Real buff durations per cooking tier. 300s is confirmed on a base dish;
      nothing confirms the higher tiers.

## Sources

- [AION 2 Crafting Calculator](https://aion2hub.com/tools/crafting-calculator) — KR client data, read 2026-09-06. Supported: the five professions by client English name (Tailoring, Blacksmithing, Jewelcrafting, Alchemy, Cooking), 1,613 craftable items, the profession-to-item mapping placing all armor under Tailoring, the class-to-weapon list, and the recursive sub-recipe expansion that makes the combo chain an expected-attempts problem.
- [AION 2 Conversion & Exchange Recipes](https://aion2hub.com/tools/conversion) — KR client data, read 2026-09-06. Supported: the exact Blacksmithing 1 / 10 / 20 / 30 ore-conversion ladder with its 100% success rates and its bidirectional structure, and the statement that conversion locks are keyed to Blacksmithing, Jewelcrafting or Alchemy mastery, a character level, or a Monolith level.
- [아이온2 인벤 — 해방자의 브로치 정보 (전투력, 강화값, 재료, 시세 등)](https://www.inven.co.kr/board/aion2/6444/1888) — KR community, read 2026-09-06. Supported: the Brooch crafted at 제작 → 세공 → 브로치 at 100% guaranteed success, "수습 세공 40 필요", the exact material list with quantities, the 3,000,000 Kinah recipe cost, and the per-material market prices summing to ~20,000,000 Kinah.
- [순례자의 브로치 recipe, questlog.gg](https://questlog.gg/aion-2/ko/db/recipe/213094001) — KR client data, read 2026-09-06. Supported: the Elyos mirror name, "Profession: Jewelcrafting", "Mastery Level: 초급 Lv 40", and the same ingredient list. This is the page that conflicts with Inven's 수습 reading.
- [아이온2 해방자의 브로치 총정리](https://baystory.tistory.com/564586) — KR, read 2026-09-06. Independent corroboration of the mastery-40 requirement, the 100% success, and the ~20M / ~40M figures, plus the point that Pure Odyle dominates the cost.
- [엔씨 〈아이온2〉, 신규 성역 '무스펠의 성배' 업데이트](https://about.ncsoft.com/news/article/aion2_update_260527) — **NC official press release, 2026-05-27**, read 2026-09-06. The primary source for the Brooch date. Supported: the 2026-05-27 update adding the Muspel's Chalice Sanctuary with *Kaldrix's Brooch* among its new equipment, and the **item level 4,500 minimum entry requirement** — which is the independent structural reason the Brooch cannot be a Season 1 target, since the launch band tops out around 3,800.
- [[뉴스] 신규 성역, 브로치 추가! 아이온2 5/26(화) 라이브 요약, 인벤](https://www.inven.co.kr/webzine/news/?news=316822) — KR games press, 2026-05-26 preview broadcast, read 2026-09-06. **The load-bearing source for "the slot did not exist earlier":** "기존의 장비와 별도로 브로치를 장착할 수 있는 **신규 슬롯 2개가 추가**된다" — two entirely new slots added in that patch, Heritage grade from crafting, Unique grade from the new Sanctuary, two Heritage Brooches worth +200 item level, and the Unique→Heroic upgrade deferred to Season 4. Slot and crafted recipe shipped together; nothing predates them.
- [엔씨 '아이온2' 성장의 천장 높였다, 신규 성역과 브로치 공개, 게임뷰](https://www.gamevu.co.kr/news/articleView.html?idxno=58205) — KR games press, 2026-05, read 2026-09-06. Corroborates the Brooch as a paired slot obtainable from the Muspel's Chalice Odyle Energy cube **and** from Jewelcrafting, with a Unique Brooch conversion recipe added to reduce acquisition pressure, and Sanctuary weapon succession recipes arriving alongside.
- [아이온2 해방자의 브로치 총정리, baystory](https://baystory.tistory.com/564586) — KR, read 2026-09-06. Independently files the Brooch slot under **"아이온2 시즌3 업데이트"**, which places it two seasons after the global launch content and corroborates the 수습 세공 40 requirement.
- [[안내] 5/27(수) 업데이트 노트, 퍼플 라운지](https://lounge.plaync.com/feed/70003?country=KR&locale=ko-KR) and [AION2 5월 27일 업데이트 요약](https://enterfreegame.com/news/aion2-may-27-update-muspel-abyss-brooch/) — KR, NC official patch note and a mirror summary, 2026-05-27, read 2026-09-06. Supported: the patch-note line "신규 장비 슬롯 「브로치」가 추가됩니다", the Brooch obtainable by crafting or by material conversion from a Muspel's Chalice equipment voucher plus Kinah, and a new Brooch tab appearing in the Market accessory category — i.e. the client UI itself had no Brooch category before this patch.
- [아이온2 인벤 — 제작 레벨별 경험치 (입문1렙~전문 70렙)](https://www.inven.co.kr/board/aion2/6444/1624) and [제작 레벨별 경험치 by 룬트리](https://www.inven.co.kr/board/aion2/6444/1161) — KR community, read 2026-09-06. Supported: 입문 1 to 전문 70 as the scale, the 2026-04-07 change making higher mastery raise final success rate, the per-craft XP figures for Crystal/Powder/Manastone/Spirit Stone/Refined Shugo Horn, the 30% failure and 130% combo-success multipliers, the 8,809 / 82,734 / 228,283 cumulative-XP figures, the 236-craft calculation, and the measured 240-versus-112 and 200-versus-112 batching results.
- [아이온2 제작 공략: PVE 엔드급 무기(기룡왕) 100% 가이드](https://game.savetip.co.kr/aion2-crafting-guide-pve-weapon/) and [아이온2 제작 공략: 직업별 추천 및 필수 재료 파밍 Top 4](https://game.savetip.co.kr/aion2-crafting-guide-materials/) — KR, read 2026-09-06. Supported: the class-to-profession routing (melee and Cleric → Blacksmithing, Ranger and Chanter → Jewelcrafting, Sorcerer and Spiritmaster → Alchemy), first-stage refining as the fast levelling route, Alchemy's Beginner-20 breakpoint, the Abyss Supply Request [Urgent] and [Weekly] tabs and what each accepts, and the do-not-turn-in list.
- [제작 확률 및 효율, 아툴](https://aion2tool.com/craft) — KR tool built on NC's official probability disclosure page, read 2026-09-06. Supported: the level-difference formula, the success-versus-failure gauge, combo producing 빛나는 items for gear and doubling output for cooking and potions, and interruption counting as a failure.
- [《AION2》萃取與製作攻略](https://sticweb.tw/aion2-%e8%90%83%e5%8f%96%e8%88%87%e8%a3%bd%e4%bd%9c%e6%94%bb%e7%95%a5/) and [《AION2》採集製作與料理速成攻略](http://a.ptt543.com/thread-447613-1-1.html) — TW, read 2026-09-06. Supported: the five professions in Traditional Chinese, the "start with Cooking" recommendation with its reasoning (cheap materials, needed for hunting, dungeons, PvP, gathering and flying), and "craft the lowest tier to save materials".
- [요리제작 승급: 전문, questlog.gg](https://questlog.gg/aion-2/ko/db/item/533370001) and [갑옷제작 승급: 전문](https://questlog.gg/aion-2/ko/db/item/533340001) — KR client data, read 2026-09-06. Supported: the promotion items existing as `craftmastery`-type consumables with their exact names and description text, and 갑옷제작 being a separate profession from 대장.
- [[升級]料理專業技術 quest, questlog.gg](https://questlog.gg/aion-2/zh/db/quest/1902060) — TW client data, read 2026-09-06. Supported: the promotion quest type `gathercraftmastery`, recommended level 10, and its two rewards — the promotion item and the `名畫：料理達人` Pantheon artwork.
- [레시피 - cooking - food, questlog.gg](https://questlog.gg/aion-2/ko/db/recipes/cooking/food) — KR client data, read 2026-09-06. Supported: the full three-tier cooking ladder with both faction mirrors, and the 입문 / 전문 요리사의 조미료 items.
- [카레 고기 볶음, questlog.gg](https://questlog.gg/aion-2/ko/db/item/510716013) — KR client data, read 2026-09-06. Supported: the 300-second buff duration and the max HP / MP / Action Point effect structure on a base dish.
- [아이온2 마석 영석 공략 2025](https://game.savetip.co.kr/aion2-magestone-spiritstone-guide/) — KR, read 2026-09-06. Supported: Alchemy 5 for Spirit Stone Powder, Alchemy 20 for mid manastones and 25 for mid spirit stones, the mid-manastone recipe shape, high grades coming primarily from a critical success on a mid-grade craft, and the Deva Pass paying manastones but not spirit stones.
- [아이온2, 첫 번째 업데이트에서 뭐가 바뀔까?, 게임톡](https://www.gametoc.co.kr/news/articleView.html?idxno=104274) — KR games press, read 2026-09-06. Supported: the Jewelcrafting bracelet blueprint and the new Alchemy scrolls (Gale, Critical, Shock Resistance) added in the first post-launch update.
- [Crafting, Aion 2 Wiki](https://aion2.wiki.fextralife.com/Crafting) — EN, read 2026-09-06. Supported: five crafting tables in the main cities each with its own skill, the vendor catalyst requirement with the two-gathered-plus-one-bought Orichalcum Ingot example, and the recipe-name lists used for the cooking and Jewelcrafting tier ladders.
- [Aion 2 Handicrafting Guide](https://www.u4n.com/news/aion-2-handicrafting-guide.html), [Aion 2 Blacksmithing Guide](https://www.u4n.com/index.php/news/aion-2-blacksmithing-guide.html) and [Aion 2 Cooking Guide](https://www.u4n.com/news/aion-2-cooking-guide.html) — EN, low-trust SEO, read 2026-09-06. **Recorded as leads only.** Sole source for the Work Order system and its Amateur → Novice → Apprentice → Journeyman tiers, for the Lainita and Hestia cooking-master names, for the Artisan's Hall / Temple of Artisans locations, and for the 30-versus-45-minute food durations. None of it is corroborated in Korean or Taiwanese sources and the Aion-1 provenance of the work-order tiers is obvious; all **confidence low**.
- [Aion 2: The Complete Guide to Gathering, Crafting, and Professions](https://www.mmoexp.com/News/aion-2-the-complete-guide-to-gathering-crafting-and-professions.html) — EN, low-trust SEO, read 2026-09-06. Lead only, for the claim that you can craft anywhere via the management menu (default N) and that stations are reference. Contradicted by the wiki. This site also advertises Kinah sales; this vault does not recommend buying currency.
