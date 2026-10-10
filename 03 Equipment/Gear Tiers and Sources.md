---
chapter: "03 Equipment"
system: Gear Tiers and Sources
type: progression-system
unlock: "continuous; the meaningful gear economy opens at level 45"
account_wide: false
cadence: "daily and weekly reward counts"
gates: ["item level 1000", "item level 1600", "item level 2400", "item level 2700", "item level 3800 Season 1 ceiling"]
currencies: ["Kinah", "Soul-bound Kinah", "Odyle Energy", "Abyss Points", "Merit Medals", "Equipment Change Tickets"]
region_verified: ["KR"]
patch: "Season 3 / Chapter 1 era, KR live as of 2026-09-04"
confidence: medium
tags:
  - aion2/progression
  - aion2/equipment
---

# Gear Tiers and Sources

> **In one sentence:** AION 2 has five equipment grades and about a dozen
> distinct gear faucets, and knowing which faucet pays which grade — and whether
> the result is tradable — is what separates efficient farming from running the
> wrong dungeon for a month.

## Why it matters

The gear you can obtain is a function of the content you can enter, and content
entry is gated on item level, which is a function of the gear you have. Getting
this loop moving in the right order is the whole early and mid game. Beyond
that, grade determines the ceiling of every upgrade system layered on top: only
Unique grade and above can be Breakthrough'd, higher grades carry more Soul
Imprint lines and more manastone sockets, and Advanced Succession exists
specifically to move a Unique item's investment into a Heroic shell.

## How it works

### The grade ladder

| Grade | Korean | Colour (medium confidence) | What it means mechanically |
| --- | --- | --- | --- |
| Common | 일반 | White / grey | Vendor trash and starting kit. Extract it. |
| Rare | 희귀 | Blue | Levelling gear. Do not enhance past +5. |
| Epic | — | Purple | The first real dungeon tier. Fine as a full set at level 45. |
| Unique | 유일 | Gold / orange | The threshold grade: Breakthrough becomes possible, Soul Imprint becomes worth investing in, and Succession Stones can be made from it. |
| Heroic | 영웅 | — | Current endgame. More imprint lines, higher base stats, and the target of Advanced Succession. |

There is also a **Special** category in the item database used for loot chests,
tickets and Empyrean Traces rather than equipment.

**Terminology warning.** The community databases disagree. `aion2hub.com` and
`talentbuilds.com` use Unique and Heroic; `questlog.gg` renders the same two
grades as **Legend** and **Mythic**. Fextralife uses Rare / Epic / Unique /
Heroic. When you cross-reference item pages, `Legend = Unique` and
`Mythic = Heroic`. Some English guides also say "Legendary" for the top grade,
which does not correspond to a live grade name.

A further wrinkle: an "Advanced" or "Uncommon" green tier appears in Korean
video translations describing the starting Noble Belt as 고급 (advanced) before
it becomes 희귀 (rare). Whether green is a sixth grade or the client's label for
Common is unresolved.

### Grade does not fix item level

Per-item **Item Lv** on the tooltip rises with the patch that introduced the
item, independently of grade. Confirmed data points, all Heroic:

| Item | Grade | Item Lv | Introduced |
| --- | --- | --- | --- |
| Ludra's Bracelet | Heroic | 98 | Season 3 Sanctuary |
| Noble Dragon Lord Fist | Heroic | 108 | Season 3 crafting |
| Splendent Nemesis Dragon Lord Breastplate | Heroic | 134 | Chapter 1 crafting |

So a new Unique from the newest content can out-level an old Heroic. Compare
Item Lv, not grade, and then compare the layers on top. See
[[Item Level vs Combat Power]].

### Character item level by patch

The character-level number that gates content is **not** the sum of per-item
Item Lv. It also inflated sharply at Chapter 1, so numbers from different
patches are not comparable. This is the single most common source of confusion
in English guides.

| Era | Level cap | Rough character item-level range |
| --- | --- | --- |
| Launch to Season 1 (global) | 45 | **0–3,800.** Doors at 200 / 1,000 / 1,600 / 2,200 / 2,400 / ~2,700. 3,800 is the bar max |
| Season 2–3 KR | 45 | Extra raids and Transcendence on the same bar (3,000 / 3,500). Still not 4,000+ |
| Chapter 1 KR (Jul 2026 –) | 50 | **Rescale.** Expedition Normal 3,800 as a *floor*, Hard 4,500, Transcendence to 4,800. **Out** |

