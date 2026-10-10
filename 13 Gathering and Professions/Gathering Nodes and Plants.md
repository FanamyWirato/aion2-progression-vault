---
chapter: "13 Gathering and Professions"
system: Gathering (Essence Extraction, 정기 추출)
type: progression-system
unlock: "available from the first zone; open the Essence Extraction window with Alt+F and spend a Specialty Point on a Seeker node before nodes appear on the map"
account_wide: false
cadence: "continuous"
gates: ["Novice 50 for the Professional promotion quest", "a Seeker node per material type to see it on the minimap", "wings and flight duration for Odyle", "possible level 45 floor in KR (disputed)"]
currencies: ["Kinah", "Common Skill Points", "Specialty Skill Points"]
region_verified: ["KR", "TW"]
patch: "KR live as of 2026-09-06; skill tree and quality tiers verified against the 2025-12-22 NC summary and the KR material tables"
confidence: medium
tags:
  - aion2/progression
  - aion2/gathering-professions
---

# Gathering Nodes and Plants

> **In one sentence:** AION 2 collapses mining, logging and foraging into one
> skill called **Essence Extraction** (정기 추출) with six node families, four
> quality tiers per material, and a minimap that shows you nothing at all until
> you spend a Specialty Point.

> **Season 1 verdict.** This is the most launch-stable system in the chapter: all
> six node families, the four quality tiers, three attempts per node, the
> Novice-50 promotion quest and the entire skill tree existed at the Korean
> launch, and everything since has been tuning rather than restructuring. A
> launch player has essentially all of it. Two things to check in the client on
> day one: whether the shipping build carries the **2025-12-17 yield and respawn
> nerf** or the more generous original rates, and whether any level floor applies
> to gathering at all.

## Why it matters

Every profession recipe, most conversion recipes, and all of your consumables
start at a node. Gathering is also the cheapest system in the game to finish:
Korean guides consistently put the full Novice-to-Professional climb at roughly
**one hour** of focused play, which makes it the best time-to-benefit ratio of
anything in this vault. And because most endgame dungeon Kinah is Bound in the
KR build, selling gathered materials is one of the few uncapped *tradable*
income routes. See [[Currencies and Economy]].

## How it works

### One skill, six node families

There is no separate mining or herbalism level. Everything rolls into a single
**정기 추출** level, and the six families only differ in which Specialty Points
apply to them.

| Family | Korean | TW | What the node looks like | Primary consumer |
| --- | --- | --- | --- | --- |
| Ore | 광석 | 礦石 | Rock outcrops, cliff faces, mountain ledges | Blacksmithing, Tailoring/Armor |
| Gem | 보석 | 寶石 | Coloured crystal veins, usually on cliff edges and rock tops | Jewelcrafting, Alchemy |
| Log | 나무 | 木頭 | Trees and stumps in forest | Jewelcrafting (bow, staff), Alchemy |
| Herb | 약초 | 藥草 | Ground plants in grassland and wetland | Alchemy (potions and elixirs) |
| Cooking Ingredient | 요리 재료 | 料理材料 | Ground plants, fruit and vegetables | Cooking |
| Odyle | 오드 | 奧德 | **Floating green orbs in the air** — you must hover on wings | Everything, via [[Material Conversion]] |

Odyle is the odd one out and gets its own note: [[Odyle and Special Resources]].

### Four quality tiers, and what each tier is for

This is the single most useful table in the system, and English guides usually
get it wrong by reporting only three tiers. The Korean material tables list
**four** quality prefixes per material, and the prefix maps directly onto the
grade of gear it can produce.

| Quality | Korean prefix | Client English | Gear grade it feeds |
| --- | --- | --- | --- |
| Standard | (no prefix) | — | Common |
| Fine | 순도 높은 | Fine | Rare |
| Pure | 순수한 | Pure | Heritage (전승) |
| Radiant | 찬란한 | Radiant | Unique and Heroic |

Higher tiers come from the **same nodes at a low chance**, from
**Duty/Mission Quests** (사명 퀘스트) as guaranteed rewards, and from
[[Material Conversion]]. They also pay more gathering XP. The Appraiser
Specialty node raises the chance of an upgraded quality roll.

Because the launch build reportedly caps at Unique, **Radiant is your ceiling
prefix** at Season 1 and Pure is what you will consume in bulk.

