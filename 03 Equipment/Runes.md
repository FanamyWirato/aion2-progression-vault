---
chapter: "03 Equipment"
system: Runes
type: progression-system
unlock: "Present from launch. Two dedicated rune slots on the character sheet"
account_wide: false
cadence: continuous
gates: ["Rune of Devotion costs roughly 5,000 Abyss Points", "enhancement destroys the rune on failure", "supply is capped by region quests, Daeva Pass and the Nightmare shop"]
currencies: ["Abyss Points", "Rune enhancement materials", "Phantasmal Fragments"]
region_verified: ["KR", "TW"]
patch: "KR live as of 2026-09-06; both runes present at the 2025-11-19 launch"
confidence: medium
tags:
  - aion2/progression
  - aion2/equipment
  - aion2/pvp
---

# Runes

> **In one sentence:** two extra equipment slots holding a PvE rune and a PvP
> rune, each worth roughly 40 item level unenhanced, and the **only** gear in
> AION 2 that is permanently destroyed when enhancement fails.

## Why it matters

Runes are cheap item level. An unenhanced rune contributes about **40 item
level**, which at the early-endgame Combat Power range of 1,100–1,300 is a
larger single jump than most gear upgrades available at that point, and it costs
nothing but a region quest. Every Korean beginner guide lists slotting both runes
among the first things to do at cap.

They matter for a second, sharper reason: **runes break.** Failed rune
enhancement does not reset the level, does not consume a protection charge, and
does not downgrade the item. It **destroys the rune.** No other equipment in the
game does this — [[Enchanting]] failures degrade or stall, [[Breakthrough]]
failures consume materials. Runes are the one place where a bad click removes the
item from your inventory. That single rule dictates the entire strategy below.

## The two runes

| Rune | Korean | Focus | Primary source |
| --- | --- | --- | --- |
| **Rune of Clash** | 격돌의 룬 | **PvE** | Region quests, Daeva Pass, Nightmare exchange shop |
| **Rune of Devotion** | 전념의 룬 | **PvP** | **~5,000 Abyss Points** from the Abyss vendor |

Both slots exist on every character from the start; there is no unlock quest for
the slots themselves. Slot the Clash rune for PvE content and the Devotion rune
for Abyss and arena play. Korean guides treat swapping between them as routine
rather than as a commitment.

The Devotion rune's Abyss Point price ties it to [[Abyss Points and Ranks]] and
makes it one of the few genuinely useful early AP purchases — most of the rest of
that vendor's stock is gear you will replace.

**Confidence:** high that both runes exist and are PvE/PvP-split; **medium-high**
on the 5,000 AP figure, which comes from community guides rather than a database
page.

## How enhancement works

Rune enhancement is its own track, separate from [[Enchanting]] on ordinary gear.

| Rule | Behaviour |
| --- | --- |
| Failure result | **The rune is destroyed.** Not downgraded, not reset — gone |
| Safe range | Low levels are commonly described as guaranteed or near-guaranteed |
| Where risk starts | **+2** is the level at which community rate tables begin, implying +1 is free |
| Materials | Duplicate runes and enhancement materials from the same supply channels |
| Protection | No protection item is documented for runes |

### The community rate chain — treat with suspicion

The figures circulating in the community for success rates from **+2 onward**
are:

| Step | Reported rate |
| --- | --- |
| +2 | 80% |
| +3 | 66% |
| +4 | 50% |
| +5 | 33% |
| +6 | 25% |
| +7 | 20% |

**Flag this as low confidence.** I could not locate an NC-published probability
page for rune enhancement in four research cycles across `lounge.plaync.com`,
the Korean patch archive, `aion2hub`, `questlog.gg` and the Korean gaming press.
Korean law requires probability disclosure for paid random elements, and NC does
publish probability tables for gacha and enhancement systems, so **such a page
very likely exists** — I simply did not find it, and it is the highest-value
missing citation in this note.

Two reasons the numbers above are still worth writing down. First, they are
internally plausible: a smooth decay from 80% to 20% across six steps matches how
AION 2's other enhancement curves behave. Second, the *expected value* they imply
matches observed behaviour — the cumulative chance of reaching +7 from +1 on the
chain above is about **1.3%**, which is consistent with how rarely high-level
runes are reported in Korean threads.

If you take one thing from this section: **the numbers may be wrong, but the
shape is right.** Rune enhancement is a lottery with total loss on failure, and
it becomes a bad bet quickly.

## Unlock and gates

