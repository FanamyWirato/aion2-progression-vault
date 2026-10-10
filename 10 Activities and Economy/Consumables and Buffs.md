---
chapter: "10 Activities and Economy"
system: Consumables and Buffs
type: progression-system
unlock: "Alchemy and Cooking professions; scrolls and potions drop from level 10"
account_wide: false
cadence: continuous
gates: ["profession mastery level for higher grades", "Intermediate Cooking Lv 90 for Epic food"]
currencies: ["Kinah", "Bound Kinah", "Quna", "profession materials"]
region_verified: ["KR"]
patch: "KR Chapter 1 (2026-07-01) Hidden Cube rate changes"
confidence: medium
tags:
  - aion2/progression
  - aion2/activities-economy
---

# Consumables and Buffs

> **In one sentence:** buff scrolls, potions and cooked food are worth roughly a
> gear tier of stats for a few thousand Kinah, which makes skipping them the
> cheapest mistake in the game and the reason most "my gear is fine but I can't
> clear this" problems resolve.

## Why it matters

AION 2's dungeon tiers are gated on hard stat cuts — accuracy in particular. A
character who is a few dozen accuracy short of the threshold does not clear
slower; they miss, and the fight is unwinnable. Consumables are how you cover
that gap without waiting for a drop.

The buff economy also connects three otherwise-separate systems: it is the main
Kinah sink that is not gear enhancement, the main reason to level Alchemy and
Cooking in [[Professions and Mastery]], and one of the few places the cash shop
touches combat power directly. It is worth being precise about which of those
last claims is true.

## How it works

### Buff scrolls (주문서)

Scrolls are **Alchemy** products. They are single-target self-buffs with a
duration in the tens of minutes, and they persist through zoning but not through
death in most reports.

| Korean | English | What it does |
| --- | --- | --- |
| 가호 | Blessing | The general-purpose stat scroll; the "상급 가호" (Greater Blessing) variant is the one endgame players actually use |
| 질주 | Sprint | Movement speed |
| 용기 | Courage | Attack-side stats |
| 광풍 | Gale | Attack speed |
| 충격 완화 | Shock Mitigation | Damage reduction / mitigation |
| 치명타 향상 | Critical Enhancement | Critical rate |
| 상태이상 저항 | Ailment Resistance | Crowd-control and debuff resistance |

Two things about grades. First, scrolls carry a **prefix ladder** — the plain
scroll and the 상급 ("Greater") version are different items with different
Alchemy requirements, and the Greater versions are what raid groups use.
Second, and contrary to a common assumption, **the scrolls I could verify sit at
Common item grade**, not at a Rare or Epic grade. The prefix, not the item
grade, carries the power difference. **Confidence medium** — I found no
comprehensive grade table for the full scroll list.

### Potions and elixirs

| Korean | English | Notes |
| --- | --- | --- |
| 생명의 물약 | Life Potion | Instant HP; the workhorse consumable |
| 정신의 물약 | Mind Potion | Instant MP |
| 상급 치유 물약 | Greater Healing Potion | Higher-tier heal |
| 비약 | Elixir | The 비약 line is distinct from 물약: longer effect, stronger, rarer |
| 바람의 비약 | Elixir of Wind | Flight time; the reported value is **1,000 flight time** |
| 부활의 정령석 | Resurrection Spirit Stone | In-place resurrection. Not a buff, but the single most raid-relevant consumable |

The 물약 / 비약 split is worth internalising because English guides collapse both
to "potion". 물약 is a potion — instant, cheap, spammed. 비약 is an elixir —
a prepared, longer-acting item, and the flight-time item lives in this family.

### Cooked food

**There is no "Master" grade cooking in AION 2.** This is a real correction
worth recording, because the term appears in circulating guides. It comes from
the original AION's food database, where 명인/명장 ("Master/Master-Artisan")
grades exist. AION 2's cooking ladder is:

