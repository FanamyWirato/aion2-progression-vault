---
chapter: "07 Pantheon"
system: Lord Stats (Pantheon Stats)
type: progression-system
unlock: "as soon as any Pantheon decoration is placed"
account_wide: false
cadence: "continuous"
gates: ["none beyond owning decorations"]
currencies: []
region_verified: ["KR", "TW"]
patch: "KR Season 1 (2025-11-19) tooltips, cross-checked against Season 3 (2026-04-08) guides"
confidence: medium
tags:
  - aion2/progression
  - aion2/pantheon
---

# Lord Stats (Pantheon Stats)

> **In one sentence:** ten Lord domains, each named after one of the Lords of
> Atreia, each capped at 200 points, each converting linearly into two
> percentage-based combat stats — and they are the only stat layer in the game
> that multiplies your whole sheet rather than adding to part of it.

## Why it matters

Lord stats are the shared currency of several systems. The [[Pantheon]] is the
largest source, [[Arcana]] is the second, [[Empyrean Traces and Feathers]]
provides a large one-off block, and some bracelets add more. Because they all
feed the same ten pools against the same cap, you cannot plan any one of them
in isolation. A Korean player pushing for the last few percent of a stat sheet
put it bluntly: the Pantheon and Arcana are the only two real levers on Lord
stats, so Arcana should be chosen for the Lord domains you need rather than for
its set bonus.

The reason they matter more than their small numbers suggest:

- They are **percentage modifiers**, so they keep pace with gear growth instead
  of being diluted by it.
- They are **permanent and free** once acquired. There is no upkeep and no
  failure chance.
- They **do not appear in Combat Power**. The in-game name for what players
  call Combat Power is item level, and Lord stats do not raise it. This makes
  the entire layer invisible to gear checks, which is both a trap (people skip
  it) and an edge (people who do not skip it are stronger than their number
  suggests). See [[Item Level vs Combat Power]] and [[Stat Reference]].

## How it works

### Terminology

Korean sources call these 주신 스탯 (main-god stats) or 주신력 (main-god power).
Chinese and Taiwanese guides use 主神力. English sources are inconsistent and
use "Pantheon stats", "Lord stats", "deity stats" and "deity-domain points"
interchangeably. This vault uses **Lord stats**. Each domain is displayed in
the client as the domain name followed by the Lord's name in brackets, for
example 지혜[루미엘] = Wisdom [Lumiel]. See [[Glossary KR TW EN]].

### The ten domains

Transcribed from the in-game Lord effect tooltips by a Korean first-hand guide
and independently reproduced by a Korean stat-summary blog and an English
stats guide. Confidence high on the pairings, with one flagged exception.

| Domain | Lord | KR | Effect 1 | Effect 2 |
| --- | --- | --- | --- | --- |
| Wisdom | Lumiel | 지혜[루미엘] | Smite chance up | Spirit (MP) consumption down |
| Time | Siel | 시간[시엘] | Combat speed up | Smite Resist up |
| Illusion | Kaisinel | 환상[카이시넬] | Cooldown reduction | Endurance Penetration up |
| Destruction | Zikel | 파괴[지켈] | Attack power up | Perfect Resist up |
| Death | Triniel | 죽음[트리니엘] | Critical hit up | Regeneration Penetration up |
| Justice | Nezekan | 정의[네자칸] | Defence up | Perfect proc chance up |
| Freedom | Vaizel | 자유[바이젤] | Accuracy up | Evasion up |
| Life | Yustiel | 생명[유스티엘] | Max HP up | Regeneration proc chance up |
| Fate | Marchutan | 운명[마르쿠탄] | Spirit (MP) up | Endurance proc chance up |
| Space | Israphel | 공간[이스라펠] | Move speed up | Block chance up |

Aliases and conflicts worth knowing:

- **Fate** is also translated Destiny. One Korean video summary labels this
  domain 정신력 (Spirit) instead of 운명, which is a translation slip, not a
  different stat.
- **Death**: one English secondary source lists Death as granting Critical Hit
  *Resist* rather than Critical Hit. Every first-hand Korean source and the
  in-game tooltip transcription say Critical Hit. Take Critical Hit.
- **Smite** (강타) is sometimes rendered "strike", "impact" or "double hit".
  **Perfect** (완벽) is sometimes rendered "perfection". **Endurance** (철벽) is
  sometimes rendered "iron wall". These are the same stats.

### What the second-order stats actually do

