from dndgame.dice import roll


class Character:
    def __init__(self, name, race, base_hp):
        self.name = name
        self.race = race
        self.stats = {}
        self.base_hp = base_hp
        self.hp = 0
        self.max_hp = 0
        self.level = 1
        self.armor_class = 10

    def get_modifier(self, stat):
        """Calculate ability modifier."""
        return (self.stats[stat] - 10) // 2

    def roll_stats(self):
        print("Rolling stats...\n")
        stats = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
        for stat in stats:
            print(f"Rolling {stat}...")
            self.stats[stat] = roll(6, 3)

        self.max_hp = self.base_hp + self.get_modifier("CON")
        self.hp = self.max_hp

    def apply_racial_bonuses(self):
        if self.race == "Dwarf":
            self.stats["CON"] += 2
        elif self.race == "Elf":
            self.stats["DEX"] += 2
        elif self.race == "Human":
            for stat in self.stats:
                self.stats[stat] += 1