The step from a ~2,400 *dungeon door* to a **3,800 ceiling** is finishing
enchants, boards and Arcana on Season 1 gear. The step from 3,800 to
4,000–4,800 is a Chapter 1 rescale, not more Season 1 grinding.

### Difficulty structure

- **Expedition** (원정) runs **Exploration**, **Conquest Normal** and
  **Conquest Hard**. Hard costs more Odyle Energy (60 versus 40) and pays
  proportionally more.
- **Transcendence** (초월) runs **Grade 1 through 4** with an item level gate per
  stage. It was reduced from more stages to four in April 2026.
- **Sanctuary** (성역) is the 10-player raid tier since Chapter 1, with Normal
  and Hard on the later instances.
- **Nightmare** is solo, organised into Dream Layers by season.

### How gear actually drops

Two channels, and they have different bind rules:

1. **The Odyle Energy reward cube** at the end of a run. This is the main faucet.
   Cube contents are **Bind on Pickup**.
2. **Clean drops off the boss body**, distributed by dice roll among eligible
   party members. These are **tradable within the party** until you leave the
   instance.

On top of both sits a **pity / ceiling** mechanism: certain rewards are marked
`ceiling` rather than a percentage, meaning they are guaranteed after a set
number of final-boss kills. The **Gear Change Voucher** and
**Equipment Change Ticket** items are the important ones — they let you convert a
wrong-class or wrong-slot drop into the piece you actually need, or convert
tickets plus Kinah directly into gear. For Sanctuary weapons and Ludra's
Bracelet the ticket route is strictly better than waiting on the drop.

## Source table

| Source | Grades it pays | Notable gear | Notes |
| --- | --- | --- | --- |
| Main story quests | up to Unique | The level 45 story weapon; the green Noble Belt; Rare and Heritage pendants from Eltnen/Morheim | One-time, free, do not skip |
| Ascension quests (levels 5, 22, 32, 45) | Unique | Ascension Bracelet at 45 | One-time |
| Sealed Dungeons | Epic–Unique | Gear plus Daevanion Points and Daevanion Crystals | One-time per dungeon per map |
| Strongholds / Garrison Dungeons | materials | **Belt Enhance Scrolls** — the only source | One-time per stronghold per map |
| Empyrean Traces / Monoliths | materials | **Revelation and Fierce Battle Amulet Enhance Scrolls** | One-time collectibles, see [[Empyrean Traces and Feathers]] |
| Expedition — Exploration | Epic–Unique | `Faith`, `Judicator`, `Red Agate` on Easy | Pays Soul-bound Kinah since Season 3 |
| Expedition — Conquest Normal | Epic–Unique | `Corrupted Judicator`, `Black Claw`, `Divine Canyon`, `Division`, `Anguish`, `Unyielding`, `Bakarma`, `Durvati`, `Nuakum`, `Vakron`, `Nathara`, `Basilus` | Pays unbound Kinah on some instances |
| Expedition — Conquest Hard | Epic–Heroic | Same sets at up to double the rate, plus `Lava Heart` armor from Citadel of the Fallen Daeva and Consumed Deus Research Base | Item level 4,500 |
| Transcendence | Epic–Unique | Arcana cards primarily, plus Theostones | The Arcana faucet, see [[Arcana Refinement and Farming]] |
| Sanctuary — Abyssal Forge: Ludra | Unique–Heroic | `Ludra's` weapons and Guard (0.5%), Ludra's Bracelet (2%), `Abyssal` Unique set, `Ancient Spirit` Heroic armor | 10-player; Gear Change Voucher: Ludra as ceiling reward |
| Sanctuary — Corroded Decontamination Facility | Unique–Heroic | `Eroded Ruler` weapons, Heroic bracelets | Sanctuary 2 |
| Sanctuary — Muspel's Chalice / Chalice of Muspel | Unique–Heroic | `Lava Heart` weapons and Barrier (1% on Hard), `Faded Shadow` Heroic armor, `Kaldrix Brooch` (10% Hard) | Sanctuary 3 |
| Crafting | Rare–Heroic | The entire Dragon Lord family, reported best in slot for PvE, and **fully tradable until equipped** | See [[Crafting]] |
| Abyss shop (Abyss Points + Merit Medals) | Unique–Heroic | Decanus → Centurion → Tribunus, Legion Commander → Elite Legion Commander → Praetorian Captain | PvP set with a −5% PvE Damage Boost penalty; see [[PvP Gear]] |
| Abyss field | materials | Potential Amplifiers, Potential Stones, Medal Boxes | |
| Field bosses and Field Elites | Epic–Heroic | Exclusive field-boss gear in Eltnen/Morheim, Artwork collectibles, loot chests | Potential enhancement available on field-boss gear since Mar 2026 |
| Shugo Festa minigames | Unique | Gear for 1st and 2nd place, plus manastones and Pantheon statue materials | See [[Seasons and Battle Pass]] |
| Daily Dungeon | materials | Enhancement Stones and consumables | 14 entries per server per week |
| Nightmare | materials, statues | Runes via exchange ticket, Pantheon statues | Solo |
| Daily missions / Dispatch quests | Unique | Tradable Unique items from certain boss kills | |
| Deva Pass / season pass | materials | Enhancement Stones, Soul Crystals, Stigma Shards, `+10 Conquest Weapon/Armor/Accessory Set Chests` | See [[Seasons and Battle Pass]] |
| Hidden Cubes | cosmetics, stones | Manastones, godstones, wings, appearances | See [[Hidden Cubes]] |
| Brokerage / World Brokerage | anything tradable | Crafted gear, materials, unbound Kinah economy | Cross-server since Dec 2025; **membership-gated** |
| Substance Morph | Unique–Heroic | Epic and Unique Amulet and Belt exist **only** here | See [[Accessories]] |

