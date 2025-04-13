from dndgame.dice import roll


class Character:
    def __init__(self, name, race):
        self.name = name
        self.stats = {}
        self.hp = 0
        self.race = race
        self.inventory = []
        self.level = 1
        self.spell_slots = {}
        self.skills = []
        self.armor_class = 10

    def get_modifier(self, stat):
        """Calculate ability modifier."""
        return (self.stats[stat] - 10) // 2

    def roll_stats(self):
        print("Rolling stats...")
        stats = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
        for stat in stats:
            self.stats[stat] = roll(6, 3)

    def get_available_skills(self):
        skills = []
        for skill in self.skills:
            if self.level >= skill.level_requirement:
                skills.append(skill)
        return skills

    def apply_racial_bonuses(self):
        if self.race == "Dwarf":
            self.stats["CON"] += 2
        elif self.race == "Elf":
            self.stats["DEX"] += 2
        elif self.race == "Human":
            for stat in self.stats:
                self.stats[stat] += 1