### The node itself

- Approach the node and press the **Gathering** prompt.
- Each node allows up to **three extraction attempts**, and they are shared
  with other players — a node someone else has hit twice has one left.
- Success is decided by a race between a blue **success gauge** and a red
  **failure gauge**, the same mechanic crafting uses. Whichever fills first wins.
- Being interrupted mid-extraction loses the attempt with no material and no XP.
- Failed extractions that complete normally **still pay XP** (roughly a third),
  so let a losing attempt finish rather than cancelling it.

One Korean route guide advocates the opposite — cancelling early to "reroll"
for a higher-quality result. That contradicts the wiki's account of how
attempts are consumed and no source corroborates it. Treat the cancel-to-reroll
technique as **confidence low** and do not build a route around it.

### Respawn behaviour

Nodes respawn on a timer after being exhausted, which is why the standard
technique is a **circular route across several clusters** rather than camping
one spot: by the time you return, the first cluster is back. No source checked
publishes an exact respawn interval, and it is not uniform.

What is documented is that respawn got **worse**. The first major KR update after
launch, on **2025-12-17**, explicitly lowered both the **acquisition rate and the
respawn speed of gathering nodes** (채집물 획득률, 리스폰 속도 하향). Plan routes
on the assumption that a single cluster cannot sustain you.

**This one cuts in the launch player's favour if it is absent.** The nerf landed
28 days after the Korean launch, so a Season 1 build could plausibly ship the
pre-nerf rates. If your first hour of gathering feels unexpectedly generous
compared with the Korean guides, that is why, and it makes a launch-window
gathering-to-Market play better than this note's figures suggest.

Contested nodes are a real constraint, not a theoretical one. **Asvata Log** in
particular is described as heavily competed in multiple Korean guides, and the
recommended answer is not to fight for it but to gather Odyle and convert.

### The skill tree

Levelling pays two point currencies. Three **Common Skill Points** skills apply
to every extraction:

| Skill | Korean | Effect |
| --- | --- | --- |
| Proficient Handling | 능숙한 손놀림 | Increases success-gauge gain |
| Delicate Touch | 섬세한 손길 | Reduces failure-gauge gain |
| Lady Luck | 행운의 여신 | Chance of a large success surge when the extraction is about to fail |

Costs are 1 point per level for 1–5 and 5 points per level for 6–10. The
Taiwanese consensus priority is **Lady Luck first**, then Proficient Handling
and Delicate Touch equally, because Lady Luck rescues attempts that are already
losing and therefore converts directly into yield.

Each of the six families then has three **Specialty Skill Point** nodes,
unlocked in order:

| Node | Korean | Cost | Effect |
| --- | --- | --- | --- |
| Seeker | 탐색 | 1 | Shows that material type on the minimap / compass |
| Plentiful Harvest | 풍요로운 수확 | 1–3 | +10% per level chance of a double yield, max 30% |
| Appraiser | 감정사 | 1–3 | +10% per level chance of an upgraded quality, max 30% (for Cooking Ingredients it increases quantity instead) |

**Seeker is not optional.** Both Taiwanese guides open with the same warning:
new players think the world has no nodes because the minimap is empty, and it
is empty because no Seeker is trained.

You cannot max everything. Full investment would need **90 Common and 42
Specialty Points**; 100 levels of Essence Extraction only yield **65 Common and
14 Specialty**. Respec costs **50,000 Kinah** and is available at any time.

### Levelling and the promotion quest

| Stage | Korean | Levels | How to get there |
| --- | --- | --- | --- |
| Novice | 입문 | 1–50 | Gather anything; volume beats value |
| — | 정기 추출 전문 기술 | promotion | Auto-generated at Novice 50; gather one **Shining Ruby** (빛나는 루비) and report to the faction NPC |
| Professional | 전문 | 1–50 | The current ceiling; Professional 50 is max |

The promotion quest is the only genuine speed bump. Notes on it:

- **Shining Ruby drops from Ruby nodes at a low chance regardless of the
  quality you actually extract.** Players routinely assume they need to roll a
  Unique Ruby; they do not. Any successful Ruby extraction can produce it.
