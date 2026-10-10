---
chapter: "90 Appendix"
system: Keybindings and Client Files
type: reference
unlock: n/a
account_wide: false
cadence: one-off
region_verified: ["GLOBAL"]
patch: "EU Steam global 2026-10-05; verified on Kaisinel 2026-10-06"
confidence: high
tags:
  - aion2/meta
  - aion2/client
  - aion2/alts
---

# Keybindings and Client Files

> **In one sentence:** keyboard and quickslot binds are **per character on NC’s
> servers**; the local `DeviceSetting_V2.dat` file is **not** a profile you can
> copy from main to alt.

## Verified on EU Steam (2026-10-06)

Experiment: Fanamy (main) key settings saved while game closed to
`DeviceSetting_V2.dat.fanamy-backup`. After full exit, file copied over
`DeviceSetting_V2.dat` before launching **Polyphenloe**. In-game binds on
Polyphenloe **unchanged**.

Supporting file evidence on the same PC:

| Observation | Implication |
| --- | --- |
| `DeviceSetting_V2.dat` **hash differed** after Polyphenloe session vs Fanamy backup | Local file updates per login/session |
| Overwriting `.dat` with Fanamy bytes **before launch did not change** Polyphenloe binds | **Server (or char-scoped) bind data wins** over local blob for gameplay |
| `Input.ini` under `Config\Windows` stays **empty** (~2 bytes) | UE default input ini is not used for rebinding |
| `GameUserSettings.ini` | Graphics / resolution only |

**Path (Steam global):**  
`%LOCALAPPDATA%\AION2\Saved_Steam\PersistentDownloadDir\UserSetting\DeviceSetting_V2.dat`

Do **not** commit or share `Game.ini` in the same config folder — it can contain
session tokens.

## In-game UI

**Settings → Key Settings** (DE: **Tastenbelegung**): tabs **General**, **Menu**,
**Quickslot**, **Marker**. Each tab has its own **Reset**. Two keys per action
are supported.

There is **no** “copy bindings to all characters” option (community reports on
Steam match this experiment).

## What presets actually copy

| Feature | Copies |
| --- | --- |
| Batch Preset Equip (Set 1–3) | Gear, bar skills, title, wings, Daevanion insight |
| Skill / Stigma presets (KR; verify on EU) | Mastery and stigma **builds**, not keys |

## Practical alt workflow

1. Screenshot or checklist all four Key Settings tabs on your main.
2. Rebind once per alt, or use **secondary binding** slots while setting the main.
3. Optional: keep `DeviceSetting_V2.dat.fanamy-backup` only to restore **this PC’s**
   last local flush — not a cross-character sync tool.

## Related notes

[[Alts and Account Wide Progression]] · [[Player Tracker - Fanamy]] · [[Home]]
