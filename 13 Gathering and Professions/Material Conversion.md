---
chapter: "13 Gathering and Professions"
system: Material Conversion (물질 변환)
type: progression-system
unlock: "opens with crafting access; hotkey Alt+H"
account_wide: false
cadence: "continuous, with per-character and per-server weekly caps on the important recipes"
gates: ["crafting mastery rank on some recipes", "character level on some recipes", "Monolith level on some recipes", "un-imprinted un-enhanced gear as material on the Potential recipes", "unequipped gear for Amulet and Belt rank-ups"]
currencies: ["Kinah", "Bound Kinah", "Odyle Energy"]
region_verified: ["KR"]
patch: "KR live as of 2026-09-06; recipe counts from the KR client extract, caps from the 2026-03-18 and 2026-04-08 patch notes"
confidence: medium
tags:
  - aion2/progression
  - aion2/gathering-professions
  - aion2/economy
---

# Material Conversion

> **In one sentence:** 물질 변환 is a universal trade-in bench with 684 recipes
> producing 334 items, and it is not a crafting convenience — it is the only
> faucet for wings, weekly Odyle Energy, Amulet and Belt rank-ups, Attunement
> Stones, Potential Amplification Stones and the Unique Brooch.

> **Season 1 verdict.** The bench is a launch system, but a much smaller one —
> the 684-recipe count is a Chapter-1-era figure. A launch player should expect
> gatherable-material substitution, the **weekly Odyle Energy conversion**,
> wings, Daevanion Crystals, Kinah boxes, Merit Medal upgrades and the **Amulet
> and Belt rank-ups**; those five or six recipes are the whole reason to open
> Alt+H on day one. **Out at launch: Potential Amplification Stones** — Potential
> Enhancement is a 2026-03-04 system, so section 3 below is roadmap, not plan —
> along with both Brooch conversions, the Kaldrix voucher, Sanctuary succession
> recipes and anything keyed to Heroic grade. Full table under
> [Global launch notes](#global-launch-notes).

## Why it matters

The name undersells it badly. "Material conversion" sounds like a way to turn
spare ore into different ore, and it does that, but the same menu is where
several complete progression systems physically live. If you never open Alt+H
you are not missing a shortcut, you are missing:

- Your entire weekly **Odyle Energy** top-up, which gates dungeon reward cubes.
- Every **wing** you can craft, each worth a permanent +200 flight power.
- **Amulet and Belt** grade increases, which exist nowhere else.
- **Daevanion Crystals** and Kinah boxes.
- **Attunement Stones** for Soul Imprint re-rolls *(borderline at Season 1)*.
- Every **Potential Amplification Stone**, which is the whole Potential layer
  *(post-launch: Potential Enhancement is KR 2026-03-04)*.
- **Soul Sealing Stones** *(post-launch: Soul Binding is KR 2026-02-11)*.

NC's own community summary calls it "a core crafting system involved in item
supply, gear growth, wing crafting and even substituting for gathering". That
is accurate and it is the right way to think about it.

## How it works

Open with **Alt+H**. You give a set of component items — sometimes plus Kinah,
sometimes plus a mastery or level requirement — and receive a product.

### Six categories

| Category | Korean | Contains |
| --- | --- | --- |
| Special | 특수 | Crystals, consumables, medals, skins, Balaur materials, the Wind Breeze shop mirror |
| Wings | 날개 | Every craftable wing, Heritage through Unique |
| Gear | 장비 | Gear selection chests, growth materials, **Potential** stones, Transfer/Succession stones, gear materials |
| Gatherable Material | 채집물 | Ore, Gem, Log, Herb, Cooking Ingredient, Odyle — the substitution engine |
| Decor | 장식 | Artwork and statues for [[Pantheon Statues and Frames]] |
| Event | 이벤트 | Rotating seasonal recipes |

### Scale

The KR client extract holds **684 conversion recipes producing 334 distinct
items**. Every recipe card shows four things: full cost, the success / critical
/ fallback odds, the unlock requirement, and any redemption limit.

That structure is the important part. Most recipes are **100% success**. A
minority are **gambles** with three outcomes.

### The gamble structure

| Outcome | Korean | What happens |
| --- | --- | --- |
| Critical success | 대성공 | An upgraded or doubled product |
| Success | 성공 | The normal product |
| Failure | 실패 | A **fallback** consolation item, not nothing |

The failure branch is what makes conversion gambles different from enchanting.
You do not lose the materials for zero; you get a downgrade. Two documented
examples from the 2026-02-11 patch notes, both medal conversions:

| Input | Critical | Success | Fallback |
| --- | --- | --- | --- |
| Silver Merit Medal + 150,000 Kinah | Gold Merit Medal ×2 | Gold Merit Medal ×1 | Silver Merit Fragment ×50 |
| Gold Merit Medal + 200,000 Kinah | Platinum Merit Medal ×2 | Platinum Merit Medal ×1 | Silver Merit Medal ×1 |

And the wing conversion, which is the gamble that matters most for a new player:

| Wing | Grade | Reported chance |
| --- | --- | --- |
| Fairy's Dream Wings (요정의 꿈 날개) | Rare | **7.0%** |
| Odyle Wings (오드의 날개) | Heritage | **2.5%** |
| Blue Butterfly Wings (푸른 나비의 날개) | Unique | **0.5%** |

Those three numbers come from one Korean guide and are the only published wing
conversion odds found; **confidence medium.**

**A variance warning that is worth reading.** One Inven poster recorded 120–140
attempts on a conversion the UI labelled 10%, and worked out that the odds of
that streak are about one in 300,000. NC separately acknowledged that the
official probability disclosure page had been **missing the material conversion
probability table entirely**, and fixed the omission in the 2026-03-18 patch
while stating that the in-client rates were correct all along. Nothing here
proves misrepresentation, but the takeaway is practical: **do not plan a
progression step around hitting a low-probability conversion.**

### Substitution: conversion as a replacement for gathering

The `채집물` category is a lattice, not a list. Within a quality tier you can
convert **Odyle into any other material**, and within a material you can move
**up and down** the quality ladder. The Blacksmithing ore ladder is the
documented example:

| Direction | Recipe | Mastery |
| --- | --- | --- |
| Down | Radiant Orichalcum ×1 → Pure ×3 | Blacksmithing 30 |
| Down | Pure ×1 → Fine ×2 | Blacksmithing 20 |
| Down | Fine ×1 → Base ×2 | Blacksmithing 10 |
| Up | into Fine / Pure / Radiant | Blacksmithing 30 |

All at 100%. Note that the conversion products carry the **(Bound)** tag —
converted materials are for your own use, not for resale. If you want tradable
materials you have to gather them.

The 2026-03-18 patch also made converted materials easier to use: recipes that
required un-enhanced gear now accept enhanced gear, and sub-materials inside a
conversion can have their substitute items swapped.

## Unlock and gates

Four gate types appear on recipe cards:

1. **Crafting mastery rank** — Blacksmithing, Jewelcrafting or Alchemy. This is
   the main one, and it is why [[Professions and Mastery]] is upstream of this
   note.
2. **Character level.**
3. **Monolith level** — resonating Empyrean Traces raises a region's Monolith,
   and some conversions check it. See [[Empyrean Traces and Feathers]].
4. **Item state** — several recipes require gear that is **un-imprinted,
   un-enhanced and unequipped**. Specifically:
   - **Potential Amplification Stones** cannot be made from soul-imprinted
     (각인) gear, and gear that has been enhanced or soul-bound may also be
     rejected. Use pristine, unbound drops.
   - **Amulet and Belt rank-ups** require the item to be **unequipped**.

## The conversions that matter for progression

### 1. Odyle Energy (오드 에너지) — the weekly non-negotiable

This is the highest-value repeatable in the chapter.

- **Recipe:** 25 Odyle + 5 Fine Odyle + 1 Pure Odyle + **50,000 Kinah** → 40
  Odyle Energy (Bound). *(Recipe composition is medium confidence; the 40-energy
  output and the 50,000 Kinah cost are well corroborated.)*
- **Reset:** Wednesday 05:00, with the rest of the weekly block.
- **Caps have moved repeatedly.** Known values:

| Date | Per character | Per server |
| --- | --- | --- |
| Launch era | 7 per week | — |
| 2026-03-18 | 4 per week | 12 per week |
| 2026-04-08 | — | raised to 20 per week |

The per-character number falling from 7 to 4 while a per-server number appeared
is the same pattern the rest of the game followed in 2026: limits moving from
character-bound to server-bound so alts stop multiplying them. See
[[Alts and Account Wide Progression]].

Why it is non-negotiable: Odyle Energy is what opens Expedition, Transcendence
and Sanctuary reward cubes, and cube rewards are the largest gear and Kinah
payout available. Regeneration also **stops dead at the cap**, so a full pool is
destroyed value. Gather Odyle, convert on Wednesday, spend it down. See
[[Odyle Energy and Entry Limits]] and [[Daily and Weekly Loops]].

An event recipe has also existed converting **300,000 unbound Kinah → 1 Odyle
Energy (Bound)**, weekly 16 per server plus 4 extra per character. Events come
and go, but it establishes the exchange rate NC is willing to set: roughly
**300,000 Kinah per point of energy** through an event tap, against **100,000
Kinah for one point** through the Wind Breeze shop. The shop is three times
better; buy that first.

### 2. Wings — permanent flight power, from Odyle

Wings are crafted in the `날개` category and each new wing you craft grants a
**permanent, cumulative +200 flight power** whether or not you equip it. That
makes wing crafting a collection system disguised as a conversion recipe.

The material structure:

| Grade | Materials |
| --- | --- |
| Heritage (전승) and below | **Sealed Wing Feather** (봉인된 날개 깃털, from Sealed Dungeon clears) + **Pure Odyle** (순수한 오드, from Odyle gathering) |
| Unique (유일) | **Radiant Odyle** (찬란한 오드) as the common material + a wing-specific feather from a Conquest dungeon |

The Unique feather map:

| Wing | Korean | Conquest dungeon |
| --- | --- | --- |
| Ancient Aullaeu | 고대 아울라우 | Urugugu Canyon |
| Kromede | 크로메데 | Fire Temple |
| Blue Wave | 푸른 파도 | Draupnir |
| Black Fragment | 검은 파편 | Krao Cave |
| Forest Spirit | 숲 정령 | Vakron Sky Island |
| Veil of Darkness | 어둠의 장막 | Ferocious Horn Den |

**Practical note:** the first wing craft costs about **10 Pure Odyle** and
crafting it **unlocks the wing crafting menu**, after which the rest of the tree
becomes visible and much easier to plan. Do that first craft early. Also check
your warehouse for Sealed Wing Feathers — Korean guides call this the most
commonly forgotten free progression in the game, because Sealed Dungeon clears
hand them out and players never look at them again.

See [[Wings Acquisition]] and [[Wings Enhancement]].

### 3. Potential Amplification Stones (잠재력 증폭석)

> **Post-launch. Roadmap only.** Potential Enhancement entered the Korean
> service on **2026-03-04** and the vault's availability matrix marks it **Out**
> at Season 1. Do not budget gear, Kinah or warehouse space for this at launch.
> Kept here because it is the largest single thing the bench does once it lands,
> and because the tier-down trick below is worth knowing in advance.

The entire Potential layer is fed from `물질 변환 → 장비 → 잠재력`.

- **You convert unwanted dungeon gear into stones**, in three categories that do
  not mix: **weapon, armor, accessory**.
- **100% success**, plus a Kinah cost.
- Stones are **tiered by the star rating of the Expedition difficulty** the
  source gear came from, and the stone must match the tier of the item you are
  enhancing.
- Potential enhancement itself is **4 stages, 100% success**, with the stone
  requirement rising by one each stage — **10 stones total** for a full item.
- The payoff: **weapon +0.6% PvE damage per stage (2.4% total)**; **armor +0.3%
  PvE damage resistance per stage (1.2%)**; **accessory +0.3% PvE damage per
  stage (1.2%)**. Roughly half what a crafted item carries natively.
- Only **Unique and above** gear from Expedition Conquest and Sanctuary can be
  Potential-enhanced. Field-boss exclusive Unique gear was slated to be added.
- **Potential does not transfer.** It is explicitly excluded from Inheritance,
  so choose the item you will keep.

**The tier-down trick.** You do not have to re-run old dungeons to get lower-tier
stones. Convert an unwanted **4-star** accessory drop into a **3-star**
Amplification Stone, and apply it to your actual best-in-slot 3-star accessory.
This is the single most useful thing in this note for a player whose main has
outgrown the dungeon that drops their favourite item.

Requirement: the source gear must be **un-imprinted and unbound**, so shuttle
pristine drops between characters through the warehouse rather than equipping
them. See [[Potential Enhancement]] and [[Enchanting]].

### 4. Amulet and Belt rank-ups

The **Amulet of Revelation** (계시의 아뮬렛) and the **Belt of Nobility**
(고결의 허리띠) are fixed, personal, un-droppable accessories. Their grade
increases exist **only** on the conversion bench:

- Enhance the item to **+10** first.
- **Unequip it**, then convert.
- The Epic and Unique versions of both items have no other source in the game.

This is the reason a player who ignores conversion silently caps two gear slots.
See [[Accessories]].

### 5. Gear-swap conversions, and the Brooch

**Equipment Change Voucher** (장비 변경권) is the one that matters at launch:
2 vouchers + 1 dungeon weapon + 1,000,000 Kinah → any other weapon from the same
dungeon. Vouchers are a guaranteed Conquest Normal reward from Krao Cave,
Urugugu Canyon and Fire Temple. Only Bound gear from Odyle Energy cubes and
guaranteed rewards is eligible. This is how a wrong-class weapon drop becomes
your weapon, and it is the reason a launch player does not urgently need a
weapon-crafting profession. *Borderline: added KR 2025-12-17, 28 days after the
Korean launch.*

The rest of this family is post-launch:

- **Core** (코어): convert an unwanted Unique from Expedition Conquest into a
  Core at `물질 변환 → 장비 → 장비 재료`, then Core + **Breath of Magic**
  (마력의 숨결) → draconic gear. *Post-launch: the recipe and the 4-per-server
  season shop limit on Breath of Magic both arrive with the KR 2026-02-11 patch,
  which is Season 2 territory. Season shop stock and limits are among the most
  frequently retuned numbers in the game — treat any figure here as a shape, not
  a value, and read it off the shop.*
- **The Brooch conversions.** A **Unique Brooch conversion recipe** was added
  alongside the Brooch slot to reduce the burden of getting one from the
  Sanctuary, and **Gear Change Voucher: Kaldrix** feeds it. *Out at launch: the
  slot itself is KR 2026-05-27.* Together with the crafted Heritage Brooch
  (Jewelcrafting 40), these are the two non-raid routes to a paired slot **once
  the slot exists**. See [[Brooch Pendant and Seal Slots]] and the roadmap
  section in [[Professions and Mastery]].
- The Sanctuary **Selection Chests** (Abyssal Forge weapon / armor / accessory,
  Chalice of Muspel weapon, Citadel of the Fallen Daeva armor) are the pity route
  into specific raid pieces. *Chalice of Muspel is 2026-05-27; the others are
  keyed to Sanctuaries above the launch band.* See [[Gear Tiers and Sources]].
- **Sanctuary weapon succession recipes** arrived 2026-05-27, on top of
  Succession Crafting from 2026-04-08. Both are marked **Out** at Season 1, so
  assume gear investment is one-way at launch and choose keeper items
  accordingly. See [[Enchanting]].

### 6. Attunement Stones

12 fragments + 100,000 Kinah, **or** 30 fragments free, at
`물질 변환 → 특수 → 소모품`. The free route makes each fragment worth about 2.4×
more; the Heroic step is the exception where paying is correct. Full working in
[[Odyle and Special Resources]].

*Borderline at Season 1.* Attunement Stones and Fragments entered the Korean
service on **2025-12-17**, 28 days after the Korean launch, and
[[Season 1 System Availability]] marks them **Borderline** with the advice to
plan around Unique fodder instead. The base Attunement system *is* a launch
system and is a launch player's only option-fixing tool; it is the *Stones* that
may not be there. The Heroic conversion step is irrelevant either way.

### 7. Feather-to-stone, and the other Special conversions

The `특수` category is where the miscellaneous but load-bearing recipes sit:

| Product | Notes |
| --- | --- |
| Daevanion Crystal (데바니온 결정) | The [[Daevanion Boards]] currency, made from Odyle |
| Soul Sealing Stone (봉혼석) | [[Soul Imprint and Soul Binding]] material. *Post-launch: Soul Binding is KR 2026-02-11* |
| Kinah Box (키나 상자) | Converts surplus materials into Kinah |
| Breakthrough Stone (돌파석) | [[Breakthrough]] material |
| Enhance Stone (강화석) | [[Enchanting]] material |
| Odyle Energy (Bound) | Above |
| Merit Medal upgrades | The silver → gold → platinum gamble ladder |
| Ariel's Trace fragments → Crystal | A weekly Kinah play; see [[Farming Routes and Kinah]] |
| Transformation Candies | Aullaeu, Dratona, Kobold, Mau, Mumu |
| Stigma conversions | Kinah cost was reduced in early 2026, with a retroactive refund |

**On "feather-to-stone":** the conversions genuinely involving feathers are the
**wing** recipes above — Sealed Wing Feather and the Conquest-specific feathers
into wings, which then pay permanent flight power. The separate
**Empyrean Trace** items (주신의 흔적, often loosely called feathers in English)
are **resonated at a Monolith**, not converted at this bench, and Monolith level
is then a *gate* on some conversions rather than a product of them. Those are
two different systems that English guides regularly merge. See
[[Empyrean Traces and Feathers]].

## Caps and limits

| Recipe family | Limit | Reset |
| --- | --- | --- |
| Odyle Energy | 4 per character and 20 per server per week (was 7 per character, then 12 per server) | Wednesday 05:00 |
| Event Odyle Energy from Kinah | 16 per server + 4 per character per week | Weekly |
| Breath of Magic (season shop input) | 4 purchases per server | Season. *Post-launch, KR 2026-02-11; season shop limits are retuned often* |
| Amulet / Belt rank-up | Effectively once per grade step per item | — |
| Most gatherable-material conversions | Uncapped | — |
| Event recipes | Usually 1–3 per character per week | Weekly |

The pattern to internalise: **anything that produces power is capped, anything
that shuffles materials is not.**

## Priorities and breakpoints

1. **The weekly Odyle Energy conversion, every week, without exception.** It is
   worth more than anything else on this page.
2. **Your first wing craft** (~10 Pure Odyle) to unlock the wing menu, then
   check the warehouse for Sealed Wing Feathers and craft everything you can.
3. **Amulet and Belt to +10 and then rank up.** Two slots you cannot otherwise
   improve.
4. **Blacksmithing mastery 30** if you intend to trade materials, because the
   bidirectional ore ladder makes you the person who can rebalance a stockpile.
5. **Kinah boxes** as the dump for materials with no other use, in preference to
   vendoring.
6. **Attunement Stones on the free 30-fragment route** unless you need Heroic —
   *if the Stones ship at launch at all; see the verdict above.*
7. **Potential stones from tier-down conversions** once your main has outgrown
   the dungeon that drops your favourite piece — *post-launch only.*

Items 1 to 5 are the whole Season 1 list. Items 6 and 7 are the two that a
Korean guide will put at the top and that a launch player may not be able to do
at all.

## Traps and mistakes

- **Never opening Alt+H.** The most expensive mistake in this note, because
  three progression systems are silently invisible.
- Letting the weekly Odyle Energy conversion lapse. It does not bank.
- Soul Imprinting or enhancing a drop you intended to convert into a Potential
  Amplification Stone. Keep conversion fodder pristine and unbound.
- Converting an Amulet or Belt while it is equipped, or before +10.
- Expecting to *sell* converted materials — conversion products are Bound.
- Building a plan around a low-probability conversion. See the 120-attempt
  anecdote above.
- Running an old dungeon for low-tier Potential stones instead of tier-down
  converting a high-tier drop.
- Assuming Empyrean Traces are converted here. They are resonated at a Monolith.
- Paying 300,000 Kinah for a point of Odyle Energy through an event recipe when
  the Wind Breeze shop sells it for 100,000.

## Global launch notes

Material conversion existed at KR launch and is not going anywhere, but the
**684 recipes are a Chapter-1-era count** and the Season 1 bench will be a
fraction of that. Recipe family by recipe family:

| Conversion family | KR introduced | Season 1 verdict |
| --- | --- | --- |
| Gatherable-material substitution, all six families | Launch | **In** |
| Blacksmithing ore ladder, both directions | Launch | **In** |
| Odyle Energy weekly conversion | Launch | **In** — the highest-value repeatable here |
| Wings, Heritage through Unique | Launch | **In** |
| Daevanion Crystals | Launch | **In** |
| Kinah boxes, Breakthrough and Enhance Stones | Launch | **In** |
| Merit Medal upgrade gambles | Launch | **In**, at harsher pre-February-2026 medal tuning |
| Amulet and Belt rank-ups | Launch | **In** — two slots with no other faucet |
| Transformation candies, Stigma conversions | Launch | **In** |
| Equipment Change Voucher weapon swap | 2025-12-17 | Borderline, 28 days post-KR-launch |
| Attunement Stone Fragments | 2025-12-17 | Borderline |
| Soul Sealing Stones | 2026-02-11 | **Out** |
| Core + Breath of Magic draconic recipe, and its 4-per-server season shop limit | 2026-02-11 | **Out** |
| **Potential Amplification Stones** | **2026-03-04** | **Out** |
| Sanctuary succession recipes | 2026-04-08 / 2026-05-27 | **Out** |
| Unique Brooch conversion, Kaldrix voucher | 2026-05-27 | **Out** |
| Draconic Essence conversions | 2026-07-01 | **Out** |
| Anything keyed to Heroic grade, incl. the Heroic Attunement step and Heroic Transfer Stones | — | **Out for planning** |

The practical consequence: at Season 1 this bench is **four things** — the weekly
Odyle Energy conversion, wing crafting, the Amulet and Belt rank-ups, and
material substitution. That is still enough to make skipping Alt+H the most
expensive habit in the chapter, but it is a much shorter list than the note's
body implies, and the two sections a Korean guide will push you toward hardest
(Potential and the Brooch) are both absent.

The **caps are the biggest unknown**. Whether global ships the launch-era 7
per-character Odyle Energy conversions or the later 4-per-character-plus-server
model changes the weekly energy budget substantially, and therefore changes how
many reward cubes a launch player can open. See [[Global Launch Differences]].

## Open questions

- [ ] How many recipes ship at Season 1, and which categories exist at all.
- [ ] Whether global uses per-character or per-server conversion caps.
- [ ] The exact Odyle Energy conversion recipe composition. The 40-output and
      50,000 Kinah cost are solid; the 25 + 5 + 1 material split is from one
      source.
- [ ] Published success / critical / fallback odds for the gamble recipes
      beyond the wings and medals documented here.
- [ ] Whether enhanced or soul-bound gear is accepted as Potential conversion
      fodder. The 2026-03-18 patch loosened the un-enhanced requirement for some
      recipes, but a community guide still warns against it for Potential.
- [ ] Whether Cooking or Tailoring mastery gates any conversion.
- [ ] The full Monolith-level-gated recipe list.

## Sources

- [AION 2 Conversion & Exchange Recipes](https://aion2hub.com/tools/conversion) — KR client data, read 2026-09-06. Supported: the **684 recipes producing 334 items** figure, the six categories (Gatherable Material, Special, Wings, Gear, Decor, Event) and their sub-categories, the success / critical / fallback structure with fallback described as a consolation item, the four gate types (crafting mastery in Blacksmithing / Jewelcrafting / Alchemy, character level, Monolith level), the per-character / per-account / per-server caps with weekly and daily resets, the "any of N interchangeable items" component slots, the full Blacksmithing 1 / 10 / 20 / 30 ore ladder in both directions at 100%, and the (Bound) tag on conversion products.
- [아이온2 인벤 — [AION2] 아이온2 필수 제작 시스템 '물질 변환' 한눈에 보기](https://www.inven.co.kr/board/aion2/6493/40) — KR, NC's AI tips board, read 2026-09-06. Supported: conversion as a core system covering item supply, gear growth, wing crafting and gathering substitution; the six Korean category names; the probability-based structure; the product list including Daevanion Crystals, Soul Sealing Stones, Kinah Boxes, Breakthrough and Enhance Stones; the Heritage-to-Unique wing material split with Sealed Wing Feather and Pure Odyle; Radiant Odyle as the common Unique-wing material; the full per-dungeon Unique feather map; the Amulet and Belt +10-then-unequip-then-convert rank-up; the 7-per-character weekly Odyle Energy craft with its Wednesday 05:00 reset; and same-grade Odyle-to-other-material substitution.
- [아이온2 인벤 — 12/17(수) 업데이트 노트](https://www.inven.co.kr/board/aion2/6388/45636) — KR patch notes, **2025-12-17** (the first major post-launch update; games-press coverage of the same patch describes it as arriving "출시 한 달째", one month after release, which fixes the year), read 2026-09-06. Supported: Attunement Stones and Fragments arriving from Expedition and Sanctuary, the fragment conversion at 물질 변환 → 특수 → 소모품, the Unique-to-Heroic stone step, the Equipment Change Voucher recipe (2 vouchers + 1 dungeon weapon + 1,000,000 Kinah), the three dungeons that pay vouchers, and the restriction to Bound gear from Odyle Energy cubes and guaranteed rewards.
- [아이온2 인벤 — 2/11(수) 업데이트 노트](https://www.inven.co.kr/board/aion2/6388/96080) — KR patch notes, 2026-02-11, read 2026-09-06. Supported: the two worked Merit Medal gamble tables showing critical / success / fallback outcomes with their Kinah costs, the Core plus Breath of Magic draconic recipe with the 4-per-server season shop limit, the reduction in materials for the 천룡/마룡 and 응룡/기룡 crafts, and the improvement letting sub-material substitutes be changed.
- [[안내] 3/18(수) 업데이트 노트, Arca.live](https://arca.live/b/aion2/165151239) — KR patch notes, 2026-03-18, read 2026-09-06. Supported: the Odyle Energy conversion cap changing to 4 per character and 12 per server per week, the change letting enhanced gear be used where un-enhanced was required (with a material-confirmation window), the fix to the favourites filter, the acknowledgement that the NC probability page was **missing the 물질 변환 확률 table** (with the statement that in-client rates were correct), and the retroactive refund on reduced Stigma conversion Kinah costs.
- [Arca.live — KR 2026-04-08 Season 3 patch notes](https://arca.live/b/aion2/167052865) — KR, 2026-04-08, read 2026-09-06. Supported: the per-server Odyle Energy conversion limit rising to 20 per week, and the Wind Breeze shop price of 100,000 Kinah per Odyle Energy.
- [아이온2 인벤 — [AION2] 30만 키나(비각인)를 통해 오드 에너지(각인)을 물질 변환할 수 있는 변환식이 추가!](https://www.inven.co.kr/board/aion2/6493/175) — KR, NC's AI tips board, 2026-06-04, read 2026-09-06. Supported: the event recipe converting 300,000 unbound Kinah into 1 Bound Odyle Energy, at 16 per server plus 4 per character per week, and that event-supplied items are untradable.
- [퍼플 라운지 — 신규로 추가된 잠재력 강화 시스템](https://lounge.plaync.com/feed/61011?country=KR&locale=ko-KR) — KR, NC official community, 2026-03-06, read 2026-09-06. Supported: Potential enhancement living at 통합강화 → 성장 → 잠재력 with 4 stages, materials made by converting same-difficulty dungeon gear, the weapon/armor/accessory category restriction, the Unique-and-above Expedition Conquest and Sanctuary requirement, the per-stage stat values, the planned addition of field-boss exclusive gear with its named boss list, and the explicit statement that Potential stages are **not** inherited.
- [[아이온2] 잠재력 강화하는 방법](https://kwonsaw.tistory.com/1576) — KR, 2026-03, read 2026-09-06. Supported: the menu path 물질 변환 → 장비 → 잠재력, the three stone categories, tier identification by the Expedition difficulty's star count, 100% success on both the conversion and the enhancement, the +1 stone per stage rising to **10 stones total**, and the observation that Potential gives roughly half of a crafted item's values.
- [아이온2 '잠재력'으로 격차 완화, 게임플](https://www.gameple.co.kr/news/articleView.html?idxno=215100) — KR games press, read 2026-09-06. Independent corroboration of the 4-stage / 100% / no-failure structure, the per-stage percentages, the Kinah cost, and the non-inheritance rule.
- [아이온2 무소과금 필수 공략! 잠재력 시스템 완벽 분석](https://gamenewb.tistory.com/57) — KR, read 2026-09-06. Supported: the **tier-down conversion** trick (4-tier drop → 3-tier stone for a best-in-slot 3-tier accessory) and the requirement that conversion fodder be un-imprinted, un-enhanced, unbound gear shuttled through the warehouse. **Single source, confidence medium.**
- [아이온2 날개 제작 및 유일 날개 획득 방법 총정리](https://game.savetip.co.kr/aion2-wing-crafting-guide/) — KR, read 2026-09-06. Supported: Sealed Wing Feather from Sealed Dungeons and Pure Odyle from field gathering as the two entry materials, the ~10 Pure Odyle first craft **unlocking the wing crafting menu**, and the wing conversion odds of 7.0% / 2.5% / 0.5% for Fairy's Dream / Odyle / Blue Butterfly Wings. **Single source on the odds.**
- [아이온2 날개 제작 완벽 가이드 2026](https://alias007.tistory.com/776) — KR, read 2026-09-06. Supported: crafting via Alt+H, each crafted wing granting a permanent cumulative +200 flight power, higher gathering level increasing Pure Odyle supply, and the check-your-warehouse-for-Sealed-Wing-Feathers advice.
- [아이온2 인벤 — NC 물질변환 확률표기 조작의심](https://www.inven.co.kr/board/aion2/6388/172289) — KR community, read 2026-09-06. Supported: the 120–140 attempt anecdote on a stated-10% medal conversion and its probability working. **Anecdote, recorded as a variance warning rather than as a claim about the rates.**
- [엔씨 '아이온2' 성장의 천장 높였다, 신규 성역과 브로치 공개, 게임뷰](https://www.gamevu.co.kr/news/articleView.html?idxno=58205) — KR games press, 2026-05, read 2026-09-06. Supported: the Unique Brooch conversion recipe added to ease acquisition, the Kaldrix equipment-change conversion from the Muspel's Chalice Odyle Energy cube, and Sanctuary weapon succession recipes.
- [Daily and Weekly Loops](https://aion2hub.com/updates/aion-2-update-2026-07-01) (Chapter 1 patch note) — KR, 2026-07-01, read 2026-09-06. Supported: the Wednesday 05:00 weekly reset covering the Odyle Energy conversion, and the general 2026 move of limits from per-character to per-server.
