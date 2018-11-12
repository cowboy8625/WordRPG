##-- This module is for all bad guys in game --##

##-- Import Module --##

import random
import time

##-- Zombies are a close fighter, he needs to be with in 1 block from mob to attack --##

class Zombie:
    
    def __init__(self):

        self.name = 'Zombie'
        self.mob_class = 'Undead'
        self.max_health = 100 
        self.health = 100 
        self.level = 1
        self.exp_gained = 10
        self.armor = 0
        self.melee_attack = 3
        self.magic_attack = 0
        self.mana = 0
        self.stamina = 0
        self.defense = 0 
        self.pures = 5
        self.luck = 0

##-- Skeletons weld swords and some times have sheilds --##

class Skeleton:
    
    def __init__(self):

        self.name = 'Skeleton'
        self.mob_class = 'Undead'
        self.max_health = 100
        self.health = 120
        self.level = 1
        self.exp_gained = 15
        self.armor = 0
        self.melee_attack = 5
        self.magic_attack = 0
        self.mana = 0
        self.stamina = 0
        self.defense = 0
        self.pures = 10
        self.luck = 0

##-- Golems can either be Rock or Earth and have high health and also are know to throw there elements as projectilse --##

class Golem:

    def __init__(self):
        
        self.name = 'Golem'
        self.mob_class = 'Elemental'
        self.max_health = 250
        self.health = 250
        self.level = 1
        self.exp_gained = 55
        self.armor = 0
        self.melee_attack = 4
        self.magic_attack = 0
        self.mana = 0
        self.stamina = 0
        self.defense = 0
        self.pures = 50
        self.luck = 0
        
##-- Witches are magical creatures, they are not physically strong but can invoke spell to make damage or confuse the mob, making him lose a turn. --##

class Witch:

    def __init__(self):
        
        self.name = 'Witch'
        self.mob_class = 'Human'
        self.max_health = 100
        self.health = 100
        self.level = 1
        self.exp_gained = 20
        self.armor = 0
        self.melee_attack = 7
        self.magic_attack = 50
        self.mana = 0
        self.stamina = 0
        self.defense = 0
        self.pures = 15
        self.luck = 0


##-- Hell Wolfes are wolfes speled by evil creatures. They are weak, but really fast. --##

class HellHounds:

    def __init__(self):
        
        self.name = 'Hell Hound'
        self.mob_class = 'Elemental'
        self.max_health = 80
        self.health = 80
        self.level = 1
        self.exp_gained = 10
        self.armor = 0
        self.melee_attack = 6
        self.magic_attack = 0
        self.mana = 0
        self.stamina = 0
        self.defense = 0
        self.pures = 5
        self.luck = 0




##-- This is for a random enemy selection                                       --##
##-- It also makes sure the enemy is with in range of difficullty of the player --##

def random_enemy(lvl):

    lvl = [i for i in range((lvl - 3), (lvl + 5))]
    lvl = random.choice(lvl)
    zombie = Zombie()
    skeleton = Skeleton()
    golem = Golem()
    witch = Witch()
    hell_hound = HellHounds()

    mobs_list = [zombie, skeleton, golem, witch, hell_hound]
    num = random.randrange(0, len(mobs_list))
    mob = mobs_list[num]

    while mob.level <= lvl:
        level_up(mob)
        
    return mob
    
##-- This Levels up the mobs to make them harder as the player get to a higher level --## 

def level_up(mob):
    

    mob.level += 1
    mob.exp_gained += mob.level
    mob.max_health += mob.level
    mob.health = mob.max_health
    mob.defense += mob.level
    mob.mana += mob.level
    mob.stamina += mob.level
    mob.luck += mob.level
    mob.pures += mob.level
    
    # print(f"Level: {mob.level}")
    # print(f"Health: {mob.max_health}")
    # print(f"Armor: {mob.armor}")
    # print(f"Mana: {mob.mana}")
    # print(f"Stamina: {mob.stamina}")
    # print(f"Luck: {mob.luck}")


