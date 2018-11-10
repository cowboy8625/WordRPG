##-- This is for all the weapons, armor, potions or any other item type in the game --##

items = {
    'health_potion': {'hp_restore': 50,
                      'mana_restore': 50
                    }
    }
weapons = {'short_sword': {
           'name': 'Rusty Short Sword', 'damage': 2
                        }
          
    }
armor = {}


##-- This class of weapons would be oriented to all player classes, but directed to the physicall classes. --##
class White_Weapons:
    
    def __init__ (self, level, damage, resistance, attribute):
        self.level = level
        self.damage = damage
        self.resistance = resistance
        self.attribute = attribute

Sword = White_Weapons (1, 20, 50, 0) #I left attribute with 0, cause I don't know how to handle it for now
Mass = White_Weapons (2, 60, 80, 0)
Bow = White_Weapons (1, 10, 100, 0)



##-- This class of weapons would be oriented to the magic class. They would be physical weapons as well as magic powers. --##
class Magic_Weapons:
    
    def __init__ (self, level, damage, magic, attribute):
        self.level = level
        self.damage = damage
        self.magic = magic
        self.attribute = attribute

Magic_Stick = Magic_Weapons (1, 20, 40, 0)
Magic_Stick2 = Magic_Weapons (2, 40, 80, 0)
Magic_Power_Fire = Magic_Weapons (3, 50, 80, 0)


class Armour:

    def __init__ (self, level, damage_support, resistance, weight):
        self.level = level
        self.damage_support = damage_support
        self.resistance = resistance
        self.weight = weight # The weight of the armour affects the stamina of the player.

Armour1 = Armour (1, 10, 50, -5) 
Armour2 = Armour (2, 20, 80, -1) 
Magic_Cloth = Armour (1, 15, 80, 0) #The cloth is protected by magic, that's why the high values.

class Items:

    def __init__ (self, max_health, magic_attack, luck):
        self.max_health = max_health
        self.magic_attack = magic_attack
        self.luck = luck

Power_Ring = Items (10, 0, 2)
Magic_Ring = Items (10, 10, 10)


