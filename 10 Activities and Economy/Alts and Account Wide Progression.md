---
chapter: "10 Activities and Economy"
system: Alts and Account Wide Progression
type: progression-system
unlock: "second character slot at character creation; alt value starts at level 45"
account_wide: true
cadence: "continuous"
gates: ["level 45 for a useful alt", "item level 1000 for Expedition Conquest on an alt", "level 45 for server transfer"]
currencies: ["Kinah", "Quna", "Enhance Stones", "Odyle Energy", "Soul Crystal"]
region_verified: ["KR", "TW"]
patch: "KR/TW Chapter 1, 2026-07-01; per-server lockout conversion from Season 3, 2026-04-08"
confidence: medium
tags:
  - aion2/progression
  - aion2/activities-economy
---

# Alts and Account Wide Progression

> **In one sentence:** alt characters were the dominant power strategy in Korea
> for the first four months, NC spent Season 3 and Chapter 1 deliberately
> dismantling that, and a global launch player should plan for one main plus at
> most one utility alt.

## Why it matters

The reason alts mattered is arithmetic. Every dungeon entry charge, every daily
quest and every field-hunting Kinah cap was per character. A player with a main
and three level-45 alts had four times the entry budget and four times the
2,000,000 Kinah daily cap, and the shared Server Warehouse let them funnel all
of it to the main. Korean players called this "barrack efficiency" (배럭 효율)
and the gap it created between multi-character and single-character players was
the explicit target of the Season 3 rework.

Understanding what is shared and what is not also matters for a much more
ordinary reason: it tells you whether re-doing content on a second character is
progress or a waste of an evening.

**Keyboard and quickslot binds are per character on the server.** Copying local
`DeviceSetting_V2.dat` from your main to an alt does not apply those binds in
game. See [[Keybindings and Client Files]].

## How it works

### What is shared, and at what scope

AION 2 has three scopes, and "account-wide" in the loose sense usually means
server-wide.

| Thing | Scope | Notes |
| --- | --- | --- |
| Kinah | Account, via the Server Warehouse | Only Kinah in the character cube and character warehouse moves on a server transfer; Server Warehouse Kinah does not |
| Quna | Account | Merged on server transfer |
| Membership | Account | Alts get the same benefits |
| Enhance Stones and most materials | Server, via the Server Warehouse | Storable and, since 2026-01-28, usable directly from the warehouse for crafting, morphing, supply requests and integrated enhancement |
| Wardrobe and skin collection | Server, since Season 2 | Duplicates consolidated, exchange tickets issued |
| Special-grade appearances | Server, since Chapter 1 | Duplicates refunded as exchange tickets |
| Pet collection and levels | Server, since Chapter 1 | Pet counts summed across characters, levels and experience recalculated, race Understanding set to the highest character's level |
| Special-race pets | Character | Explicitly excluded from the pet consolidation |
| Empyrean Trace / feather progress | Reported to become shared, date not confirmed | A Korean guide states main-character feather work will be shared with alts, with no date given. Confidence low |
| Equipment | Character | Bound on equip; tradable pieces can move via the warehouse only before they are equipped |
| Soul-engraved (tuned) equipment | Character, permanently | Cannot be worn by another character or listed |
| Potential Amplification Stones | Character | Cannot be stored in or moved through the Server Warehouse |
| Daevanion Boards, Stigmas, Skills, Arcana | Character | No sharing mechanism |
| Battle passes | Per character or per server depending on the pass | Some passes are limited to one per server |
| Character slots | Server | 4 base per server, 1,000 Quna per extra slot; Chapter 1 added one free slot to every account |

### Entry limits: the shift from per-character to per-server

This is the change that broke the alt meta, and it happened in two steps.

**Season 3, 2026-04-08.** NC stated the goal explicitly as "homework reduction
and barrack-efficiency compression": raise the value of playing one character
and reduce the relative deprivation felt by players who do not run alts.
Expedition, Transcendence, Daily Dungeon, Shugo Festa, Dimensional Invasion,
Orders and Duty were converted from per-character to per-server counting.
Concretely:

- Shugo Festa reward keys went from 7 per character per week to 7 per server per
  week, 14 with a subscription, with rewards doubled to compensate.
- Order purchase limits became per server.
- Wind Breeze special-tab limits went from "4 per character and 12 per server" to
  a flat "21 per server".
- Odyle Energy material conversion went from 4 per character to 20 per server,
  and the per-character blueprint was removed.

