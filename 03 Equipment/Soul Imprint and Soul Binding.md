---
chapter: "03 Equipment"
system: Soul Imprint and Soul Binding
type: progression-system
unlock: "Soul Imprint fires automatically the first time you equip an un-imprinted item; Soul Binding needs Unique grade, a 100% imprint rate, and the KR 2026-02-11 patch"
account_wide: false
cadence: continuous
gates: ["Unique (유일) grade or higher for Soul Binding", "soul imprint rate 100% before Soul Binding", "quest-awarded Unique gear is excluded from Soul Binding"]
currencies: ["Soul Codex (영혼의 서)", "Soul Codex: Reset (영혼의 서: 초기화)", "Philosopher's Stone: Revelation (현자의 돌: 계시)", "Philosopher's Stone: Authority (현자의 돌: 권능)", "Kinah"]
region_verified: ["KR", "TW"]
patch: "KR live as of 2026-09-06; Soul Imprint present at the 2025-11-19 launch, Soul Binding added 2026-02-11, Philosopher's Stone: Authority added 2026-05-27"
confidence: high
tags:
  - aion2/progression
  - aion2/equipment
---

# Soul Imprint and Soul Binding

> **In one sentence:** every equippable item silently rolls four to six random
> sub-stat lines the first time you put it on, those lines are worth more than
> the item's base stats at endgame, and everything else in this note is
> machinery for fixing a bad roll or buying one extra line.

## Why it matters

Soul Imprint (영혼 각인) is the layer that separates a character with real
damage from a character with a big Combat Power number. A Korean guide title
that circulated all through Season 2 puts it bluntly: soul imprint is "how to
double your character stats". The base item and its enhancement level are the
easy part; two identical +20 weapons can differ by a large multiple of real DPS
depending on whether they rolled Weapon Damage Amplification and Combat Speed or
rolled Movement Speed and Status Effect Resist.

It also matters because it is the point of no return for trading. Imprinting is
automatic and irreversible, and it converts a tradable item into a bound one.
Everything in [[Gear Tiers and Sources]] about crafted Dragon Lord gear being
Bind-on-Equip is really a statement about this system.

This note owns the **initial roll and the permanent lines**: how imprinting
happens, how you raise the imprint rate, how the extra Soul Binding line is
bought, and what to aim for per slot. The **economy of rerolling** — Attunement
Stones, sacrificial Unique fodder, expected costs — lives in
[[Attunement and Option Rerolls]]. Keep the boundary in mind when reading Korean
guides, which treat the two as one workflow.

## Naming: this is the worst-translated system in the game

Four vocabularies are in circulation for the same three Korean words, and two of
them are NC's own. Use this table before trusting any English guide.

| Korean | This vault | aion2hub | NC official English | questlog / other |
| --- | --- | --- | --- | --- |
| 영혼 각인 | **Soul Imprint** | Soul Engraving; also "Soul Binding" in item text | "Soul Inscription" (2026-05-27 release), "Soul Binding" (2026-01-21 release) | Soul Imprint, Soul Bind |
| 영혼 각인율 | **soul imprint rate** | "binding rate" | — | 刻印率 (TW) |
| 조율 | **Attunement** | Attune | "Sync" (2026-01-21 release) | Tuning, Sync, 靈魂調整 (TW) |
| 초기화 | **Reset** | Reset | — | Reset, 初始化 (TW) |
| 영혼 결속 | **Soul Binding** | Soul Binding | "Soul Binding" (2026-05-27 release) | 靈魂結合 (TW) |
| 영혼의 서 | **Soul Codex** | Soul Codex | — | Soul Tome, Soul Book, Soul Scroll, 靈魂之書 (TW) |

Two consequences. First, an English article headlined "Soul Binding: Bind, Sync
and Reset" is describing **Soul Imprint**, not the February 2026 Philosopher's
Stone system, because it is following NC's Season 2 press-release wording. The
mmoexp gear-enhancement guide is exactly this case, and it is otherwise accurate.
Second, "Soul Fuse" — see the ruling below — is not a fifth system.

**Grade vocabulary.** This note uses **Unique (유일)** and **Heroic (영웅)**,
matching [[Gear Tiers and Sources]] and aion2hub. `questlog.gg` renders the same
grades **Legend** and **Mythic**, and renders 전승 as **Epic** where NC's own
English says **Heritage**. The Korean word is the stable identifier.

