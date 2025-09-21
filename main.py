import argparse
import random

from dndgame.character import Character
from dndgame.combat import Combat
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
                print("Goodbye!")
                break  # Exit the program
            else:
                choice = "1"  # Default to fighting in auto mode
                print(f"Auto mode: Choosing to fight goblin (combat {auto_combat_count}/{auto_combat_limit})")
        else:
            choice = input("Enter choice (1-3): ")

        if choice == "1":
            # Ensure the player isn't starting combat at 0 HP
            if player.hp <= 0:
                if args.auto:
                    print("Auto mode: Restoring HP to full before combat.")
                    player.hp = getattr(player, "max_hp", player.hp)
                else:
                    resp = input("You are at 0 HP. Rest to recover to full HP before fighting? (y/n): ").strip().lower()
                    if resp.startswith("y"):
                        player.hp = getattr(player, "max_hp", player.hp)
                        print(f"{player.name} rests and recovers to {player.hp} HP.")
                    else:
                        print("You decide not to fight while at 0 HP.")
                        continue
            # Create enemy for combat
            from dndgame.enemy import Enemy
            enemy = Enemy("Goblin", "Goblin", 7)
            enemy.roll_stats()
            enemy.apply_racial_bonuses()

            # Use the new Combat class
            combat = Combat(player, enemy, max_rounds=300)
            winner, log = combat.run()

            # Check if max_rounds was reached
            if log and isinstance(log[-1], dict) and log[-1].get("event") == "max_rounds_reached":
                print(f"Combat ended due to reaching maximum rounds ({log[-1]['rounds']})")
                print(f"Winner determined by HP comparison: {winner}")
            elif winner == "Player":
                print("You defeated the goblin!")
            else:
                print("You were defeated by the goblin!")
        elif choice == "2":
            display_character(player)
        elif choice == "3":
            break


if __name__ == "__main__":
    main()
