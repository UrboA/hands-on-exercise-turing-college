from __future__ import annotations

from dndgame.dice import roll
from dndgame.entity import Entity
from typing import TypedDict, Literal, Union, List, Tuple


class AttackEvent(TypedDict):
    attacker: str
    defender: str
    roll: int
    crit: bool
    dmg: int
    defender_hp: int


class MaxRoundsEvent(TypedDict):
    event: Literal["max_rounds_reached"]
    rounds: int


LogEvent = Union[AttackEvent, MaxRoundsEvent]


class Combat:
    """Orchestrates combat between two Entity instances.

    Manages turn-based combat with proper attack resolution using Entity
    methods and attributes.

    Attributes:
        player: The player Entity.
        enemy: The enemy Entity.
        max_rounds: Maximum number of rounds before forced resolution.
        log: List of combat events.
    """

    def __init__(self, player: Entity, enemy: Entity, max_rounds: int = 300) -> None:
        """Initialize a new combat encounter.

        Args:
            player: The player Entity participating in combat.
            enemy: The enemy Entity participating in combat.
            max_rounds: Maximum rounds before combat is force-resolved.
        """
        self.player: Entity = player
        self.enemy: Entity = enemy
        self.max_rounds: int = max_rounds
        self.log: List[LogEvent] = []

    def run(self) -> Tuple[str, List[LogEvent]]:
        """Orchestrate the combat between player and enemy.

        Alternates turns between entities until one dies or max_rounds
        is reached. Each round, the current attacker attempts to attack
        the defender using Entity.roll_attack().

        Returns:
            A tuple of (winner_name, combat_log) where winner_name is
            either "Player" or "Enemy" and combat_log is a list of dicts
            containing combat events.

        The log format for attacks:
        {
            "attacker": name,
            "defender": name,
            "roll": attack_roll,
            "crit": is_crit,
            "dmg": damage_dealt,
            "defender_hp": defender_hp_after
        }
        """
        self.log = []
        rounds: int = 0
        current_attacker: Entity = self.player
        current_defender: Entity = self.enemy

        while (self.player.alive() and self.enemy.alive() and
               rounds < self.max_rounds):

            rounds += 1

            # Perform attack
            attack_roll, is_crit = current_attacker.roll_attack()
            damage = max(0, attack_roll - current_defender.defense)

            # Apply damage
            current_defender.take(damage)

            # Log the attack
            self.log.append({
                "attacker": current_attacker.name,
                "defender": current_defender.name,
                "roll": attack_roll,
                "crit": is_crit,
                "dmg": damage,
                "defender_hp": current_defender.hp
            })

            # Check if defender died from this attack
            if not current_defender.alive():
                break

            # Alternate turns
            current_attacker, current_defender = current_defender, current_attacker

        # Determine winner
        if rounds >= self.max_rounds:
            # Max rounds reached - determine winner by HP
            self.log.append({
                "event": "max_rounds_reached",
                "rounds": rounds
            })

            if self.player.hp >= self.enemy.hp:
                winner = "Player"
            else:
                winner = "Enemy"
        else:
            # Normal victory
            if self.player.alive():
                winner = "Player"
            else:
                winner = "Enemy"

        return winner, self.log