## Ruling: what "Soul Codex" (영혼의 서) actually is

**It is a stackable consumable item, in two variants. It is not a permanent stat
system and it is not a trait tree.** Two other research passes reached opposite
conclusions on this; the item database settles it outright, because both
variants have item IDs, stack sizes and vendor prices.

| Item | ID | Description on the item page | Stack | Vendor |
| --- | --- | --- | --- | --- |
| **Soul Codex (Bound)** — 영혼의 서 (각인) | 535400001 | "A tome with the power to draw out the latent potential within the soul. Increases the binding rate of already bound gear through Soul Binding." When used: *Grants soul bind*. | 10,000 | 1,000 |
| **Soul Codex: Reset (Bound)** — 영혼의 서: 초기화 (각인) | 535200001 | "A special power that resets bound souls. Use to reset the binding on already bound gear and perform a new binding." When used: *Grants soul bind reroll*. | 1,000 | 24,000 |

So the plain Codex is the **imprint-rate fuel** — you feed it in repeatedly to
drag the imprint rate from wherever it landed up toward 100% — and the Reset
Codex is the **four-line reroll consumable**, costing an additional 300,000
Kinah per use. The Taiwanese client uses 靈魂之書 and 靈魂之書：初始化 for the
same two items, and the Bahamut translation of the 100-Day gift box lists them
by those names alongside quantities, which is only consistent with consumables.

**Where the confusion comes from,** and it is worth recording so the mistake is
not repeated: aion2hub translates 영혼 각인 as "Soul **Binding**" and 각인율 as
"**binding rate**". An English reader meeting the sentence "increases the binding
rate of already bound gear" with no Korean reference will reasonably guess at a
persistent character-level "binding" track that a codex advances — i.e. a stat
and trait system. It is not; "binding rate" is a per-item percentage on one
piece of equipment's tooltip, and the Codex is the item you burn to raise it.

Sources per side, so you can re-check: the **consumable** reading is supported by
the aion2hub and questlog item pages above, by NC's own 2026-02-11 patch note
listing new *acquisition sources* for 영혼의 서 (각인) including a material
conversion of 200 Enhancement Stones + 10,000 Kinah into **one** Codex, by the
Korean guides that describe "burning Codexes to 100%", and by the Taiwanese
description that each use rolls a fresh 1–100% rate. No source in Korean,
Chinese or English describes a Soul Codex screen, board, node or unlock. **Ruled:
consumable.**

**Related ruling — "Soul Fuse".** Two English SEO sites list Soul Imprinting,
Soul Binding *and* Soul Fuse as three systems. Reading their own descriptions,
"Soul Fuse" is defined as "equipment with 100% Soul Binding can use two
Philosopher's Stone: Revelation to apply additional Soul Binding effects" —
which is the definition of 영혼 결속, the February 2026 system, restated. No
Korean or Chinese term matching "soul fusion" (영혼 융합) exists in any patch
note or database entry I could find. **Ruled: an English-source alias for Soul
Binding, not a distinct system.** Recorded at high confidence on the negative.

## How it works

### 1. The initial imprint

The first time you equip an item that has never been imprinted, the client
imprints it automatically. There is no confirmation prompt for the imprint
itself and no way to decline it.

- **You get a fixed number of random option lines**, drawn from a pool specific
  to that slot. Most dropped gear rolls **four**. Higher-grade and crafted gear
  rolls more: the Taiwanese database lists Heroic maces at four, five and six
  lines depending on the item, the crafted Unique weapon is commonly described
  as five lines, and NC's own release for the Genesis/Nemesis Dragon Lord weapon
  and Guard states **six base Soul Inscription options**. The Guard is the
  exception in the other direction — Korean guides note "늘무" (extended-range)
  weapons roll three.
- **The item becomes untradable, permanently.** It also stops moving through the
  account warehouse between your own characters. This applies even to
  Bind-on-Equip crafted gear that you were planning to resell.
- **The imprint rate (영혼 각인율) starts low and random.** The rate is a single
  percentage for the whole item that scales *every* line's value. A line that
  reads "Combat Speed 3.2%" at 100% reads much less at 40%.

### 2. Raising the imprint rate with Soul Codexes

