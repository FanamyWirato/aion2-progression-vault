"""Generate the Obsidian canvas mindmap for this vault.

Run from anywhere:  py "f:\\aion2\\90 Appendix\\tools\\generate_canvas.py"
It rewrites f:\\aion2\\Progression Mindmap.canvas from the CHAPTERS table below,
so the canvas stays in sync whenever notes are added or renamed.
"""

import json
import os

VAULT = r"f:\aion2"
OUT = os.path.join(VAULT, "Progression Mindmap.canvas")

ROOT_LABEL = "# Aion 2 progression\n\nEvery path that makes a character stronger.\nOpen [[Progression Phases Roadmap]] for the order to do them in."

# chapter label, folder, colour, [note file names]
CHAPTERS = [
    ("01 Foundations\nLevels, item level, Combat Power, stats", "01 Foundations", "5", [
        "Foundations",
        "Level and Ascension",
        "Item Level vs Combat Power",
        "Stat Reference",
        "Progression Phases Roadmap",
    ]),
    ("02 Skills and Talents\nSkill levels, Stigmas, Daevanion", "02 Skills and Talents", "6", [
        "Skills and Talents",
        "Skills and Mastery Points",
        "Stigmas",
        "Daevanion Boards",
        "Essence Extraction",
    ]),
    ("03 Equipment\nSlots, tiers and every upgrade layer", "03 Equipment", "1", [
        "Equipment",
        "Weapons",
        "Armor",
        "Accessories",
        "Gear Tiers and Sources",
        "Crafting",
        "Enchanting",
        "Breakthrough",
        "Soul Imprint and Soul Binding",
        "Attunement and Option Rerolls",
        "Potential Enhancement",
        "Runes",
        "Brooch Pendant and Seal Slots",
        "Succession and Transfer",
        "Manastones Spirit Stones and Godstones",
        "Extraction and Refunds",
    ]),
    ("04 Arcana\nCards, sets, refinement", "04 Arcana", "2", [
        "Arcana",
        "Arcana Cards and Types",
        "Arcana Sets and Meta",
        "Arcana Refinement and Farming",
    ]),
    ("05 Pets and Mounts\nCollection, levels, understanding rerolls", "05 Pets and Mounts", "3", [
        "Pets and Mounts",
        "Pet Collection and Levels",
        "Pet Understanding",
        "Species Understanding",
        "Mounts",
    ]),
    ("06 Wings and Flight\nWing stats, enhancement, flight power", "06 Wings and Flight", "5", [
        "Wings and Flight",
        "Wings Acquisition",
        "Wings Enhancement",
        "Flight and Traversal",
    ]),
    ("07 Pantheon\nStatues, frames, Lord stats", "07 Pantheon", "6", [
        "Pantheon",
        "Pantheon Statues and Frames",
        "Pantheon Stats",
        "Nightmare Mode",
    ]),
    ("08 Collections and Exploration\nFeathers, cubes, wardrobe, titles", "08 Collections and Exploration", "4", [
        "Collections and Exploration",
        "Empyrean Traces and Feathers",
        "Monolith Resonance",
        "Garrisons and Sealed Dungeons",
        "Hidden Cubes",
        "Kibelisks and Map Registration",
        "Wardrobe and Skin Collection",
        "Titles and Achievements",
        "Housing",
    ]),
    ("09 PvP Progression\nAbyss Points, ranks, PvP gear", "09 PvP Progression", "1", [
        "PvP Progression",
        "Abyss Points and Ranks",
        "Merit Medals",
        "PvP Gear",
        "PvP Boards and Transformations",
        "Arenas Sieges and Seasons",
    ]),
    ("10 Activities and Economy\nLoops, dungeons, seasons, currencies", "10 Activities and Economy", "3", [
        "Activities and Economy",
        "Daily and Weekly Loops",
        "Shugo Festa",
        "Odyle Energy and Entry Limits",
        "Dungeons and Raids",
        "Trials and Rankings",
        "Consumables and Buffs",
        "Legions",
        "Seasons and Battle Pass",
        "Currencies and Economy",
        "Alts and Account Wide Progression",
    ]),
    ("11 Class Playbooks\nBest in slot plans per class", "11 Class Playbooks", "2", [
        "Class Playbooks",
        "Templar BiS Roadmap",
        "Templar Gear and Slots",
        "Templar Skills and Stigmas",
        "Templar Support Systems",
        "Chanter BiS Roadmap",
        "Chanter Gear and Slots",
        "Chanter Skills and Stigmas",
        "Chanter Support Systems",
    ]),
    ("12 Routines\nDaily and weekly checklists", "12 Routines", "5", [
        "Routines",
        "Daily Routine Main",
        "Weekly Routine Main",
        "Alt Routines",
        "Season 1 Launch Plan",
    ]),
    ("13 Gathering and Professions\nGathering, crafting, conversion, farming", "13 Gathering and Professions", "3", [
        "Gathering and Professions",
        "Gathering Nodes and Plants",
        "Odyle and Special Resources",
        "Professions and Mastery",
        "Material Conversion",
        "Farming Routes and Kinah",
    ]),
    ("90 Appendix\nGlossary, global differences, sources", "90 Appendix", "4", [
        "Season 1 System Availability",
        "Glossary KR TW EN",
        "Global Launch Differences",
        "Sources",
        "Open Questions",
        "Note Template",
    ]),
]

