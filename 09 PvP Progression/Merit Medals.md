---
chapter: "09 PvP Progression"
system: Merit Medals
type: currency-system
unlock: "Abyss access at endgame"
account_wide: false
cadence: weekly
gates: ["Abyss rank for weekly purchase limits"]
currencies: ["Silver Merit Medal", "Gold Merit Medal", "Platinum Merit Medal", "Merit Fragments", "Abyss Points", "Kinah"]
region_verified: ["KR", "TW"]
patch: "KR 2026-01-21, 2026-02-11, Chapter 1 2026-07-01"
confidence: medium
tags:
  - aion2/progression
  - aion2/pvp
---

# Merit Medals

> **In one sentence:** Abyss Points are the soft currency you earn by playing,
> but Merit Medals are the hard currency that actually gates PvP gear tier —
> and because their weekly supply is capped by your Abyss rank, your PvP
> progression speed is set weeks in advance regardless of how much you play.

> **Season 1 verdict:** medals are in, they gate PvP gear, and the launch
> tuning is the **harsher pre-February-2026** version. Tradable Medal Boxes
> are Chapter 1 and are out. Per-class boss ranking is out. This note is the
> medal economy; [[Abyss Points and Ranks]] is the AP wallet — do not
> duplicate the two.

## Why it matters

This is the correction that reframes PvP progression. [[Abyss Points and Ranks]]
describes a currency you accumulate through kills and objectives, and it is easy
to read that as the gating resource. It isn't.

**Abyss Points are abundant; Merit Medals are not.** Every meaningful PvP gear
purchase in the Abyss Shop wants medals, the weekly medal supply is capped, and
the cap scales with your Abyss rank. The consequence is that a player who grinds
eighteen hours a day and a player who does their weekly caps end the month with
similar PvP gear — the grinder just has more Abyss Points they cannot spend.

If you are planning a route to a top-tier PvP weapon, plan it in weeks of medal
caps, not in hours of play. See [[PvP Gear]].

## How it works

### The three tiers

Korean 공훈 훈장 is "Merit Medal" (also rendered "Medal of Honour" in some
English sources — same item, see [[Glossary KR TW EN]]). Three tiers:

| Korean | English | Role |
| --- | --- | --- |
| 은 공훈 훈장 | **Silver Merit Medal** | The base tier and the bulk of your income |
| 금 공훈 훈장 | **Gold Merit Medal** | Mid-tier; feeds the better Abyss Shop stock |
| 백금 공훈 훈장 | **Platinum Merit Medal** | Top tier; the gate on top-end PvP weapons and armour |

Two supporting item types sit alongside them:

- **Merit Fragments** (e.g. 은빛 공훈 파편, Silver Merit Fragment) — sub-medal
  units that convert upward into whole medals. They are how the game pays out
  partial medal value from activities that would otherwise be too granular.
- **Merit Chests / Medal Boxes** (훈장 상자) — containers that open into medals.
  These are the main payout format from Abyss bosses. Chapter 1 added
  **tradable** Medal Boxes to the Abyss, which is significant because it lets
  medal value move through the player economy for the first time.

### Where medals come from

| Source | What it gives | Cap |
| --- | --- | --- |
| **Abyss Shop purchase with Abyss Points** | Silver and Gold medals | Weekly, **rank-gated** — see below |
| **Abyss boss kills** | Merit Chests / Medal Boxes | Per boss spawn; tradable boxes since Chapter 1 |
| **Artifact capture and fortress sieges** | Medals and chests | Per siege cycle |
| **Dimensional core / objective capture** | Medals | Per objective |
| **Season missions and weekly PvP missions** | Medals and fragments | Weekly |
| **Battlefields and arenas** | Fragments primarily | Weekly caps |
| **Material Conversion** | Upgrades fragments and lower medals into higher | Weekly craft count |

Taiwanese coverage independently confirms medal acquisition from fortress wars,
which is useful corroboration that the siege payout is not a Korea-only tuning.

### The rank gate — the mechanism that actually throttles you

The Abyss Shop lets you **buy medals with Abyss Points**, and this is the most
reliable source. But the weekly purchase limit is **gated on your Abyss rank**.

The reported structure from Korean patch coverage is a weekly limit in the order
of **10 per medal type per week**, later raised for Silver (a figure of 20
appears in a subsequent patch), with **higher Abyss ranks unlocking higher
weekly caps**. **Confidence medium on the exact numbers** — they have been
retuned at least twice and I could not find a single current authoritative
table.

The structural point is solid and is what matters for planning:

1. Abyss Points are earned faster than you can spend them on medals.
2. The medal purchase cap, not your point balance, sets your weekly income.
3. Raising the cap requires raising your **rank**, which is a slower and more
   competitive process than earning points. See [[Abyss Points and Ranks]].

So Abyss rank is a **multiplier on PvP gear velocity**, not just a title. That
is the single most important thing in this note.

### The conversion ladder

Medals convert upward through [[Material Conversion]], and **Kinah is the fuel**.