Feeding a Soul Codex re-rolls the imprint rate. The Taiwanese system description
is the clearest statement of the mechanic anywhere: **each attempt generates a
random rate between 1% and 100%, and the result is never lower than the rate
already applied** — it only ratchets upward. That is why the last few percent
cost so many Codexes: you are waiting for a roll that beats a number already
near the ceiling.

You may also use *the same item* as imprint material instead of a Codex, per the
Taiwanese guide, though Korean practice is Codexes.

**Get to 100% before you spend anything on rerolls.** Every Korean guide leads
with this and the reason is arithmetic, not superstition: rolling a perfect
option set at 60% imprint rate gives you 60% of a perfect item, and the rate work
is cheap compared with the reroll work.

### 3. Attunement and Reset

The two ways to change *which* options you have:

- **Attunement (조율)** replaces **one** chosen line with a new random line, at
  the cost of a sacrificial Unique item or an Attunement Stone. No Kinah, no
  failure state.
- **Reset (초기화)** rerolls **all four** lines at once, costing one Soul Codex:
  Reset plus 300,000 Kinah.

Both belong to [[Attunement and Option Rerolls]]; they are listed here only
because they share the Integrated Enhancement → Soul Imprint tab (hotkey `N`).

One rule that lives here rather than there, because it is about the imprint rate
and not the reroll economy: **attuning or resetting a line re-rolls its imprint
rate as well.** A line that Soul Binding placed at a guaranteed 100% drops to a
random rate the moment you attune it. NC states this explicitly.

### 4. Soul Binding (영혼 결속) — the fifth line

Added **2026-02-11**. This is a separate, later system that buys one extra
imprint line on an already-finished item.

| Rule | Value |
| --- | --- |
| Requirement | Soul imprint rate at **100%** |
| Grade | **Unique or Heroic** only |
| Excluded | Unique gear awarded by quests cannot be bound |
| Cost | **2× Philosopher's Stone: Revelation (각인) + 1,000,000 Kinah** — identical for Unique and Heroic |
| Success rate | **100%.** Unlike enhancement, breakthrough and inheritance, this cannot fail |
| Result | One additional option, chosen randomly from the lines that slot can roll, **excluding options already on the item**, granted at **100% imprint rate** |
| Afterwards | The new line behaves like any other: it can be imprinted, attuned and reset — but attuning or resetting it drops it off 100% |
| Inheritance | **Soul Binding effects are not inherited.** They are excluded from the transfer entirely |

That last row is the expensive trap and it has a second edge. During Succession,
if the *source* item carries a soul imprint effect identical to the *target*
item's Soul Binding effect, that effect is dropped from the transfer rather than
merged. See [[Succession and Transfer]].

**The counter-intuitive optimisation.** A widely upvoted Inven write-up argues
you should Soul Bind the **target** item *before* inheriting into it, not after.
Take the fresh item to 100% imprint rate (cheap on a blank item, because the
Codex counter starts from zero), spend the Philosopher's Stones to open the fifth
slot, and only then inherit your old item into it. The inheritance carries the
old options across, the opened slot survives, and — critically — **the Codex
consumption counter resets**, so topping the finished item back to 100% starts
from 10 Codexes per press instead of from wherever your old item had climbed to.
The author reports finishing at roughly 320 Codexes and 1.28M Kinah on a Genesis
Dragon Lord Guard done this way. Single detailed source with screenshots;
**confidence medium-high**, and the mechanism is checkable in ten minutes in
game.

### 5. The Philosopher's Stone material chain

This chain is what actually gates Soul Binding, and it has been revised twice.

| Item | Korean | Status | Source |
| --- | --- | --- | --- |
| Sealed Philosopher's Stone | 봉인된 현자의 돌 (각인) | **Retired.** Season 2 placeholder, no longer drops except in the season shop | Dying Dramata's Nest (Season 2) |
| **Philosopher's Stone: Revelation** | 현자의 돌: 계시 (각인) | **Current baseline.** The Soul Binding material | Tier-4 Conquest Odyle Energy Cubes (Dying Dramata's Nest, Cradle of Nihility) on Normal and Hard; a **guaranteed** reward in both since 2026-03-11; material conversion from Sealed stones at 1:1 |
| **Philosopher's Stone: Authority / Power** | 현자의 돌: 권능 (각인) | Added **2026-05-27** for Genesis/Nemesis Dragon Lord gear and the new Abyss sets | Material conversion, **10× Revelation → 1 Authority** |

