---
chapter: "01 Foundations"
system: Stat Vocabulary and Priorities
type: progression-system
unlock: "primary attributes from level 1; Empyrean Lord stats from the 2nd Ascension at level 22"
account_wide: false
cadence: "continuous"
gates: ["accuracy about 2350 for Sanctuary 2", "smite 30 percent minimum", "critical stat about 1179 for efficiency"]
currencies: ["Kinah", "Manastones", "Spirit Stones", "Mysterious Crystals"]
region_verified: ["KR", "TW"]
patch: "KR 2026-03-25 (PvE/PvP coefficient split), 2026-07-01 (attack power cap and PvP damage resistance cap abolished)"
confidence: medium
tags:
  - aion2/progression
  - aion2/foundations
---

# Stat Reference

> **In one sentence:** Aion 2 has six primary attributes, ten Empyrean Lord
> attributes and roughly thirty derived combat stats, and only about six of
> them decide whether your character works.

## Why it matters

Aion 2's character sheet is a wheel: six primary attributes in the centre, ten
Empyrean Lord attributes around the outside, and a long derived stat list
behind them. Attributes are not something you allocate — they arrive from gear,
Monoliths, the Bracelet and Arcana — so the practical question is never "where
do I put my points", it is "which of these stats do I chase on rerolls, and how
much is enough".

That question has a specific and unintuitive answer in Aion 2, because
Accuracy is a hard prerequisite rather than a nice-to-have. High-tier bosses
have very high parry and block rates, and an under-accuracy character does not
do reduced damage, it does no damage on a large fraction of its swings. Every
Korean stat guide leads with the same line: Accuracy first, everything else
second.

## How it works

### The attribute wheel

Attributes convert into derived stats at fixed per-point rates read from the
client's `PcStatSecond` table. The conversion is **perfectly linear with no
diminishing returns**. Primary attributes give +0.10 percent per point; the ten
Empyrean Lord attributes give +0.20 percent per point.

**Primary attributes (centre of the wheel, +0.10%/pt):**

| Attribute | Korean-source alias | Converts into |
| --- | --- | --- |
| Might | Strength | Attack |
| Constitution | — | HP |
| Dexterity | — | Evasion, Block, Critical Resist |
| Intelligence | — | Status Effect Chance |
| Precision | — | Accuracy, Critical |
| Willpower | — | Status Effect Resist |

**Empyrean Lord attributes (outer ring, +0.20%/pt).** These are usually called
"deity stats" or "Pantheon Lord stats" in English sources and are named for the
twelve Empyrean Lords:

| Attribute | Lord | Converts into |
| --- | --- | --- |
| Justice | Nezekan | Defense, Perfect Chance |
| Destruction | Zikel | Attack, Perfect Resist |
| Freedom | Vaizel | Accuracy, Evasion |
| Death | Triniel | Critical, Regeneration Penetration |
| Illusion | Kaisinel | Cooldown Reduction, Endurance Penetration |
| Wisdom | Lumiel | Smite, MP Cost Reduction |
| Life | Yustiel | HP, Regeneration |
| Destiny (alias Fate) | Marchutan | MP, Endurance |
| Time | Siel | Combat Speed, Smite Resist |
| Space | Israphel | Movement Speed, Block |

Light (Ariel) and Darkness (Azphel) appear on the wheel as the two supreme
Lords but have no conversion in the current client data, so they contribute
nothing directly.

The Empyrean Lord attributes come from exactly three places: the **Monolith**
regional collections, which are the main source; the **Bracelet**, whose
sub-stats are Empyrean Lord attributes; and **Arcana** cards, each of which
carries a flat Empyrean Lord main stat. This is why the Bracelet and the
Monoliths matter so much more than their item level suggests. See
[[Pantheon Stats]] and [[Kibelisks and Map Registration]].

Because Wisdom is the only source of Smite, and Smite is a flat doubling of
damage when it procs, Wisdom is the standout attribute for damage dealers:
Smite percent equals Wisdom multiplied by 0.2.

### Offensive derived stats

