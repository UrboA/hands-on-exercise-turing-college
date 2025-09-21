from __future__ import annotations

from dndgame.character import Character


class Spell:
    """A magical spell with casting properties.

    Represents a D&D spell with its basic properties like name, level,
    school of magic, and power level.

    Attributes:
        name: The spell's name (e.g., "Magic Missile", "Fireball").
        level: The spell level (0 for cantrips, 1-9 for leveled spells).
        school: The school of magic (e.g., "Evocation", "Abjuration").
        spell_power: The spell's power level for damage calculations.
    """

    def __init__(self, name: str, level: int, school: str, spell_power: int) -> None:
        """Initialize a new spell.

        Args:
            name: The spell's name.
            level: The spell level (0-9).
            school: The school of magic this spell belongs to.
            spell_power: The spell's power level for damage calculations.
        """
        self.name = name
        self.level = level
        self.school = school
        self.spell_power = spell_power

    def cast(self, caster: Character, target: Character) -> None:
        """Cast the spell on a target.

        This is a base method that should be overridden by specific spell types.
        The base implementation does nothing.

        Args:
            caster: The character casting the spell.
            target: The character being targeted by the spell.
        """
        pass


class SpellBook:
    """A collection of spells available to a character.

    Manages a character's spell list and provides methods to add spells
    and find available spells based on caster level.

    Attributes:
        spells: List of all spells in the spellbook.
    """

    def __init__(self) -> None:
        """Initialize an empty spellbook."""
        self.spells: list[Spell] = []

    def add_spell(self, spell: Spell) -> None:
        """Add a spell to the spellbook.

        Args:
            spell: The spell to add to the spellbook.
        """
        self.spells.append(spell)

    def get_available_spells(self, spell_level: int) -> list[Spell]:
        """Get all spells available at or below a given caster level.

        Args:
            spell_level: The caster's maximum spell level.

        Returns:
            List of spells that can be cast at the given level.
        """
        available = []
        for spell in self.spells:
            if spell.level <= spell_level:
                available.append(spell)
        return available
