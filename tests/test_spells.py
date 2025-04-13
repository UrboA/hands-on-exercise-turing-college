import pytest
from dndgame.spells import Spell, SpellBook


def test_spell_creation():
    """Test spell initialization with all attributes."""
    spell = Spell("Fireball", 3, "Evocation", 8)
    assert spell.name == "Fireball"
    assert spell.level == 3
    assert spell.school == "Evocation"
    assert spell.spell_power == 8


def test_spellbook_creation():
    """Test spellbook initialization."""
    spellbook = SpellBook()
    assert isinstance(spellbook.spells, list)
    assert len(spellbook.spells) == 0


def test_add_spell():
    """Test adding spells to spellbook."""
    spellbook = SpellBook()
    spell = Spell("Magic Missile", 1, "Evocation", 3)

    spellbook.add_spell(spell)
    assert len(spellbook.spells) == 1
    assert spellbook.spells[0] == spell


def test_get_available_spells():
    """Test filtering spells by level."""
    spellbook = SpellBook()

    # Add spells of different levels
    spells = [
        Spell("Magic Missile", 1, "Evocation", 3),
        Spell("Fireball", 3, "Evocation", 8),
        Spell("Shield", 1, "Abjuration", 2),
        Spell("Wish", 9, "Conjuration", 20),
    ]

    for spell in spells:
        spellbook.add_spell(spell)

    # Test filtering
    level_1_spells = spellbook.get_available_spells(1)
    assert len(level_1_spells) == 2
    assert all(spell.level <= 1 for spell in level_1_spells)

    level_3_spells = spellbook.get_available_spells(3)
    assert len(level_3_spells) == 3
    assert all(spell.level <= 3 for spell in level_3_spells)


def test_empty_spellbook_available_spells():
    """Test getting available spells from empty spellbook."""
    spellbook = SpellBook()
    available = spellbook.get_available_spells(1)
    assert len(available) == 0


def test_spell_cast():
    """Test spell cast method (currently a placeholder)."""
    spell = Spell("Test Spell", 1, "Test", 1)
    # Since cast() is currently a placeholder that does nothing,
    # we just verify it can be called without raising an exception
    spell.cast(None, None)
