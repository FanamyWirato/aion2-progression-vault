---
chapter: "06 Wings and Flight"
system: Wings Enhancement
type: progression-system
unlock: "KR/TW live from 2026-05-27; requires owning at least one stat-bearing pair of wings"
account_wide: false
cadence: "continuous"
gates: ["wing must not be a paid, Deva Pass or ranking-reward pair"]
currencies: ["Kinah", "Enhancement Stone", "Tuning Stone (Unique)"]
region_verified: ["KR", "TW"]
patch: "2026-05-27 (Season 3, Grail of Muspel update)"
confidence: high
tags:
  - aion2/progression
  - aion2/wings-and-flight
---

# Wings Enhancement

> **In one sentence:** Every pair of wings you own — worn or not — can be pushed
> to +10 for permanent retention stats, +10 Flight Power and +1 item level per
> step, and the correct plan for almost everyone is to bring the whole
> collection to +5 rather than to push any single pair to +10.

## Why it matters

Wing enhancement is the reason the wing chapter is a progression chapter rather
than a cosmetics chapter. It was added to KR/TW on 2026-05-27 in the Season 3
"Grail of Muspel" update, announced at the 2026-05-26 developer livestream, and
confirmed in NCSoft's own English press release for that patch.

Three properties make it unusual:

- **It applies to your whole collection.** Enhancement grows the retention
  block, so a pair you never equip still pays out. Item level accumulates from
  every owned pair's enhancement level, not just the equipped one.
- **It is safe.** There is no destruction and no downgrade on failure at any
  step; a failed attempt only consumes materials.
- **It is enormously Kinah-hungry at the top.** One Unique pair from +0 to +10
  has an expected total cost of roughly 76 million Kinah once you price the
  materials. This is the single largest Kinah sink documented in this vault
  outside [[Enchanting]].

## How it works

### The ladder

Maximum enhancement is **+10**. Success rate depends on grade:

- **Rare (희귀) and Legendary (전승) wings: 100% success all the way to +10.**
  There is no gamble at all on these.
- **Unique (유일) wings: guaranteed to +3, then the rate decays.** This is where
  all the cost lives.

Every successful step, on every grade, grants:

| Gain | Value |
| --- | --- |
| Flight Power | +10 |
| Item level | +1 |
| Retention stat | One increment of that wing's specific option (see [[Wings Acquisition]]) |

### Unique-grade cost and success table

This is the shipped KR table for Unique-grade wings. The rightmost column is the
**optional** rate booster: from +4 onward you may spend extra Tuning Stones and
Kinah to add 10 percentage points of success per application.

| Step | Base success | Enhancement Stone | Tuning Stone (Unique) | Kinah | Optional +10% booster (Tuning Stone / Kinah) |
| --- | --- | --- | --- | --- | --- |
| +1 | 100% | 800 | 2 | 240,000 | — |
| +2 | 100% | 1,600 | 4 | 480,000 | — |
| +3 | 100% | 2,400 | 6 | 720,000 | — |
| +4 | 90% | 3,200 | 7 | 840,000 | 1 / 120,000 |
| +5 | 80% | 4,800 | 8 | 960,000 | 1 / 160,000 |
| +6 | 50% | 4,800 | 10 | 1,200,000 | 2 / 240,000 |
| +7 | 50% | 4,800 | 10 | 1,250,000 | 2 / 260,000 |
| +8 | 50% | 4,800 | 10 | 1,300,000 | 2 / 300,000 |
| +9 | 40% | 6,000 | 12 | 1,400,000 | 3 / 400,000 |
| +10 | 30% | 6,000 | 12 | 1,500,000 | 4 / 500,000 |

Cumulative totals, assuming every attempt succeeds on the first try:

| Target | Enhancement Stone | Tuning Stone (Unique) | Kinah |
| --- | --- | --- | --- |
| +5 | 12,800 | 27 | 3,240,000 |
| +10 | 39,200 | 81 | 9,890,000 |

Those totals are the floor, not the expectation. See **Costs and math** below.