The 10:1 conversion is the real cost of Soul Binding a top-tier crafted weapon:
two Authority stones means twenty Revelation stones, on top of every Revelation
stone you spent on lesser slots.

There is one more conversion worth knowing because it links the two currencies:
**1 Philosopher's Stone + 200,000 Kinah → 50 Soul Codexes**. If you are short of
Codexes and long on stones, that recipe exists; in practice the reverse is true
for everyone.

## Unlock and gates

| Thing | Requirement |
| --- | --- |
| Soul Imprint | Automatic on first equip, any grade, any level |
| Raising the imprint rate | Possession of Soul Codexes |
| Reset | A Soul Codex: Reset plus 300,000 Kinah |
| Attunement | A Unique-grade sacrifice or an Attunement Stone — see [[Attunement and Option Rerolls]] |
| Soul Binding | Unique grade or above, imprint rate 100%, not quest-awarded, 2 Philosopher's Stones and 1M Kinah |

[[Stat Reference]] records level 32 as the point where soul imprint "supplies the
highest-value tuned options". That is a statement about when the system starts to
matter, not a hard unlock — the imprint fires on your level 5 gear too. Treat the
level 32 figure as **medium confidence** and the "automatic on first equip" rule
as high.

## Inputs: currencies, materials, sources

| Resource | Feeds | Where it comes from |
| --- | --- | --- |
| **Soul Codex** (영혼의 서) | Imprint rate | Transcendence Odyle Energy Cubes; material conversion of **200 Enhancement Stones + 10,000 Kinah → 1**; material conversion of **1 Philosopher's Stone + 200,000 Kinah → 50**; Shugo Festa shop (3 per character per week); Deva Pass and attendance books in 10s and 20s; supply-request rewards; event coin shops; the 100-Day and 200-Day gift boxes (500 at a time) |
| **Soul Codex: Reset** | Full four-line reroll | Nightmare exchange shop at **8,000 Phantasmal Fragments**; Season 4 shop at 60,000 season coin; Subjugation trade shop at 6,000 marks; Verteron/Altgard/Eltnen/Morheim Monolith levels; Hidden Cubes; achievements; Battle Pass; four level-45 island quests |
| **Philosopher's Stone: Revelation** | Soul Binding | Tier-4 Conquest Odyle cubes, Normal and Hard, guaranteed since 2026-03-11 |
| **Philosopher's Stone: Authority** | Soul Binding on Genesis/Nemesis Dragon Lord and new Abyss gear | 10× Revelation via material conversion |
| Kinah | 1,000,000 per Soul Binding; 300,000 per Reset | Everything |
| Unique-grade fodder / Attunement Stones | Attunement | [[Attunement and Option Rerolls]] |

Note the Nightmare price. 8,000 Phantasmal Fragments for one Reset Codex is why
[[Nightmare Mode]] appears in a gear note at all, and why Korean beginner guides
tell you to buy Reset Codexes first in that shop.

## Progression path

1. **Levelling.** Ignore the whole system. Do not spend a Codex on anything you
   will replace, and be conscious that trying on a tradable drop burns its
   tradability.
2. **First Unique set.** Still mostly ignore it. Take whatever lines dropped.
   The Korean rule of thumb is not to invest below roughly item level 1,600
   worth of gear on the pre-Chapter-1 scale.
3. **Weapon and Guard, imprint rate to 100%.** These two slots first, always,
   because they are the only ones that roll Weapon Damage Amplification and
   Combat Speed.
4. **Reset the weapon until one tier-0 line appears**, then stop resetting.
5. **Attune the remaining lines one at a time** — see
   [[Attunement and Option Rerolls]] for how to pay for that.
6. **Repeat down the slot order**: Guard, gloves, chest, shoulders, rings.
7. **Soul Bind only your final items.** Weapon and Guard first, then rings.
8. **Re-imprint to 100% last**, after the option set is settled, so that Codexes
   are not spent on lines you are about to replace.

The single most repeated sentence in Korean guides is a version of step 8:
**set the options first, then imprint.** Doing it the other way round is the
standard new-player money fire.

## Priorities and breakpoints

### Which options to want