| Stat | Korean | What it does | Notes |
| --- | --- | --- | --- |
| Attack Power | 공격력 | Base damage term | The attack power upper cap was abolished in Chapter 1 |
| Accuracy | 명중 | Beats enemy parry, block and evasion | The gating stat; see thresholds below |
| Critical Hit | 치명타 | Chance to crit | Crits are 1.5x, and crit damage bonuses are additive on top |
| Critical Damage Amplification | 치명타 피해 증폭 | Raises crit multiplier | Additive: base 150 percent plus your bonuses |
| Smite (aliases: Crushing Blow, Strike, Heavy Blow) | 강타 | Chance to deal double damage | Internally "HardHit". Flat 2x, no resistance interaction beyond Smite Resist |
| Damage Amplification (alias Damage Increase or Boost) | 피해 증폭 | Multiplier on all damage | See stacking rules below |
| PvE Damage Amplification | PVE 피해 증폭 | PvE-only multiplier | Adds into the same pool as generic Damage Amplification |
| Boss Damage Amplification | 보스 피해 증폭 | Boss-only multiplier | Adds into the same pool |
| Weapon Damage Amplification | 무기 피해 증폭 | Multiplier on the weapon damage term | Named as a top-priority tuning option |
| Rear Damage Amplification | 후방 피해 증폭 | Damage from behind the target | Multiplies **independently** of the main pool, which makes it one of the two strongest real damage options |
| Attribute Resistance Reduction | 속성 내성 감소 | Lowers the target's elemental resistance | The other of the two strongest real damage options |
| Penetration | 관통 | Adds damage, offset by target Defense | Strong on multi-hit skills, weak against high-defence targets |
| Perfect | 완벽 | Forces the weapon's maximum damage roll | Worth only about 5 percent; the weakest of the three proc stats |
| Multi-hit | 다단히트 | Extra hits on a skill | About 5 percent extra damage per additional hit, up to 4 hits for about 20 percent |
| Combat Speed | 전투 속도 | Raises both attack speed and cast speed | Highest-value utility stat; more skills per burst window |
| Attack Speed / Cast Speed | 공격 속도 / 시전 속도 | Component speeds | Counted at 100 CP per percent |
| Cooldown Reduction | 재사용 대기시간 감소 | Shorter cooldowns | From Illusion (Kaisinel) |
| Status Effect Chance | 상태이상 적중 | Land stuns, silences | From Intelligence; matters for control classes and PvP |

### Defensive derived stats

| Stat | Korean | What it does | Notes |
| --- | --- | --- | --- |
| Defense | 방어력 | Flat mitigation | Reported as relatively weak in PvE compared to Damage Resistance |
| Damage Resistance (alias Damage Tolerance or Reduction) | 피해 내성 | Percentage mitigation | Community-measured cap of 80 percent |
| Critical Damage Resistance | 치명타 피해 내성 | Mitigates incoming crits | The key PvP defensive stat |
| Boss Damage Resistance | 보스 피해 내성 | Mitigates boss damage | What defensive titles and the Frenzy Arcana set supply |
| Weapon Damage Resistance | 무기 피해 내성 | Mitigates the weapon damage term | Interacts with enemy Weapon Damage Amplification |
| Evasion | 회피 | Chance to be missed entirely | Full negation |
| Block | 막기 | Chance to block | Large reduction; requires a shield |
| Parry | 무기 방어 | Chance to parry | Moderate reduction; the stat bosses use against your Accuracy |
| Iron Wall | 철벽 | Block-type defensive proc | Appears as a Marchutan board and pet-understanding option, usually paired with Regeneration |
| Critical Resist | 치명타 저항 | Lowers incoming crit chance | Boss crit resistance is why your crit stat requirement is so high |
| Status Effect Resist | 상태이상 저항 | Anti-crowd-control | From Willpower |
| Perfect Resist / Smite Resist | 완벽 저항 / 강타 저항 | Suppress enemy procs | From Destruction and Time respectively |
| Regeneration / Endurance | 재생 / 기력 | Sustain stats | Paired with their Penetration counterparts |
| HP / MP | 생명력 / 정신력 | Resource pools | Only 0.05 CP per point, so they read as low-value on the CP display |

### PvE and PvP split

The PvE and PvP damage coefficients were separated on 2026-03-25 so classes
could be balanced independently in each. In practice this means several stats
exist in three variants — generic, PvE-only and PvP-only — and that
PvP-specific stats **do not contribute to your displayed Combat Power at all**.
A PvP title or set will read as zero CP.

Chapter 1 abolished the PvP damage resistance cap, so PvP mitigation is now
uncapped where PvE Damage Resistance still caps around 80 percent.

### Stacking rules

These are the rules that decide whether a stat is worth chasing:

- **Damage Amplification, PvE Damage Amplification and Boss Damage
  Amplification all add together into one pool, then multiply.** Consequence:
  the type does not matter, only the total. Take whichever number is larger.
