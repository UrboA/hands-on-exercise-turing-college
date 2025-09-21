import argparse
import random

from dndgame.character import Character
from dndgame.dice import roll


def create_character(auto_mode=False, default_name="Hero"):
    print("Welcome to D&D Adventure!")

    if auto_mode:
        name = default_name
        print(f"Auto mode: Using default name '{name}'")
    else:
        name = input("Enter your character's name: ")

    print("\nChoose your race:")
    print("1. Human (+1 to all stats)")
    print("2. Elf (+2 DEX)")
    print("3. Dwarf (+2 CON)")

    if auto_mode:
        race_choice = "1"  # Default to Human in auto mode
        print(f"Auto mode: Using default race 'Human'")
    else:
        race_choice = input("Enter choice (1-3): ")

    print("\n")
    race = ["Human", "Elf", "Dwarf"][int(race_choice) - 1]

    character = Character(name, race, 10)
    character.roll_stats()
    character.apply_racial_bonuses()
    return character


def display_character(character):
    print(f"\n{character.name} the {character.race}")
    print("\nStats:")
    for stat, value in character.stats.items():
        modifier = character.get_modifier(stat)
        print(f"{stat}: {value} ({'+' if modifier >= 0 else ''}{modifier})")
    print(f"\nHP: {character.hp}")


def simple_combat(player, auto_mode=False, max_rounds=300):
    print("\nA goblin appears!")
    goblin_hp = 5
    rounds = 0
    log = []

    while goblin_hp > 0 and rounds < max_rounds:
        rounds += 1
        print(f"\nGoblin HP: {goblin_hp}")
        print("\nYour turn!")
        print("1. Attack")
        print("2. Run away")
        print()

        if auto_mode:
            choice = "1"  # Auto mode always attacks
            print("Auto mode: Choosing to attack")
        else:
            choice = input("What do you do? ")

        if choice == "1":
            attack = roll(20, 1)
            if attack >= 10:
                damage = roll(4, 1)
                goblin_hp -= damage
                print(f"You hit for {damage} damage!")
                log.append(f"Round {rounds}: Player hits for {damage} damage")
            else:
                print("You missed!")
                log.append(f"Round {rounds}: Player misses")
        elif choice == "2":
            log.append(f"Round {rounds}: Player runs away")
            return "Goblin", log

    # Check if max_rounds was reached
    if rounds >= max_rounds:
        log.append({"event": "max_rounds_reached", "rounds": rounds})
        # Determine winner based on HP (player wins ties)
        if player.hp >= goblin_hp:
            winner = "Player"
        else:
            winner = "Goblin"
        return winner, log

    # Normal victory
    log.append(f"Round {rounds}: Goblin defeated!")
    return "Player", log


def main():
    parser = argparse.ArgumentParser(description="D&D Adventure Game")
    parser.add_argument("--seed", type=int, help="Set random seed for reproducible gameplay")
    parser.add_argument("--auto", action="store_true", help="Run in auto mode (skip inputs, use default name 'Hero')")
    args = parser.parse_args()

    # Set random seed if provided
    if args.seed is not None:
        random.seed(args.seed)
        print(f"Random seed set to: {args.seed}")

    # Create character with auto mode support
    player = create_character(auto_mode=args.auto)

    # Auto mode settings
    auto_combat_limit = 10 if args.auto else None  # Limit auto mode to 10 combats
    auto_combat_count = 0

    while True:
        print("\nWhat would you like to do?")
        print("1. Fight a goblin")
        print("2. View character")
        print("3. Quit")

        if args.auto:
            auto_combat_count += 1
            if auto_combat_count > auto_combat_limit:
                print(f"Auto mode: Completed {auto_combat_limit} combats, ending auto mode.")
                print("What would you like to do?")
                print("1. Fight a goblin")
                print("2. View character")
                print("3. Quit")
                choice = "3"  # Quit after reaching combat limit
                print("Auto mode: Choosing to quit")
            else:
                choice = "1"  # Default to fighting in auto mode
                print(f"Auto mode: Choosing to fight goblin (combat {auto_combat_count}/{auto_combat_limit})")
        else:
            choice = input("Enter choice (1-3): ")

        if choice == "1":
            winner, log = simple_combat(player, auto_mode=args.auto)

            # Check if max_rounds was reached
            if log and isinstance(log[-1], dict) and log[-1].get("event") == "max_rounds_reached":
                print(f"Combat ended due to reaching maximum rounds ({log[-1]['rounds']})")
                print(f"Winner determined by HP comparison: {winner}")
            elif winner == "Player":
                print("You defeated the goblin!")
            else:
                print("You ran away!")
        elif choice == "2":
            display_character(player)
        elif choice == "3":
            break


if __name__ == "__main__":
    main()