Rare and Legendary wings use the same ladder shape but succeed unconditionally,
and their material costs are not documented in the Korean tables — the figures
above are explicitly stated to be Unique-grade values. Assume Rare and Legendary
are cheaper, and treat that as an open question.

### The rate-booster trap

The optional 10%-per-application booster looks like the obvious way to tame the
50% and 30% steps. Both a Korean cost analysis and a Taiwanese Bahamut analysis
independently concluded that **it is not worth using at any step**. The Korean
analysis modelled every step and found the base rate optimal throughout:

| Step | Base rate | Cheapest setting | Verdict |
| --- | --- | --- | --- |
| +1 to +3 | 100% | 100% | Fixed |
| +4 | 90% | 90% | Keep base |
| +5 | 80% | 80% | Keep base |
| +6 | 50% | 50% and 100% tie on Kinah, 50% wins on Enhancement Stones | Keep base |
| +7 | 50% | 50% | Keep base |
| +8 | 50% | 50% | Keep base |
| +9 | 40% | 40% | Keep base |
| +10 | 30% | 30% and 100% tie on Kinah, 30% wins on Enhancement Stones | Keep base |

The Taiwanese post title says the same thing bluntly: "don't blindly max it to
100%".

### Materials and what they used to be called

The naming shifted between announcement and release, which is why English
coverage disagrees:

| Announced 2026-05-26 | Shipped 2026-05-27 | Korean | Also translated as |
| --- | --- | --- | --- |
| Mysterious Feather | Enhancement Stone | 강화석 | Enhance Stone, Reinforcement Stone |
| Unique Tuning Stone | Tuning Stone (Unique) | 조율석(유일) | Sync Stone (Unique) |
| Kinah | Kinah | 키나 | Kina |

The livestream described "1 Expedition Wing Feather → 1 Mysterious Feather". In
the shipped version, every kind of wing feather obtainable from Expeditions
material-converts 1:1 into either an **Enhancement Stone** or a **Soul Crystal**.
If you see "Mysterious Feather" in an English guide, it is describing a
pre-release name for the shipped Enhancement Stone flow.

Note also that Enhancement Stones are the **same** currency used for gear
enchanting, so wing enhancement and [[Enchanting]] compete directly for the same
pile. That competition is the real budgeting problem in this note.

## Unlock and gates

| Gate | Detail |
| --- | --- |
| Patch | KR/TW from 2026-05-27; unknown for global launch |
| Eligible wings | Any wing earned in game: quests, dungeon drops, shop purchases with in-game currency, world collection |
| Ineligible wings | Cash-shop wings, Deva Pass (battle pass) wings, ranking-reward wings. These are Special grade, carry no stats and have no enhance button. |
| Interface | The wing enhancement panel is reached per-wing from the Wings menu. Taiwanese players note you must open each wing individually to see what option it enhances. |

## Inputs: currencies, materials, sources

### Enhancement Stone (강화석)

| Source | Yield | Notes |
| --- | --- | --- |
| Expedition wing feathers | 1:1 material conversion | The intended primary source. Alternative conversion is Soul Crystal. |
| Sealed Dungeons / hideouts | 500 on a first clear, ongoing thereafter | The single best bulk daily source for a levelling character |
| Dismantling spare wings | ~500 per wing | Nerfed in a November 2025 patch, then reverted the same week. Costs you a permanent retention effect. |
| Traces of the Lord | 50 per trace via conversion | Added in the December 3 patch. See [[Empyrean Traces and Feathers]]. |
| Duty Missions | Variable | Five per day |
| Expedition/Transcendence Odyle Energy Cubes | Scales with Odyle Energy spent | |

One Korean analyst priced Enhancement Stones at roughly **111 Kinah each** by
reference to a bundle costing 10,000,000 Kinah for 90,000 stones.

### Tuning Stone (Unique) (조율석(유일))