| Grade | Korean tier name | Notes |
| --- | --- | --- |
| Common | (plain) | Simple HP/MP/Stamina restoration, ~300 seconds |
| Rare | 장인의 — "Artisan's" | Mid-tier, modest stat lines |
| Epic | 백룡의 / 흑룡의 — "White Dragon's" / "Dark Dragon's" | The real endgame food; ~30 minute stat buffs |

The Epic tier is **faction-split**, and this catches people out when following a
cross-faction guide:

- **Elyos** cook the **White Dragon's** line, using Cypri, Inina and Kukuru
  ingredients.
- **Asmodians** cook the **Dark Dragon's** line, using Pujery, Conide and Ohkra.

They are mechanically parallel, not different in power. Epic recipes need
**Intermediate Cooking around level 90** and consume gathered materials
including **Odyle** — the raw material covered in [[Odyle and Special Resources]],
not the reward currency in [[Odyle Energy and Entry Limits]].

Effects are stat lines rather than restoration: the Dragon's-tier dishes give
things like accuracy and attack for roughly 30 minutes. **Accuracy food is the
one every endgame player carries**, for the reason in the next section.

### Stacking and duration

The rule reported consistently in Korean play discussion is that
**food, drink and scroll occupy separate buff categories, and a new item in a
category overwrites the old one rather than stacking.** So you can run food plus
a scroll plus a potion effect simultaneously, but not two foods.

I want to be honest that this is **community consensus, not a published rule** —
I found no official documentation of the buff-category table. **Confidence
medium.** The practical advice is unaffected: one food, one scroll of each type,
refresh before a boss rather than after.

Durations cluster around 30 minutes for food and scrolls, 300 seconds for Common
restoration food, and instant for potions. Buffs are per character, so alts
buff separately; see [[Alts and Account Wide Progression]].

### Where they come from

| Source | What it provides | Notes |
| --- | --- | --- |
| **Alchemy** | The whole scroll line, potions, elixirs | The primary route. See [[Professions and Mastery]] |
| **Cooking** | All food tiers | Faction-split at Epic; needs gathering |
| **Hidden Cubes** | Mind Potions, Life Crystals, godstones, scrolls | Chapter 1 **raised the drop rates** for exactly these categories |
| **Attendance calendars** | Bundled potions and scrolls | Reliable early-game supply |
| **Wind Breeze Trading Company** | Consumables in the membership tab | See [[Currencies and Economy]] |
| **NPC shops** | Basic potions | Common grade only |
| **Events**, including [[Shugo Festa]] | Resurrection Spirit Stones, buff bundles; Festa cubes also spill generic gear and Unique pieces | Frequent. Festa is hourly, not a limited banner — see that note for keys and the shop |
| **Cash shop** | Consumable tab; growth-support packs bundle them | See below |
| **Player market** | Everything craftable | Alchemy and Cooking are genuinely profitable professions because of this |

### An honest note on what is shop-sold

The cash shop does sell consumables, and growth-support and starter packs bundle
them. But the framing matters: **the meaningful buff items are all craftable and
all tradable.** The shop route is a convenience purchase, not an exclusive one —
you can buy a raid's worth of Greater Blessing scrolls and Dragon's-tier food
from other players for Kinah, and most endgame players do exactly that rather
than levelling Alchemy themselves.

The one consumable that is genuinely economically sensitive is the
**Resurrection Spirit Stone**, because it converts money into attempts in timed
content. It is obtainable from events and crafting, so it is not paywalled, but
a player who buys them has more attempts per week than one who does not.

## Unlock and gates

- Basic potions and scrolls from roughly level 10, via drops and NPC shops.
- Alchemy and Cooking unlock with the profession system; grade access follows
  mastery level.
