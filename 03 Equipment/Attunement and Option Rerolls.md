---
chapter: "03 Equipment"
system: Attunement and Option Rerolls
type: progression-system
unlock: "Available from launch on any imprinted item; Attunement Stones as a distinct currency arrived KR 2025-12-17"
account_wide: false
cadence: continuous
gates: ["item must already be soul-imprinted", "sacrificial gear must be the same grade or higher", "armour attunement options expanded in Season 2"]
currencies: ["Attunement Stone (조율석)", "Attunement Stone Fragment (조율석 조각)", "sacrificial Unique gear", "Soul Codex: Reset", "Kinah"]
region_verified: ["KR", "TW"]
patch: "KR live as of 2026-09-06; base attunement present 2025-11-19, Attunement Stones 2025-12-17, option pools expanded 2026-01-21, duplicate-roll protection 2026-02-25"
confidence: medium-high
tags:
  - aion2/progression
  - aion2/equipment
  - aion2/economy
---

# Attunement and Option Rerolls

> **In one sentence:** attunement (조율) lets you point at exactly one of your
> item's soul-imprint lines and replace it with a fresh random one, paid for by
> destroying a Unique-grade item or spending an Attunement Stone — and it is the
> single largest recurring gear cost in the Korean endgame.

## Why it matters

[[Soul Imprint and Soul Binding]] gives you four to six random lines and no
choice about them. Attunement is the choice. Everything a Korean endgame player
does with surplus Unique gear — every duplicate drop, every set piece they will
never wear, every reward from a raid they have outgeared — is routed here.

The reason this is a separate note from imprinting is that it behaves like an
economy rather than a mechanic. The mechanic is four lines and a button. The
economy is: where does fodder come from, what is the exchange rate between
fodder and Attunement Stones, how many presses does a good line take, and at
what point do you stop and accept a mediocre item. That last question is the
one most players get wrong, in both directions.

Boundary with the neighbouring note, restated because Korean guides do not
observe it: **the initial roll, the imprint rate and the Soul Codex belong to
[[Soul Imprint and Soul Binding]]. The per-line reroll and its funding belong
here.** Reset (초기화) — the all-four-lines reroll — is a hybrid and is described
in both, but its cost model lives here.

## How it works

Open Integrated Enhancement (default `N`) and pick the Soul Imprint tab. An
imprinted item shows its lines with an index. You select **one line index**,
choose a payment, and confirm. The selected line is replaced with a new random
line drawn from that slot's pool. The other lines are untouched.

| Property | Behaviour |
| --- | --- |
| Failure | **There is none.** The line always changes. This is not enhancement |
| What changes | Exactly one line, the one you selected |
| New line's value | Random within the line's range, **and its imprint rate re-rolls too** |
| Result pool | The slot's normal option pool, **minus the option currently in that slot** since 2026-02-25 |
| Can it roll a line you already have elsewhere on the item? | Yes. Only the selected slot's own current option is excluded |
| Undo | None |

That 2026-02-25 change matters more than its one-line patch note suggests.
Before it, a reroll could hand you back the same option you were trying to get
rid of, which on a pool of a dozen options is a meaningful fraction of your
presses wasted. After it, every press is guaranteed to be a *different* option,
even if not a better one.

### Paying for it: fodder versus stones

Two payment methods, and they are not equivalent.

**Sacrificial gear.** You destroy an item of the same grade or higher in the
same slot family. This is the launch method and still the cheapest for anyone
raiding regularly, because Unique duplicates arrive faster than you can use them.
The item is consumed whether or not you like the result.

There is a widely repeated community claim that using **Unique fodder on a
Heroic item only has about a 10% chance of changing the option**, with the
implication that Heroic items need Heroic fodder or stones. I could not find
this in any patch note or on any database page, and the mechanic as described
elsewhere has no failure state at all, which is hard to reconcile. Treat the
grade-mismatch penalty as **low confidence and unverified** — but do not feed
Unique fodder into Heroic gear at scale until you have tested it yourself, since
the downside if true is total.