This is the scarce input, not the stones. It is purchasable, and the same
analyst valued it at roughly **300,000 Kinah each**. At that price the Tuning
Stones are about 63% of the total cost of taking one pair to +10. Other coverage
places Unique Tuning Stones as drops from high-difficulty dungeons and seasonal
rewards, but the Korean cost model assumes exchange purchase.

## Progression path

1. **Enhance nothing until you have several pairs.** Enhancement rewards breadth,
   so acquiring your fourth pair is worth more than taking your first pair from
   +3 to +4.
2. **Push everything to +3 first.** These three steps are 100% on every grade and
   cost 4,800 stones, 12 Tuning Stones and 1,440,000 Kinah per Unique pair.
3. **Take Rare and Legendary wings straight to +10.** They never fail. There is
   no reason to stop short except material budget.
4. **Take every Unique pair to +5.** 90% and 80% are cheap failures. This is the
   Korean consensus stopping point and the plateau the whole community
   converges on.
5. **Finish [[Breakthrough]] before going past +5.** Korean guides explicitly
   recommend completing the Breakthrough system first, because the resources
   compete and Breakthrough pays better per Kinah.
6. **Only then push +6 to +10, on your two or three highest-value pairs.**

## Priorities and breakpoints

| Player type | Stop at | Reasoning |
| --- | --- | --- |
| Casual | **+5 on everything you own** | Costs about a third of what +10 costs and captures most of the retention value; item level accrues from every pair |
| Item-level chaser | **+5 on everything, widened first** | 17 Unique pairs at +5 is +85 item level, which Korean guides call decisive for hitting a 4,500 item-level target |
| Boss-focused min-maxer | **+10 on the top two or three** | Nightmare Wings' Smite line and the PvE amplification lines are the only ones that change a parse |
| Title hunter | **+10 on 15 of 17 Unique pairs** | Required for the Smite 4% attack title, at roughly 1.15 billion Kinah for ten pairs |

Which pairs to prioritise, by retention option, follows the Korean PvE ranking:
Nightmare (Smite) → Dramata Nest (Damage Amplification) → Azure Flash and
Brawler (Weapon Damage Amplification) → Redeemed (Frontal Damage Amplification)
→ Forest Spirit and Blue Wave (PvE Damage Amplification) → the flat attack-power
group → the critical and accuracy group → the defensive group.

Note that Unique wings should be enhanced before Rare and Legendary ones for
combat value, because the Unique enhancement options are amplification and
critical stats, while the lower grades give HP and regeneration. The lower
grades are still worth finishing because they are free of failure risk and they
still pay item level and Flight Power.

## Costs and math

### One Unique pair to +10, expected

Running the base rates against the cost table gives the expected consumption for
a single Unique pair from +0 to +10:

| Resource | Expected consumption | Imputed Kinah value |
| --- | --- | --- |
| Enhancement Stone | ~78,156 | ~8,683,951 |
| Tuning Stone (Unique) | ~159.78 | ~47,933,333 |
| Kinah, spent directly | ~19,573,333 | 19,573,333 |
| **Total** | | **~76,190,666** |

The ratio worth internalising: expected consumption is about **twice** the
first-try cost in stones and Tuning Stones, and about **double** in direct Kinah,
because of the 50/40/30 band.

### Scaling out

| Goal | Approximate cost |
| --- | --- |
| One Unique pair to +5 | 12,800 stones, 27 Tuning Stones, 3.24M Kinah, plus a small failure margin at +4 and +5 |
| One Unique pair to +10 | ~76M Kinah all-in |
| Ten pairs to +10 | ~1.15 billion Kinah |
| Fifteen of seventeen Unique pairs to +10 | The Smite 4% title requirement; extrapolates to roughly 1.7 billion Kinah |

### What you get for it

| Investment | Item level | Flight Power | Example stat |
| --- | --- | --- | --- |
| 17 Unique pairs at +5 | +85 | +850 | 1% Smite from Nightmare, 1.5% PvE amplification from Forest Spirit |
| 17 Unique pairs at +10 | +170 | +1,700 | 2% Smite, 3% PvE amplification |