The ladder runs fragments → Silver → Gold → Platinum, with each step consuming a
quantity of the lower tier plus a Kinah fee, and with the conversion count
limited weekly like every other conversion recipe. A patch during 2026 **reduced
the Kinah cost of the Silver Merit Fragment conversion**, which tells you both
that the fee was originally considered punitive and that this ladder is a
deliberate Kinah sink.

The practical reading: **Kinah is convertible into PvP progression speed**, but
only up to the weekly conversion count. This is the same design shape as
[[Odyle Energy and Entry Limits]] — an uncapped resource (Kinah) buying a capped
one (medals), with the cap doing the real balancing work.

Some conversion steps are reported as probabilistic rather than deterministic
at the upper tiers. **Unverified** — flagged in Open questions.

### What medals buy

In the Abyss Shop, medals are the price tag on:

- **PvP weapons** — the top tier is Platinum-gated and is the long pole in any
  PvP gearing plan.
- **PvP armour sets** — Gold and Platinum by slot and tier.
- **PvP accessories** — typically Silver and Gold.
- **Enhancement and upgrade materials** specific to the PvP line.

Abyss Points, by contrast, buy consumables, the medals themselves, and lower-end
stock. The division of labour is deliberate: **points are the throughput
currency, medals are the store of value.**

### Interaction with the Abyss Point economy

The two currencies are coupled at exactly one place — the rank-gated weekly medal
purchase — and that coupling is the whole PvP economy:

```
play → Abyss Points (uncapped) → [WEEKLY RANK-GATED CAP] → Merit Medals → gear
                                          ↑
                          raise this by raising Abyss rank
```

Everything to the left of the cap is abundant. Everything to the right is
scarce. Any optimisation that increases Abyss Point income without increasing
rank or medal caps is **worthless for gearing**, which is a genuinely
counter-intuitive result and the reason the community took months to converge on
it.

The Chapter 1 tradable Medal Boxes partially open this: medal value can now be
bought from other players with Kinah, routing around the cap. How much this
matters depends on box supply, which comes from Abyss boss kills.

## Unlock and gates

- Merit Medals become available with Abyss access at endgame.
- **Weekly purchase limits are gated on Abyss rank** — this is the primary gate.
- Conversion needs crafting access and Kinah.
- Top-tier Abyss Shop stock has its own rank requirements on top of the medal
  price.

## Inputs: currencies, materials, sources

| Resource | Role |
| --- | --- |
| Abyss Points | Buys Silver and Gold medals, up to the weekly rank-gated cap |
| Kinah | Fuels every step of the conversion ladder |
| Silver / Gold / Platinum Merit Medals | The actual gear currency |
| Merit Fragments | Sub-medal units; convert upward |
| Merit Chests / Medal Boxes | Payout container; tradable since Chapter 1 |
| Abyss rank | Sets the weekly cap — the real gate |

## Progression path

1. **Get Abyss access and start the weekly medal purchase immediately.** The cap
   does not roll over. A missed week is permanently lost progression, and this
   is the most common error in PvP gearing.
2. **Prioritise rank over points.** Rank raises your cap; points do not. See
   [[Abyss Points and Ranks]].
3. **Do every capped medal source every week** — season missions, battlefields,
   sieges, artifact captures. Individually small, collectively the difference
   between a nine-week and a sixteen-week weapon.
4. **Run every Abyss boss you can reach.** Merit Chests are the largest
   non-capped-by-rank source, and since Chapter 1 the boxes are tradable.
5. **Convert upward as soon as you have the inputs.** The conversion count is
   weekly and does not bank.
6. **Buy Platinum-gated pieces in weapon-first order.** The weapon is the
   largest single power increase in [[PvP Gear]].

## Priorities and breakpoints

- **Weekly reset** is the single most important moment in PvP progression.
  Purchases, conversions and mission caps all cycle. See [[Weekly Routine Main]].
- **Each Abyss rank threshold** that raises your weekly cap is worth more than
  any amount of extra play at your current rank.
- **The Platinum threshold** for your target weapon is the number to work
  backwards from when planning.
- Medals are per character, so alts do not pool medal income — but alts do have
  their own weekly caps, which is one of the few remaining reasons to run them
  for PvP. See [[Alts and Account Wide Progression]].

## Costs and math

### The 9-to-16-week weapon

The community-reported timeline for a top-tier PvP weapon is **9 to 16 weeks**.
The spread is not about play time — it is about which of these you achieve:

| Factor | Fast end (≈9 weeks) | Slow end (≈16 weeks) |
| --- | --- | --- |
| Abyss rank | High, unlocking the larger weekly caps | Low, stuck on the base cap |
| Weekly medal purchases | Every week, both tiers, at cap | Missed weeks |
| Abyss boss participation | Consistent, on a coordinated legion | Occasional |
| Siege and artifact attendance | Every cycle | Sporadic |
| Kinah for the conversion ladder | Ample; all weekly conversions used | Limited |
| Season and weekly missions | Fully cleared | Partial |

Note what is **not** on that list: hours played beyond what is needed to hit the
caps. This is the arithmetic behind the claim at the top of the note.