**Attunement Stones (조율석).** Added **2025-12-17**, roughly four weeks after
the Korean launch. A dedicated currency that does the same job without needing a
matching item, which decouples rerolling from raid loot and makes it purchasable.
Their introduction is what turned attunement from "a use for junk" into a
resource sink with a market price.

**Attunement Stone Fragments (조율석 조각)** are the sub-unit, dropped by field
bosses and awarded by open-world content, and converted upward into whole stones.
Fragments are the reason field-boss rotations remain worth running for endgame
characters who need nothing else from them.

### Reset, for comparison

Reset (초기화) rerolls **all four lines at once** for one Soul Codex: Reset plus
**300,000 Kinah**. Use it when three or more lines are junk; attune when one or
two are. The crossover is roughly at two bad lines, because a Reset Codex costs
8,000 Phantasmal Fragments in the [[Nightmare Mode]] shop and two attunement
presses are usually cheaper than that.

## Unlock and gates

| Thing | Requirement |
| --- | --- |
| Attuning a line | The item is imprinted, and you hold either matching-grade fodder or an Attunement Stone |
| Attunement Stones | Exist from KR 2025-12-17; before that, fodder only |
| Fragments | Field bosses and open-world content |
| Armour options worth attuning | Substantially expanded in Season 2, KR 2026-01-21 |
| Weapon Damage Amplification | Weapon and Guard slots only |
| Active skill levels | Rings only |

There is a per-item **attunement attempt counter** whose cost or availability
scales with use — [[Succession and Transfer]] states that inheritance **resets
the target item's attunement attempts**, which only makes sense if attempts are
tracked and escalate. The exact escalation curve is not published; see Open
questions.

## Inputs: currencies, materials, sources

| Resource | Where it comes from | Notes |
| --- | --- | --- |
| **Unique-grade fodder** | Duplicate raid and expedition drops, Abyss set pieces you have replaced, crafted overflow | Free if you raid; the default endgame supply |
| **Attunement Stone** (조율석) | KR 2025-12-17 onward: content rewards, shops, fragment conversion | Decouples rerolling from loot |
| **Attunement Stone Fragment** (조율석 조각) | **Field bosses**, open-world objectives | Converts up into whole stones |
| **Soul Codex: Reset** | Nightmare exchange at 8,000 Phantasmal Fragments; season and Subjugation shops; Monolith levels; achievements; Battle Pass; level-45 island quests | For the all-lines reroll |
| **Kinah** | Everything | 300,000 per Reset |

Do not extract Unique duplicates for materials before checking whether you need
attunement fodder — the two uses compete directly. See
[[Extraction and Refunds]] and [[Material Conversion]].

## Progression path

1. **Levelling and first Unique set.** Do not attune. Stockpile duplicates
   instead; they are worth more later than any line you would roll now.
2. **Weapon and Guard to 100% imprint rate first** ([[Soul Imprint and Soul
   Binding]]), because attuning re-rolls a line's imprint rate and undoes that
   work if done in the wrong order.
3. **Reset the weapon** until at least one tier-0 line (Combat Speed) appears.
4. **Attune the remaining weapon lines one at a time**, cheapest payment first.
   Stop at three good lines out of four.
5. **Repeat down the slot order**: Guard, gloves, chest, shoulders, then rings.
6. **Buy the last line with a Philosopher's Stone** rather than attuning for it,
   once Soul Binding is available — a guaranteed new line at 100% imprint rate
   beats an unbounded number of random presses.
7. **Field-boss fragments become your fodder floor** once raid duplicates stop
   arriving faster than you spend them.

## Priorities and breakpoints

### The signature options endgame players actually chase

Attunement is worth spending on when the slot has an option that exists nowhere
else. These are the ones that justify repeated presses:

| Slot | Signature option | Why it is chased |
| --- | --- | --- |
| **Weapon / Guard** | Weapon Damage Amplification, **Combat Speed** | The only two slots that roll them; Combat Speed is the universal tier-0 line |
| **Ring** | **Active skill level** | The only slot granting active skill levels — how players reach skill 20 |
| **Gloves** | Combat Speed | Second-best Combat Speed source |
| **Chest** | Damage Amplification | Season 2 addition |
| **Shoulders** | Critical Damage Amplification | |
| **Cloak** | Critical Damage Resistance; class passive levels | PvP-defining |
| **Legs** | Damage Resistance | |
| **Boots** | Movement Speed | Real value in PvP and in [[Nightmare Mode]] |
| **Necklace / Earrings** | Class passive skill levels | |
| **Bracelet** | Empyrean Lord attributes, at an unusually high roll rate | |

Rings and the weapon are where the money goes. A ring with two active-skill
lines on your main damage skills is worth more presses than anything else in the
game, and it is the reason [[Accessories]] treats the crafted ring as a
long-term project.

### Where to stop

- **Three of four lines good is the finish line.** The fourth costs more than
  the first three combined.
- **Do not attune for a value upgrade on a line you already want.** Rolling
  Combat Speed 9% into Combat Speed 10% is not worth a press; rolling Movement
  Speed into Combat Speed is.
- **Free-to-play: attune only the weapon and one ring.** Everywhere else, wear
  what dropped well.
- **Never attune a Soul-Bound line.** It sits at a guaranteed 100% imprint rate
  and attuning throws that away.
- **Check the slot index twice.** The most common expensive misclick in the game
  is attuning line 2 when you meant line 3. There is no undo.

## Costs and math

Honest statement first: **no published expected-cost table exists for
attunement.** Korean cost threads discuss the Kinah cost of *enhancement* and
*pendant* work in detail, but attunement cost is reported in fodder items, and
fodder has no stable price because it comes from loot rather than a shop.

What can be said with numbers:

- **Reset:** exactly 1 Soul Codex: Reset + **300,000 Kinah**, no failure. The
  Reset Codex's clearest hard price is **8,000 Phantasmal Fragments** in the
  Nightmare exchange shop, so a reset is "one Nightmare shop purchase plus
  300k".
- **Attunement:** one fodder item or one Attunement Stone per press, no Kinah
  cost reported, no failure state.
- **Presses per good line:** with a pool of roughly eight to twelve options per
  slot and the current option excluded, hitting a specific named option is
  around one press in eight to eleven. Two specific options in one slot is
  correspondingly worse. That arithmetic — not any published figure — is why
  Korean guides tell you to reset first (four fresh lines for one Codex) and
  attune only the stragglers.
- **The Philosopher's Stone alternative:** 2 stones + 1M Kinah buys one
  guaranteed *new* line at 100%. Whenever the expected number of attunement
  presses to fix a slot exceeds what two Philosopher's Stones cost you, bind
  instead of attune. For most players in Season 3 that crossover is around three
  to four presses.

**Confidence: medium** on the reasoning, **high** on the two hard prices, **low**
on any claim about typical total spend. Anyone quoting an average Kinah cost for
"finishing attunement" is extrapolating.

## Traps and mistakes

- **Attuning before the imprint rate is at 100%.** Wrong order; the rate re-rolls
  with the line.
- **Extracting Unique duplicates you will need as fodder.** Check
  [[Extraction and Refunds]] before dismantling anything Unique.
- **Feeding Unique fodder into Heroic gear** on the assumption it works the same
  — the reported 10% change rate is unverified but the downside is total loss of
  the fodder.
- **Attuning a stepping-stone item.** Anything you will replace within a season
  is not worth a press.
- **Attuning after Soul Binding rather than before.** Bind last, so the
  guaranteed 100% line is the one you keep.
- **Forgetting that inheritance resets the attunement counter on the target.**
  This is an *advantage* if you plan for it — see the bind-before-inherit
  optimisation in [[Soul Imprint and Soul Binding]].

## Global launch notes