The Korean community's tier list for weapon and Guard has been stable across
three seasons. The nickname for the target set is **3신기**, "the three sacred
treasures".

| Tier | Options | Note |
| --- | --- | --- |
| SS / tier 0 | **Combat Speed** | Every class, non-negotiable |
| S | **Weapon Damage Amplification**, **Might (위력, attack power %)**, **Precise (accuracy + crit)** | Precise rose sharply in value with the Dramata raid |
| A | **Damage Amplification** (added in Season 2), **Multi-hit Chance** | Multi-hit is class-dependent |
| B | Accuracy, flat Attack Power | Real, but behind the above |

Per-slot signature options — the ones that appear only on that slot and are
therefore what you actually chase:

| Slot | First-priority option |
| --- | --- |
| Weapon / Guard | Weapon Damage Amplification, Combat Speed |
| Gloves | **Combat Speed** |
| Chest | **Damage Amplification** |
| Shoulders | **Critical Damage Amplification** |
| Legs | **Damage Resistance** |
| Boots | **Movement Speed** |
| Cloak | **Critical Damage Resistance**; also class passive skill levels |
| Helm | Received Healing (healers and tanks), Smite, Attack Power increase |
| Ring | **Active skill levels** — the only slot that grants them |
| Necklace / Earrings | Class passive skill levels |
| Bracelet | Empyrean Lord attributes roll here at an unusually high rate |

Two of those deserve emphasis because they change how you spend elsewhere.
**Rings roll active skill levels**, which is how players close the gap from
skill level 19 to 20 without further skill investment; this is the reason
[[Accessories]] singles the crafted ring out. And the imprint pool includes
**class-specific passive skills** — the Sorcerer's Robe of Flame is the stock
example — so on the cloak, necklace and earrings you are effectively rolling for
your class's top-four passives and grinding away anything else.

### Where to stop

- **Do not chase the last 1–2% on a line.** Korean guides are explicit: whether
  Combat Speed rolled 9% or 10% matters far less than whether your next slot has
  Combat Speed at all. Breadth beats depth here.
- **Three good lines out of four is the practical finish** for most slots. Attune
  the fourth if fodder is free, and otherwise buy it with a Philosopher's Stone.
- **Free-to-play players should not Reset at all** below endgame gear. Farm items
  that happened to roll well and attune one or two lines.
- **Soul Bind the weapon, the Guard and your rings, and nothing else,** until
  those are done.

## Costs and math

- **Reset:** 1 Soul Codex: Reset + **300,000 Kinah** per attempt. Endgame players
  report one to three resets on a weapon, not more.
- **Soul Binding:** 2 Philosopher's Stones + **1,000,000 Kinah**, 100% success.
  With the 10:1 Authority conversion, a Genesis/Nemesis Dragon Lord piece costs
  **20 Revelation stones plus 1M Kinah** for its one extra line.
- **Codex conversion floor:** 200 Enhancement Stones buy exactly one Codex, so
  Codexes and [[Enchanting]] compete for the same pile. That exchange rate is
  the reason nobody converts at scale.
- **Codex-to-100% totals:** no published table exists, because the cost depends
  on where your random rolls landed. The one detailed report gives roughly **320
  Codexes and ~1.28M Kinah** to take a freshly inherited six-line Guard from a
  reset counter to 100%, with individual presses starting at 10 Codexes. Single
  source, **confidence medium**.
- **Taiwanese launch-week pricing** put a single Soul Codex at 60,000 tokens in
  the shop, which is why the TW community advice at launch was simply "do not
  reroll before you have endgame gear". Historic; **confidence low** on the
  number, high on the sentiment.

## Traps and mistakes

- **Trying on a tradable item to see how it looks.** The imprint fires and the
  item is bound forever. Use the wardrobe preview.
- **Spending Codexes before the options are settled.** Attuning or resetting a
  line re-rolls its imprint rate, so imprint work done first is thrown away.
- **Soul Binding an item you will inherit out of.** The bound line does not
  transfer. Bind the *destination*, not the source.
- **Soul Binding a stepping-stone item.** Korean guides name the Decanus-tier
  Abyss set specifically: bind the Tribunus, Legion Commander or crafted piece
  you will keep, not the one you are passing through.
- **Attuning a Soul-Bound line.** It was granted at a guaranteed 100%; attuning
  it throws that guarantee away for a random rate.