The honest caveat: I could not reconstruct this timeline from published medal
costs and caps, because the current numbers for both have been retuned and are
not consolidated anywhere authoritative. The 9-to-16 range is community
reporting and should be treated as **medium confidence** — directionally right,
numerically soft.

### Why Kinah matters more than it looks

Every step of the conversion ladder charges Kinah, and the weekly conversion
count is the cap. So the relevant question is not "can I afford this
conversion" but "am I using all of my weekly conversions". A player with Kinah
to spare and unused conversion counts is leaving medals on the table; see
[[Currencies and Economy]] for where the Kinah comes from.

## Traps and mistakes

- **Optimising Abyss Point income.** Points are not the gate. Above the weekly
  medal purchase cap, additional points do nothing for gearing.
- **Missing a weekly medal purchase.** The cap does not roll over. This is
  permanent lost progression and it is the most damaging routine error in PvP.
- **Ignoring rank because you don't care about the title.** Rank *is* your
  weekly cap. It is a gearing stat.
- **Hoarding fragments.** They convert on a weekly count; unused counts are
  lost, so convert continuously rather than in a batch.
- **Skipping Abyss bosses.** Merit Chests are among the few sources not throttled
  by your rank.
- **Assuming medals pool across alts.** They do not — but alts have their own
  caps, so alts are additive, not shared.
- **Following pre-2026-02 guides.** Medal costs, weekly limits and rank
  requirements were substantially retuned on 2026-02-11 and again afterwards.
- **Not selling or buying tradable Medal Boxes.** Since Chapter 1 this is a real
  market and it is the only route around the weekly cap.

## Global launch notes

The medal framework ships. **Launch Scale Test: Silver medals only.** Abyss
shop therefore tops out around **tier 2, item level 77**. Gold and Platinum
are out for week-one planning. Tradable Medal Boxes remain Chapter 1 / out.
Crafted gear may beat T2 PvP until Gold exists. See [[PvP Gear]] and
[[Global Launch Differences]].

## Open questions

- [ ] What are the **current** weekly medal purchase limits per rank? Reported
      around 10 per type, with Silver later raised to 20, and higher ranks
      unlocking more — but no single current table exists.
- [ ] What is the exact Abyss Point price of each medal tier on the live build?
- [ ] What are the conversion ratios and Kinah fees at each rung of the ladder?
- [ ] Are the upper conversion steps probabilistic? Some Korean coverage of the
      Abyss boss material conversion recipes suggests a chance-based outcome.
- [ ] What exactly do Merit Chests and Medal Boxes contain, and at what rates?
- [ ] Can the 9-to-16-week weapon timeline be reconstructed arithmetically from
      caps and costs, and does it hold on the current build?
- [ ] Does the tradable Medal Box market meaningfully bypass the weekly cap, or
      is box supply too low for it to matter?
- [ ] Which global-launch PvP weapon is the actual top tier inside the 0–3,800
      band, and what does it cost in medals?

## Sources

- [Inven — 공훈 훈장 AP 비용, 주간 제한, 등급 요구치](https://www.inven.co.kr/board/aion2/6388/96080) — KR, 2026-02-11, Merit Medal Abyss Point costs, weekly purchase limits, Abyss rank requirements on those limits, Material Conversion recipes for medals, and changes to Abyss boss medal acquisition.
- [Inven — 훈장 상자 및 어비스 보스 획득](https://www.inven.co.kr/board/aion2/6388/72727) — KR, 2026-01-21, Merit Chest / Medal Box contents and their acquisition from Abyss bosses.
- [Inven — 은빛 공훈 파편 물질변환 키나 비용 인하](https://www.inven.co.kr/board/aion2/6388/110938) — KR, 2026, reduction of the Kinah cost for the Silver Merit Fragment material conversion, establishing Kinah as the ladder's fuel and that the original fee was considered punitive.
- [AION2 Hub — Chapter 1 patch notes (2026-07-01)](https://aion2hub.com/updates/aion-2-update-2026-07-01) — KR, 2026-07-01, addition of tradable Medal Boxes to the Abyss, and the shift of Abyss boss-kill and artifact-capture rewards to per-class contribution ranking.
- [PURPLE Lounge — official KR Abyss and season announcements](https://lounge.plaync.com/board/aion2/list?country=KR&locale=ko-KR) — KR official, 2026, corroboration of the Abyss Shop structure and rank gating.
- [Bahamut — 永恆紀元2 深淵與要塞戰討論](https://forum.gamer.com.tw) — TW, 2026, independent Traditional Chinese confirmation that Merit Medals are obtained from fortress wars, corroborating the siege payout outside Korean sources.
- [Namu Wiki — 아이온2](https://namu.wiki/w/%EC%95%84%EC%9D%B4%EC%98%A82) — KR, the Abyss Shop's division between Abyss Point stock and Merit Medal stock, and the Silver/Gold/Platinum tier structure.
- Community reporting, Korean PvP discussion boards, 2026 — the 9-to-16-week
  top-tier PvP weapon timeline. **Medium confidence**; not reconstructible from
  published caps and costs, which have been retuned at least twice.