| Thing | Requirement |
| --- | --- |
| Rune slots | Present from the start, no unlock |
| Rune of Clash | A region quest reward; also Daeva Pass and the Nightmare shop |
| Rune of Devotion | ~5,000 Abyss Points |
| Enhancement | Spare runes as material; no level gate documented |
| Enhancement risk | Begins at +2 |

## Inputs: currencies, materials, sources

| Source | Supplies | Notes |
| --- | --- | --- |
| **Region quests** | Rune of Clash | The free baseline. Do these; the rune is worth ~40 item level |
| **Daeva Pass** | Runes and rune materials | The battle-pass track; both free and paid tiers |
| **[[Nightmare Mode]] exchange shop** | Runes and rune materials | Phantasmal Fragments, competing with Soul Codex: Reset and Potential materials |
| **Abyss vendor** | Rune of Devotion, ~5,000 AP | See [[Abyss Points and Ranks]] |

The supply is **capped and slow**. There is no farmable source of runes — every
channel above is a weekly or one-off. That is the second half of why enhancement
is dangerous: you cannot replace a destroyed rune on demand.

## Progression path

1. **Do the region quests and slot a Rune of Clash.** Free ~40 item level.
2. **Buy a Rune of Devotion at ~5,000 Abyss Points** once you engage with the
   Abyss at all. Same free item level for PvP.
3. **Take both to +1.** Reported as safe.
4. **Stop.** Genuinely — for most players this is the end of the note.
5. **If and only if you have spare runes accumulating faster than you can use
   them**, push a spare to +2 or +3 and see what happens. Never push your only
   rune.
6. **Never push past +4 without a stockpile.** The reported 50% at +4 and 33% at
   +5 mean the expected number of runes consumed to reach +5 is large, and each
   failure is a total loss.

## Priorities and breakpoints

### Where free players should stop

**+1, and then stop.** This is the clearest "stop here" line in the whole
Equipment chapter and it is worth being blunt about.

The arithmetic: a rune supplies ~40 item level at +0 for free. Each enhancement
step adds a fraction of that, while the failure chance climbs toward and past a
coin flip and the penalty is the whole item. With supply capped at a few runes
per month from passes and shops, a free-to-play player who fails at +4 has thrown
away weeks of accumulation and is back to an empty slot — losing the 40 item
level they already had.

**Paid and heavy players** with rune stockpiles from Daeva Pass tiers and
Nightmare shop purchases can treat runes as a lottery ticket, which is what the
system is designed to be. Everyone else should regard rune enhancement as
content that does not exist.

### Which rune first

Clash before Devotion if you are primarily PvE, and it is free anyway. If you
intend to enter the Abyss at all, buy Devotion early — 5,000 AP is achievable
quickly and the rune's contribution does not scale away.

## Costs and math

- **Rune of Devotion: ~5,000 Abyss Points.** The only hard price in the note.
  Medium-high confidence.
- **Rune of Clash: free**, via a region quest.
- **Unenhanced rune value: ~40 item level.** Widely repeated in Korean community
  guides; **medium confidence**, because it presumably varies by rune grade and
  nobody states which grade the figure refers to.
- **Expected runes to reach +7 from +1**, using the unverified community chain:
  the product 0.80 × 0.66 × 0.50 × 0.33 × 0.25 × 0.20 is about **0.0044**, so
  roughly **1 attempt in 227 succeeds straight through**. Even allowing that
  failures only lose the rune from its current level rather than restarting a
  chain, the material cost of a +7 rune is in the dozens of runes. This is why
  Korean threads treat +5 and above as a whale bracket.

**All rune cost math in this note is built on unverified rates.** If NC's
published table differs, recompute.

## Traps and mistakes

- **Enhancing your only rune.** The failure destroys it and you lose the ~40 item
  level you already had. This is the mistake.
- **Assuming rune failure behaves like gear failure.** It does not. There is no
  downgrade, no reset, no protection.
- **Spending Phantasmal Fragments on runes before Soul Codex: Reset.** The
  Nightmare shop currency is contested; reroll consumables usually matter more.
- **Buying Rune of Devotion for PvE.** It is PvP-tagged. AION 2 keeps the tags
  separate everywhere — see [[Stat Reference]].
- **Forgetting to swap runes between PvE and PvP content.** The slots hold one
  each and the wrong one is dead stat weight in the wrong content.
- **Treating the community rate table as fact.** It is uncited. Verify before
  spending.

## Global launch notes

**Both runes will be present at global launch.** Rune of Clash and Rune of
Devotion, their two slots, the region-quest and Abyss-Point supply, and the
destroy-on-failure enhancement rule were all in the Korean client at the
2025-11-19 launch and in the Taiwanese client from the same date.

A Season 1 global player should expect:

- **Rune of Clash from region questing during levelling**, giving a free ~40 item
  level toward the launch gate range.
- **Rune of Devotion once they have ~5,000 Abyss Points**, which is an early Abyss
  milestone rather than a grind.
- **A very thin rune supply for the first month**, because Daeva Pass tiers and
  the Nightmare shop take time to accumulate. This makes the "stop at +1" advice
  *more* binding at launch than it is in Korea today, not less.

The one uncertainty is whether the global build includes any subsequent Korean
rebalancing of rune rates or supply. I found no rune-specific change in the
Korean patch archive between launch and 2026-09-06, so this is likely moot.
**Confidence high** on availability, **medium** on rates being unchanged.

## Open questions

- [ ] **NC's published rune enhancement probability table.** The single most
      important missing citation here. Korean disclosure rules make it likely to
      exist on `lounge.plaync.com` or in the in-game probability window. Finding
      it would upgrade this note from medium to high confidence.
- [ ] **What rune grades exist**, and whether the ~40 item level figure is for
      the common grade or a higher one.
- [ ] **The exact enhancement material.** Duplicate runes are assumed; a
      dedicated material may exist.
- [ ] **Whether +1 is truly guaranteed.** The rate chain starting at +2 implies
      it, but no source states it outright.
- [ ] **What each rune actually gives in stats**, beyond the aggregate item-level
      figure. Neither rune's stat lines are documented in the sources I reached.
- [ ] **The exact Rune of Devotion price.** 5,000 AP is community-reported; the
      Abyss vendor listing would confirm it.
- [ ] **Whether runes can be extracted or refunded** if you decide to stop. See
      [[Extraction and Refunds]].

## Sources

- [아이온2 성장에 필수인 재화 총정리](https://gametoc.hankyung.com/news/articleView.html?idxno=104206) — KR press (GameToc), launch era. **Load-bearing for supply**: lists 격돌의 룬 among essential growth materials and names region quests, Daeva Pass and the Nightmare exchange shop as its acquisition channels.
- [아이온2 인벤 — 전투력 1100~1300 구간 성장 가이드](https://www.inven.co.kr/board/aion2/6444) thread, KR, 2025-12-08. The ~40 item level value of an unenhanced rune, the advice to slot both runes early at that Combat Power range, and the destroy-on-failure warning framed as "the only gear that disappears".
- [《永恆紀元2》裝備強化系統介紹](https://www.animattoys.com/detail/zXNs9G79/) — TW, read 2026-09-06. Confirms the two rune slots existed in the Taiwanese launch client alongside the imprint system, which is the basis for the global-launch verdict.
- [AION 2 patch archive](https://aion2hub.com/updates) — KR translated, read 2026-09-06. Searched across all entries from 2025-11-19 to 2026-09-06 for rune changes; **no rune rebalance found**, which is the evidence for "rates likely unchanged since launch".
- [Aion 2 Gear Guide](https://boostroom.com/blog/aion-2-gear-guide-weapons-armor-upgrades-and-progression) — EN, boosting-shop SEO, 2026. **Lead only.** Source of the Rune of Clash / Rune of Devotion English names, the ~5,000 Abyss Point price for Devotion, and the +2 onward rate chain (80/66/50/33/25/20). The names and the PvE/PvP split are corroborated by Korean sources; **the rate chain and the AP price are not**, and are flagged low and medium-high confidence respectively in the body.
- [[Aion 2] Detailed Equipment System Guide](https://vortexgaming.io/en/postdetail/594067) — EN translation of a KR video guide, launch era. Corroborates the two rune slots at launch and the destroy-on-failure rule.

**Not found, and sought:** an NC-published rune enhancement probability page on
`lounge.plaync.com`, a rune entry in the `aion2hub` or `questlog.gg` item
databases with stat lines, and any Abyss vendor listing confirming the Rune of
Devotion price. Four search cycles in Korean (격돌의 룬, 전념의 룬, 룬 강화 확률),
Traditional Chinese and English did not surface them. This note should be
re-verified when they are.

## Related notes

[[Equipment]] · [[Accessories]] · [[Enchanting]] · [[Breakthrough]] ·
[[Soul Imprint and Soul Binding]] · [[Attunement and Option Rerolls]] ·
[[Potential Enhancement]] · [[Brooch Pendant and Seal Slots]] ·
[[Extraction and Refunds]] · [[Material Conversion]] ·
[[Gear Tiers and Sources]] · [[Stat Reference]] · [[Abyss Points and Ranks]] ·
[[Nightmare Mode]] · [[Global Launch Differences]] · [[Glossary KR TW EN]] ·
[[Home]]