## Bind rules and what is tradable

| Category | Rule |
| --- | --- |
| Cube / reward-package items | **Bind on Pickup** — yours alone |
| Clean boss-body drops | **Group-tradable** inside the instance, distributed by dice roll; the window closes when you leave |
| Crafted top-tier gear | **Bind on Equip** — confirmed on the Noble Dragon Lord and Splendent Nemesis Dragon Lord item pages. This is why crafted gear drives the economy |
| Crafting materials | Fully tradable, and this is where most crafter income comes from |
| Anything named `(Bound)` | Soul-bound; cannot be traded, and this suffix expanded steadily through 2026 |
| Any item after Soul Imprinting | Becomes permanently untradable, even if it was Bind on Equip |
| Kinah | Split into Kinah and **Soul-bound Kinah** in March 2026; dungeon payouts moved progressively toward the bound form |
| Broker access | Requires an active membership; part of the November 2025 anti-bot package |

Two loot-rule changes worth knowing: premium loot was restricted to dice rolls
in November 2025, and from August 2026 dice can only be rolled from inside the
distribution range, with the Sanctuary exempt.

The important consequence for a fresh global player: **the only gear you can buy
is crafted gear.** Dungeon drops are bound, Abyss gear is Abyss-Point-only, and
the Belt and Amulet are personal. If you want to convert Kinah into power, the
broker sells crafted Dragon Lord pieces and crafting materials, and nothing else
of consequence.

## Unlock and gates

Content entry is the real gate structure. **Season 1 doors** are in
[[Item Level vs Combat Power]] (200 / 1,000 / 1,600 / 2,200 / 2,400 / ~2,700,
ceiling 3,800). The table below is **current Korean Chapter 1**, not launch:

| Content | Level | Item level | Season 1 |
| --- | --- | --- | --- |
| Expedition Exploration / Conquest Normal (Citadel of the Fallen Daeva, …) | 50 | 3,800 as a *floor* | **Out** |
| Conquest Hard | 50 | 4,500 | **Out** |
| Transcendence Abyssal Horn Den stages 1–4 | 50 | 3,800 / 4,100 / 4,500 / 4,800 | **Out** |
| Reshanta Surface (Abyss) | — | **≤** 4,300, or ≤400k Combat Power | **Out** |
| Rift of Time and Space Contest | 50 | 4,500 and 500.0k Combat Power | **Out** |

Note that the Abyss surface layer has an **upper** bound — it is a low-gear
bracket, not a progression gate.

## Inputs: currencies, materials, sources