- Expect roughly **15–25 raw Ruby extractions** for one Shining Ruby.
- It is **quest-only and untradable**, so you must gather it yourself.
- Ruby nodes sit on **cliff edges and rock tops**, not on flat ground, so bring
  wings and take the Gem Seeker first. See [[Flight and Traversal]].
- After the quest you restart at Professional level 1.

For fast levelling, the repeated advice is to farm a **dense cluster of
material slightly below your current proficiency** rather than chasing the
highest-tier nodes, and to gather while doing something else — dungeon queues,
party waits, quest routes.

## Unlock and gates

- No level requirement in any Korean gathering guide checked; you gather from
  the first zone. Korea's January 2026 anti-bot package reportedly set resource
  gathering to **level 45**, which the guides do not reflect. Unresolved; see
  Open questions.
- **Seeker node** per material type before it appears on the map.
- **Wings** for Odyle, and Ruby/Ore nodes on cliffs. Flight duration is the real
  limiter on Odyle routes.
- **Novice 50** for the Professional promotion quest.
- No tool items. AION 2 has no pickaxe/axe/sickle equipment; guides describing
  "use a pick to mine" are importing conventions from other MMOs and one of
  them is a bot-tool site. There is a reported gathering-oriented **gear set**
  and movement-speed scrolls that improve throughput, but that is a
  gear-optimisation choice, not an unlock requirement.

## Node catalogue by family

### Ore (광석)

| Material | Korean | Feeds |
| --- | --- | --- |
| Orichalcum Ore | 오리하르콘 | Blacksmithing weapons and Tailoring/Armor at every grade; the single most-consumed base material in the game |

Ore is a one-material family, which is why Blacksmithing is the easiest
profession to feed and why "mine Orichalcum, refine into ingots, repeat" is the
standard mastery-levelling loop. See [[Professions and Mastery]].

### Gem (보석)

| Material | Korean | Feeds |
| --- | --- | --- |
| Ruby Ore | 루비 원석 | Jewelcrafting **necklaces**; Alchemy scrolls (Sorcerer-side); the Brooch craft |
| Sapphire Ore | 사파이어 원석 | Jewelcrafting **rings** and Orbs; Alchemy (Spiritmaster-side); the Brooch craft |
| Diamond Ore | 다이아몬드 원석 | Jewelcrafting **earrings**; from Fine grade upward, weapon, armor and accessory crafting generally; the Brooch craft |

Gems are the highest-demand family on the Market because accessory enhancement
consumes them continuously. Korean route guides say Ruby has the heaviest
demand and Diamond the better margin. All three Pure-grade gemstones plus Pure
Odyle are the bulk of the Brooch's cost — see [[Brooch Pendant and Seal Slots]].

### Log (나무)

| Material | Korean | Feeds |
| --- | --- | --- |
| Asvata Log | 아스바타 나무 | Jewelcrafting bows and staves, Guards, higher-grade Alchemy scrolls |
| Yggdrasil Log | (이그드라실) | The faction-mirror log; appears in the conversion data alongside Asvata at all four qualities |

The Asvata/Yggdrasil pairing is inferred from the conversion browser listing
both at every quality tier while every other family has a single line; the
Korean name for the Yggdrasil log was not observed directly. **Confidence
medium.**

### Herb (약초)

Herbs are faction-mirrored and there are only two per faction.

| Elyos | Asmodian | Feeds |
| --- | --- | --- |
| Angelica (안젤리카) | Annus (안누스) | Life Potion, Wind Elixir (the flight potion); Fresh grade makes the superior versions |
| Tarragon (타라곤) | Calendula (카렌두라) | Mind and Healing Potions, Wind Elixir; Fresh grade makes superior Healing and Wind |

The upgraded prefix on herbs is **신선한** ("Fresh") rather than the
Fine/Pure/Radiant ladder used by ore and gems, which is a real inconsistency in
the data and not a translation error.

**Flight potions are the sleeper item here.** NC's own summary flags the
flight and mind potions as popular, high-demand goods with strong Abyss and
Rift-of-Time-and-Space demand. Herb gathering into potion crafting is the
lowest-capital seller in the game.

### Cooking Ingredient (요리 재료)

Also faction-mirrored, four per faction, plus shared monster drops.

