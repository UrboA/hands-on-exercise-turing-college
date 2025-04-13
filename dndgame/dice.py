import random


def roll(dice_type: int, number_of_dice: int) -> int:
    """Roll dice and return sum."""
    rolls = []
    total = 0
    for _ in range(number_of_dice):
        roll_result = random.randint(1, dice_type)
        rolls.append(roll_result)
        total += roll_result
    print(f"Rolling {number_of_dice}d{dice_type}: {rolls} = {total}")
    return total


def roll_with_advantage(dice_type: int) -> int:
    """Roll with advantage (roll twice, take highest)."""
    roll1 = roll(dice_type, 1)
    roll2 = roll(dice_type, 1)
    return max(roll1, roll2)


def roll_with_disadvantage(dice_type: int) -> int:
    """Roll with disadvantage (roll twice, take lowest)."""
    roll1 = roll(dice_type, 1)
    roll2 = roll(dice_type, 1)
    return min(roll1, roll2)