| Resource | Role |
| --- | --- |
| Odyle Energy | Gates the reward cube, which is the actual gear faucet. Regenerates, purchasable from the Breeze Shop, dropped by Conquest bosses (15 per boss kill across 5 players) |
| Weekly reward counts | Expedition 14 per server per week, Transcendence 7, Daily Dungeon 14 (Apr 2026 values; changed repeatedly) |
| Final-boss kill count | Drives the guaranteed / ceiling rewards, halved to 1 kill per Sanctuary in Chapter 1 |
| Kinah and Soul-bound Kinah | Enhancement, crafting, ticket conversions |
| Abyss Points, Silver / Gold Merit Medals | The whole Abyss ladder; medals capped at 20 silver and 10 gold per character per week |
| Equipment Change Tickets | Converting Sanctuary loot into usable gear |

## Progression path

1. Story to level 45 taking every quest reward.
2. Clear all Sealed Dungeons and Strongholds once, on **both** faction maps, and
   collect all Empyrean Traces. This is one-time item level plus the scroll
   economy for [[Accessories]].
3. Epic Expedition set from Exploration and Conquest Normal.
4. Unique Expedition set from Conquest Normal and Hard, plus Abyss-Point
   accessories if you PvP.
5. Transcendence for [[Arcana]], which contributes item level in its own right.
6. Sanctuary for Heroic weapons and bracelets, via tickets rather than drops.
7. Crafting for the pieces that are best in slot and for anything you want to
   sell.

## Priorities and breakpoints

- Fix the **lowest** slot, not the highest. One badly outdated piece drags the
  whole average and therefore your content access.
- Separate **gate gear** from **investment gear**. A higher-Item-Lv piece with
  bad stats is a fine key to the next dungeon and a terrible target for
  Breakthrough Stones.
- Run the **highest difficulty you clear reliably**, not the highest you qualify
  for. Wipes consume Odyle Energy and weekly reward counts, which are the actual
  scarce resources.
- Do limited-reward content before unlimited farming. Weekly counts expire;
  field mobs do not.

## Costs and math

Representative drop rates, per roll from the boss pool, from the datamined
tables:

| Grade | Typical per-roll chance |
| --- | --- |
| Epic armor / accessory | 8–30% depending on slot and difficulty |
| Epic weapon | 3–7% |
| Unique armor | 1–8% |
| Unique weapon | 0.5–2.5% |
| Heroic armor | 0.13–2% |
| Heroic weapon | 0.5–1% |

Rings are consistently the highest-rate item in any pool, weapons the lowest.
That asymmetry is why accessories are the cheap way to raise item level and
weapons need the ticket and crafting routes.

## Traps and mistakes

- Comparing item-level numbers across patches. 2,400 and 4,800 describe similar
  states of progression at different level caps.
- Trusting a grade name from one database against a different database. Check
  whether the site says Unique/Heroic or Legend/Mythic.
- Leaving the instance before distributing clean drops the group agreed to trade.
- Soul Imprinting a Bind-on-Equip crafted item you intended to resell.
- Farming a 0.5% Heroic weapon drop when the ticket conversion is available.
- Assuming the broker is usable without a membership.
- Entering the Abyss surface layer over the item-level cap; it ejects you and
  deducts an hour of usage time.

## Global launch notes

**No Heroic** and **no Hard-mode Conquest** still reshape the source table:
Unique is the ceiling.

**Launch Scale Test additions:**

- Conquest doors **700 / 1,400–1,500 / 2,100–2,200**, not 1,000 / 1,600 / 2,200.
- Base Attack and Defense **higher** than KR; built-in PvE Damage Boost
  **missing**.
- Early enhancement caps reported **green +5 / blue +10** (KR +10 / +15).
- Pity boxes include **accessories and armour**.
- Silver medals only → PvP shop around item level 77.

See [[Item Level vs Combat Power]] and [[Global Launch Differences]].

## Open questions

- [ ] Whether green "Advanced / Uncommon" is a distinct sixth grade or the
      client's rendering of Common.
- [ ] The exact colour assigned to Heroic in the client.
- [ ] The formula relating per-item Item Lv, enhancement, Arcana, wings and
      Pantheon to character item level.
- [ ] Which specific Sanctuary drops the `Eroded Ruler` weapon set; the succession
      chain names it but the datamined drop table I read predates it.
