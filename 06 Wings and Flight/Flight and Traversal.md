---
chapter: "06 Wings and Flight"
system: Flight and Traversal
type: progression-system
unlock: "level 5 (Elyos) / level 6 (Asmodian) ascension quest"
account_wide: false
cadence: "continuous"
gates: ["Ascension quest", "zone flight rules", "out of combat"]
currencies: ["Flight Power", "Kinah", "Wind Elixir"]
region_verified: ["KR", "TW"]
patch: "2026-07-01 (Chapter 1) / Season 3"
confidence: medium
tags:
  - aion2/progression
  - aion2/wings-and-flight
---

# Flight and Traversal

> **In one sentence:** Flight Power is a stamina pool rather than a countdown
> timer, it grows permanently with every pair of wings you own and every
> enhancement level you buy, and the technique you use to spend it matters about
> three times as much as the size of the pool.

## Why it matters

Flight is not a progression system in the sense that it grants combat stats, but
it is a **progression multiplier**, and in AION 2 it is a very large one:

- The open world is dramatically larger than the original AION. Almost every
  collection route in the game — [[Hidden Cubes]] (172 locations: 102 in
  Verteron, 69 in Altgard, 1 in Reshanta), [[Empyrean Traces and Feathers]],
  [[Kibelisks and Map Registration]], gathering nodes for Pure Odyle — is
  distributed vertically across cliffs, towers and floating islands. Ground
  movement is not a substitute.
- Those same routes are the acquisition routes for wings themselves, so flight
  and wing collection are a positive feedback loop: more wings means more Flight
  Power means faster cube and trace routes means more wings.
- In the Abyss, Flight Power is a survival stat. Running out mid-escape is a
  common death.

The important insight is that Flight Power is spent, not counted down. Two
players with identical Flight Power can travel distances that differ by a factor
of three depending on technique.

## How it works

### Flight Power (비행력)

Flight Power is the flight stamina resource. It drains while your wings are
deployed, drains fastest while dash-flying, and regenerates while you are
grounded or gliding. It replaces the original AION's fixed flight-time seconds.

English coverage sometimes calls this the "Flight Meter" or "Glide Gauge". The
Korean term is 비행력, and Flight Power is the term used in the wing tooltips, so
that is the term this vault uses. See [[Glossary KR TW EN]].

### Controls

| Action | Default input |
| --- | --- |
| Deploy / retract wings | V |
| Flight dash | Shift while flying |
| Glide | Spacebar while airborne or falling |
| Dive | Hold W while gliding |

Korean guides recommend rebinding the flight toggle from V to a mouse button,
because the core technique requires tapping it constantly.

### The wing-fold technique (날접컨)

This is the single highest-value skill in the chapter. Flight dash gives a burst
of momentum; keeping your wings open after that burst is what drains the bar.
So you take the burst and immediately fold the wings, coast on the momentum, and
repeat.

1. Press **V** to deploy.
2. Aim roughly **30–40 degrees upward** in your travel direction (about **70
   degrees** if you need altitude) and press **Shift** to dash.
3. Press **V** again immediately to fold the wings.
4. Coast until the momentum decays.
5. Repeat.

Reported result: roughly **one third** of the Flight Power consumption of
sustained flight, and close to **three times** the distance for the same bar.
Flight Power also regenerates slightly during the folded phase, so a practised
player can chain almost indefinitely with a Wind Elixir or two.

Confidence medium — this comes from one detailed Korean guide, but the same
technique is described independently in English coverage as the "momentum
trick", "glide cancel" and "fast-glide", and the underlying physics (dive
converting altitude into velocity, glide cancel preserving momentum) are
consistent across all of them.

The same input pattern is a PvP tool: an abrupt fold produces an immediate stall
and vertical drop, and re-deploying with a strafe produces the sharp V-shaped or
Z-shaped path that breaks an opponent's camera lock.

### Raising Flight Power

| Method | Gain | Confidence |
| --- | --- | --- |
| Acquire a new pair of wings | +200, permanent, retention effect, no need to equip | Medium — two Korean blogs |
| Enhance any owned pair | +10 per level, permanent, all grades | High — Purple Lounge and Inven |
| Accessory Soul Imprint options | Roughly +15% with Flight Power rolled on a full Decurion accessory set | Medium — single Korean guide |
| Ride a tall mount before taking off | Reduced consumption, because you start higher | Low — single Korean guide, mechanism plausible |