| Elyos | Asmodian | Cooking effect of the dish |
| --- | --- | --- |
| Morpha (모르파) | Raydam (레이담) | HP / MP and Action Point natural recovery |
| Sherry (쉐리) | Conide (코니데) | Block, Critical, max Action Points |
| Kukur (쿠쿠르) | Ohkra (오크라) | Attack, Defense, max Action Points |
| Killi (킬리) | Pujery (푸제리) | Evasion, Critical, Attack, Accuracy |

Transliterations for the Elyos side are unstable across sources — NC's own post
writes them as 쉐리, 멜라, 쿠쿠르, 킬리 while the English database renders the
mirrors as Morfa, Conide, Ohkra and Pujery, and one machine translation
produced "Sherimella" and "Coriolis". Treat the Elyos names as **confidence
medium** and the effects as high.

Not gathered, but cooking materials all the same:

| Material | Korean | Source |
| --- | --- | --- |
| Fresh Raw Meat | 싱싱한 생고기 | Monster drops |
| Fresh Fruit | 신선한 열매 | Monster drops |
| Draconic Tender Meat | 용족의 부드러운 고기 | Draconic monsters; Heritage-grade cooking |
| Draconic Sweet Fruit | 용족의 달콤한 열매 | Ruby Isle (홍옥의 섬, Elyos) / Spirit Isle (정령의 섬, Asmodian); Heritage-grade cooking |

### Odyle (오드)

Air-only. Fully covered in [[Odyle and Special Resources]].

## Where the density is

Zone names below are the Korean live names. The two starting faction maps are
**Verteron** (베르테론, Elyos) and **Altgard** (알트가르드, Asmodian); Chapter 1
added **Eltnen** (엘테넨) and **Morheim** (모르헤임). At Season 1 you should
expect the Verteron/Altgard band plus the mid-level zones, in the 0–3,800 item
level range.

### Elyos

| Spot | Korean | Best for | Notes |
| --- | --- | --- | --- |
| Dawn Legion Base | 새벽의 레기온 기지 | **Odyle** | The standout Odyle spot. Wide aerial volume, dense orbs; with Odyle Seeker trained, 10 focused minutes reportedly covers a whole week of conversion crafts |
| Verteron Fortress Ruins entrance, mid Elun River | 베르테론 요새 폐허 / 엘룬강 중류 | **Ruby** | Highest reported Ruby density and a short loop; the standard Shining Ruby farm |
| Garden of the Illusion God, upper cliff | 환영신의 정원 | Ruby | Cliff-top nodes, needs flight |
| Ortum Coast | 오르툼 해안 | **Orichalcum** | Ore runs along the cliff line; the route advice is to start at the coast then sweep to the map's 11 o'clock and 7 o'clock clusters |
| Ruby Isle | 홍옥의 섬 | Draconic Sweet Fruit | Cooking material, relatively safe |

### Asmodian

| Spot | Korean | Best for | Notes |
| --- | --- | --- | --- |
| NE of the Muddy Camp kibelisk | 진흙탕 야영지 | **Ruby** | Many spawn points; the in-game quest itself points here |
| NW cliff from the Kwairing Camp kibelisk | 콰이링 야영지 | Ruby | Cliff nodes |
| SE cliff by the Steelhammer Temporary Trading Post | 강철망치 임시 교역소 | Ruby, Diamond | Far east of the map |
| Altgard mountain ranges, behind the ridgelines | 알트가르드 산맥 | **Diamond** | Rougher terrain, higher-value nodes; the hidden spots behind the ranges are the point |
| Spirit Isle | 정령의 섬 | Draconic Sweet Fruit | Cooking material |

**Herbs** cluster in grassland and wetland, **ore** in mountains and highlands,
**gems** on cliffs and rock tops, **logs** in forest, **Odyle** in open sky.
That is the general rule the Taiwanese guides give and it holds across both
maps.

For precise points, use the community interactive maps rather than screenshots:
select faction, filter to the single material you want, then design a circular
route around the densest cluster so the respawn timer works in your favour.
[[Kibelisks and Map Registration]] matters here — register the kibelisk closest
to your loop.

## Efficient route advice

1. **Filter to one material per run.** Mixed routes look efficient and are not,
   because each family has its own cluster geography.
2. **Design a circle, not a line.** Three or four clusters visited in rotation
   beats camping one, given the nerfed respawn rate.
