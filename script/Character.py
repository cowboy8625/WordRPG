# Program imports
import random

import Items
from Mechanics.ui_mechanics import *
from Map_Gen.ParseMap import WorldMap


class Character:
    def __init__(self, name=None, max_health=1, health=max_health, melee_attack=None, magic_attack=None,
                 max_mana=None, max_stamina=None, defense=None, luck=None, level=1):
        self.name = name
        self.level = level
        # Stats
        self.max_health = max_health
        self.health = health
        self.melee_damage = melee_attack
        self.magic_damage = magic_attack
        self.max_mana = max_mana
        self.max_stamina = max_stamina
        self.defense = defense
        self.luck = luck

        # Inventory 
        self.equipped_weapon = Items.fist
        self.equipped_armor = None

    # These classes can be used for testing for the time being. They will need to integrate combat at some point.
    def melee_attack(self):
        return random.randint(self.melee_damage // 2, self.melee_damage)

    def magic_attack(self):
        return random.randint(self.magic_damage // 2, self.magic_damage)

    def set_health(self, new_health):
        self.health += new_health
        if self.health > self.max_health:
            self.health = self.max_health
    
    def set_max_health(self, new_max_health):
        max_health = new_max_health


class Player(Character):
    def __init__(self, name, _class, max_health, melee_attack, magic_attack,
                 max_mana, max_stamina, defense, luck, gender, gold=0, xp=0,
                 equipped_weapon= None, equipped_armor=Items.farm_clothing):
        super().__init__(name, max_health, melee_attack, magic_attack,
                         max_mana, max_stamina, defense, luck)
        self._class = _class
        self.gender = gender
        self.gold = gold
        self.xp = xp
        self.equipped_weapon = equipped_weapon
        self.equipped_armor = equipped_armor

        self.inventory = [Items.flint, Items.water]
        # start with a couple of things so we can play with inventory management
        self.inventory_limit = 10

        # Map position
        self.pos_x = 1
        self.pos_y = 1

    def move(self, _dir):
        directions = {"North":(0, -1), "South":(0, 1), "East":(1, 0), "West":(-1, 0)}
        delta_x, delta_y = directions[_dir]
        new_x, new_y = self.pos_x + delta_x, self.pos_y + delta_y
        if WorldMap.access_information(new_x, new_y, "Crossable"):
            self.pos_x, self.pos_y = new_x, new_y
        else:
            clear()
            print("You cannot cross here:")
            print(WorldMap.access_information(new_x, new_y, "Name"))
            pause()

    # Add item to inventory if space is available
    # Return true if add was successful
    def add_to_inv(self, item):
        if len(self.inventory) >= self.inventory_limit:
            return False
        self.inventory.append(item)
        
    # Remove item at given position
    def remove_from_inv(self, index):
        if index in range(len(self.inventory)):
            del self.inventory[index]
        else:
            raise ValueError(f'Index {index} invalid for inventory {self.inventory}')
        
    # TODO methods like this should probably be moved to mechanics
    # the script classes shouldn't be dealing with UI, only handling the class instances
    def inspect_area(self):
        info = {
            "Name": WorldMap.access_information(self.pos_x, self.pos_y, "Name"),
            "Resources": WorldMap.access_information(self.pos_x, self.pos_y, "Resources"),
            "Spawns": WorldMap.access_information(self.pos_x, self.pos_x, "Spawns"),
            "Info": WorldMap.access_information(self.pos_x, self.pos_y, "Info")
        }
        clear()
        print("Name: " + str(info["Name"]))
        print("Resources: " + str(info["Resources"]))
        print("Spawns: " + str(info["Spawns"]))
        print("Info: " + str(info["Info"]))
        pause()