- **Extracting Unique duplicates.** They are attunement fodder. See
  [[Extraction and Refunds]].
- **Selecting the wrong slot number in the attunement UI.** The most-repeated
  practical warning in Korean guides is to check the slot index twice before
  confirming, because there is no undo and the good line is one click away from
  the bad one.
- **Reading an English guide without checking its vocabulary.** "Soul Binding"
  in an English article is roughly 50/50 to mean 영혼 각인 or 영혼 결속.

## Global launch notes

**Soul Imprint, the imprint rate, Soul Codexes, Reset and Attunement were all
present in the Korean and Taiwanese clients at the 2025-11-19 launch.** A
Season 1 global player on 2026-10-05 will have the full imprint loop on day one,
and should expect it to be the main thing they misspend resources on in week one.

**Soul Binding — the Philosopher's Stone system — will not be there.** It arrived
on **2026-02-11**. Everything in this note about a fifth line, 100%-guaranteed
effects, the 10:1 Authority conversion, and the bind-before-inherit optimisation
is roadmap.

**Launch Scale Test:** crafted weapon, Guard, and accessories still paid an
**extra soul-bind / imprint line** — that is the launch-era extra roll, not the
February Philosopher's Stone system. Global accessories used that extra line
for **Might, Precision, Move Speed, Combat Speed**. Armour used it for
**Weapon Damage Tolerance** on chest and helm. See [[Accessories]], [[Armor]],
[[Crafting]], [[Global Launch Differences]].

**Philosopher's Stone: Authority is further out still** (2026-05-27) and is
attached to Genesis/Nemesis Dragon Lord gear, which is Heroic-tier crafting and
therefore doubly absent if the reported no-Heroic-gear-at-launch claim in
[[Global Launch Differences]] holds.

Two smaller Korean revisions that a Season 1 global build may also lack: the
**2026-01-21 Season 2 additions to the imprint option pools** (Damage
Amplification on weapons; Attack Power Increase, Smite, Defense Increase and
Iron Wall on armour), and the **2026-02-25 change that removes the currently
equipped option from the attunement result pool** so you cannot roll the same
line back. Without the latter, rerolling is meaningfully worse. Both
**confidence high** on the KR dates, **medium** on the inference about global.

## Open questions

- [ ] The exact per-slot option pool and the drop weight of each line. Inven
      posts include screenshots with per-option percentages next to each entry,
      which implies the client displays reroll odds; nobody has transcribed the
      full table.
- [ ] Whether the number of imprint lines is fixed by grade, by item, or by
      source. Observed values are 3 (extended-range weapons), 4 (most drops),
      5 (crafted Unique) and 6 (Heroic and Genesis/Nemesis crafted). A grade rule
      alone does not explain all four.
- [ ] Whether the Soul Codex imprint-rate roll is uniform on 1–100 or weighted.
      The Taiwanese description says "random 1%–100%, never lower than current",
      which if uniform makes the expected Codex count to 100% computable.
- [ ] Whether Soul Binding can be used more than once on a single item to add a
      sixth and seventh line, or is strictly one extra line. Every source says
      "one line"; none says "once only" in so many words.
- [ ] What resets the Soul Codex consumption counter besides inheritance. The
      bind-before-inherit trick depends on this and it is documented only by one
      player.
- [ ] Whether Soul Imprint has a true level gate at 32, as [[Stat Reference]]
      records, or whether that is the level at which the good option pools open.

## Sources

