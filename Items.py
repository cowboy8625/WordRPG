##-- This is for all the weapons, armor, potions or any other item type in the game --##


##-- This class of weapons would be oriented to all player classes, but directed to the phisycall classes. --##
class White_Weapons:
    
    def __init__ (self, level, damage, resistance, attribute):
        self.level = level
        self.damage = damage
        self.resistance = resistance
        self.attribute = attribute

Sword = White_Weapons (1, 20, 50, 0) #I left attribute with 0, cause I don't know how to handle it for now
Mass = White_Weapons (2, 60, 80, 0)
Bow = White_Weapons (1, 10, 100, 0)



##-- This class of weapons would be oriented to the magic class. They would be phisycal weapons as well as magic powers. --##
class Magic_Weapons:
    
    def __init__ (self, level, damage, magic, attribute):
        self.level = level
        self.damage = damage
        self.magic = magic
        self.attribute = attribute

Magic_Stick = Magic_Weapons (1, 20, 40, 0)
Magic_Stick2 = Magic_Weapons (2, 40, 80, 0)
Magic_Power_Fire = Magic_Weapons (3, 50, 80, 0)
