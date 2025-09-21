"""Entity base types used throughout the game.

Provides the `Entity` abstract base class with shared attributes
and minimal behavior for all combatants.

Examples:
    >>> from dndgame.entity import Entity
    >>> class Dummy(Entity):
    ...     def roll_attack(self):
    ...         return (1, False)
    >>> d = Dummy("Test", 5, 0, 10)
    >>> d.alive()
    True
    >>> d.take(10); d.alive()
    False
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Entity(ABC):
    """Abstract base class for all entities in the game.

    Defines the common interface for playable characters, enemies,
    and other entities that can engage in combat.

    Attributes:
        name: The entity's display name.
        hp: Current hit points (health).
        attack: Attack bonus/strength value.
        defense: Defense bonus/armor class value.
    """

    def __init__(self, name: str, hp: int, attack: int, defense: int) -> None:
        """Initialize an Entity.

        Args:
            name: The entity's display name.
            hp: Starting hit points.
            attack: Attack bonus value.
            defense: Defense bonus value.
        """
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def alive(self) -> bool:
        """Check if the entity is still alive.

        Returns:
            True if hp > 0, False otherwise.
        """
        return self.hp > 0

    def take(self, dmg: int) -> None:
        """Apply damage to the entity, clamping hp at 0.

        Args:
            dmg: Amount of damage to apply (must be non-negative).
        """
        self.hp = max(0, self.hp - dmg)

    @abstractmethod
    def roll_attack(self) -> tuple[int, bool]:
        """Roll an attack for this entity.

        Returns:
            A tuple of (roll_value, is_crit) where:
            - roll_value: The attack roll result
            - is_crit: True if the roll was a critical hit

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement roll_attack()")
