---
chapter: "11 Class Playbooks"
system: Spiritmaster Progression Plan
type: progression-system
unlock: "class chosen at character creation; the plan becomes real at level 45"
account_wide: false
cadence: "continuous"
gates: ["item level 1000 for Expedition", "item level 1600 for two-star Conquest", "item level 2200 for Fire Temple", "item level 2700 for Sanctuary 1", "item level 3800 practical ceiling"]
currencies: ["Kinah", "Odyle Energy", "Enhance Stones", "Breakthrough Stones", "Stigma Shards", "Daevanion Crystals", "Mysterious Crystals", "Abyss Points"]
region_verified: ["KR", "GLOBAL"]
patch: "KR Inven Spiritmaster board 2026-07; written for global Season 1 (2026-10-05)"
confidence: medium
tags:
  - aion2/progression
  - aion2/class-playbooks
  - aion2/spiritmaster
---

# Spiritmaster BiS Roadmap

> **In one sentence:** the Spiritmaster (정령성) is a **ranged orb DPS** whose
> power is **spirit uptime, buff snapshot on `Summon: Ancient Spirit`, and
> DoT/fusion bursts** — so the plan chases Accuracy, **`Spirit Strike`** levels,
> and stigma buffs before raw Crit stacking.

## Why it matters

Community consensus and hub copy both call Spiritmaster one of the **strongest
solo** classes: spirits tank and press buttons while you layer **`Jointstrike:
Curse`**, **`Jointstrike: Corrode`**, and **`Elemental Fusion`**. In groups the
class is **hands-on** — if summons die or buffs are applied in the wrong order,
damage collapses.

Mechanics live in [[Stat Reference]], [[Item Level vs Combat Power]], and
[[Progression Phases Roadmap]]. Rotation and stigma math live in
[[Spiritmaster Skills and Stigmas]].

## The Season 1 baseline

Same vault baseline as the other playbooks: level **45**, gates **0–3,800**,
**four stigma slots**, stigma cap **20**, Unique gear ceiling, no Heroic.
See [[Global Launch Differences]].

## Stat priority

Spiritmaster follows the **mage row** in [[Stat Reference]] (Accuracy → Smite →
Critical) with two class-specific twists: **`Spirit Strike`** (정령타격) doubles
your buff on **both you and spirits**, and **`Mental Focus`** (정신집중) adds
**0.3% Smite per passive level** like the Chanter — so Smite from passives is
cheaper than on most DPS.

| Rank | Stat | Why |
| --- | --- | --- |
| 1 | **Accuracy** | Floor for you **and** spirit hits; DoTs still need to land |
| 2 | **Smite** | `Mental Focus` passive scaling; stigma **`Flame Blessing`** procs |
| 3 | **Critical Hit** | `Element Unification` stacks from spirit hits; stop near practical ceiling (~80%) |
| 4 | **Damage / Weapon Damage Amplification** | Imprint and Daevanion; spirits scale from your attack at summon time |
| 5 | **Combat Speed** | More left-click procs and **`Elemental Fusion`** windows |
| 6 | **Multi-hit** | **`Consecutive Countercurrent`** (연속 역류) procs on DoT targets |
| 7 | **Max Attack Power** vs Additional Attack | Same late-game argument as Chanter: **Max Attack** can beat Additional when **Perfect** stacks — see [[Chanter BiS Roadmap]] |
| — | **HP** | Wind spirit heals; solo comfort, not a CP chase |

Korean gear guides also list **Perfect** on legs/gloves/cloak as a late polish stat;
treat as optional until Accuracy/Smite/Crit are settled.

## Phase plan

