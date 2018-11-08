##-- This module is for all bad guys in game --##

##-- Zombies are a close fighter, he needs to be with in 1 block from player to attack --##

class Zombie:
    
    def __init__(self):

        self.max_health = 100
        self.heath = 100
        self.armor = 0
        self.melee_attack = 0
        self.magic_attack = 0
        self.mama = 0
        self.stamina = 0
        self.deffence = 0
        self.pures = 0
        self.luck = 0

##-- Skeletons weld swords and some times have sheilds --##

class Skeleton:
    
    def __init__(self):

        self.max_health = 100
        self.heath = 120
        self.armor = 0
        self.melee_attack = 0
        self.magic_attack = 0
        self.mama = 0
        self.stamina = 0
        self.deffence = 0
        self.pures = 0
        self.luck = 0

##-- Golems can either be Rock or Earth and have high health and also are know to throw there elements as projectilse --##

class Golem:

    def __init__(self):
    
        self.max_health = 250
        self.heath = 250
        self.armor = 0
        self.melee_attack = 0
        self.magic_attack = 0
        self.mama = 0
        self.stamina = 0
        self.deffence = 0
        self.pures = 0
        self.luck = 0