Doubling the enhancement level roughly doubles the stat, for roughly twenty
times the resources. That asymmetry is the whole argument for stopping at +5.

## Traps and mistakes

- **Paying for success rate.** Two independent regional analyses agree the base
  rate is cheapest at every step. The booster is a Kinah sink.
- **Pushing one pair to +10 before spreading to +5.** You lose the item-level
  breadth and the retention breadth for a marginal equip-effect gain.
- **Racing Breakthrough.** Wing enhancement and [[Breakthrough]] draw from the
  same wallet, and Korean guides put Breakthrough first.
- **Dismantling wings for stones.** ~500 stones is 0.6% of a +10 push, and you
  permanently lose a retention effect plus 200 Flight Power.
- **Expecting to move investment between pairs.** No Korean or Taiwanese source
  describes any way to transfer enhancement levels from one pair to another.
  Two low-trust English seller sites claim extraction refunds 100% of
  Enhancement Stones with Kinah lost, but no patch note or Korean guide
  corroborates it. **Plan as if enhancement is permanently locked to that pair.**
  See [[Extraction and Refunds]].
- **Believing the English "100% to +10" claim.** Several English sites state that
  all wings enhance at 100% to +10 and only become chance-based beyond +10.
  That contradicts the shipped KR table and the developer livestream, both of
  which describe decay on Unique-grade wings from +4 and a hard cap at +10.

## Global launch notes

- Wing enhancement did not exist at KR launch. It arrived six months later, on
  2026-05-27, as part of Season 3. Whether a September 2026 global launch ships
  with it depends entirely on which content baseline global starts from.
- If global launches without it, the correct early behaviour is unchanged:
  collect wings anyway, because retention effects and Flight Power are
  launch-era features.
- The stat caps that make wing enhancement worth chasing (250 on primary
  attributes, 130% attack and defence boost) were raised in the same 2026-05-27
  patch. A global launch on an earlier baseline would have lower caps and
  correspondingly different marginal value for wing stats.
- The Korean tables are Season 3 values and NCSoft has adjusted wing-related
  economy numbers before, so treat the cost table as current-KR rather than
  eternal.

## Open questions

- [ ] What are the Enhancement Stone, Tuning Stone and Kinah costs per step for
      **Rare** and **Legendary** wings? The published table is Unique-only.
      Settled by an in-game screenshot of a Rare wing's enhance panel.
- [ ] Can enhancement investment be extracted, refunded or transferred between
      wings? Settled by a patch note or the in-game extraction UI. Currently
      claimed only by low-trust English sites.
- [ ] Does the 100%-success guarantee for Rare and Legendary wings also cover
      Common-grade wings?
- [ ] Does enhancing a wing also grow its **equip** effect, or only the retention
      block? Korean sources say "new retention effect stats", implying retention
      only, but this is not stated unambiguously.
- [ ] Exact Tuning Stone (Unique) sources and drop rates. The Korean cost model
      assumes exchange purchase at ~300,000 Kinah; English coverage says
      high-difficulty dungeons and seasonal rewards.
- [ ] Is there any pity or accumulating-bonus mechanic on repeated failures? The
      Korean table shows flat rates, but one English site claims a stacking +5%.
- [ ] Confirm the "15 of 17 Unique wings at +10" requirement for the Smite 4%
      title.

## Sources

