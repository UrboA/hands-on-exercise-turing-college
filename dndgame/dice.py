"""Dice rolling helpers.

Pure functions to roll dice with/without advantage or disadvantage.

Examples:
    >>> from dndgame.dice import roll, roll_with_advantage
    >>> total = roll(6, 2); isinstance(total, int)
    True
    >>> isinstance(roll_with_advantage(20), int)
    True
"""

from __future__ import annotations

import random


def roll(dice_type: int, number_of_dice: int) -> int:
    """Roll multiple dice and return the sum.

    Simulates rolling the specified number of dice with the given number
    of sides and returns the total result.

    Args:
        dice_type: The number of sides on each die (e.g., 6 for d6, 20 for d20).
        number_of_dice: How many dice to roll.

    Returns:
        The sum of all dice rolls.

    Examples:
        roll(6, 2)  # Roll 2d6
        roll(20, 1)  # Roll 1d20
    """
    rolls = []
    total = 0
    for _ in range(number_of_dice):
        roll_result = random.randint(1, dice_type)
        rolls.append(roll_result)
        total += roll_result
    print(f"Rolling {number_of_dice}d{dice_type}: {rolls} = {total}")
    return total


def roll_with_advantage(dice_type: int) -> int:
    """Roll a die with advantage.

    Rolls the specified die twice and returns the higher result.
    Commonly used in D&D for situations where a character has advantage
    on a roll (inspiration, flanking, etc.).

    Args:
        dice_type: The number of sides on the die (e.g., 20 for d20).

    Returns:
        The higher of the two dice rolls.

    Examples:
        roll_with_advantage(20)  # Roll d20 with advantage
    """
    roll1 = roll(dice_type, 1)
    roll2 = roll(dice_type, 1)
    return max(roll1, roll2)


def roll_with_disadvantage(dice_type: int) -> int:
    """Roll a die with disadvantage.

    Rolls the specified die twice and returns the lower result.
    Commonly used in D&D for situations where a character has disadvantage
    on a roll (poor visibility, difficult terrain, etc.).

    Args:
        dice_type: The number of sides on the die (e.g., 20 for d20).

    Returns:
        The lower of the two dice rolls.

    Examples:
        roll_with_disadvantage(20)  # Roll d20 with disadvantage
    """
    roll1 = roll(dice_type, 1)
    roll2 = roll(dice_type, 1)
    return min(roll1, roll2)
