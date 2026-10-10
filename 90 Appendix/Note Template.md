---
chapter: "90 Appendix"
type: template
tags:
  - aion2/meta
---

# Note Template

Copy this structure for every progression-system note in the vault. Keep the
section order identical so notes stay comparable across chapters.

```markdown
---
chapter: "0X Chapter Name"
system: System Name
type: progression-system
unlock: "level 12 / after ascension quest / ..."
account_wide: false        # true if the progress benefits every character
cadence: "one-off | daily | weekly | seasonal | continuous"
gates: ["item level 1800", "combat power 2500"]
currencies: ["Kinah", "Enhancement Stones"]
region_verified: ["KR", "TW"]
patch: "YYYY-MM-DD or chapter/season name"
confidence: high           # high | medium | low
tags:
  - aion2/progression
  - aion2/<chapter-slug>
---

# System Name

> **In one sentence:** what this system gives you and why you care.

## Why it matters
Where this sits in the overall power budget, and what it competes with for
resources.

## How it works
Mechanics, tiers, rules, success rates, caps. Tables where numbers exist.

## Unlock and gates
Level, quest, item level or content requirement to open the system.

## Inputs: currencies, materials, sources
Table of every resource the system consumes and where each one comes from.

## Progression path
Ordered stages from first unlock to endgame, with the milestone each stage buys.

## Priorities and breakpoints
What to do first, where to stop, which thresholds are worth pushing to.

## Costs and math
Known numbers: costs per step, expected attempts, kinah totals, caps.

## Traps and mistakes
Irreversible choices, resource sinks, things that look good but are not.

## Global launch notes
Expected differences at global launch versus the KR/TW live version, plus which
patch the KR/TW information above comes from.

## Open questions
- [ ] Unverified item, with what evidence would settle it.

## Sources
- [Title](url) — region, publication date, what it was used for.
```

## Conventions used in this vault

- **Terminology**: global/English term first, KR term in parentheses on first use.
- **Confidence**: mark any number that comes from a single unverified source as
  `confidence: medium` or lower, and repeat the caveat inline.
- **Regions**: `KR` = Korean live server, `TW` = Taiwan live server,
  `GLOBAL` = confirmed for the global release.
- **Links**: link systems by note name, e.g. `[[Enchanting]]`, so notes can move
  between folders without breaking.
