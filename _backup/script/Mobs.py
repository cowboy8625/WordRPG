##-- This module is for all bad guys in game --##

##-- Import Module --##

import random
import time

##-- Zombies are a close fighter, he needs to be with in 1 block from mob to attack --##

class Mobs:
    def __init__(self, name, mob_class, max_health, melee_attack, magic_attack, mana, stamina, defense, luck, gold_drop, exp_drop, item_drop):
        self.level = 1                      # level can be changed using a function
        self.name = name
        self.mob_class = mob_class 
        ##-- Stats --##               
        self.max_health = max_health  
        self.health = self.max_health
        self.melee_attack = melee_attack
        self.magic_attack = magic_attack
        self.mana = mana
        self.stamina = stamina
        self.defense = defense
        self.luck = luck
        ##-- Equipable Slots --##
        self.in_hand = ''                    # in hand is the weapon of the mob
        self.armor = ''
        ##-- Drops --##
        self.gold_drop = gold_drop
        self.exp_drop = exp_drop
        self.item_drop = item_drop

    def level_up(self):
        pass
        ##-- make this function bulit in instead of making it outside --##
    
class Boss(Mobs):

    def __init__(self, name, mob_class, max_health, melee_attack, magic_attack, mana, stamina, defense, luck, gold_drop, exp_drop, item_drop, special_item_drop):
        super().__init__(name, mob_class, max_health, melee_attack, magic_attack, mana, stamina, defense, luck, gold_drop, exp_drop, item_drop)
        self.special_item_drop = item_drop

    def special_move(self):
        pass

##-- name, mob_class, max_health, melee_attack, magic_attack, mana, stamina, defense, luck, gold_drop, exp_drop, item_drop --##
##-- enemy mobs --##
zombie = Mobs("Zombie", "Undead", 100 ,10 ,0 ,0 , 20, 15, 5, 10, 10, "Flesh")
yeti = Mobs("Yeti", "Undead", 100 ,10 ,0 ,0 , 20, 15, 5, 10, 10, "Flesh")
bandit = Mobs("Bandit", "Human", 100 ,10 ,0 ,0 , 20, 15, 5, 10, 10, "Flesh")
mercinary = Mobs("Mercinary", "Human", 100 ,10 ,0 ,0 , 20, 15, 5, 10, 10, "Flesh")
skeleton = Mobs("Skeleton", "Undead", 100 ,10 ,0 ,0 , 20, 15, 5, 10, 10, "Flesh")
golem = Mobs("Golem", "Elemental", 100 ,10 ,0 ,0 , 20, 15, 5, 10, 10, "Flesh")
witch = Mobs("Witch", "Human", 100 ,10 ,0 ,0 , 20, 15, 5, 10, 10, "Flesh")
hellHounds = Mobs("Hell Hounds", "Undead", 100 ,10 ,0 ,0 , 20, 15, 5, 10, 10, "Flesh")

##-- animals mobs --##

dog = Mobs("Dog", "Animal", 100 ,10 ,0 ,0 , 20, 15, 5, 10, 10, "Flesh")

##-- bosses --##
wyrm = Boss("Wyrm", "Dragon", 100 ,10 ,0 ,0 , 20, 15, 5, 10, 10, "Dragon Scale", "Speical Drop")
kracken = Boss("Kracken", "Dragon", 100 ,10 ,0 ,0 , 20, 15, 5, 10, 10, "Dragon Scale", "Speical Drop")


hostail_mobs = {"Zombie": zombie, "Yeti": yeti, "Bandit": bandit, "Mercinary": mercinary, "Skeleton": skeleton, "Golem": golem, "Witch": witch,
                "Hell Hounds": hellHounds}

friendly_mobs = {"Dog": dog}

bosses = {"Wyrm": wyrm, "Kracken": kracken}













##----------------------------------------------------------------------------------------------------------##
##                                   OLD                                 CODE                               ##



##-- This is for a random enemy selection                                       --##
##-- It also makes sure the enemy is with in range of difficullty of the player --##

# def random_enemy(lvl):

#     lvl = [i for i in range((lvl - 3), (lvl + 5))]
#     lvl = random.choice(lvl)
#     zombie = Zombie()
#     skeleton = Skeleton()
#     golem = Golem()
#     witch = Witch()
#     hell_hound = HellHounds()

#     mobs_list = [zombie, skeleton, golem, witch, hell_hound]
#     num = random.randrange(0, len(mobs_list))
#     mob = mobs_list[num]

#     while mob.level <= lvl:
#         level_up(mob)

#     return mob

# ##-- This Levels up the mobs to make them harder as the player get to a higher level --##

# def level_up(mob):


#     mob.level += 1
#     mob.exp_gained += mob.level
#     mob.max_health += mob.level
#     mob.health = mob.max_health
#     mob.defense += mob.level
#     mob.mana += mob.level
#     mob.stamina += mob.level
#     mob.luck += mob.level
#     mob.pures += mob.level

    # print(f"Level: {mob.level}")
    # print(f"Health: {mob.max_health}")
    # print(f"Armor: {mob.armor}")
    # print(f"Mana: {mob.mana}")
    # print(f"Stamina: {mob.stamina}")
    # print(f"Luck: {mob.luck}")