- [ ] Whether the July 2026 note's "enhancement first, then untradeable" material
      rule changes bind behaviour for crafted gear.
- [ ] Current weekly reward counts. They changed in November 2025, December 2025,
      April 2026, May 2026 and July 2026, and Chapter 1 replaced counts with a
      leave-without-collecting decrement.

## Sources

- [AION 2 Drop Rates](https://aion2hub.com/database/drop-rates) — KR datamined,
  read 2026-09-06. 811 dropped items with per-roll percentages by boss and
  difficulty, the ceiling / pity mechanism, the grade labels, and the Gear Change
  Voucher entries. Primary basis for the source table and the rate table.
- [AION 2 Item Database](https://aion2hub.com/database) — KR datamined,
  read 2026-09-06. 12,805 items; the grade vocabulary and the Special category.
- [Items, questlog.gg](https://questlog.gg/aion-2/en/db/items) — KR datamined,
  read 2026-09-06. Shows the same items graded Legend and Mythic, which is where
  the terminology warning comes from.
- [Noble Dragon Lord Fist](https://aion2hub.com/database/items/110920001) and
  [Splendent Nemesis Dragon Lord Breastplate](https://aion2hub.com/database/items/210120020)
  — KR data, read 2026-09-06. Bind on Equip on crafted gear, and the Item Lv 108
  versus 134 comparison.
- [AION 2 Update — July 1, 2026: Chapter 1](https://aion2hub.com/updates/aion-2-update-2026-07-01)
  — KR. Expedition and Transcendence item-level gate tables, Sanctuary becoming
  10-player, Odyle Energy cost changes, the Reshanta Surface upper cap, and the
  ticket-plus-Kinah conversion blueprints.
- [AION 2 Update — August 12, 2026](https://aion2hub.com/updates/aion-2-update-2026-08-12)
  — KR. Consumed Deus Research Base and Noiran's Hidden Legacy gate tables, and
  the dice distribution-range rule.
- [AION 2 Update — September 2, 2026](https://aion2hub.com/updates/aion-2-update-2026-09-02)
  — KR. Item level 4,500 and Combat Power 500.0k as the current top gate.
- [AION 2 — April 8, 2026 Update Notes](https://aion2t.com/news/19) — KR.
  Transcendence reduced to four stages with 1,200 / 1,500 / 1,800 / 2,200 gates,
  weekly reward counts, Merit Medal caps, and Sanctuary reward changes.
- [AION 2 Patch Notes index](https://aion2hub.com/updates) — KR/Global,
  read 2026-09-06. The Kinah / Soul-bound Kinah split (Mar 2026), cross-server
  World Brokerage (Dec 2025), membership-gated brokerage and premium-loot dice
  restriction (Nov 2025), Potential enhancement on dungeon and field-boss gear
  (Mar 2026).
- [Aion 2 Gear-Guide](https://mmo-news.audio/aion-2-gear-guide) — DE mirror of
  the Mein-MMO guide, read 2026-09-06. The launch-era item-level roadmap of
  1,000 / 1,300 / 1,600 / 1,800 / 2,200 / 2,400.
- [Aion 2 F2P Endgame Gearing Guide](https://vortexgaming.io/en/postdetail/598251)
  — EN translation of a KR video. The Unique-equipment acquisition table: main
  quest, Expedition, Abyss Points, Shugo Festa, daily missions, field named mobs.
- [Aion 2](https://aion2.wiki.fextralife.com/) — EN wiki. Dungeon gear is Bind on
  Pickup with some pieces tradable among group members, and PvP gear is
  Abyss-Point-only.
- [10 Secrets of Aion 2 Economy and Trading System](https://www.u4n.com/news/10-secrets-of-aion-2-economy-and-trading-system.html)
  and [Aion 2 Dungeon Loot Explained](http://yowland.com/blog/aion-2-dungeon-loot-explained-rng-vs-pity-systems)
  — EN, low-trust SEO. Used as leads for the cube-versus-clean-drop bind
  distinction, which the fextralife wiki and the patch notes corroborate.
- [AION 2 Global Changes Revealed](https://www.mmoexp.com/News/aion-2-global-changes-revealed-no-heroic-gear-higher-ilevel-gates-level-cap-20-more.html)
  — EN, low-trust. Sole source for the no-Heroic-gear and higher-gate claims;
  recorded as low confidence.
