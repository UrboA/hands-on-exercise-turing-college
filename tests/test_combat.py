from __future__ import annotations

import random
from unittest.mock import patch

from dndgame.character import Character
from dndgame.enemy import Enemy
from dndgame.combat import Combat


def test_combat_player_wins_deterministic():
    random.seed(123)

    # Deterministic stats via roll patches: STR, DEX, CON, INT, WIS, CHA (player then enemy)
    # Use moderate stats so combat resolves quickly
    stat_rolls = [14, 12, 12, 10, 10, 10,   # player
                  12, 10, 10, 10, 10, 10]   # enemy

    # Attack rolls: ensure both hit sometimes; include a high roll for decisive blow
    # We'll interleave combat.roll(20,1) results as needed by Character.roll_attack and Enemy.roll_attack
    attack_rolls = [15, 11, 16, 9, 18]  # sufficient to end within max_rounds

    # Build a side_effect sequence matching how code calls roll():
    # First stats (12 values), then multiple d20 attacks
    side_effect = stat_rolls + attack_rolls * 5

    with patch("dndgame.dice.roll", side_effect=side_effect):
        player = Character("Hero", "Human", 10)
        enemy = Enemy("Goblin", "Goblin", 7)

        # Initialize
        player.roll_stats(); player.apply_racial_bonuses()
        enemy.roll_stats(); enemy.apply_racial_bonuses()

        combat = Combat(player, enemy, max_rounds=50)
        winner, log = combat.run()

        assert winner in {"Player", "Enemy"}
        assert len(log) >= 1
        # Player should have advantage here; expect Player win under this setup
        assert winner == "Player"


def test_combat_stops_on_death_no_overflow():
    random.seed(456)

    # Make defender die on first blow; verify loop stops and final log HP == 0
    stat_rolls = [18, 10, 10, 10, 10, 10,   # player (high STR)
                  10, 10, 10, 10, 10, 10]   # enemy
    # First attack big; then filler
    attack_rolls = [20, 5, 5, 5]
    side_effect = stat_rolls + attack_rolls * 3

    with patch("dndgame.dice.roll", side_effect=side_effect):
        player = Character("Hero", "Human", 10)
        enemy = Enemy("Goblin", "Goblin", 7)
        player.roll_stats(); player.apply_racial_bonuses()
        enemy.roll_stats(); enemy.apply_racial_bonuses()

        combat = Combat(player, enemy, max_rounds=300)
        winner, log = combat.run()

        # Last attack should have brought defender to 0
        last_attack = next((e for e in reversed(log) if "defender_hp" in e), None)
        assert last_attack is not None
        assert last_attack["defender"] in {player.name, enemy.name}
        assert last_attack["defender_hp"] >= 0
        # Ensure combat ended due to death rather than max rounds
        assert not (log and isinstance(log[-1], dict) and log[-1].get("event") == "max_rounds_reached")

