from dndgame.dice import roll


class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.round = 0
        self.initiative_order = []

    def roll_initiative(self):
        """Roll initiative for combat order."""
        player_init = roll(20, 1) + self.player.get_modifier("DEX")
        enemy_init = roll(20, 1) + self.enemy.get_modifier("DEX")

        if player_init >= enemy_init:
            self.initiative_order = [self.player, self.enemy]
        else:
            self.initiative_order = [self.enemy, self.player]

        return self.initiative_order

    def attack(self, attacker, defender):
        attack_roll = roll(20, 1)
        if attack_roll >= defender.armor_class:
            damage = attacker.get_modifier("STR")
            defender.hp -= damage
            return damage
        return 0