- **Epic (Dragon's) cooking needs Intermediate Cooking around level 90** and
  faction-appropriate gathered ingredients.
- No content gates consumables themselves — the gate is your profession level or
  your Kinah.

## Inputs: currencies, materials, sources

| Resource | Consumed by |
| --- | --- |
| Kinah / Bound Kinah | Buying from players and NPCs; crafting fees |
| Gathered herbs, meats, Odyle | Alchemy and Cooking recipes |
| Cypri / Inina / Kukuru | Elyos Epic cooking |
| Pujery / Conide / Ohkra | Asmodian Epic cooking |
| Quna | Cash-shop consumable tab and packs |
| Profession mastery | Grade access |

## Progression path

1. **Levelling.** Use whatever drops and whatever the attendance calendar gives.
   Do not spend Kinah on scrolls before endgame; the stat gap does not bind.
2. **First endgame dungeons.** Start carrying Greater Blessing and a Life Potion
   stack. This is the point where consumables begin paying for themselves.
3. **First accuracy wall.** Add accuracy food. This is usually the actual fix
   for a dungeon that "should" be clearable.
4. **Progression raiding.** Full kit: food, Greater Blessing, the situational
   scroll for the fight (Ailment Resistance for CC-heavy bosses, Shock
   Mitigation for damage checks), and Resurrection Spirit Stones.
5. **If you want to fund it yourself,** level Alchemy and Cooking. Both are
   profitable on the player market precisely because everyone else skips them.

## Priorities and breakpoints

- **The accuracy threshold is the breakpoint that matters.** Korean community
  reporting puts an accuracy cut around **1,100** for the harder endgame content
  — Transcendence 10 and Conquest Hard are the two named. Food is how most
  players cross it. **Confidence medium**; the number is community-reported,
  not from a patch note.
- **Buff before entering, not after the pull.** Since Season 3, Ascension Trial
  starts its clock on entry, so buffing inside costs score. See
  [[Trials and Rankings]].
- **Refresh at 30 minutes, i.e. between bosses,** not mid-fight.
- **Ailment Resistance is fight-specific and often the difference** in CC-heavy
  encounters, more than a raw damage scroll would be.
- **Resurrection Spirit Stones are the highest-value consumable per Kinah in
  timed content,** because they convert directly into attempts.

## Costs and math

The comparison to make is against gear. A Dragon's-tier accuracy dish plus a
Greater Blessing scroll costs a few thousand Kinah on the player market and
provides a stat block comparable to a meaningful piece of gear upgrade — for one
run. Against enhancement costs in the hundreds of thousands to millions of Kinah
per attempt (see [[Currencies and Economy]]), consumables are the cheapest stats
in the game by more than an order of magnitude.

That is the whole argument, and it is why the mistake is universal: players
optimise the expensive system and ignore the cheap one.

Crafting your own inverts the economics again — the Kinah cost becomes gathering
time, and surplus becomes player-market income. Alchemy and Cooking are the two
professions with reliable endgame demand for this reason.

## Traps and mistakes

- **Looking for "Master-grade" food.** It does not exist in AION 2. The top tier
  is Epic — White Dragon's for Elyos, Dark Dragon's for Asmodians. Guides using
  "Master" are quoting the original AION's database.
- **Following the wrong faction's recipe list.** Cypri/Inina/Kukuru versus
  Pujery/Conide/Ohkra. The dishes are parallel; the ingredients are not.
- **Confusing 물약 with 비약.** Instant potion versus prepared elixir. The
  flight-time item is an elixir.
- **Confusing Odyle the cooking ingredient with Odyle Energy.** Selling gathered
  Odyle because you have spare energy destroys your Epic cooking inputs.
- **Doubling up in one buff category.** A second food overwrites the first;
  you have wasted the item, not stacked it.
- **Buffing after the timer starts.** Costs score in Trial content and wastes
  duration everywhere else.
- **Assuming buffs are shop-exclusive.** Every meaningful consumable is
  craftable and tradable.
- **Skipping consumables while grinding for gear.** The stat gap they close is
  frequently larger than the upgrade you are grinding for.
- **Using the original AION's item database for research.** The tiers,
  ingredients and effects genuinely differ between the two games.

## Global launch notes

Consumables are core systems rather than seasonal content, so this is the most
Season-1-safe note of the five.

| Element | Season 1 global player has it? |
| --- | --- |
| Buff scrolls (Blessing, Sprint, Courage, Gale, Shock Mitigation, Critical, Ailment Resistance) | **Yes.** Core Alchemy output, present from early levels |
| Life and Mind potions, Greater Healing Potions | **Yes** |
| Elixirs including the flight elixir | **Yes** |
| Resurrection Spirit Stones | **Yes** |
| Common and Rare (Artisan's) cooking | **Yes** |
| Epic Dragon's-tier cooking | **Yes in principle** — but it needs Intermediate Cooking around level 90, so it is a late-Season-1 goal rather than a launch-week one |
| Chapter 1 Hidden Cube rate increases for potions, godstones and scrolls | **No.** That specific buff to drop rates is a Chapter 1 change; expect the older, stingier rates |
| Cash-shop consumable tab and growth packs | **Yes.** Confirmed for global monetisation |
| Attendance-calendar consumable bundles | **Yes** |

The one genuine difference to expect: **consumables will feel scarcer at global
launch than Korean guides describe**, because Chapter 1's Hidden Cube rate
increase has not happened yet. Budget more Kinah for market purchases early on.
See [[Global Launch Differences]].

## Open questions

- [ ] What is the full buff-category table — how many simultaneous categories
      exist and which scrolls share one? Community consensus says
      food/drink/scroll are separate; no official source confirms it.
- [ ] Exact durations and magnitudes per scroll grade. I found the scroll list
      and the prefix ladder but no numeric table.
- [ ] Are the scroll items really all Common grade, or do Rare and Epic scroll
      grades exist at higher Alchemy levels?
- [ ] Is the endgame accuracy cut actually 1,100, and does it differ between
      Transcendence 10 and Conquest Hard?
- [ ] Do buffs survive death? Reports say most do not; not verified.
- [ ] Full stat lines for the White Dragon's and Dark Dragon's dish list — which
      dish gives which stat, at what magnitude.
- [ ] Does the global build sell Resurrection Spirit Stones directly for Quna,
      or only bundle them in packs and events?

## Sources

- [questlog.gg — AION 2 crafting database, Dark Dragon's Beef Wellington](https://questlog.gg/aion-2/en/crafting/524084002) — EN database of KR data, retrieved 2026-09-06, Epic cooking tier naming, Odyle as an ingredient, Intermediate Cooking level requirement, faction-split ingredient lines.
- [questlog.gg — AION 2 item and crafting browser](https://questlog.gg/aion-2/en) — EN database of KR data, retrieved 2026-09-06, the Common / Artisan's / Dragon's cooking ladder and the Alchemy scroll list with prefix variants; establishes that no "Master" grade exists.
- [AION2 Hub — Chapter 1 patch notes (2026-07-01)](https://aion2hub.com/updates/aion-2-update-2026-07-01) — KR, 2026-07-01, increased Hidden Cube acquisition rates for Mind Potions, Life Crystals, godstones and scrolls.
- [Inven — 아이온2 게시판, 요리/연금 관련 팁](https://www.inven.co.kr/board/aion2/6444/257) — KR, 2026, cooking mastery progression and the practical value of Dragon's-tier food at endgame.
- [Namu Wiki — 아이온2](https://namu.wiki/w/%EC%95%84%EC%9D%B4%EC%98%A82) — KR, the 물약 versus 비약 distinction, the Elixir of Wind flight value, and the profession structure behind Alchemy and Cooking.
- [Arca.live — 아이온2 채널, 소모품 및 정확도 컷 논의](https://arca.live/b/aion2) — KR, 2026, community reporting of the ~1,100 accuracy cut for Transcendence 10 and Conquest Hard, and the food/drink/scroll buff-category convention. **Community consensus, not official.**
- [Inven Aion 1 food database](https://aion.inven.co.kr/dataninfo2/item/?type=food) — KR, checked and **rejected** as a source. This is the original AION's database, where 명인/명장 "Master" food grades exist. It is the origin of the incorrect "Master-grade cooking" claim about AION 2 and is cited here only to document that correction.