**Chapter 1, 2026-07-01.** Expedition and Transcendence lost their reward-count
and kill-count caps entirely. Instead, a weekly count is consumed only when you
leave a cleared dungeon without claiming the final reward, and that count "is
shared across characters on the same server".

The net effect: running the same dungeon on four characters no longer multiplies
your rewards, because the limiting resource is now Odyle Energy, which is per
character but regenerates slowly, and the weekly counts, which are per server.

### The Kinah routes and how they closed

Korean alt strategy was primarily a Kinah strategy, and its history is a series
of closed doors.

| Route | Status |
| --- | --- |
| Fire Temple Exploration on alts | Converted to Bound Kinah in Season 3. Dead. |
| All Season 1 Expedition dungeons | Converted to Bound Kinah in Season 3. Dead. |
| Dying Dramata's Nest and Cradle of Nihility (Season 2) | Survived Season 3 as tradable Kinah, went 50 percent Bound in Chapter 1, went fully Bound on 2026-08-26. Dead. |
| Field hunting, 2,000,000 per character per day | Still per character and still tradable. **The last surviving alt Kinah route.** |
| Abyss hunting | Kinah payout reduced in Season 3 |

As of the 2026-08-26 patch, the only meaningful per-character tradable Kinah
income left in Korea is field hunting. An alt is worth 2,000,000 tradable Kinah
per day and nothing else, and it costs roughly 8 to 24 hours to build.

### The strategies that still work

**Proxy enhancing.** You can move a main-character item to an alt through the
Server Warehouse, perform enhancement there, and move it back. The documented
use is Potential enhancement: because Potential Amplification Stones cannot move
through the Server Warehouse, players farm them on the alt, transfer the main's
equipment to the alt, enhance on the alt, and transfer the finished item back.
The catch is that material conversion only works on items bound to that
character, so an item transferred in cannot be converted on the receiving alt.

A Taiwan community guide adds practical variants on the same warehouse route:
**soul-imprinted main gear** can still be **enhanced on an alt** (the alt cannot
wear it, but enhancement UI works), letting you spend **Bound Kinah and stones
 stuck on the alt** on main pieces; alts can also supply **manastone/soulstone
 rolls** and, via **Soulwinding**, **substat rerolls** using junk drops the alt
 cannot equip. See [[Twink Playbook - YouTube Ey_xTunLIg0]].

**Abyss Point and Nightmare twink loops.** Abyss Points are per character; several
**items** are warehouse-eligible (corridor manastones, crafted trace crystals,
**Amplify Stones**, Asphalt Trace fragments). **Global release:** **Silentium**
 from Ascension Trial is **not** warehouse-eligible, and the TW video’s **AP →
 PvP gear → dismantle for wardrobe skins** route is **not in launch** — see
 [[Twink Playbook - YouTube Ey_xTunLIg0]]. Nightmare fragment banking and proxy
 enhance still apply where the UI allows transfer.

**Enhance Stone extraction laundering.** Alts can enhance tradable Normal or
Superior gear to +3, at which point the enhancement carries with the item
through the warehouse. A related route enhances low-tier gear to +10 on an alt,
transfers it to the main, and extracts the stones there. See
[[Extraction and Refunds]].

**Abyss Point conversion.** Alts farm Abyss Points, buy manastones or recipes
with them, and send the items to the main or the Market. This is reported by a
low-trust source at 1,000-2,000 Abyss Points per manastone, uncorroborated.

**Faction coverage.** An alt on the opposing faction lets you clear the
opposing faction's Sealed Dungeons and Empyrean Traces, and clearing the
opposing faction's Sealed Dungeon is a prerequisite for using the Spacetime
Rift. Whether that is worth a second character depends on whether you can do it
by crossing over instead.

### Building an alt: documented timings

From a Korean alt-levelling guide, per character:

| Goal | Time |
| --- | --- |
| Max level only | about 8 hours |
| Max level plus Expedition solo capability | about 12 hours |
| Plus region quests and Sealed Dungeons | about 16 hours |
| To 1,600 Combat Power, including opposing faction content, gear purchases, Abyss Corridor and Orders | about 24 hours |

Kinah rates measured on alts, before the Bound Kinah conversion:

| Activity | Kinah per hour |
| --- | --- |
| Fire Temple grinding in a four-person party | about 1.4 million |
| Expedition solo play | about 2 million |
| Expedition Conquest at 1,500 Combat Power | about 4.8 million |

Those rates are now largely Bound Kinah, so treat them as a measure of growth
fuel rather than spendable money.

## Unlock and gates

- Four character slots per server by default, plus one free slot added in
  Chapter 1. Additional slots cost 1,000 Quna each.
