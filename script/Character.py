__author__ = 'byteme8bit'

# File imports

# Module imports


class Character:        # Base class
    def __init__(self, name, level):
        self.char_name = name
        self.level = level


class Player(Character):        # User's entity
    def __init__(self, name, level, health_points, char_class):
        super().__init__(name, level)
        self.type = char_class
        self.exp = 0
        self.hp = health_points

    def melee_attack(self):
        return 17

    def magic_attack(self):
        pass

    def health_generation(self):
        pass


class Mob(Character):       # Combat based entities
    def __init__(self, name, level, health_points):
        super().__init__(name, level)
        self.hp = health_points

    def melee_attack(self):
        return 5


class NPC(Character):       # Non-combat entities
    pass