- [Soul Codex (Bound) — item 535400001](https://aion2hub.com/database/items/535400001) — KR datamined, read 2026-09-06. **Load-bearing for the Soul Codex ruling**: item type, description, stack size, vendor price, and the full acquisition list including the Nightmare and season shops.
- [Soul Codex: Reset (Bound) — item 535200001](https://aion2hub.com/database/items/535200001) and [the same item on questlog](https://questlog.gg/aion-2/en/db/item/535200001) — KR datamined, read 2026-09-06. Second half of the Soul Codex ruling; the "grants soul bind reroll" behaviour, the 8,000 Phantasmal Fragment Nightmare price, and the Monolith and quest sources.
- [아이온2 인벤 — 2/11(수) 업데이트 노트](https://www.inven.co.kr/board/aion2/6388/96080) — KR, 2026-02-11. The authoritative Soul Binding rules: 100% imprint-rate requirement, Unique-or-above, quest gear excluded, the 2 stones + 1,000,000 Kinah cost table for Unique and Heroic, the "excludes options already present" rule, the 100% granted rate, that bound lines can still be imprinted/attuned/reset but lose the 100%, that bound effects are not inherited, and the three new Soul Codex acquisition routes including both material conversions.
- [퍼플 라운지 — 신규 시스템 '영혼결속' 우선순위](https://lounge.plaync.com/feed/59057?country=KR&locale=ko-KR) — KR official community, 2026-02-13. Per-slot Soul Binding priority (weapon → Guard → rings → bracelet → helm/cloak), the ring-for-active-skills and bracelet-for-Empyrean-stats observations, the inheritance-overlap warning, and confirmation that attuning a bound line re-rolls its rate. Note the page carries NC's own AI-generated disclaimer.
- [아이온2 인벤 — 영혼 결속 시스템 개요](https://www.inven.co.kr/board/aion2/6444/1336) — KR, 2026-02. Community Q&A confirming the same-cost-for-Unique-and-Heroic rule and that bound effects are excluded from inheritance.
- [[뉴스] 영웅, 계승에 쓴 키나 환급! 아이온2 2/10(화) 라이브 요약](https://www.inven.co.kr/webzine/news/?news=313506&site=aion2) — KR, 2026-02-10. NC's live-stream announcement of Soul Binding, the retirement of the Sealed Philosopher's Stone, and the 100% success rate framed against enhancement and breakthrough.
- [AION 2 Patch Notes — February 11, 2026](https://aion2hub.com/updates/aion-2-update-2026-02-11) index entry and [May 27, 2026: Muspel's Chalice](https://aion2hub.com/updates/aion-2-update-2026-05-27) — KR translated, read 2026-09-06. The Soul Binding launch date, and the Philosopher's Stone: Authority item with its 10× Revelation conversion.
- [AION 2 Introduces New Sanctuary 'Chalice of Muspel'](https://about.ncsoft.com/en/news/article/aion2_update_260527) — NC official English, 2026-05-27. Six base "Soul Inscription" options on Genesis/Nemesis Dragon Lord weapons and Guards, and "Philosopher's Stone: Power (Bound), which enables Soul Binding". Primary evidence for NC's inconsistent English naming.
- [AION 2 Launches Season 2 Update](https://about.ncsoft.com/en/news/article/aion2_update_260121) — NC official English, 2026-01-21. "Expanded Soul Binding options, additional Sync slots" — the other half of the naming evidence, and the origin of the Bind/Sync/Reset vocabulary in English guides.
- [AION 2 Patch Notes — January 21, 2026 (Season 2)](https://aion2hub.com/updates/aion-2-update-2026-01-21) — KR translated. The Sealed Philosopher's Stone's origin in Dying Dramata's Nest and its description as opening "an extra soul-engraving slot"; the new weapon and armour attunement options; and the inheritance rule that resets the target's attunement attempts.
- [《永恆紀元2》裝備強化系統介紹](https://www.animattoys.com/detail/zXNs9G79/) — TW, read 2026-09-06. The clearest mechanical statement of the imprint-rate roll: automatic on first equip, untradable afterwards, Soul Codex *or the same item* as material, and **each attempt rolls 1–100% but never below the current rate**. Also the imprint / adjust / initialise three-function UI.
- [《永恆紀元2》英雄級釘錘一覽](https://www.animattoys.com/detail/wS4AipiP/index.html) — TW item listing, read 2026-09-06. Per-item line counts of 4, 5 and 6 on Heroic maces, which is what rules out a simple grade-to-line-count mapping.
- [【討論】2/25更新公告內容 @AION2 哈啦板](https://forum.gamer.com.tw/C.php?bsn=82913&snA=4240) — TW Bahamut translation of the KR 2026-02-25 note. The 靈魂調整 change removing the currently-slotted option from the result pool, the 靈魂結合 section, and the 100-Day box contents listing 靈魂之書 ×500 and 靈魂之書：初始化 ×5 as stackable items.
- [아이온2 영혼 각인, 1순위로 뽑을 '필수 옵션'은?](https://www.gameple.co.kr/news/articleView.html?idxno=214690) — KR press (Gameple), Dec 2025. Imprint fires automatically on first equip; the imprint rate scales option values; Soul Codex: Reset resets all effects; the per-slot signature-option table for armour; and the PvE/PvP split in what counts as a valid option.
- [아이온2 인벤 — PVE 기준 부위별 영혼 각인 우선순위 추천](https://www.inven.co.kr/board/aion2/6444/1205) — KR, Season 2. The SS/S/A/B/C tier lists per slot, the note that Damage Amplification, Attack Power Increase, Smite, Defense Increase and Iron Wall were Season 2 additions, and the five-line crafted-weapon target set.
- [아이온2 인벤 — '영혼 각인 옵션' 우선 순위 (장비 부위별)](https://www.inven.co.kr/board/aion2/6444/556) — KR. The reset-then-attune workflow with screenshots, and the observation that the client displays per-option reroll percentages.
- [아이온2 인벤 — 계승할 때 무조건 현돌 미리 뚫는게 이득!](https://www.inven.co.kr/board/aion2/6444/2091) — KR, 2026-07-16. Sole source for the bind-before-inherit optimisation and the ~320 Codex / 1.28M Kinah figure. Screenshot-backed but single-source; recorded at medium confidence.
- [[Aion 2] Detailed Equipment System Guide](https://vortexgaming.io/en/postdetail/594067) and [[Aion 2] Soul Imprint Guide: How to Double Your Character Stats](https://vortexgaming.io/en/postdetail/605057) — EN translations of KR video guides, launch era. The four-random-options rule, the tradable-to-untradable conversion, the warehouse restriction, the 300,000 Kinah reset cost, and the Unique-versus-Heroic reroll strategy split.
- [아이온2 영혼 각인 조율 완벽 가이드 2026](https://alias007.tistory.com/759) — KR blog, Season 3. The Codex-to-100%-first rule, the "three sacred treasures" target set, the Shugo Festa weekly Codex limit of 3, and the stop-resetting-once-a-tier-0-line-appears heuristic.
- [아이온2 영혼 각인 공략: 부위별 1티어 옵션 우선순위 종결 (2026)](https://game.savetip.co.kr/aion2-soul-engraving-guide-option-priority/) and [PVE 영혼 각인 종결 가이드](https://game.savetip.co.kr/aion2-soul-imprint-pve-priority-guide/) — KR blogs, 2026. The tier table with roll percentages, the hotkey `N` navigation, the "don't chase the last 1–2%" advice, and the "compromise then finish with a Philosopher's Stone" endgame pattern.
- [Aion 2 Gear Enhancement Guide: Mastering Soul Binding and Syncing](https://www.mmoexp.com/News/aion-2-gear-enhancement-guide-mastering-soul-binding-and-syncing.html) — EN, boosting-shop SEO, 2026-01-16. Used as a **terminology exhibit** for the Bind/Sync/Reset framing and the "Soul Binding Books" phrasing. Its mechanical description of syncing (fodder Unique destroyed, one of four stats replaced, pool includes class passives and active-skill lines, can roll the same stat back) matches Korean sources and is corroborated; treat its numbers as unverified.
- [Aion 2 Soul Fuse System](https://www.u4n.com/news/aion-2-soul-fuse-system.html) and [Aion 2 Gear Guide](https://boostroom.com/blog/aion-2-gear-guide-weapons-armor-upgrades-and-progression) — EN, kinah/boosting-shop SEO, 2026. Used as **exhibits for the Soul Fuse ruling**: both describe "Soul Fuse" with the exact definition of 영혼 결속, and boostroom lists it alongside Soul Binding as though they were separate. Low trust; cited only to document the error.

## Related notes

[[Equipment]] · [[Attunement and Option Rerolls]] · [[Enchanting]] ·
[[Breakthrough]] · [[Succession and Transfer]] · [[Extraction and Refunds]] ·
[[Potential Enhancement]] · [[Runes]] · [[Brooch Pendant and Seal Slots]] ·
[[Manastones Spirit Stones and Godstones]] · [[Accessories]] ·
[[Gear Tiers and Sources]] · [[Stat Reference]] · [[Nightmare Mode]] ·
[[Material Conversion]] · [[Abyss Points and Ranks]] ·
[[Global Launch Differences]] · [[Glossary KR TW EN]] · [[Home]]