| Phase | Item level | What you are doing |
| --- | --- | --- |
| **0. Levelling** | 0–1,000 | Story Orb, green Belt of Nobility. Passives: **`Spirit Strike`** → **`Mental Focus`** → **`Element Unification`**. Alchemy for orb craft path |
| **1. First Uniques** | 1,000–1,600 | Krao / Draupnir. **`Combustion`** and **`Elemental Fusion`** toward 20; **`Summon: Fire/Water Spirit`** toward 16 |
| **2. Two-star Conquest** | 1,600–2,200 | Urugugu / Vakron. Stigma **`Summon: Ancient Spirit`** and **`Enhance: Spirit's Benediction`** toward 20 |
| **3. Fire Temple band** | 2,200–2,700 | Enraged Kromede Orb or crafted Dragon Lord Orb. **`Jointstrike: Corrode`** stigma 20. Ariel crystals once armour is ~+12 |
| **4. Ceiling** | 2,700–3,800 | Ludra / Unique +10 belt and amulet. Four stigmas 15–20. Do not chase Heroic |

## Stigma headline (four slots)

Season 1 default: **`Enhance: Spirit's Benediction` 20 → `Summon: Ancient Spirit`
20 → `Jointstrike: Corrode` 20 → `Flame Blessing` 20.** Apply **Benediction and
Flame Blessing before summoning Ancient Spirit** so the spirit snapshots buffed
stats. Details and shard order in [[Spiritmaster Skills and Stigmas]].

## Gear headline

**Orb** (Alchemy) plus universal **Guard**. Same dungeon ladder as other DPS —
see [[Spiritmaster Gear and Slots]]. Imprint priority: **Weapon Damage
Amplification** and **Combat Speed** on weapon/Guard; **active skill levels** on
rings for **`Combustion`**, **`Elemental Fusion`**, **`Jointstrike: Curse`**.

## Traps

- Summoning **`Ancient Spirit`** before **`Flame Blessing`** / **`Spirit's
  Benediction`** — the spirit copies stats at summon; buffs after are wasted on it.
- Ignoring spirit dismiss/slot management and fighting without three elementals
  down in solo content.
- Copying a **five-stigma / level-25** Korean screenshot onto global **four
  slots, cap 20**.
- Crafting under **Blacksmithing** — Orb is **Alchemy** ([[Crafting]]).
- Chasing Crit before Accuracy on a class whose spirits inherit your hit rating.

## Open questions

- [ ] Exact global English strings for stigma names (`Enhance: Spirit's
      Benediction` vs older translations).
- [ ] Whether global spiritmaster retains **four-element fusion** and **Ancient
      Spirit** snapshot rules unchanged from KR/TW.
- [ ] **`Jointstrike: Destructive Attack`** (파멸의 공세) as fifth-slot flex vs
      **`Siphon`** for Season 2 when a fifth stigma slot exists.

## Sources

- [AION 2 Hub — Spiritmaster](https://aion2hub.com/classes/spiritmaster) — global
  skill list and role, retrieved 2026-10-08.
- [아이온2 인벤 — 뉴비지침) 정령성 스킬트리 / 장비옵션 / 아르카나 (PVE)](https://www.inven.co.kr/board/aion2/6454/8165) — KR, 2026-07-02. Skill tiers, stigma set, gear options, Arcana targets.
- [아이온2 인벤 — 새로 시작하는 뉴비 기본 정보 / PVE](https://www.inven.co.kr/board/aion2/6454/8152) — KR. Stigma 20 order, specialisation table, Ancient Spirit buff order.
- [아이온2 인벤 — 정령성 세팅, 딜싸이클](https://www.inven.co.kr/board/aion2/6454/2760) — KR. Opener, CDR sync for Benediction/Ancient, Corrode timing.
- [MetaBot.GG — Spiritmaster build](https://metabot.gg/ko_KR/aion-2/classes/spiritmaster) — KR/global datamine summary; stat priority and Daevanion headline.
- [[Templar BiS Roadmap]] / [[Cleric BiS Roadmap]] — shared dungeon gates and Unique ladder.

## Related notes

[[Spiritmaster Gear and Slots]] · [[Spiritmaster Skills and Stigmas]] ·
[[Spiritmaster Support Systems]] · [[Class Pet Farm Priority]] ·
[[Daevanion Boards]] · [[Stat Reference]] · [[Global Launch Differences]] ·
[[Home]]