**The core attunement mechanic will be present at global launch.** Rerolling one
imprint line with sacrificial gear existed in the Korean and Taiwanese clients
from 2025-11-19. A Season 1 global player can attune from day one.

**Attunement Stones as a distinct item are borderline.** They arrived on
**2025-12-17**, twenty-eight days after the Korean launch. Global builds
generally ship the Korean base plus accumulated fixes rather than the exact
day-one client, so stones may well be in the launch build — but plan the first
month around **fodder gear**, not stones, and be pleasantly surprised if the
shop has them. **Confidence medium.**

**The Season 2 option-pool expansion is probably not there.** Damage
Amplification on weapons and Attack Power Increase, Smite, Defense Increase and
Iron Wall on armour were added **2026-01-21**. If the global build is a true
Season 1 build, your armour option pools will be noticeably shallower than every
Korean guide assumes, and armour attunement will be correspondingly less
attractive. **Confidence medium.**

**The duplicate-roll protection is probably not there either.** The
2026-02-25 change that removes the currently equipped option from the reroll
pool is a quality-of-life fix that arrived over three months into the Korean
service. Without it, budget more presses than any current Korean guide implies.
**Confidence medium.**

**Soul Binding is definitely not there** (KR 2026-02-11), so the "buy the last
line with a Philosopher's Stone" escape hatch does not exist at Season 1. Every
line you want, you must roll. That single fact makes attunement fodder more
valuable at global launch than it is in Korea today, and it is the strongest
practical reason to hoard Unique duplicates through the first months.

## Open questions

- [ ] **The per-item attunement attempt counter.** [[Succession and Transfer]]
      says inheritance resets it, so it exists and presumably escalates cost.
      Nobody has published the curve, or even whether the escalation is in Kinah,
      in fodder count, or in stone count.
- [ ] **The grade-mismatch rule.** Does Unique fodder on a Heroic item really
      only change the option ~10% of the time? Not in any patch note. Testable
      in ten presses.
- [ ] **Whether attunement costs Kinah at all**, and if so how much. Sources
      describe only the item cost.
- [ ] **Attunement Stone acquisition specifics.** The 2025-12-17 introduction is
      firm; the current shops, prices and fragment-to-stone conversion ratio are
      not documented anywhere I could reach.
- [ ] **The exact size of each slot's option pool**, which is what turns the
      presses-per-line estimate above from arithmetic into a real number. Inven
      screenshots show the client displays per-option percentages; a transcription
      would settle this.
- [ ] **Whether armour attunement was genuinely "added" in Season 2** or merely
      expanded. The 2026-01-21 note lists new armour options; it does not say
      armour was previously unattunable. This note assumes expansion.

## Sources