- An alt needs level 45 to be useful and roughly 1,600 Combat Power to solo
  Conquest Expeditions.
- Server transfer requires level 45, a character standing in a town, no legion
  membership or pending application, no active Duty Mission, and no unclaimed
  Market listings, shop storage or mail.

## Inputs: currencies, materials, sources

| Cost of running alts | Amount |
| --- | --- |
| Extra character slot | 1,000 Quna |
| Server transfer base | 1,000 Quna per account, once only |
| Server transfer per character | 200 Quna |
| Server transfer slot expansion at the destination | 1,000 Quna per locked slot |
| Time to build one useful alt | 8 to 24 hours |
| Odyle Energy per alt | Regenerates separately per character, which is the one genuine multiplier left |

## Progression path

A recommended account plan for a global launch player.

1. **Pick one main and commit.** Every character-scoped system — Daevanion,
   Stigmas, Arcana, gear, Pantheon — is unshared and expensive. Splitting
   investment is the most common self-inflicted wound.
2. **Use the free slots for class trials, not for farming.** Chapter 1 gave
   everyone a free slot and the sensible use is trying the Fist Fighter or
   another role before committing.
3. **Build exactly one alt, and only after your main is comfortable.** Its jobs,
   in order: a second 2,000,000 Kinah field-hunting cap, a separate Odyle
   Energy pool, a proxy-enhancing mule, and warehouse overflow space.
4. **Put the alt on the same server as the main.** Everything that is shared is
   shared per server. An alt on another server shares only Kinah and Quna and
   loses the wardrobe, pet, and warehouse benefits.
5. **Consider the opposing faction only if you cannot reach opposing-faction
   Sealed Dungeons and Empyrean Traces any other way.**
6. **Do not build three or four alts on the KR pre-Season-3 model.** The entries
   they were built to consume are now per server.

## Priorities and breakpoints

- If you play under about 90 minutes a day, do not build an alt at all. Your
  main will not exhaust its own Odyle Energy.
- If you play more than that and are Kinah-limited rather than material-limited,
  one alt at level 45 with basic gear is worth the 8 hours.
- The break-even for a second alt is very poor post-Chapter-1 and Korean players
  who kept large barracks did so for content that no longer exists in that form.
- Consolidate materials on the main constantly. Since 2026-01-28 warehouse items
  can be used directly for crafting and enhancement, so there is no reason to
  carry anything.

## Costs and math

| Quantity | Value | Confidence |
| --- | --- | --- |
| Base character slots per server | 4 | medium |
| Free slot added in Chapter 1 | 1 per account | high |
| Extra slot price | 1,000 Quna | medium |
| Server transfer | 1,000 Quna + 200 per character + 1,000 per locked destination slot, once per account | high |
| Tradable Kinah per alt per day, post-2026-08-26 | 2,000,000 from field hunting | high |
| Time to build a 1,600 Combat Power alt | about 24 hours | medium |
| Wind Breeze special-tab limits | per server, not per character, since 2026-04-08 | high |
| Expedition and Transcendence weekly counts | shared across characters on the same server since Chapter 1 | high |

A worked example: a second alt built to 1,600 Combat Power costs about 24 hours
of play and returns 2,000,000 tradable Kinah per day if you actually spend an
hour a day hunting on it, plus its own Odyle Energy pool of roughly 560 per week
which converts to about 14 additional reward cubes. Whether that is a good trade
depends entirely on whether your main is already consuming its own energy. If it
is not, the alt is strictly worse than spending the same hour on the main.

## Traps and mistakes

- **Building alts against Korean guides written before April 2026.** Almost
  every English alt guide in circulation describes the pre-Season-3 model where
  entries were per character. Those guides are wrong for the current build and
  probably wrong for global.
- **Splitting gear investment.** Equipment binds on equip and soul-engraved gear
  binds permanently, so gear given to an alt is gone.
- **Trying to material-convert transferred items.** Material conversion only
  accepts items bound to the character performing it.
- **Expecting to move Potential Amplification Stones.** They cannot go through
  the Server Warehouse, which is precisely why proxy enhancing exists.
- **Putting the alt on a different server.** You lose the warehouse, the shared
  wardrobe and the pet consolidation, and a server transfer to fix it is once
  per account and costs Quna.
- **Forgetting Server Warehouse Kinah on a transfer.** Only cube and character
  warehouse Kinah moves; Server Warehouse Kinah is left behind.
- **Assuming battle passes are per character.** Several are limited to one per
  server, and a character holding a server-limited pass cannot transfer to a
  server where that pass is already active.

