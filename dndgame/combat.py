from __future__ import annotations

from dndgame.dice import roll
from dndgame.character import Character


class Combat:
    """Manages combat between two characters.

    Handles initiative rolling, attack resolution, and turn order.

    Attributes:
        player: The player character.
        enemy: The enemy character.
        round: Current combat round number.
        initiative_order: List of characters in initiative order.
    """
    def __init__(self, player: Character, enemy: Character) -> None:
        """Initialize a new combat encounter.

        Args:
            player: The player character participating in combat.
            enemy: The enemy character participating in combat.
        """
        self.player: Character = player
        self.enemy: Character = enemy
        self.round: int = 0
        self.initiative_order: list[Character] = []

    def roll_initiative(self) -> list[Character]:
        """Roll initiative to determine combat order.

        Each character rolls 1d20 + Dexterity modifier to determine
        who acts first in combat.

        Returns:
            List of characters in initiative order (highest to lowest).

        Note:
            The player always goes first on ties.
        """
        player_init = roll(20, 1) + self.player.get_modifier("DEX")
        enemy_init = roll(20, 1) + self.enemy.get_modifier("DEX")

        if player_init >= enemy_init:
            self.initiative_order = [self.player, self.enemy]
        else:
            self.initiative_order = [self.enemy, self.player]

        return self.initiative_order

    def attack(self, attacker: Character, defender: Character) -> int:
        """Resolve an attack roll between two characters.

        The attacker makes an attack roll (1d20 + Strength modifier) against
        the defender's armor class. If successful, deals damage based on
        weapon type (currently fixed at 1d6).

        Args:
            attacker: The character making the attack.
            defender: The character being attacked.

        Returns:
            The amount of damage dealt (0 if attack missed).

        Note:
            Currently uses a fixed 1d6 weapon damage for simplicity.
        """
        attack_roll = roll(20, 1) + attacker.get_modifier("STR")
        weapon_max_damage = 6
        if attack_roll >= defender.armor_class:
            damage = roll(weapon_max_damage, 1)
            defender.hp -= damage
            return damage
        return 0