- **Rear Damage Amplification multiplies independently** of that pool, which is
  why it is disproportionately strong.
- **Critical damage is additive**, not multiplicative: base 150 percent plus a
  20 percent bonus gives 170 percent, not 180.
- **Smite is a flat doubling** when it procs, regardless of anything else.
- **Continuous (damage-over-time) effects ignore both Defense and
  Penetration**, which systematically favours classes with DoT-heavy kits.
- **Attribute-to-stat conversion is linear with no diminishing returns.** The
  diminishing returns people observe come from the derived stats' own
  breakpoints, not from the conversion.

### Caps, thresholds and breakpoints

This is the most contested area in the note. Where sources disagree I give both.

| Stat | Value | Confidence and notes |
| --- | --- | --- |
| Damage Resistance | 80 percent cap | Medium. A Korean Guardian player's measurement; not officially published |
| PvP Damage Resistance | No cap | High. Chapter 1 abolished it |
| Attack Power | No cap | High. Chapter 1 abolished the cap |
| Critical Hit chance | No 50 percent cap | Medium-high. A widely believed 50 percent cap was explicitly tested and debunked; one earlier Taiwanese damage-meter analysis still asserts 50 percent, so treat the older figure as superseded |
| Critical Hit chance | Practical ceiling about 80 percent | Medium. A community DPS calculator caps normal-skill crit at 80 percent |
| Critical Hit stat | About 1,179 for good efficiency (roughly 75 to 80 percent chance) | Medium. Single source, from experiment data |
| Critical Hit stat | About 2,150 to be effective in Season 2 top dungeons, or 1,850 to 1,950 with party synergy | Medium. Single source; higher than the efficiency figure because boss Critical Resist is very high |
| Accuracy | About 2,350 required for Sanctuary 2 | Medium. Single source, but a specific and plausible number |
| Smite | 30 percent minimum, 40 percent recommended | Medium. Single source, widely repeated in KR guides |
| Primary attribute caps | None documented | Low. No source publishes attribute caps; the conversion table implies none |

The pattern to take away is that Aion 2's real caps are *content* requirements
rather than mechanical ceilings. Nothing stops you from stacking Accuracy past
2,350; the number matters because that is where a specific raid's parry rate
stops eating your damage.

## Unlock and gates

| Requirement | Opens |
| --- | --- |
| Level 1 | Primary attributes |
| Level 22, 2nd Ascension | [[Pantheon]] statues begin supplying stats |
| Level 32 | Soul imprint, which supplies the highest-value tuned options |
| Level 45 | Monoliths, Bracelet and Arcana, i.e. all three Empyrean Lord attribute sources |

## Inputs: which system supplies which stat

| Stat family | Supplied mainly by |
| --- | --- |
| Primary attributes | Gear base stats, [[Manastones Spirit Stones and Godstones]], [[Pantheon Stats]] |
| Empyrean Lord attributes | [[Kibelisks and Map Registration]] Monoliths, the Bracelet, [[Arcana Cards and Types]] |
| Attack Power, Defense, HP | Gear base stats and [[Enchanting]] / [[Breakthrough]] |
| Accuracy, Critical Hit | [[Manastones Spirit Stones and Godstones]], the "Precise" gear option, titles, pet understanding |
| Damage Amplification | Gear tuned options, [[Daevanion Boards]], [[Arcana Sets and Meta]], pet understanding |
| Smite | Wisdom (Lumiel), so Monoliths, Bracelet and Arcana; plus gear options |
| Combat Speed | Time (Siel), glove tuned options, [[Soul Imprint and Soul Binding]] |
| Boss Damage Amplification / Resistance | [[Titles and Achievements]], Arcana sets, crafted gear |
| Weapon Damage Amplification | Weapon tuning, pet special-race understanding |
| Cooldown Reduction | Illusion (Kaisinel) |
| PvP stats | [[PvP Gear]], [[PvP Boards and Transformations]], PvP titles |
| Flight, movement | [[Wings Enhancement]], Space (Israphel) |

## Progression path

1. **Accuracy to the threshold of the content you are running.** Nothing else
   matters until this is done. Sources of accuracy: the Precise option on
   weapons and off-hands, Freedom (Vaizel), manastones, and the accuracy
   titles.
2. **Smite to 30 percent, then 40.** Wisdom from Monoliths is the cheapest
   route, and Monoliths are one-time collection content you should be doing
   anyway.
