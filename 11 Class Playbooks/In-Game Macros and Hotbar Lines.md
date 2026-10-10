---
chapter: "11 Class Playbooks"
system: In-Game Macros and Hotbar Lines
type: reference
unlock: "skill window from level 4; stigma skills from ~22"
account_wide: false
cadence: "set once, revise after level 45 and at 16/20 specs"
region_verified: ["GLOBAL", "KR"]
patch: "KR 2026-01-28 skill macro; global client Oct 2026"
confidence: medium
tags:
  - aion2/progression
  - aion2/class-playbooks
  - aion2/combat
---

# In-Game Macros and Hotbar Lines

> **In one sentence:** the **native** macro (Skill window → **Macro**, not third-party
> software) repeats **whole hotbar columns** while you hold a bound key — and each
> column is a **priority stack** of up to four skills, **bottom slot = fires first**.

## Setup (every class)

1. **Bind Macro key:** Esc → Settings → Key Settings → **General** → **Gameplay →
   Macro** (empty by default). Common: side mouse button or a keyboard key. **AION 1
   control mode** may block mouse-bound macros — use AION 2 controls or a keyboard key.
2. **Build columns** in the skill window (`K`): drag skills into the **same column**
   (one hotkey). Up to **four skills per column**.
3. **Priority rule:** the **bottom** skill in the column is tried **first**. Put your
   **highest-priority cooldown** at the **bottom** and the **no-cooldown filler at the
   top**. A filler at the bottom locks the column on one skill forever.
4. **Macro editor:** `K` → **Macro** → **Add macro** → pick a **column** (not a single
   skill). **Delay 10 ms** per step on low ping; **40–50 ms** if ping is ~80–100 ms.
5. **Combat:** **hold Macro key + left mouse (basic attack)** together for animation
   cancels (Grobs / Daeva Guides method). Dark afterimages = cancels working.

**Do not put in the macro:** toggles (Chanter mantras, **`Light of Protection`**),
charged skills (**`Hellfire`**, **`Deadshot`**, charged **`Bolt`**), long buffs/stigma
bursts you want on the boss, dashes, **`Defiance`**, **`Doom Shield`** (charge).