- [AION 2 Patch Notes — January 21, 2026 (Season 2)](https://aion2hub.com/updates/aion-2-update-2026-01-21) — KR translated, read 2026-09-06. New attunement options for weapons (Damage Amplification) and armour (Attack Power Increase, Smite, Defense Increase, Iron Wall); the Sealed Philosopher's Stone; and the inheritance rule that **resets the target item's attunement attempts**, which is the evidence that an attempt counter exists.
- [【討論】2/25更新公告內容 @AION2 哈啦板](https://forum.gamer.com.tw/C.php?bsn=82913&snA=4240) — TW Bahamut translation of the KR 2026-02-25 patch, read 2026-09-06. The 靈魂調整 change excluding the currently equipped option from the reroll result pool. Sole source for the duplicate-roll protection and its date.
- [아이온2 인벤 — 2/11(수) 업데이트 노트](https://www.inven.co.kr/board/aion2/6388/96080) — KR, 2026-02-11. Confirms that Soul-Bound lines can subsequently be attuned but lose their guaranteed 100% imprint rate, and that attunement re-rolls the line's rate.
- [Soul Codex: Reset (Bound) — item 535200001](https://aion2hub.com/database/items/535200001) — KR datamined, read 2026-09-06. The 8,000 Phantasmal Fragment Nightmare price and the rest of the Reset Codex supply list, which is what makes the reset-versus-attune crossover calculable.
- [《永恆紀元2》裝備強化系統介紹](https://www.animattoys.com/detail/zXNs9G79/) — TW, read 2026-09-06. The three-function UI (imprint / adjust / initialise), the same-grade-or-higher fodder rule, and the statement that adjusting replaces one selected option.
- [아이온2 영혼 각인, 1순위로 뽑을 '필수 옵션'은?](https://www.gameple.co.kr/news/articleView.html?idxno=214690) — KR press (Gameple), Dec 2025. Reset costs 300,000 Kinah and rerolls all lines; the per-slot signature options for armour; the PvE/PvP option split.
- [아이온2 인벤 — PVE 기준 부위별 영혼 각인 우선순위 추천](https://www.inven.co.kr/board/aion2/6444/1205) — KR, Season 2. The per-slot chase list reproduced above, the rings-grant-active-skill-levels rule, and the Season 2 marking on the new armour options.
- [아이온2 인벤 — '영혼 각인 옵션' 우선 순위 (장비 부위별)](https://www.inven.co.kr/board/aion2/6444/556) — KR. The reset-first-then-attune-stragglers workflow, and screenshots showing per-option percentages in the client.
- [아이온2 영혼 각인 조율 완벽 가이드 2026](https://alias007.tistory.com/759) — KR blog, Season 3. The "three of four lines is the finish line" heuristic, the slot-index misclick warning, and the argument for buying the last line with a Philosopher's Stone rather than attuning.
- [아이온2 영혼 각인 공략: 부위별 1티어 옵션 우선순위 종결 (2026)](https://game.savetip.co.kr/aion2-soul-engraving-guide-option-priority/) — KR blog, 2026. Hotkey `N`, the don't-chase-small-value-upgrades rule, and the compromise-then-Philosopher's-Stone endgame pattern.
- [Aion 2 Gear Enhancement Guide: Mastering Soul Binding and Syncing](https://www.mmoexp.com/News/aion-2-gear-enhancement-guide-mastering-soul-binding-and-syncing.html) — EN, boosting-shop SEO, 2026-01-16. **Lead only, corroborated where used**: describes syncing as consuming a fodder Unique to replace one of four stats, with a pool that includes class passives and active-skill lines, and notes the same stat can return (true before 2026-02-25). Source of the unverified grade-mismatch claim; that claim is marked low confidence in the body.
- [Aion 2 Gear Guide](https://boostroom.com/blog/aion-2-gear-guide-weapons-armor-upgrades-and-progression) — EN, boosting-shop SEO, 2026. **Lead only.** Origin of the "Attunement Stone Fragments from field bosses" and "armour attunement added in Season 2" leads. The field-boss fragment claim is consistent with Korean open-world reward lists but I could not confirm it on a database page; treat as **medium-low confidence**.
- [Aion 2 Patch Notes archive — December 17, 2025](https://aion2hub.com/updates) — KR translated, read 2026-09-06. The introduction date for Attunement Stones as a distinct item.
- [[Aion 2] Detailed Equipment System Guide](https://vortexgaming.io/en/postdetail/594067) — EN translation of a KR video guide, launch era. Confirms attunement existed at launch with sacrificial gear as the only payment, before stones.

## Related notes

[[Soul Imprint and Soul Binding]] · [[Equipment]] · [[Accessories]] ·
[[Enchanting]] · [[Breakthrough]] · [[Succession and Transfer]] ·
[[Extraction and Refunds]] · [[Material Conversion]] · [[Potential Enhancement]] ·
[[Runes]] · [[Brooch Pendant and Seal Slots]] · [[Gear Tiers and Sources]] ·
[[Stat Reference]] · [[Nightmare Mode]] · [[Abyss Points and Ranks]] ·
[[Global Launch Differences]] · [[Glossary KR TW EN]] · [[Home]]