3. **Critical Hit toward 1,850 to 2,150** depending on the content and your
   party's synergy buffs.
4. **Damage Amplification everywhere.** Once accuracy, smite and crit are in
   place, amplification is the stat that scales with everything else.
5. **Combat Speed on gloves**, which is the slot's conventional must-have
   option because it converts directly into extra skills per burst window.
6. **Rear Damage Amplification and Attribute Resistance Reduction last**,
   because they are the highest-value options but only reachable through
   endgame tuning.

## Priorities and breakpoints

The KR consensus priority order, for attack and defence in parallel:

| Rank | Offensive | Defensive |
| --- | --- | --- |
| 1 | Accuracy | Damage Resistance |
| 2 | Smite (30 percent required, 40 recommended) | Damage Amplification |
| 3 | Critical Hit | Combat Speed |
| 4 | Attack Power percent | Movement Speed |
| 5 | Attack Speed | Healing |

By role, from a KR stat-priority guide. Class names are given with their
Korean originals because English localisations vary:

| Class | 1st | 2nd | 3rd |
| --- | --- | --- | --- |
| Gladiator (검성) | Accuracy | Smite | Critical |
| Assassin (살성) | Accuracy | Critical | Smite |
| Ranger (궁성) | Accuracy | Critical | Attack Speed |
| Sorcerer / Mage (마도성) | Accuracy | Smite | Critical |
| Spiritmaster (정령성) | Accuracy | Smite | Critical — same row as mage; **`Spirit Strike`** also buffs spirit damage |
| Guardian / Templar (수호성) | Accuracy | Damage Resistance | HP percent |
| Cleric (치유성) | Accuracy | Healing | Damage Resistance |

Note that Accuracy is first for every class including the healer, and that even
tanks need it, because tank damage contributes to clear timers.

Conventional must-have option per gear slot:

| Slot | Must-have | Second choice |
| --- | --- | --- |
| Weapon | Precise (Accuracy plus Critical) | Attack Speed, Power |
| Off-hand / Guarder | Precise, Attack percent | Smite, Critical |
| Chest | Damage Amplification | Attack percent, Critical |
| Legs | Damage Resistance | HP percent, Defense |
| Gloves | Combat Speed | Attack Speed, Critical |
| Helmet | Healing, Smite | HP percent, Damage Resistance |
| Boots | Movement Speed, Attack percent | Smite, Critical |

Manastone reroll priority: Damage Amplification first, then Accuracy and Attack
Power, then Critical Hit and Guaranteed Critical.

Pet understanding option priority: slot 3 takes Critical Hit or Damage
Amplification, slot 6 takes Damage Resistance and then Iron Wall, and the
remaining slots take Attack Power, Accuracy and Critical Hit. Slots 3, 6 and 9
are the ones worth locking for Smite or Damage Amplification. See
[[Pet Understanding]].

Arcana main-stat picks by part, based on Combat Power value and real
contribution: Parchment takes Time, then Destiny; Bell takes Destruction over
Justice; the Libra (Scales) part takes Destruction, then Destiny, then Justice,
then Life. Between Freedom and Death, Death is slightly better. See
[[Arcana Sets and Meta]].

## Costs and math

- Attribute conversion: `derived stat percent = attribute value × rate`, where
  the rate is 0.1 for primaries and 0.2 for Empyrean Lord attributes. Example:
  Wisdom 178 gives +35.6 percent Smite and −35.6 percent MP cost.
- Critical Hit efficiency: roughly 3.5 percent damage per 50 points of the
  Critical Hit stat, from one Korean source's simulation.
- **Intermediate manastones beat Superior manastones for most players.** A
  Superior manastone's blue-tier option rolls 10 while an Intermediate's rolls
  13, so three blue options on an Intermediate reaches 39 against a Superior's
  typical 40. Cost to reach 30 combined Accuracy and Critical: about 960,000
  Kinah with Intermediate stones against about 4,750,000 with Superior — a five
  to seven times difference. Single source, but the mechanism is checkable.
- Intermediate manastones require Alchemy craft level 20; intermediate spirit
  stones require level 25.
- Arcana set effects, for scale: Frenzy gives PvE Attack +50 at 2 pieces and
  Boss Damage Amplification +5 percent plus Boss Damage Resistance +10 percent
  below 70 percent HP at 4 pieces. Pure Blood gives PvE Defense +500 at 2
  pieces and Critical Damage Amplification +5 percent plus Defense +1,000 below
  70 percent HP at 4 pieces.

## Traps and mistakes