- [[AION2] 아이온2 시즌3 효율적인 날개 강화 가이드, 등급별 강화 비용 정리해 드립니다](https://lounge.plaync.com/feed/70658?country=KR&locale=ko-KR) — Purple Lounge, NCSoft's own KR community platform, 2026-06-04 — the full Unique-grade cost and success-rate table, the 100%-to-+10 rule for Rare and Legendary, the +10 Flight Power and +1 item level per step rules, the all-to-+5 recommendation, the 500-stones-per-dismantle figure and the 17-wings item-level worked example. Note the post is flagged by its author as AI-assisted, but its table matches the Inven community table exactly.
- [[AION2] 아이온2 시즌3 효율적인 날개 강화 가이드](https://www.inven.co.kr/board/aion2/6493/176) — Inven KR, 2026 — independent posting of the same cost table, used as corroboration.
- [날개 강화 가이드 (키나 기준 비용 최적화)](https://www.inven.co.kr/board/aion2/6444/1891) — Inven KR community, 2026 — the cumulative +5 and +10 material totals, the step-by-step optimal-probability analysis showing the base rate is cheapest everywhere, and the expected-consumption model totalling ~76,190,666 Kinah for one pair to +10.
- [PvE 기준 - 날개 강화 우선순위 (옵션, 수치 정리) (7.8 Update)](https://www.inven.co.kr/board/aion2/6444/1893) — Inven KR community, 2026-07-08 — the per-wing enhancement option table, the ~76.2M Kinah per pair figure, the 1.15 billion Kinah for ten pairs figure, and the Smite 4% title requirement.
- [別盲目點滿100%！翅膀強化「基納最省錢」機率點法與成本大數據分析](https://forum.gamer.com.tw/B.php?bsn=82913&subbsn=9) — Bahamut AION2 board, TW, post-2026-05-27 — independent Taiwanese confirmation that maxing the success rate is not the cheapest route. Only the thread listing was retrievable, so this is corroboration of direction rather than of numbers.
- [New Sanctuary and Brooches Added! Aion 2 Live Stream Summary (May 26, Tue)](https://labs.invenglobal.com/articles/22212/new-sanctuary-and-brooches-added-aion-2-live-stream-summary-may-26-tue) — Inven Global, 2026-05-26 — the announcement material names (Mysterious Feather, Unique Tuning Stone, Kinah), the 1:1 Expedition Wing Feather conversion, the grade-dependent success rules and the exclusion of paid, ranking and pass wings.
- [UPDATE: May 27, 2026 Patch Notes](https://aion2t.com/news/25) — aion2t, 2026-05-27 — the shipped material list (Kinah + Sync Stone (Unique) + Enhance Stone), the +10 cap, and the feather-to-Enhance-Stone-or-Soul-Crystal conversion.
- [AION2 May 27 Update Adds New Sanctuary, Brooch Slot, Wing Enhancement](https://questlog.gg/aion-2/en/patch-notes/aion2-may-27-update) — questlog.gg, 2026-05-27 — second English rendering of the same patch note, using "Tuning Stone (Unique)".
- [AION 2 Introduces New Sanctuary 'Chalice of Muspel'](https://about.ncsoft.com/en/news/article/aion2_update_260527) — NCSoft official, 2026-05-27 — official confirmation of the Wings Enhance System and the 250 / 130% stat cap increases.
- [Patch Notes](https://aion2.wiki.fextralife.com/Patch_Notes) — Fextralife AION 2 wiki, KR/TW patch archive — the November 2025 nerf and same-week revert of Enhancement Stones from dismantling wing items.
- [AION2 Dec 3 Update: PvP/PvE Toggle, AP Caps](https://questlog.gg/aion-2/en/patch-notes/aion2-dec-3-patch-notes) — questlog.gg, 2025-12-03 — Traces of the Lord converting to 50 Enhancement Stones each.
- [Aion 2 Asmodian Leveling Guide 1–10](https://aion2hub.com/leveling/asmodian-levels-1-10) — AION2 Hub, 2026 — Sealed Dungeon first clears paying 500 Enhance Stones.
- [How Aion 2 Wings Enhance System Works](https://www.u4n.com/news/how-aion-2-wings-enhance-system-works.html) and [Aion 2 Wings Upgrade Guide](https://friends4ed.co.zw/read-blog/14986_aion-2-wings-upgrade-guide-best-enhancement-methods-explained.html) — **low-trust SEO/seller sites, cited only to document the incorrect claims** that all wings are 100% to +10, that enhancement continues past +10, and that extraction refunds 100% of stones. The first two claims are contradicted by the KR table and the developer livestream; the third is unverified.