The domain effects only make sense if you know the underlying combat stats,
which live in [[Stat Reference]]. The short versions:

- **Smite (강타)**: a proc that roughly doubles the damage of the hit. Critically,
  Smite can itself critically strike, so a Smite that crits reportedly lands
  around four times normal damage. This compounding is why Smite is treated as
  the tier-zero damage stat at endgame.
- **Perfect (완벽)**: a proc that pushes the roll toward the weapon's maximum
  attack value, so it raises effective weapon damage. Countered by Perfect
  Resist.
- **Endurance (철벽)**: a proc that halves incoming damage. Countered by
  Endurance Penetration.
- **Regeneration**: heals based on damage taken. Countered by Regeneration
  Penetration.
- **Combat speed**: raises both attack and cast speed, so it is a
  near-universal DPS and healing throughput stat.
- **Cooldown reduction**: reported cap of 60 percent from all sources combined,
  confidence medium, single secondary source.

### The conversion

Points are summed per domain, and each point raises both linked combat stats.
The rate is disputed:

| Claim | Rate | Source quality |
| --- | --- | --- |
| 0.1 percent per point per linked stat | A 45-point Death difference read as critical hit +4.5 percent and regeneration penetration +4.5 percent in the in-game Lord effect panel | High. First-hand, read off the client while comparing two colossi. |
| 0.2 percent per point, for Wisdom to Smite | "Every 5 Wisdom adds 1 point of Smite chance"; 45 Wisdom stated as 9 percent Smite | Medium. Chinese endgame guide, internally consistent, and independently echoed by a Korean video summary that gives 0.2 percent per point for all domains. |
| "Each point gives +20 internal units across 2 combat stats per domain" | aion2hub database tooltip text | Medium. Client-derived but expressed in internal units with no published conversion to percent. |

Working assumption for this vault: **0.1 percent per point per linked stat**,
with the Wisdom-to-Smite rate possibly double that. Both readings agree the
relationship is linear with no diminishing returns inside the cap, which is the
part that matters for planning. Repeat this caveat wherever you use a number.

### The cap

Each domain caps at 200 points, after which further points in that domain stop
converting. Sourced from the aion2hub item database tooltip; confidence medium,
single source. At 0.1 percent per point that is a 20 percent ceiling per linked
combat stat, which is very large and not reachable from the Pantheon alone.

The practical consequence is that the cap is not a real constraint on a
Pantheon build. A Season 1 endgame Pantheon reaches roughly 45 in its best
domains. The cap only becomes relevant once Pantheon, Arcana, Traces of the
Lord and bracelets stack on the same domain, which is why Time and Space are
the first domains to approach it: the Traces of the Lord collection gives all
domains +20 and Space and Time an extra +20 on top.

## Unlock and gates

None beyond owning decorations. The conversion is automatic and applies the
moment a decoration is placed. There are no points to allocate, no reset cost
and no respec currency.

## Inputs: currencies, materials, sources

| Source | Which domains | Rough magnitude | Note |
| --- | --- | --- | --- |
| Pantheon colossus | Justice, Time, Destruction | 35–45 per domain | Only realistic source of Destruction |
| Pantheon statues | Freedom, Death, Space in Season 1 | 8–12 per domain, 4 slots | Cannot give Wisdom |
| Pantheon artworks | Wisdom, Illusion, Life, Fate | 3–5 per domain, 12 slots | Only realistic source of Wisdom and Illusion |
| [[Arcana]] | Varies by card | Not documented here | Second-largest lever; choose cards for domains, not just set bonuses |
| [[Empyrean Traces and Feathers]] | All ten | +20 to all, plus +20 more to Space and Time at the 160-trace milestone | One-off collection; 200 traces are documented per Abyss region set |
| [[Accessories]] bracelets | Multiple domains at once | Not documented here | Reported to roll several Lord domains simultaneously; confidence low, single secondary source |

The domain-to-slot restriction is the most important planning fact on this
page: **Wisdom and Illusion come almost entirely from artworks, and Destruction
comes almost entirely from the colossus.** If you want Wisdom you must do the
slow artwork grind; there is no shortcut through the statue slots.

## Progression path

1. Place every decoration you own to establish a baseline in all ten domains.
2. Complete the Traces of the Lord collection for the flat +20 to everything.
   This is the cheapest Lord stat in the game per hour spent.