- **Dropping Accuracy to raise Combat Power.** The CP formula values Accuracy
  at 0.25 per point, which is far below its real worth for anyone not already
  over the content threshold. This is the defining mistake of the post-2026-03
  meta and Korean analysts warned about it explicitly on patch day.
- **Building into Penetration because it shows huge CP.** Penetration was
  counted at 10 CP per point against an intended 1 to 1.25. It is a bug and it
  is being fixed. Penetration is also offset by target Defense, so it is
  mediocre outside multi-hit skills.
- **Chasing Perfect.** It applies the weapon's maximum damage roll rather than
  multiplying, so its real value is around 5 percent, against Smite's 100
  percent and Critical's 50 percent.
- **Assuming a 50 percent critical cap.** It was tested and is false, and
  building around it leaves a large amount of damage on the table.
- **Distinguishing between Damage Amplification types.** They all add into one
  pool. Take the bigger number and stop agonising.
- **Buying Superior manastones early.** Intermediate stones are the correct
  answer until you are optimising a finished set.
- **Stacking Defense in PvE on a Guardian.** One detailed Korean Guardian
  write-up argues Defense is nearly meaningless in PvE next to Damage
  Resistance, and that a Defense-oriented armour set is not worth taking.

## Global launch notes

The stat vocabulary itself is client data and will ship intact, but the English
localisation of the names is the main unknown. Korean sources use 강타, which
this vault calls **Smite** following aion2hub's datamined naming, but Vortex
Gaming's translations render it as "Strike", u4n as "Heavy Blow", and
"Crushing Blow" appears in some community glossaries. Expect at least a few
official global names to differ from every table here; the Korean term in the
tables above is the stable identifier.

Whether the PvE/PvP coefficient split and the abolished attack power and PvP
resistance caps ship at global launch depends on the content state. All three
are post-launch KR changes.

**Launch Scale Test — new accessory and bind lines KR does not have:**

| Stat | Where it showed up | Why it matters |
| --- | --- | --- |
| **Might** | Earrings, necklace, rings | Increases Attack. Must-have offensive line |
| **Precision** | Same | Crit + Accuracy. Important until those caps, dead after |
| **Move Speed** | Earrings | Must-have alongside Might |
| **Combat Speed** | Necklace | Same weight as on any other slot |
| **Weapon Damage Tolerance** | Chest and helm soul-bind | Best PvP mitigation Welps called out; reason to craft those two pieces |

Built-in PvE Damage Boost was **missing** from crafted and dungeon gear.
Daevanion and title **percentages were cut** (example Empty Closet 5% → 3.5%).
Accuracy/Crit dungeon caps may differ from the KR Sanctuary numbers above.
See [[Accessories]], [[Armor]], [[Global Launch Differences]].

## Open questions

- [ ] Do primary attributes have caps? No source addresses this.
- [ ] The current Critical Hit chance ceiling. Community tools cap normal-skill
      crit at 80 percent, but no one has published the underlying formula.
- [ ] The Damage Resistance 80 percent cap is single-sourced from a player
      measurement. Settled by a developer note or a second measurement.
- [ ] Whether the CP weights for Accuracy and Critical Hit were revised after
      the 2026-03 feedback. Settled by a KR patch note.
- [ ] Exact Accuracy requirements for Sanctuary 3, Sanctuary 4 and the Chapter 1
      dungeons. Only the Sanctuary 2 figure of 2,350 is documented.
- [ ] The official global English name for Smite, Damage Amplification and the
      Empyrean Lord attributes.
- [ ] How Guaranteed Critical (확정 치명) interacts with the crit chance
      ceiling; community calculators treat it as a separate calculation.

## Sources

