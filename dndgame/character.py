"""Character implementation for the player.

Defines `Character`, a concrete `Entity` with ability scores, racial
bonuses, and player-specific attack behavior (supports crits).

Examples:
    >>> from dndgame.character import Character
    >>> c = Character("Hero", "Human", 10)
    >>> c.roll_stats(); c.apply_racial_bonuses()
    >>> c.alive()
    True
"""

from __future__ import annotations

from dndgame.dice import roll
from dndgame.races import apply_race_bonuses
from dndgame.entity import Entity


class Character(Entity):
    """A D&D character with stats, health, and racial bonuses.

    Inherits from Entity and adds character-specific functionality
    like stat rolling and racial bonuses.

    Attributes:
        name: The character's name (inherited from Entity).
        race: The character's race (Dwarf, Elf, Human, etc.).
        stats: Dictionary mapping stat names to their values.
        base_hp: Base hit points before modifiers.
        hp: Current hit points (inherited from Entity).
        max_hp: Maximum hit points including modifiers.
        level: Character level.
        armor_class: Armor class for defense.
        attack: Attack bonus (derived from STR modifier).
        defense: Defense bonus (same as armor_class).
    """
    def __init__(self, name: str, race: str, base_hp: int) -> None:
        """Initialize a new Character.

        Args:
            name: The character's name.
            race: The character's race (affects stat bonuses).
            base_hp: Base hit points before Constitution modifier.
        """
        # Initialize Entity with placeholder values
        # These will be updated after stats are rolled
        super().__init__(name, 0, 0, 10)  # hp=0, attack=0, defense=10

        self.race: str = race
        self.stats: dict[str, int] = {}
        self.base_hp: int = base_hp
        self.max_hp: int = 0
        self.level: int = 1
        self.armor_class: int = 10

    def get_modifier(self, stat: str) -> int:
        """Calculate the ability score modifier for a given stat.

        Args:
            stat: The stat name (e.g., 'STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA').

        Returns:
            The ability modifier (positive or negative integer).

        Raises:
            KeyError: If the stat is not found in self.stats.
        """
        return (self.stats[stat] - 10) // 2

    def roll_stats(self) -> None:
        """Roll ability scores for all six stats and calculate hit points.

        This method generates random values for STR, DEX, CON, INT, WIS, and CHA
        using 3d6 rolls, then calculates max HP including Constitution modifier.
        Also updates Entity attributes (attack and defense).
        """
        print("Rolling stats...\n")
        stats = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
        for stat in stats:
            print(f"Rolling {stat}...")
            self.stats[stat] = roll(6, 3)

        self.max_hp = self.base_hp + self.get_modifier("CON")
        self.hp = self.max_hp

        # Update Entity attributes after stats are rolled
        self.attack = self.get_modifier("STR")  # Attack bonus from STR
        self.defense = self.armor_class  # Defense is armor class

    def apply_racial_bonuses(self) -> None:
        """Apply racial bonuses to ability scores via the race registry."""
        apply_race_bonuses(self.stats, self.race)

    def roll_attack(self) -> tuple[int, bool]:
        """Roll an attack for this character.

        Returns:
            A tuple of (roll_value, is_crit) where:
            - roll_value: The attack roll result (1d20 + STR modifier)
            - is_crit: True if the roll was a critical hit (natural 20)
        """
        attack_roll = roll(20, 1)  # Roll 1d20
        is_crit = (attack_roll == 20)  # Natural 20 is always a crit
        roll_value = attack_roll + self.attack  # Add STR modifier

        return roll_value, is_crit