**Skill Queue** (Settings → Combat): community split — test on a dummy with your class
macro; see [[#Common mistakes]].

Sources: [Daeva Guides — macros](https://daevaguides.com/en/guides/macros/),
[Corpus — macro guide](https://corpus.gg/blog/aion-2/macros-guide), KR Inven class
boards.

---

## Templar (수호성)

Two playstyles; pick one macro set.

### A — Recommended PvE (`Vicious Strike` + `Judgment`, 맹심)

Accessible rotation, ~same DPS as cancel build, **no MP floor**. Skill queue **ON**
(KR board). Manual: **`Punishment`** buff, **`Flash Rampage`**, **`Shield Rush`**.

| Column | Bottom → top (priority → filler) | Macro step |
| --- | --- | --- |
| **Judgment line** | **`Judgment`** → **`Warding Strike`** → **`Shield Smite`** | Step 1 |
| **Strike line** | **`Vicious Strike`** → (optional **`Punishing Strike`** chain slots) | Step 2 + hold **LMB** |

### B — Ceiling cancel (`Pummel` + `Judgment`, 연심캔)

From [Inven macro share](https://www.inven.co.kr/board/aion2/6438/24397). Higher skill
floor; MP management required. **Right-click column + key `3` column** in that post.

| Column | Bottom → top | Notes |
| --- | --- | --- |
| **RMB line** | **`Judgment`** → **`Punishment`** (buff window) → **`Warding Strike`** → **`Shield Smite`** | Open with ranged **`Punishment`**, then **`Punishment`** buff before **`Warding Strike`** |
| **Key 3 line** | **`Pummel`** / chain fillers (**`Debilitating Smash`**, **`Annihilate`** per Daeva) | Second macro step |

**Manual:** **`Doom Shield`** (charge), **`Defiance`**, party **`Debilitating Smash`**
if used, groggy **`Flash Rampage`**.

Detail: [[Templar Skills and Stigmas#In-game macro (PvE)]].

---

## Gladiator (검성)

From Daeva / Antochi / Ulfhednar. **Mobile spec on filler** (`Rending Blow` movement
spec) or you stand still in the macro.

| Column | Bottom → top |
| --- | --- |
| **Main DPS line** | **`Rage Burst`** → **`Overhead Slam`** → **`Sword Aura Rampage`** → **`Rending Blow`** (filler) |

**Macro:** one step = main line only from ~27; **10 ms**. **`Sword Aura Rampage`** only
procs on **Stagger break** — the line fires it when the window exists.

**Manual:** buffs, gap closers. After 45, some players add **`Overhead Slam` 16+** as a
**second macro step** or separate key (unmeasured vs one-step).

---

## Assassin (살성)

| Column | Bottom → top |
| --- | --- |
| **Damage line** | **`Insignia Explosion`** → **`Heart Gore`** → **`Ambush`** → **`Savage Roar`** (filler) |

**Macro:** damage line → **`Quick Slice`** (second step), **10 ms**. **Hold** macro +
**LMB**; avoid **clicking** macro (drops skills).

**Manual:** **`Illusive Clone`**, **`Swift Contract`**, **`Savage Fang`**, defensives.

---

## Ranger (궁성)

| Column | Bottom → top |
| --- | --- |
| **Griffon line** | **`Griffon Arrow`** (or **`Explosive Arrow`** from 37) → **`Snare Shot`** → **`Burst Arrow`** |
| **Gale line** | **`Gale Arrow`** → **`Drill Dart`** → **`Tempest Shot`** (filler) |

**Macro:** Griffon line → Gale line, **10 ms** each + **LMB**.

**Manual:** **`Deadshot`** on its own key — **hold charge** with macro + LMB running;
**`Marking Shot`**, buffs, traps.

---

## Sorcerer (마도성)

| Column | Bottom → top |
| --- | --- |
| **Core line** | **`Bittercold Wind`** → **`Blaze`** → **`Firestorm`** → **`Wish of Concentration`** (filler last; at 16 cuts CDs) |

**Macro:** one step = core line + **LMB** (**`Flame Arrow`** weave).

**Manual:** burst line **`Element Enhancement`** → **`Delayed Explosion`** → **`Winter's
Shackles`**; ground AoE; **`Hellfire`** charged — **never in macro** (only stage 1).
Leveling-only: frost **`Ice Chain`** line.

---

## Spiritmaster (정령성)

Aligns [Inven 8165](https://www.inven.co.kr/board/aion2/6454/8165) + Antochi/Daeva.

| Column | Bottom → top |
| --- | --- |
| **Jointstrike line** | **`Jointstrike: Corrode`** → **`Jointstrike: Curse`** → **`Dimensional Control`** → **`Combustion`** (filler) |
| **Spirit line** | **`Elemental Fusion`** → **`Summon: Water Spirit`** → **`Summon: Earth Spirit`** → **`Summon: Fire Spirit`** (Fire last so it stays out) |

**Macro steps (order):** **Jointstrike column** → **Spirit column**, **10 ms** each +
**LMB**.

**Manual opener (boss):** optional **`Assault Terror`** → **`Flame Blessing`** →
**`Enhance: Spirit's Benediction`** → **`Summon: Ancient Spirit`** → **`Jointstrike:
Corrode`**; then hold macro. Do **not** charge **`Elemental Fusion`** in macro.

---

## Cleric (치유성)

| Column | Bottom → top |
| --- | --- |
| **Stigma / mark line** | **`Prayer of Amplification`** → **`Earth Punishment`** → **`Chain of Torment`** → **`Condemnation`** |
| **Filler line** | **`Lightning Strike Scattershot`** → **`Divine Aura`** → **`Light of Regeneration`** → **`Judgment Thunder`** |

**Macro:** stigma line → filler line, **10 ms** + **LMB**.

**Manual:** **`Radiant Recovery`**, **`Healing Light`**, **`Debilitating Mark`**, **`Bolt`**,
**`Light of Protection`** (toggle — **never** in macro).

---

## Chanter (호법성)

| Column | Bottom → top |
| --- | --- |
| **Crush line** | **`Dark Crush`** → **`Spinning Strike`** → **`Incandescent Blow`** (filler) |

**Macro:** Crush line → **`Onslaught`** (second step) + **LMB**.

**Manual:** **`Impactful Crush`**, **`Marchutan's Wrath`** (or pre-45 openers when **`Dark
Crush`** still has CD), **`Undefeated Mantra`**, **`Power of the Storm`**, heals —
**mantras are toggles; second macro press turns them off**.

Detail: [[Chanter Skills and Stigmas#In-game macro (PvE)]].

---

## Common mistakes

| Mistake | Effect |
| --- | --- |
| Filler at **bottom** of column | One skill spam forever |
| Unbound **Macro** key | Macro does nothing |
| Toggles in macro | Mantras / **`Light of Protection`** flip off |
| Charged skills in macro | Partial charge only |
| Buffs on trash | Boss CD wasted (Season 1 CDR is low) |
| AFK field macro | Ban risk — macro is for active play |

## Related

[[Class Playbooks]] · [[Keybindings and Client Files]] · [[Global Launch Differences]]
(2026-01-28 macro) · per-class **Skills and Stigmas** notes.

## Sources

- [Daeva Guides — Aion 2 Macro Guide (all 8 classes)](https://daevaguides.com/en/guides/macros/) — EN, 2026-10-08, column layouts and manual exceptions.
- [Corpus — Aion 2 macro guide](https://corpus.gg/blog/aion-2/macros-guide) — EN, 2026-10-04, row priority and LMB hold.
- [Inven — Templar macro (연심캔)](https://www.inven.co.kr/board/aion2/6438/24397) — KR, 2026-08-28.
- [Inven — Spiritmaster newbie macro](https://www.inven.co.kr/board/aion2/6454/8165) — KR, 2026-07-02.
- [Inven — Chanter PVE (평캔 매크로)](https://www.inven.co.kr/board/aion2/6451/7090) — KR.
- [[Templar Skills and Stigmas]] — Vicious-Judgment vs Pummel-Judgment DPS note.