- [AION 2 Stat Calculator — Attributes, Deity Stats & Smite Formula](https://aion2hub.com/tools/stat-calculator) — EN, datamined from the client `PcStatSecond` table; used for all six primary and ten Empyrean Lord attributes, their conversion targets and per-point rates, the linearity claim, the three sources of Empyrean Lord stats, the internal "HardHit" name for Smite, and Light/Darkness having no conversion.
- [[Aion 2] Damage Meter Appearance and Damage Formula Analysis](https://vortexgaming.io/en/postdetail/624458) — EN translation of a KR analysis of TW damage-meter data; used for Smite 2x, Critical 1.5x, Perfect applying weapon maximum damage, multi-hit at 5 percent per hit to 4 hits, Rear Damage Amplification multiplying independently, damage amplification types adding then multiplying, DoT ignoring defence and penetration, and the older 50 percent crit cap claim.
- [아이온2 데미지 공식 & 스탯 효율 분석](https://game.savetip.co.kr/aion2-damage-formula-stat-guide/) — KR blog; used to debunk the 50 percent crit cap, for critical damage being additive, for the crit stat 1,179 efficiency point, and for Rear Damage Amplification and Attribute Resistance Reduction being the strongest real damage options.
- [아이온2 명중 강타 스탯 우선순위 2026](https://tamagotch.tistory.com/1535) — KR blog, Season 2; used for the five-rank offensive and defensive priority tables, the per-class priority table and the per-slot must-have option table.
- [[아이온2 공략] 상급 마석보다 좋다? 중급 마석작이 '정답'인 이유](https://gamenewb.tistory.com/34) — KR blog, Season 2; used for the crit stat 2,150 requirement, the 1,850 to 1,950 synergy compromise, the 3.5 percent damage per 50 crit figure, and the Intermediate vs Superior manastone option values and Kinah costs.
- [Aion 2 Combat Power System Complete Breakdown](https://vortexgaming.io/en/postdetail/717212) — EN translation of a KR video guide, 2026-03; used for the accuracy 2,350 Sanctuary 2 requirement, the manastone reroll priority order, pet understanding slot recommendations, Arcana main-stat picks by part, PvP stats not counting toward CP, and the Penetration CP bug.
- [Aion 2 Stats Explained 2026](https://www.u4n.com/news/aion-2-stats-explained-2026.html) — EN, SEO source used for leads only; its definitions of Weapon Damage Boost, Damage Tolerance, Critical Damage Tolerance and the Evasion/Block/Parry distinction are consistent with Korean sources, but treat any number in it as unverified.
- [(스압)개인적인 pve 수호성 스킬 특화 및 스티그마 세팅](https://www.inven.co.kr/board/aion2/6438/12045) — KR Inven Guardian board; used for the 80 percent Damage Resistance cap measurement and the argument that Defense is weak in PvE relative to Damage Resistance.
- [아이온2 딜 효율 계산기](https://bongbong99999-debug.github.io/aion2ssow/) — KR community DPS calculator; used for the 80 percent normal-skill crit ceiling and for the treatment of Guaranteed Critical as a separate calculation. Author explicitly labels values as comparative rather than absolute.
- [아이온2 "3월 25일에 클래스별 신규 스티그마 추가한다"](https://www.gametoc.co.kr/news/articleView.html?idxno=107107) and [[뉴스] 전투력 시스템 도입! 아이온2 3/17(화) 라이브 요약](https://www.inven.co.kr/webzine/news/?news=314483) — KR, 2026-03; used for the PvE/PvP coefficient separation date.
- [엔씨 '아이온2', 7월 1일 챕터1 업데이트 확정](https://www.playforum.net/news/articleView.html?idxno=634607) — KR, 2026-06; used for the abolition of the attack power upper cap.
- [(완료) 6/14(일) 여름 쇼케이스 요약](https://www.inven.co.kr/board/aion2/6388/214447) — KR Inven, 2026-06-14; used for the abolition of the PvP damage resistance cap.
- [신규 초월과 천칭 등장! 2/25(수) 패치 핵심 정리](https://www.inven.co.kr/webzine/news/?news=313897&site=aion2) — KR Inven, 2026-02-25; used for the Frenzy and Pure Blood Arcana set effect values and the Marchutan board option types (Weapon Damage Amplification/Resistance, Iron Wall/Regeneration).
- [🐾 [아이온2] 펫작 빠르게 끝내는 완벽 가이드](https://madimi.tistory.com/42) — KR blog; used for special-race pet understanding supplying PvE Attack, Boss Attack and Weapon Damage Amplification, and for the 3/6/9 slot convention.

## Related notes

[[Foundations]] · [[Item Level vs Combat Power]] · [[Progression Phases Roadmap]] ·
[[Level and Ascension]] · [[Skills and Talents]] · [[Stigmas]] ·
[[Daevanion Boards]] · [[Manastones Spirit Stones and Godstones]] ·
[[Soul Imprint and Soul Binding]] · [[Extraction and Refunds]] ·
[[Arcana Sets and Meta]] · [[Pantheon Stats]] · [[Pet Understanding]] ·
[[Wings Enhancement]] · [[Titles and Achievements]] · [[PvP Gear]] ·
[[Glossary KR TW EN]] · [[Global Launch Differences]]