3. Secure the colossus, which locks in Justice, Time and Destruction.
4. Fill statues with the best Death and Space pairs available.
5. Grind artworks toward Wisdom and Illusion for a damage build, or Life and
   Fate for a support build.
6. Align Arcana selections with whichever domains your Pantheon cannot reach.

## Priorities and breakpoints

### Why Wisdom-centred setups dominate PvE

The argument runs in three steps:

1. **Smite is multiplicative and compounding.** It roughly doubles a hit, and
   because it can itself crit, a critical Smite lands around four times normal
   damage. Nothing else in the Lord stat list touches final damage that hard.
2. **Wisdom is the only meaningful source of Smite chance.** No other Lord
   domain grants it, and Smite is otherwise hard to acquire.
3. **Its counter-stat is rare in PvE.** Smite Resist comes from Time, which
   players stack for PvP. Boss encounters do not stack Smite Resist the way
   players do, so the proc rate you buy is the proc rate you keep.

Attack power is deliberately deprioritised despite being the obvious choice.
Korean guides point out that attack power is already abundant from breakthrough
progression (see [[Breakthrough]]), so spending scarce Pantheon slots on
Destruction has poor marginal value beyond what the colossus gives for free.

### Per-role priority ordering

**PvE damage dealer**

Wisdom > Illusion > Death > Time > Life > Space > Destruction > Fate > Justice > Freedom

Wisdom for Smite, Illusion for cooldown reduction that compounds with
everything, Death for critical hit which multiplies into Smite. Time is high
but comes free on the colossus. Freedom is last because accuracy overflows in
most endgame PvE content.

**PvE healer and support**

Life > Fate > Illusion > Time > Justice > Wisdom > Space > Death > Destruction > Freedom

Life for the HP pool that lets you survive mechanics, Fate for spirit and the
Endurance proc, Illusion and Time for throughput. A Taiwanese healer guide is
explicit that a survivability-first healer should not bother stacking Wisdom.

**PvE tank**

Justice > Life > Space > Fate > Time > Illusion > Death > Wisdom > Destruction > Freedom

Justice for defence and the Perfect proc, Life for the HP pool, Space for block
chance and positioning, Fate for the Endurance proc that halves damage.

**PvP and sieges**

Time > Illusion > Freedom > Life > Justice > Space > Death > Wisdom > Destruction > Fate

Time first, unanimously, across Korean sources. Combat speed is unconditional
where Smite is not, and Smite Resist blunts enemy Wisdom builds. Freedom
recovers value here because opposing players do stack evasion. Wisdom drops
because opponents stack the counter.

**Farming and open world**

Space > Time > Illusion > Life, then whatever. Move speed dominates time-per-run
in open-world and collection content; see [[Flight and Traversal]].

### Breakpoints

- The first Unique colossus. Adds a third domain at full value.
- The Traces of the Lord 160 milestone. Flat +20 to all ten domains, plus +20
  more to Space and Time.
- Six Wisdom-bearing artworks. Roughly the point at which Smite becomes visibly
  frequent in play rather than a statistical footnote.

## Costs and math

- Linear conversion, no diminishing returns observed inside the 200 cap.
- At 0.1 percent per point, 45 points in a domain is 4.5 percent on each of its
  two linked stats, so 9 percentage points of combined stat value from one
  colossus domain.
- A complete Season 1 damage Pantheon at roughly Wisdom 45, Illusion 45,
  Justice 45, Time 45, Destruction 45, Death 40, Space 40, Life 27, Fate 15,
  Freedom 12 totals about 359 points, or roughly 36 percentage points spread
  across twenty combat stats. Small per stat, large in aggregate, and free.
- Cooldown reduction is reported to cap at 60 percent from all sources
  combined; confidence medium, single secondary source. Evasion is reported to
  cap at 50 percent and normal critical hit chance at 80 percent, same
  confidence.

## Traps and mistakes

- Optimising for the Combat Power number. Lord stats do not raise it, so
  optimising for it will make you skip this system entirely.
- Stacking Wisdom for PvP. Time is the counter-stat and PvP players stack it.
- Stacking Freedom at PvE endgame. Accuracy overflows against most bosses;
  check your own accuracy against the specific encounter before spending slots.
- Picking Arcana purely for set bonuses. A Korean spec-pushing player argues
  the Lord domains on the cards matter more, since Arcana is one of only two
  real sources.
- Reading percentage figures from secondary English sources without checking
  the rate. The 0.1 versus 0.2 percent question is unresolved and doubles or
  halves every derived number.
