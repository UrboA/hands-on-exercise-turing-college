from __future__ import annotations

from unittest.mock import patch

from dndgame.character import Character


def test_roll_stats_initializes_core_fields():
    # Mock totals for 3d6 per stat in order: STR, DEX, CON, INT, WIS, CHA
    with patch("dndgame.dice.roll", side_effect=[12, 14, 14, 8, 13, 11]):
        c = Character("Hero", "Human", 10)
        c.roll_stats()

        assert set(c.stats.keys()) == {"STR", "DEX", "CON", "INT", "WIS", "CHA"}
        assert c.stats["STR"] == 12
        assert c.stats["DEX"] == 14
        assert c.stats["CON"] == 14

        # CON 14 -> modifier +2, so max_hp = base_hp (10) + 2
        assert c.max_hp == 12
        assert c.hp == 12

        # STR 12 -> modifier +1
        assert c.attack == 1
        # Defense mirrors armor_class default 10
        assert c.defense == 10


def test_apply_racial_bonuses_human_elf_dwarf():
    # Start with baseline stats
    base_stats = {"STR": 10, "DEX": 10, "CON": 10, "INT": 10, "WIS": 10, "CHA": 10}

    # Human: +1 all
    human = Character("H", "Human", 10)
    human.stats = base_stats.copy()
    human.apply_racial_bonuses()
    assert all(v == 11 for v in human.stats.values())

    # Elf: +2 DEX
    elf = Character("E", "Elf", 10)
    elf.stats = base_stats.copy()
    elf.apply_racial_bonuses()
    assert elf.stats["DEX"] == 12
    for k, v in elf.stats.items():
        if k != "DEX":
            assert v == 10

    # Dwarf: +2 CON
    dwarf = Character("D", "Dwarf", 10)
    dwarf.stats = base_stats.copy()
    dwarf.apply_racial_bonuses()
    assert dwarf.stats["CON"] == 12
    for k, v in dwarf.stats.items():
        if k != "CON":
            assert v == 10