## Global launch notes

Two structural facts point toward global being less alt-friendly than Korean
launch was. First, the global build ships after the Season 3 and Chapter 1
per-server rework, so if NC ships the current systems the multiplier that made
Korean barracks worthwhile will not exist. Second, the global Market and
Exchange are Membership-gated, which caps the practical benefit of funnelling
tradable Kinah from many characters into one wallet: a free player cannot sell
what the alts farm.

What might still favour alts at global launch is that the earliest content is
easy and per-character Odyle Energy is a real multiplier, so an alt built in the
first month can absorb energy the main cannot. That is a short-lived window.

Global also introduces something Korea did not have at launch: separate
early-access servers with their own Market, Exchange and PvP matchmaking, plus a
Server Market from early access and a Cross-Server Market that opens later.
Founders should expect their early-access economy to be isolated for a period.
See [[Global Launch Differences]].

## Open questions

- [ ] Whether the global build uses per-server or per-character weekly counts.
      This is the decisive question for alt planning and can only be answered by
      reading the entry UI at launch.
- [ ] The exact base number of character slots per server in the global build,
      and the Quna price of extra slots. The 4-plus-1,000-Quna figure comes from
      one Korean community guide.
- [ ] Whether Empyrean Trace and feather progress is shared across characters,
      and from which patch. One Korean guide says it will be, with no date.
- [ ] Whether numeric per-character or per-server caps exist on the Kinah-Quna
      Exchange itself. No source checked documents one; the caps that are
      documented are all content purchase limits.
- [ ] Whether the global service offers server transfer at all, and at what
      price.
- [ ] Whether Bound Kinah exists at global launch, which determines whether alt
      dungeon farming produces spendable money.

## Sources

- [Vortex Gaming — Alt Character Leveling Guide](https://vortexgaming.io/en/postdetail/606901) — KR, translated Korean video guide, what is shared, equipment binding rules, alt build timings, Kinah-per-hour measurements.
- [Vortex Gaming — Potential System Complete Guide](https://vortexgaming.io/en/postdetail/689274) — KR, translated guide, proxy enhancing workflow, Potential Amplification Stone warehouse restriction, material conversion binding rule.
- [Kinah supply guide, Season 3 (Korean)](https://madimi.tistory.com/54) — KR, 2026-04-08, the alt Kinah route table, character slot count and Quna price, which routes converted to Bound Kinah.
- [GameY — Aion 2 Season 3 full rework preview](http://www.gamey.kr/news/articleView.html?idxno=3016741) — KR, 2026, NC's stated goal of compressing barrack efficiency and the full list of content converted from per-character to per-server.
- [Arca.live — KR 2026-04-08 patch notes](https://arca.live/b/aion2/167052865) — KR, 2026-04-08, per-server purchase limits, Shugo Festa key conversion, Odyle Energy conversion limit change.
- [AION2 Hub — Chapter 1 patch notes (2026-07-01)](https://aion2hub.com/updates/aion-2-update-2026-07-01) — KR, 2026-07-01, weekly counts shared across same-server characters, free character slot, server-wide special appearances and pets.
- [Inven — KR 2026-08-26 patch notes](https://www.inven.co.kr/board/aion2/6388/260802) — KR, 2026-08-26, the final Bound Kinah conversions and the full server transfer product terms.
- [Playforum — Aion 2 pet sharing and consolidation](https://www.playforum.net/news/articleView.html?idxno=633596) — KR, pet collection summed server-wide, race Understanding taken from the highest character, special-race pets excluded.
- [Questlog — AION2 Season 2 patch notes](https://questlog.gg/aion-2/en/patch-notes/aion2-season-2-launch-update) — KR, 2026-01-21, wardrobe ownership shared across same-server characters.
- [BoostRoom — Aion 2 inventory management](https://boostroom.com/blog/aion-2-inventory-management-guide-storage-rules-that-save-hours) — used for the lead only; the 2026-01-28 warehouse-usable-directly change it describes is corroborated by the behaviour documented in the Korean guides above.
- [Mein-MMO — Aion 2 early access and market structure](https://mein-mmo.de/en/) — GLOBAL, 2026, Server Market versus Cross-Server Market and early-access isolation.
- [YouTube — Twinking guide (DE, TW)](https://www.youtube.com/watch?v=Ey_xTunLIg0) — TW, 2026, per-character twink activity menu, AP/skin dismantle loop, Nightmare fragment routing, proxy enhance and Soulwinding; vault synthesis [[Twink Playbook - YouTube Ey_xTunLIg0]].
