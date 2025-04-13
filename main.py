from dndgame.character import Character
from dndgame.dice import roll


def create_character():
    print("Welcome to D&D Adventure!")
    name = input("Enter your character's name: ")

    print("\nChoose your race:")
    print("1. Human (+1 to all stats)")
    print("2. Elf (+2 DEX)")
    print("3. Dwarf (+2 CON)")
    race_choice = input("Enter choice (1-3): ")
    race = ["Human", "Elf", "Dwarf"][int(race_choice) - 1]

    character = Character(name, race)
    character.roll_stats()
    character.apply_racial_bonuses()
    return character


def display_character(character):
    print(f"\n{character.name} the {character.race}")
    print("\nStats:")
    for stat, value in character.stats.items():
        modifier = character.get_modifier(stat)
        print(f"{stat}: {value} ({'+' if modifier >= 0 else ''}{modifier})")


def simple_combat(player):
    print("\nA goblin appears!")
    goblin_hp = 5

    while goblin_hp > 0:
        print(f"\nGoblin HP: {goblin_hp}")
        print("\nYour turn!")
        print("1. Attack")
        print("2. Run away")

        choice = input("What do you do? ")
        if choice == "1":
            attack = roll(20, 1)
            if attack >= 10:
                damage = roll(4, 1)
                goblin_hp -= damage
                print(f"You hit for {damage} damage!")
            else:
                print("You missed!")
        elif choice == "2":
            return False

    return True


def main():
    player = create_character()

    while True:
        print("\nWhat would you like to do?")
        print("1. Fight a goblin")
        print("2. View character")
        print("3. Quit")

        choice = input("Enter choice (1-3): ")

        if choice == "1":
            victory = simple_combat(player)
            if victory:
                print("You defeated the goblin!")
            else:
                print("You ran away!")
        elif choice == "2":
            display_character(player)
        elif choice == "3":
            break


if __name__ == "__main__":
    main()