The wings route dominates. Seventeen Unique pairs owned and taken to +5 is
+3,400 from ownership plus +850 from enhancement, which is a different game from
a fresh Daeva with two pairs.

Note the interaction with [[Soul Imprint and Soul Binding]]: Flight Power is a
rollable accessory option that competes with combat stats. It is a comfort
choice, not a power choice, and Korean guides describe it as optional.

### Restoring Flight Power

| Item | Restore | Source |
| --- | --- | --- |
| Wind Elixir (바람의 비약) | 1,000 instantly | Alchemy crafting bench in any town, exchange, achievement rewards |
| Superior Wind Elixir (상급 바람의 비약) | 2,000 instantly | Alchemy crafting; usable from level 10 |
| Grounded regeneration | Passive | Free |
| Updrafts and wind paths (바람길) | Refills and carries you | Free, placed by the world designers |
| Flight rings | Instant restore | Reported in Altgard and Verteron; confidence low, single low-trust English source |

Keep a Wind Elixir in the quickslot permanently. The two situations Korean
players name are reaching a Kibelisk that sits just out of range, and escaping
in the Abyss.

### Zone rules

This is the area where sources conflict most, so read the confidence column.

| Rule | Detail | Confidence |
| --- | --- | --- |
| Open world | Free flight almost everywhere, unlike the original AION's designated flight zones | High — repeated across all coverage and stated by the developers |
| In combat | Wings cannot be deployed while in combat | Medium — English coverage, not seen in a patch note |
| Dungeons | No free flight inside dungeons, but gliding and hovering remain usable and are part of boss mechanics and route-finding | Medium — hands-on preview reporting plus dungeon guides that describe glide segments |
| Abyss lower layer (Chaotic Ereshanta, Lower) | Full flight | Medium |
| Abyss mid layer (Chaotic Ereshanta, Mid), added in Season 3 | **No flight.** Gliding, walking and running only. The four new monster islands are reached by wind paths and updrafts. | Medium — the no-fly rule comes from lower-trust English sites, but the 2026-05-27 patch note independently confirms the islands are reached "via a nearby wind path" |
| Arenas | No flight | Low — single low-trust source |

The mid-layer no-fly rule is the most interesting design decision in the
chapter. It exists specifically to stop players from escaping vertically out of
PvP, and it turns glide skill and terrain knowledge into the deciding factor
instead. See [[Arenas Sieges and Seasons]] and [[PvP Progression]].

### Gliding, water and mounts

- Gliding descends slowly and covers distance, costs far less Flight Power than
  powered flight, and can be initiated from a jump, from a fall or from flight.
- Diving converts altitude into velocity; the resulting speed carries into the
  next glide.
- Updrafts refill the bar and can push you above the normal ceiling.
- Mounts and flight are complementary rather than exclusive: mounts are the
  ground-speed answer, flight is the vertical answer, and starting a flight from
  a tall mount is claimed to save Flight Power. See [[Mounts]].
- Underwater and water traversal exist as a distinct movement mode in AION 2's
  movement kit, but I could not verify any interaction between swimming and
  Flight Power. Flagged as an open question.

## Unlock and gates

Flight unlocks at ascension: level 5 for Elyos via "Fledgling Wings", level 6 for
Asmodians via "Spread Your Wings", both by talking to Asahr in the Ascension
Subspace. There is no separate flight skill or licence. Wind Elixirs are usable
from level 10. See [[Level and Ascension]].

## Inputs: currencies, materials, sources

| Input | Feeds | From |
| --- | --- | --- |
| Wings owned | Base Flight Power | [[Wings Acquisition]] |
| Enhancement Stone, Tuning Stone, Kinah | +10 Flight Power per step | [[Wings Enhancement]] |
| Alchemy materials | Wind Elixirs | [[Crafting]] |
| Accessory Soul Imprint rolls | Percentage Flight Power | [[Soul Imprint and Soul Binding]] |
| Practice | The 3× multiplier from the wing-fold technique | Free |

## Progression path

1. **Ascend and learn V–Shift–V immediately.** Technique is free and it is worth
   more than any amount of Flight Power you will accumulate in the first month.
2. **Craft and stock Wind Elixirs.** They are cheap alchemy items and they
   convert "I cannot reach that" into "I can".