NOTE_W, NOTE_H, NOTE_PITCH = 380, 72, 92
CHAP_W, CHAP_H = 340, 110
CHAP_GAP = 70
COL_ROOT, COL_CHAP, COL_NOTE = 0, 620, 1180

nodes = []
edges = []
y = 0
chapter_ys = []

for chap_label, folder, color, notes in CHAPTERS:
    block_top = y
    chap_id = "chap-" + folder.replace(" ", "-").lower()
    for i, note in enumerate(notes):
        note_id = "note-" + note.replace(" ", "-").lower()
        nodes.append({
            "id": note_id,
            "type": "file",
            "file": f"{folder}/{note}.md",
            "x": COL_NOTE,
            "y": block_top + i * NOTE_PITCH,
            "width": NOTE_W,
            "height": NOTE_H,
            "color": color,
        })
        edges.append({
            "id": f"e-{chap_id}-{note_id}",
            "fromNode": chap_id,
            "fromSide": "right",
            "toNode": note_id,
            "toSide": "left",
        })
    block_height = (len(notes) - 1) * NOTE_PITCH + NOTE_H
    chap_y = block_top + block_height / 2 - CHAP_H / 2
    chapter_ys.append(chap_y)
    nodes.append({
        "id": chap_id,
        "type": "text",
        "text": "## " + chap_label,
        "x": COL_CHAP,
        "y": chap_y,
        "width": CHAP_W,
        "height": CHAP_H,
        "color": color,
    })
    y = block_top + block_height + CHAP_GAP

total_height = y - CHAP_GAP
root_h = 200
nodes.append({
    "id": "root",
    "type": "text",
    "text": ROOT_LABEL,
    "x": COL_ROOT,
    "y": total_height / 2 - root_h / 2,
    "width": 420,
    "height": root_h,
    "color": "3",
})

for (chap_label, folder, color, _notes) in CHAPTERS:
    chap_id = "chap-" + folder.replace(" ", "-").lower()
    edges.append({
        "id": f"e-root-{chap_id}",
        "fromNode": "root",
        "fromSide": "right",
        "toNode": chap_id,
        "toSide": "left",
    })

with open(OUT, "w", encoding="utf-8") as fh:
    json.dump({"nodes": nodes, "edges": edges}, fh, indent=1, ensure_ascii=False)

print(f"wrote {OUT}: {len(nodes)} nodes, {len(edges)} edges")