- Assuming domains are interchangeable across slot classes. Statues cannot give
  Wisdom and artworks cannot give Destruction.

## Global launch notes

- The ten-domain structure with its Lord names is core to the design and will
  be present at global launch.
- English domain names in the global client are not yet confirmed. "Destiny"
  and "Fate" both appear in English-language sources for 운명, and the global
  client may use either. Same risk for Smite, Perfect and Endurance.
- The conversion rate is a balance value and NC has adjusted stat caps at
  patch boundaries before, including raising pet attack and defence caps from
  100 to 120 percent in Season 3. Treat 0.1 percent per point as a KR Season 1
  to Season 3 figure.
- The 200-point cap should hold, but the systems that stack toward it will be
  partly absent at launch, so no global player will be near it for months.

## Open questions

- [ ] The true point-to-percentage rate, and whether it differs per domain.
      Would be settled by a screenshot of the Lord effect detail panel at two
      known point totals in the same domain.
- [ ] Whether the 200-point cap is confirmed anywhere besides the aion2hub
      tooltip, and whether it counts Pantheon-only points or all sources.
- [ ] The exact Smite damage multiplier, and whether a critical Smite is
      exactly four times or approximately four times normal damage.
- [ ] Whether Wisdom's spirit-consumption reduction is a flat percentage or
      scales differently from its Smite component.
- [ ] How much Lord stat a full Arcana set actually contributes, which decides
      whether the cap is reachable.
- [ ] Whether bracelets really roll multiple Lord domains, and at what
      magnitude.
- [ ] The English domain names in the global client.

## Sources

- [아이온2 만신전 공략 — 정보의 호수](https://joinfo.tistory.com/41) — KR, first-hand. Verbatim transcription of all ten in-game Lord effect tooltips with Lord names, which is the backbone of the domain table.
- [충전권 추천: 악몽 도전권 (지켈의 사념체 파밍 + 만신전 세팅)](https://www.inven.co.kr/board/aion2/6444/565) — KR, 2025-12-01. The 0.1 percent per point reading from the Lord effect panel, the worked 45-point Death example, the statement that Lord stats do not raise item level, and the argument that Pantheon and Arcana are the only two real sources.
- [아이온2 만신전 스탯 총정리 — Naver blog](https://m.blog.naver.com/zovo3/224255772536) — KR, 2026. Independent reproduction of the ten-domain table with the same pairings, plus a role grouping of dealer, tank and balance domains.
- [【永恒之塔2】主神殿输出毕业搭配](http://news.17173.com/content/12162025/052013463.shtml) — CN, 2025-12-16. The "5 Wisdom = 1 Smite chance" rate, the description of Smite doubling damage and crit-Smite quadrupling it, the Endurance and Regeneration explanations, and the Wisdom > Illusion > Life > Fate ordering.
- [무과금 유저를 위한 주신 스탯 200 이상 확보 방법](https://vortexgaming.io/postdetail/607387) — KR video guide in translation. The 0.2 percent per point claim, the Traces of the Lord +20 to all domains with +20 extra to Space and Time, and the six-route list for accumulating Lord stats.
- [Artwork: Eternal Gartua — AION 2 Item Database](https://aion2hub.com/database/items/514310111) — client-extracted data. The 200-point domain cap and the two-combat-stats-per-domain conversion statement.
- [Aion 2 Stats: How to Build Your Character for Global Launch](https://www.mmoexp.com/News/aion-2-stats-how-to-build-your-character-for-global-launch.html) — EN, low-trust commercial site, used for leads only. Its ten-domain table matches the Korean tooltips on nine of ten rows, which is useful corroboration; its Death row is wrong. Also the sole source for the 60 percent cooldown, 50 percent evasion and 80 percent critical caps, which are therefore flagged medium confidence.
- [Aion 2 Man Pantheon Core Stat Setting Guide](https://vortexgaming.io/en/postdetail/628306) — KR video guide in translation. Wisdom as the tier-one stat, the argument that attack power is covered by breakthrough, and the Time-for-PvP recommendation.
- [《AION2》治癒星養成攻略](https://jisu.tw/aion2-治癒星養成攻略/) — TW healer guide. The support-role ordering and the explicit advice not to stack Wisdom on a survivability healer.
- [어비스 하층 주신의 흔적 200/200](https://www.inven.co.kr/board/aion2/6444/634) — KR, Inven. Establishes the scale of the Traces of the Lord collection, 200 traces per Abyss region set.