3. **Collect wings relentlessly.** Every pair is +200 permanently, whether you
   wear it or not.
4. **Enhance the whole collection to +5.** +10 Flight Power per step across
   dozens of pairs is a large cumulative pool, and you were going to do this for
   the item level anyway.
5. **Build a repeatable Hidden Cube and Empyrean Trace route.** This is where
   the traversal investment converts back into wings, statues and materials.
6. **Consider Flight Power on accessory Soul Imprints only once combat stats are
   settled.**

## Priorities and breakpoints

- **Technique before stats.** A player with the wing-fold technique and two pairs
  of wings out-travels a player with twenty pairs who holds Shift.
- **Wind Elixirs before Soul Imprint rolls.** A consumable that restores 1,000 or
  2,000 is a bigger practical gain than a 15% larger bar.
- **Flight Power on accessories is a comfort purchase.** It reduces ring-recall
  trips and makes the Abyss pleasant, but it costs a combat-stat roll.
- **Do not build for Flight Power in the mid-layer Abyss.** Flight is disabled
  there; glide skill and wind-path knowledge are what matter.

## Costs and math

| Item | Cost | Value |
| --- | --- | --- |
| Wing-fold technique | Free | ~3× effective distance per bar |
| Wind Elixir | Alchemy materials | +1,000 Flight Power, instant |
| Superior Wind Elixir | Alchemy materials | +2,000 Flight Power, instant |
| One new pair of wings | Varies | +200 permanent |
| One enhancement step | 800–6,000 Enhancement Stones, 2–12 Tuning Stones, 240,000–1,500,000 Kinah | +10 permanent, plus item level and a retention stat |

Flight Power is therefore almost free as a by-product: you are already buying
enhancement levels for item level and retention stats, and the +10 per step
arrives regardless. Nobody should be buying enhancement levels *for* Flight
Power.

## Traps and mistakes

- **Holding Shift.** Sustained dash flight burns roughly three times the Flight
  Power per unit distance compared with the fold technique. This is the single
  most common mistake and it is the one that gets people killed in the Abyss.
- **No Wind Elixir in the quickslot.** The item exists precisely for the moment
  you are 200 Flight Power short of a Kibelisk or a cliff-top cube.
- **Assuming you can always fly out of trouble.** Mid-layer Reshanta removes
  flight entirely, and wings cannot be deployed in combat.
- **Rolling Flight Power on accessories early.** It competes with combat stats
  on the same rolls and it is a quality-of-life stat, not a power stat.
- **Ignoring wind paths.** They are free travel and free Flight Power, and in the
  Season 3 mid-layer they are the *only* way to reach the new islands.
- **Treating flight as separate from progression.** The compounding loop —
  traversal speed → collection throughput → more wings → more Flight Power — is
  one of the strongest early-game accelerators in the game.

## Global launch notes

- Free open-world flight is a launch feature and a headline marketing point, so
  it will be present at global launch.
- The mid-layer Abyss no-fly zone arrived with Season 3 and is described by
  commentators as an experiment. It may not be present at global launch, and
  NCSoft may modify it based on KR/TW feedback.
- Wing enhancement, and therefore the +10 Flight Power per level channel, may
  not be in the global launch build. The +200 per acquired pair channel is
  launch-era and will be.
- Key bindings and the English names for Flight Power, Wind Elixir and the glide
  controls are unverified for the global client.

## Open questions

- [ ] What is a character's base Flight Power at ascension, and what does the bar
      cap at? Settled by a character sheet screenshot.
- [ ] How much distance or how many seconds does 1,000 Flight Power actually buy?
      Everything here is relative; there is no absolute conversion published.
- [ ] Is the +200 per acquired pair figure exact, and is it constant across
      grades?
- [ ] Confirm that wings cannot be deployed while in combat, and whether that is
      a combat-flag rule or a cooldown.
- [ ] Full list of no-fly zones. Only mid-layer Reshanta, dungeon interiors and
      arenas are attested, and only two of those confidently.
- [ ] Does swimming or underwater movement consume or interact with Flight Power?
- [ ] Do the "green flight rings" in Altgard and Verteron exist as described, and
      what exactly do they restore?
- [ ] Does the tall-mount launch trick measurably reduce Flight Power
      consumption, or is it only the free altitude?
