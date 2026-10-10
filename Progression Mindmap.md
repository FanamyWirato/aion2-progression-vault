---
chapter: "00 Home"
type: mindmap
tags:
  - aion2/progression
  - aion2/home
confidence: high
---

# Progression Mindmap

Three views of the same thing: the full map of progression types, the order to
invest in them, and which activity feeds which system. The clickable version is
the Obsidian canvas `Progression Mindmap.canvas`, where every box opens its note.

If the diagrams render as plain code, your Obsidian predates Mermaid mindmap
support; use the canvas instead, or update Obsidian.

Everything below is scoped to the Season 1 global launch baseline: gate range 0
to about 3,800 and no Heroic-grade equipment. Branches marked *roadmap* exist in
Korea today but are not expected at launch.

## 1. Every progression type

```mermaid
mindmap
  root((Aion 2 character power))
    Foundations
      Character level
        Ascension gauge
        Ascension quests
      Item level
        Content entry gates
      Combat Power
        Real strength metric
      Stats
        Primary attributes
        Offensive and defensive
        PvE and PvP split
        Lord attributes
    Skills and talents
      Skill levels
        Mastery Points to base cap
        Breakpoints 8 12 16 20
      Stigmas
        Slot expansion
        Stigma levels
      Daevanion boards
        Stat nodes
        Active skill nodes
        Passive skill nodes
        Core nodes
        PvE and PvP boards
    Equipment
      Slots
        Weapon and off hand
        Seven armor pieces
        Revelation Amulet
        Noble Belt
        Bracelet
        Rings and earrings
        Brooch and Pendant and Seal roadmap
      Item grades
        Rare and Epic
        Unique as launch ceiling
        Heroic roadmap
      Upgrade layers
        Enchanting
        Breakthrough
        Manastones and Spirit Stones
        Godstones
        Runes
        Potential roadmap
      Option layers
        Soul Imprint
        Attunement rerolls
        Soul Binding roadmap
      Carry forward
        Transfer and Inheritance
        Succession Crafting
        Extraction refunds
    Arcana
      Skill card slots
        Chalice
        Parchment
        Compass
        Bell
        Mirror
        Scales roadmap
      Stat card slots roadmap
        Key
        Hourglass
        Dice
        Lantern
      Card stats
        Vitality line
        Magic Power line
        Skill level bonuses
      Set effects
      Refinement and extraction
      Transcendence dungeons
        Deus
        Arcanis
    Pets and mounts
      Pet collection
        Five families
        Souls and fragments
      Pet levels
        Level 5 active skill
        Possession effects
      Pet Understanding
        Per monster kill counter
      Species Understanding
        Family levels
        Nine reroll slots
        Smite priority
      Mounts
        Traversal roles
    Wings and flight
      Wing sources
        Ascension quests
        Boss drops
        Hidden cubes
        Expeditions
      Wing effects
        Equip effects
        Retention effects
      Wing enhancement roadmap
      Flight Power
        Stamina pool
        Fold technique
    Pantheon
      Colossus slot
      Statue slots
      Artwork slots
      Lord attributes
        Wisdom
        Freedom
        Death
        Time
        Destruction
        Justice
        Life
        Fate
        Illusion
        Space
      Nightmare Mode ladder
    Collections and exploration
      Empyrean Traces
        Field pickups
        Surplus conversion
      Monolith resonance
        Wisdom Stones to skill points
        Amulet enhance scrolls
        Lord attribute points
      Garrisons and Sealed Dungeons
        One time sweep
        Belt enhance scrolls
      Hidden cubes
      Kibelisks and outposts
      Wardrobe skin collection
      Titles and achievements
      Housing not live
    PvP progression
      Abyss Points
        Weekly caps
      Merit Medals
        Real gear gate
      Abyss rank ladder
      PvP gear
        Fierce Battle Amulet
      PvP board and crystals
      Transformations
      Arenas sieges and seasons
    Activities and economy
      Odyle Energy
        The real weekly budget
      Daily loops
      Weekly loops
      Trials and rankings
      Consumables and buffs
      Seasons and battle pass
      Currencies
        Kinah
        Bound Kinah
        Quna
      Legions
      Alts and account plan
    Gathering and professions
      Gathering nodes
        Ore and wood
        Herbs and plants
        Gems and cooking
        Odyle resources
      Professions
        Blacksmithing
        Jewelcrafting
        Alchemy
        Cooking
      Material conversion
      Farming routes and Kinah
```

## 2. Order of investment

The reasoning behind this ordering lives in [[Progression Phases Roadmap]], and
the class-specific version in [[Templar BiS Roadmap]],
[[Chanter BiS Roadmap]] and [[Cleric BiS Roadmap]].

```mermaid
flowchart TD
    A[Level to cap while sweeping one time content] --> B[Weapon enchant first]
    A --> C[Traces and Kibelisks and cubes as you pass them]
    C --> D[Monolith donations for skill points and amulet scrolls]
    A --> E[Garrisons and Sealed Dungeons for belt scrolls and Daevanion]
    B --> F[Armor and accessories to a comfort breakpoint]
    E --> G[Daevanion boards toward main skill nodes]
    G --> H[Skill breakpoints 8 then 12 then 16]
    F --> I[Item level gate for endgame dungeons]
    I --> J[Arcana green set then higher grades]
    I --> K[Pantheon statues from Nightmare Mode]
    I --> L[Pet families and reroll slots]
    J --> M[Combat Power for group content]
    K --> M
    L --> M
    M --> N[Breakthrough and Succession on keeper gear]
    M --> O[Wardrobe filling and title collecting]
    N --> P[PvP track only if you want the Abyss]
    O --> P
```

## 3. What feeds what

Work backwards from the system you want to progress to the activity that pays
for it. The gating resource is usually Odyle Energy rather than entries, so see
[[Odyle Energy and Entry Limits]] before planning a week.

```mermaid
flowchart LR
    SD[Sealed dungeons] --> ES[Enhancement stones]
    SD --> DP[Daevanion points]
    GA[Garrisons] --> BS[Belt enhance scrolls]
    RQ[Region and side quests] --> DP
    ES --> ENC[Enchanting]
    DP --> DB[Daevanion boards]
    EX[Exploration] --> FE[Empyrean traces]
    FE --> MO[Monolith resonance]
    MO --> SP[Skill points]
    MO --> AS[Amulet enhance scrolls]
    MO --> LA[Lord attributes]
    HC[Hidden cubes] --> WG[Wings]
    TD[Transcendence dungeons] --> AR[Arcana cards]
    NM[Nightmare Mode] --> ST[Pantheon statues]
    ST --> LA
    DD[Daily dungeons] --> PS[Pet souls and crystals]
    PS --> PU[Species Understanding]
    RAID[Raids and expeditions] --> UG[Unique gear]
    UG --> SUC[Succession and transfer]
    GATH[Gathering] --> MAT[Materials]
    MAT --> CR[Crafting]
    CR --> BIS[Best in slot crafted gear]
    MAT --> MC[Material conversion]
    MC --> ENC
    PVP[Arenas and Abyss] --> AP[Abyss Points]
    PVP --> MM[Merit Medals]
    MM --> PG[PvP gear]
    SEASON[Season and battle pass] --> SM[Season shop materials]
    SM --> AR
    SM --> ST
    OE[Odyle Energy] --> UG
    OE --> AR
```

## Related

- [[Home]]
- [[Progression Phases Roadmap]]
- [[Season 1 Launch Plan]]
- [[Item Level vs Combat Power]]
- [[Glossary KR TW EN]]
