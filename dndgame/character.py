from __future__ import annotations

from dndgame.dice import roll


class Character:
    """A D&D character with stats, health, and racial bonuses.

    Attributes:
        name: The character's name.
        race: The character's race (Dwarf, Elf, Human, etc.).
        stats: Dictionary mapping stat names to their values.
        base_hp: Base hit points before modifiers.
        hp: Current hit points.
        max_hp: Maximum hit points including modifiers.
        level: Character level.
        armor_class: Armor class for defense.
    """
    def __init__(self, name: str, race: str, base_hp: int) -> None:
        """Initialize a new Character.

        Args:
            name: The character's name.
            race: The character's race (affects stat bonuses).
            base_hp: Base hit points before Constitution modifier.
        """
        self.name: str = name
        self.race: str = race
        self.stats: dict[str, int] = {}
        self.base_hp: int = base_hp
        self.hp: int = 0
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
        """
        print("Rolling stats...\n")
        stats = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
        for stat in stats:
            print(f"Rolling {stat}...")
            self.stats[stat] = roll(6, 3)

        self.max_hp = self.base_hp + self.get_modifier("CON")
        self.hp = self.max_hp

    def apply_racial_bonuses(self) -> None:
        """Apply racial bonuses to ability scores.

        Applies the standard D&D racial bonuses:
        - Dwarf: +2 Constitution
        - Elf: +2 Dexterity
        - Human: +1 to all stats

        Note: Only supports Dwarf, Elf, and Human races currently.
        """
        if self.race == "Dwarf":
            self.stats["CON"] += 2
        elif self.race == "Elf":
            self.stats["DEX"] += 2
        elif self.race == "Human":
            for stat in self.stats:
                self.stats[stat] += 1