- [ ] What is the Flight Power regeneration rate, grounded versus gliding versus
      wings-folded mid-air?

## Sources

- [아이온2 비행력 올리는법 총정리｜비행력 소모 줄이는 조작 방법](https://redwendy.com/archives/2724) — Korean guide blog, 2026 — the wing-fold (날접컨) technique with exact inputs and angles, the ~1/3 consumption and ~3× distance figures, the rebind recommendation, the four ways to raise Flight Power, the ~15% figure for a fully rolled Decurion accessory set, and the tall-mount tip.
- [비행력이 부족할 때는 '바람의 비약'을 쓰자!](https://www.inven.co.kr/board/aion2/6444/266) — Inven KR community — Wind Elixir restores 1,000 Flight Power instantly, craftable at any town alchemy bench, and its use case of reaching high Kibelisks.
- [상급 바람의 비약 (각인)](https://questlog.gg/aion-2/ko/db/item/530116014) — questlog.gg item database — Superior Wind Elixir restores 2,000 Flight Power, usable from level 10.
- [[AION2] 아이온2 시즌3 효율적인 날개 강화 가이드](https://lounge.plaync.com/feed/70658?country=KR&locale=ko-KR) — Purple Lounge (NCSoft community), KR, 2026-06-04 — +10 Flight Power per enhancement level on every wing grade.
- [아이온2 날개 제작 완벽 가이드 2026](https://alias007.tistory.com/776) — Korean blog, 2026-05 — the +200 Flight Power per acquired pair rule and the claim that Flight Power persists when you swap wings.
- [UPDATE: May 27, 2026 Patch Notes](https://aion2t.com/news/25) — aion2t, 2026-05-27 — the four new Abyss mid-layer islands "accessible via a nearby wind path", which independently supports the glide-and-wind-path traversal model for that zone.
- [Aion 2: The New Abyss Map - Chaotic Middle Reshanta](https://www.mmoexp.com/News/aion-2-the-new-abyss-map-chaotic-middle-reshanta.html) — mmoexp, 2026 — **low-trust seller site, lead only**; the source of the explicit "Middle Reshanta permits no flying" claim. Corroborated in direction by the patch note above and by a forum write-up, so recorded at medium confidence.
- [AION 2: NC Wants to Do a Lot Better With the Western Release](https://guided.news/en/opinion/aion-2-nc-wants-to-do-a-lot-better-with-the-western-release/) — guided.news hands-on preview, 2026 — first-hand confirmation that you cannot freely fly inside dungeons but that gliding and hovering remain usable to dodge attacks.
- [Aion 2 Conquest: Bakron's Sky Island Guide](https://vortexgaming.io/en/postdetail/608955) — Vortex Gaming, English translation of a KR video guide, 2026 — a worked example of glide segments, wind paths and "turn on flight" moments being load-bearing dungeon mechanics.
- [Aion 2 Has All The Tools To Soar Above Expectations](https://www.thegamer.com/aion-2-wings-customization-flight-focused-mmorpg/) — TheGamer hands-on preview, 2026 — wind-stream travel used as in-dungeon fast travel, and the developer framing that collecting more wings increases movement speed.
- [Complete Map for Aion 2 Hidden Cubes](https://talkfever.com/blogs/107687/Complete-Map-for-Aion-2-Hidden-Cubes) and [AION 2 Tools, Database, Builds & DPS Meter](https://aion2hub.com/) — 2026 — the 172 Hidden Cube locations (Verteron 102, Altgard 69, Reshanta 1) and the observation that cube hunting depends on aerial scouting.
- [Aion 2 Flying Walkthrough: How to Fly](https://www.u4n.com/news/aion-2-flying-walkthrough-how-to-fly.html) and [AION 2 Aerial Combat Guide](https://www.u4n.com/news/aion-2-aerial-combat-guide-master-glide-control-and-sky-battle-tactics.html) — u4n, 2026 — **low-trust seller sites, leads only**; the default keybinds, the "cannot use wings in combat" claim, the flight-rings claim and the glide-cancel PvP description. Each is flagged inline with its confidence.
- [Aion Classic Flight and Gliding](https://eip.gg/aion-classic/guides/flight-and-gliding/) — EIP Gaming — original-AION reference used only to establish what AION 2 changed (fixed one-minute flight timer and designated flight zones, both replaced).