3. **Overlap gathering with something else.** The best-regarded Korean routine
   is to take a Duty Quest whose kill target sits in a herb-dense zone and do
   both at once. Duty Quests also pay guaranteed high-quality materials, which
   is the answer to contested nodes.
4. **Clear the mobs first.** Aggro during extraction is a failed attempt.
5. **Bring flight potions** for Odyle and cliff work, and movement-speed
   scrolls for ground routes. One route guide measured a **30%+ swing in yield
   per hour** from movement speed and a gathering-oriented gear setup;
   single-source, **confidence low**, but the direction is not controversial.
6. **Watch your wings on Odyle.** Taiwanese guides are blunt: running out of
   flight time over a drop kills you. Every one of them has the same warning.
7. **Share locations with your Legion.** Live position sharing is repeatedly
   cited as the single biggest practical efficiency gain on contested nodes.
8. **Stack event windows.** Running a route while Shugo Festa or Dimensional
   Invasion is up lets one block of time pay twice.

A cosmetic bonus drops from gathering at a low rate: an **appearance package**
(외형 꾸러미, "Pokorun"). It is not progression, but do not vendor it — see
[[Wardrobe and Skin Collection]].

## Costs and math

Reported gathering XP, for route planning:

| Material | Success XP | Fail XP |
| --- | --- | --- |
| Standard Orichalcum Ore | 24 | 8 |
| Fine Orichalcum Ore | 31 | 10 |
| Pure Orichalcum Ore | 38 | 12 |
| Standard Odyle | 28 | — |
| Fine Odyle | 36 | — |

Income: one Korean route guide claims **500,000 to 2,000,000 Kinah per hour**
from a dedicated gathering route including incidental drops. That is a single
blog with no methodology, and it is the highest figure anywhere;
**confidence low.** A second, more conservative Korean income table puts plain
herb-and-ore gathering at "hundreds of thousands per day" as a background
activity. Both are believable descriptions of different intensities. See
[[Farming Routes and Kinah]].

## Priorities and breakpoints

- **Seeker nodes before anything else.** An untrained minimap is the number one
  reason new players think gathering is broken.
- **Lady Luck to 5 early.** It is the highest-value Common Skill Point spend.
- **Novice 50 → promotion → Professional as one continuous session.** The
  system is short enough that stopping halfway wastes the momentum.
- **Then seven Specialty Points into Odyle** and one Common skill finished.
  Everything else comes from conversion.
- **Gem Seeker second**, both for the promotion quest and because gems are the
  best sellers.
- Stop caring about Ore and Log specialisation entirely. Odyle plus conversion
  covers them, and Asvata is the most contested node in the game.

## Traps and mistakes

- Spreading Specialty Points across all six families, then paying 50,000 Kinah
  to fix it. Focus Odyle.
- Farming Asvata Log by hand because a recipe wants it, instead of converting
  Odyle.
- Chasing a Unique-quality Ruby for the promotion quest. Quality is irrelevant.
- Cancelling an extraction you think will fail — the attempt is already spent
  and finishing it pays XP.
- Extracting Odyle over a cliff on the last seconds of flight time.
- Camping a single node cluster after the respawn nerf.
- Vendoring the cosmetic package that drops from gathering.
- Gathering "everything" for the first ten levels and filling your bag. Decide
  your one profession first and gather for it, plus Odyle.

## Global launch notes

Gathering should be the most launch-stable system in this chapter, because it
existed complete at KR launch and the changes since have been tuning rather
than restructuring. Expect the six families, four qualities, three-attempt
nodes, the Novice-50 promotion quest and the same skill tree.

Two things to check in the client on day one: whether any level floor applies
to gathering, and whether the post-launch respawn nerf is in the shipping data
or whether global gets the more generous original rates. See
[[Global Launch Differences]].

## Open questions

- [ ] Whether the KR level 45 gathering gate exists at global launch. The
      January 2026 anti-bot reporting says yes; Korean gathering guides written
      afterwards describe unrestricted levelling. Settled by the client.
- [ ] Exact node respawn intervals per family. No source publishes them.
- [ ] The Korean name and faction split for the Yggdrasil Log.
- [ ] Whether "cancel to reroll quality" does anything. One route guide claims
      it; the mechanic as documented says the attempt is already consumed.
