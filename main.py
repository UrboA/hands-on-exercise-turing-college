import argparse
import random

from dndgame.character import Character
from dndgame.combat import Combat
from dndgame.dice import roll
from dndgame.races import list_races, get_race, register_race, STAT_NAMES


def create_character(auto_mode=False, default_name="Hero"):
    """Create and initialize the player's character.

    Interactively (or non-interactively in --auto mode) collects a name
    and race, applies racial bonuses, rolls initial stats, and returns a
    ready-to-play `Character` instance.

    Args:
        auto_mode: When True, skip prompts and use safe defaults.
        default_name: Fallback name when none is provided.

    Returns:
        Character: The initialized player character.
    """
    print("Welcome to D&D Adventure!")

    if auto_mode:
        name = default_name
        print(f"Auto mode: Using default name '{name}'")
    else:
        name = input("Enter your character's name: ").strip()
        if not name:
            # Re-prompt once if empty after stripping; then fallback to default
            name = input("Name cannot be empty. Please enter a name: ").strip()
            if not name:
                name = default_name
                print(f"No name provided. Using default name '{name}'.")

    print("\nChoose your race:")
    available = list_races()
    for idx, r in enumerate(available, start=1):
        print(f"{idx}. {r}")
    print("C. Custom (define your own race)")

    if auto_mode:
        race = "Human"
        print(f"Auto mode: Using default race '{race}'")
    else:
        selection = input("Enter race number, name, or 'C' for Custom: ").strip()

        # Custom race flow
        if selection.lower() == "c":
            custom_name = input("Enter custom race name: ").strip() or "Custom"
            bonuses: dict[str, int] = {}
            print("Enter stat bonuses (blank for 0):")
            for stat in STAT_NAMES:
                raw = input(f"  {stat} bonus: ").strip()
                try:
                    bonuses[stat] = int(raw) if raw else 0
                except ValueError:
                    bonuses[stat] = 0
            register_race(custom_name, bonuses)
            race = custom_name
        else:
            # Try number selection
            chosen: str | None = None
            if selection.isdigit():
                idx = int(selection)
                if 1 <= idx <= len(available):
                    chosen = available[idx - 1]
            # Try name selection
            if chosen is None and selection:
                if get_race(selection):
                    chosen = selection
            # Reprompt once if invalid, then fallback to Human
            if chosen is None:
                selection2 = input("Invalid race. Enter number, name, or 'C': ").strip()
                if selection2.lower() == "c":
                    custom_name = input("Enter custom race name: ").strip() or "Custom"
                    bonuses = {}
                    print("Enter stat bonuses (blank for 0):")
                    for stat in STAT_NAMES:
                        raw = input(f"  {stat} bonus: ").strip()
                        try:
                            bonuses[stat] = int(raw) if raw else 0
                        except ValueError:
                            bonuses[stat] = 0
                    register_race(custom_name, bonuses)
                    chosen = custom_name
                elif selection2.isdigit():
                    idx = int(selection2)
                    if 1 <= idx <= len(available):
                        chosen = available[idx - 1]
                elif selection2 and get_race(selection2):
                    chosen = selection2

            race = chosen or "Human"
            if chosen is None:
                print("Invalid input again. Defaulting to Human.")

    print("\n")

    character = Character(name, race, 10)
    character.roll_stats()
    character.apply_racial_bonuses()
    return character


def display_character(character):
    """Print a human-readable summary of a character's stats and HP.

    Args:
        character: The character to display.
    """
    print(f"\n{character.name} the {character.race}")
    print("\nStats:")
    for stat, value in character.stats.items():
        modifier = character.get_modifier(stat)
        print(f"{stat}: {value} ({'+' if modifier >= 0 else ''}{modifier})")
    print(f"\nHP: {character.hp}")





def main():
    """Entry point for the D&D Adventure game CLI.

    Parses command-line options, creates the player, and runs the main
    menu loop. Key options:
    - --seed <int>: Seed RNG for reproducible runs
    - --auto: Non-interactive mode using sensible defaults
    """
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
            choice = input("Enter choice (1-3): ").strip()
            if choice not in {"1", "2", "3"}:
                choice = input("Invalid choice. Please enter 1, 2, or 3: ").strip()
                if choice not in {"1", "2", "3"}:
                    choice = "2"
                    print("Invalid input again. Showing character info.")

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