- [ ] The Elyos cooking-ingredient names. 쉐리 / 멜라 may be one item
      ("Sherimella") or two.
- [ ] Whether a gathering-specific gear set exists as a real item category or
      whether that guide means ordinary movement-speed stat gear.
- [ ] Whether Herb uses a two-tier (Standard / Fresh) quality ladder while
      other families use four, or whether the higher herb tiers simply were not
      listed.

## Sources

- [퍼플 라운지 — [AION2] 아이온2 정기 추출 🌱 왜 필수인가?](https://lounge.plaync.com/feed/52266?country=KR&locale=ko-KR) — KR, NC official community, 2025-12-22, read 2026-09-06. Supported: the name 정기 추출, the six specialty families in Korean, the three Common skills with their exact effects, the Seeker / Plentiful Harvest / Appraiser node functions including the Cooking-Ingredient Appraiser exception, the faction-split herb and cooking-ingredient lists, flight and mind potions as high-demand goods, the ~30 min + 30–60 min levelling estimate, the Shining Ruby promotion quest, and the cosmetic package drop.
- [아이온2 획득처 완벽 정리: 강화석, 오드부터 제작 재료까지](https://game.savetip.co.kr/%ec%95%84%ec%9d%b4%ec%98%a82-%ec%9e%ac%eb%a3%8c-34%ec%a2%85-%ed%9a%8d%eb%93%9d%ec%b2%98-%ec%99%84%eb%b2%bd-%ec%a0%95%eb%a6%ac-%ea%b0%95%ed%99%94%ec%84%9d-%ec%98%a4%eb%93%9c%eb%b6%80%ed%84%b0/) — KR, read 2026-09-06. Supported: the four-tier quality ladder with the exact Korean prefixes 순도 높은 / 순수한 / 찬란한 and the grade each feeds, the per-material consumer table for Orichalcum, Asvata, Ruby, Sapphire and Diamond, the two-herb-per-faction list with 신선한 as the herb prefix, the eleven cooking materials with their dish effects, and Duty Quests as a guaranteed high-quality material source. Affiliate-style guide site, so treated as a data table rather than as analysis.
- [Gathering, Aion 2 Wiki](https://aion2.wiki.fextralife.com/Gathering) — EN, updated 2026-01-09, read 2026-09-06. Supported: the six categories, three attempts per node shared between players, the success/failure gauge, interruption losing the attempt, the point budget of 65 Common and 14 Specialty against 90 and 42, the 50,000 Kinah respec, the Odyle-must-be-gathered-in-flight rule, and the XP table.
- [아이온2 빛나는 루비 위치 총정리｜정기 추출 승급 퀘스트 완벽 공략](https://choatravel.tistory.com/220) — KR, read 2026-09-06. Supported: 입문 50 → auto-accepted promotion quest → 전문, Professional 50 as the current ceiling, one node giving up to three consecutive extractions, roughly 15–25 rubies per Shining Ruby, Shining Ruby being quest-only and untradable, the named Elyos and Asmodian ruby spots, and the respawn-and-rotate advice.
- [[아이온2] 정기추출 50렙 승급 가이드: '빛나는 루비' 획득 꿀팁](https://lnm015.tistory.com/58) — KR, read 2026-09-06. Supported: Shining Ruby drops regardless of the quality rolled — the specific misconception this note corrects.
- [아이온2 인벤 — 채집 등급업 퀘 - 정기추출 전문기술 - 루비 위치 (천족)](https://www.inven.co.kr/board/aion2/6444/392) — KR community, read 2026-09-06. Supported: ruby nodes sit on cliff edges and rock tops rather than on the ground, so flight is required.
- [아이온2 정기추출 스킬 트리 추천 입문부터 전문까지](https://vgamelifev.com/%ec%95%84%ec%9d%b4%ec%98%a82-%ec%a0%95%ea%b8%b0%ec%b6%94%ec%b6%9c-%ec%8a%a4%ed%82%ac-%ed%8a%b8%eb%a6%ac-%ec%b6%94%ec%b2%9c-%ec%9e%85%eb%ac%b8-%ec%a0%84%eb%ac%b8-%ea%b3%b5%eb%9e%b5/) and [아이온2 정기추출 가이드 2026 최신](https://vgamelifev.com/%ec%95%84%ec%9d%b4%ec%98%a82-%ec%a0%95%ea%b8%b0%ec%b6%94%ec%b6%9c-%ec%a0%84%eb%ac%b8-%ec%8a%b9%ea%b8%89-%ec%8a%a4%ed%82%ac-%ed%8a%b8%eb%a6%ac-%ed%9a%a8%ec%9c%a8-%eb%a0%88%eb%b2%a8%ec%97%85/) — KR, read 2026-09-06. Supported: the unified level rather than per-material levels, Alt+F as the window hotkey, Novice and Professional each capping at 50, restarting at Professional 1, and the gather-during-downtime advice.
- [《AION2》萃取與製作攻略｜新手必懂材料來源與培養順序](https://sticweb.tw/aion2-%e8%90%83%e5%8f%96%e8%88%87%e8%a3%bd%e4%bd%9c%e6%94%bb%e7%95%a5/) and [《AION2》採集製作與料理速成攻略](http://a.ptt543.com/thread-447613-1-1.html) — TW, read 2026-09-06. Supported: the minimap shows nothing without a Seeker skill, the recommended Seeker order, the Lady Luck > Handling = Touch priority, the Traditional Chinese family names, the terrain-to-material mapping, and the Odyle wing-durability death warning.
- [아이온2 천족 마족 채집 재료 지도 위치 공략 가이드 총정리](https://danasn.tistory.com/3802) — KR, 2025-12, read 2026-09-06. Supported: the Ortum Coast Orichalcum cliff line and the 11 o'clock / 7 o'clock sweep, clearing mobs first, stacking Shugo Festa and Invasion windows, and the 500,000–2,000,000 Kinah per hour claim recorded here as **low confidence**.
- [아이온2 채집 지도 및 재료 위치 가이드](https://game.savetip.co.kr/aion2-gathering-map-guide/) — KR, read 2026-09-06. Supported: Verteron as the flat Ruby map and Altgard as the rugged Diamond map, the interactive-map workflow (faction → filter one material → circular route), farming slightly below your proficiency to level fastest, and the 30%+ throughput claim from movement speed and gathering gear, recorded as **low confidence**.
- [아이온2 오드 에너지 충전 방법 총정리](https://saiha.tistory.com/560912) — KR, read 2026-09-06. Supported: Dawn Legion Base as the dense Elyos Odyle area and the ten-minutes-covers-the-week claim.
- [아이온2, 첫 번째 업데이트에서 뭐가 바뀔까?, 게임톡](https://www.gametoc.co.kr/news/articleView.html?idxno=104274) — KR games press, read 2026-09-06. Supported: the first post-launch update lowering gathering acquisition rate and respawn speed, plus the Jewelcrafting bracelet blueprint and new Alchemy scrolls added at the same time.
- [아이온2 제작 공략: 직업별 추천 및 필수 재료 파밍 Top 4](https://game.savetip.co.kr/aion2-crafting-guide-materials/) and [아이온2 제작 공략: PVE 엔드급 무기(기룡왕) 100% 가이드](https://game.savetip.co.kr/aion2-crafting-guide-pve-weapon/) — KR, read 2026-09-06. Supported: Asvata Log being the most contested node and conversion being the recommended answer, and overlapping Duty Quest routes with gathering routes.
- [AION 2 Conversion & Exchange Recipes](https://aion2hub.com/tools/conversion) — KR client data, read 2026-09-06. Supported: the client English strings Fine / Pure / Radiant, and both Asvata Log and Yggdrasil Log appearing at every quality tier.
- [Aion2 采集系统与资源获取指南](https://www.aion.onl/blog/2025/09/01/Aion2-%E9%87%87%E9%9B%86%E7%B3%BB%E7%BB%9F%E4%B8%8E%E8%B5%84%E6%BA%90%E8%8E%B7%E5%8F%96%E6%8C%87%E5%8D%97/) — zh-CN, read 2026-09-06. **Distrusted.** It describes separate Miner and Herbalist professions, pickaxes, axes, fishing rods and an "auto-gathering tool", none of which match AION 2; the site sells automation software. Recorded only to warn that the "use a pick to mine" advice circulating in English comes from this family of pages.
