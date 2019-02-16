# Program imports
import random

from script import Items
from Mechanics.ui_mechanics import *
# from Map_Gen.ParseMap import WorldMap


class Character:
    def __init__(self, name, level=1):
        self.char_name = name
        self.level = level

        # Inventory
        self.equipped_weapon = Items.fist
        self.equipped_armor = None


class Player(Character):
    def __init__(self, name, level, char_class, max_stamina, max_mana, defense, gender, gold=0, exp=0,
                 equipped_weapon=None, equipped_armor=Items.farm_clothing):
        super().__init__(name, level)

        # General Stats
        self.char_class = char_class
        self.max_health = 100
        self.health = self.max_health
        self.max_mana = max_mana
        self.mana = self.max_mana
        self.max_stamina = max_stamina
        self.stamina = self.max_stamina
        self.defense = defense
        self.gender = gender
        self.gold = gold
        self.exp = exp
        self.died_count = 0
        # start with a couple of things so we can play with inventory management
        self.inventory = [Items.flint, Items.water]
        self.inventory_limit = 10
        self.equipped_weapon = equipped_weapon
        self.equipped_armor = equipped_armor

        # Core stats
        if self.char_class == 'Warrior':
            self.strength = int(15 + (self.level * 4.2))
            self.agility = int(13 + (self.level * 3.7))
            self.intelligence = int(11 + (self.level * 2.8))

        elif self.char_class == 'Assassin':
            self.strength = int(13 + (self.level * 3.5))
            self.agility = int(15 + (self.level * 4.2))
            self.intelligence = int(11 + (self.level * 2.9))

        elif self.char_class == 'Archer':
            self.strength = int(13 + (self.level * 3.7))
            self.agility = int(15 + (self.level * 4))
            self.intelligence = int(11 + (self.level * 2.9))

        elif self.char_class == 'Mage':
            self.strength = int(13 + (self.level * 2.8))
            self.agility = int(11 + (self.level * 3.7))
            self.intelligence = int(15 + (self.level * 4.2))

        # Map position
        self.pos_x = 1
        self.pos_y = 1

    def melee_attack(self):
        return 17  # TODO Formula will be used after testing
        # return random.randint(self.melee_damage // 2, self.melee_damage)

    def magic_attack(self):
        return 17  # TODO Formula will be used after testing
        # return random.randint(self.magic_damage // 2, self.magic_damage)

    def health_generation(self):
        """
        Determines maximum amount of health
        :return: Max. health
        """

        # If ranger
        if self.char_class == 'Assassin' or self.char_class == 'Archer':
            return ((100 * self.level) + (self.strength * 1.7) // (1.25 * self.level)) * 0.97

        # If warrior
        elif self.char_class == 'Warrior':
            return ((100 * self.level) + (self.strength * 2) // (1.1 * self.level)) * 1.15

        # If mage
        elif self.char_class == 'Mage':
            return ((100 * self.level) + (self.strength * 1.4) // (1.35 * self.level)) * 0.89

        # If none type
        else:
            return (100 * self.level) + (self.strength * 1.2) // (1.35 * self.level) * 0.85

    def health_regeneration(self):
        """
        Logic responsible for health regeneration
        :return: None
        """
        max_hp = self.health_generation()  # Sets value of max. health

        if self.health < max_hp:  # If current health is less than max. health
            self.health += (max_hp * 0.023)  # Rate of regeneration

    def player_fainted(self):
        """
        Defines what happens when Player health reach <= 0
        :return: None
        """

        self.died_count += 1
        print(f"{self.char_name} has fainted and needs to recover...\n")
        # time.sleep(5)
        # self.resource_reset()
        print(f'{self.char_name} has recovered! {self.char_name} and has fallen {self.died_count} times.\n')

    # def move(self, _dir):
    #     directions = {"North": (0, -1), "South": (0, 1), "East": (1, 0), "West": (-1, 0)}
    #     delta_x, delta_y = directions[_dir]
    #     new_x, new_y = self.pos_x + delta_x, self.pos_y + delta_y
    #     if WorldMap.access_information(new_x, new_y, "Crossable"):
    #         self.pos_x, self.pos_y = new_x, new_y
    #     else:
    #         clear()
    #         print("You cannot cross here:")
    #         print(WorldMap.access_information(new_x, new_y, "Name"))
    #         pause()
    #
    # # Add item to inventory if space is available
    # # Return true if add was successful
    # def add_to_inv(self, item):
    #     if len(self.inventory) >= self.inventory_limit:
    #         return False
    #     self.inventory.append(item)
    #
    # # Remove item at given position
    # def remove_from_inv(self, index):
    #     if index in range(len(self.inventory)):
    #         del self.inventory[index]
    #     else:
    #         raise ValueError(f'Index {index} invalid for inventory {self.inventory}')
    #
    # # TODO methods like this should probably be moved to mechanics
    # # the script classes shouldn't be dealing with UI, only handling the class instances
    # def inspect_area(self):
    #     info = {
    #         "Name": WorldMap.access_information(self.pos_x, self.pos_y, "Name"),
    #         "Resources": WorldMap.access_information(self.pos_x, self.pos_y, "Resources"),
    #         "Spawns": WorldMap.access_information(self.pos_x, self.pos_x, "Spawns"),
    #         "Info": WorldMap.access_information(self.pos_x, self.pos_y, "Info")
    #     }
    #     clear()
    #     print("Name: " + str(info["Name"]))
    #     print("Resources: " + str(info["Resources"]))
    #     print("Spawns: " + str(info["Spawns"]))
    #     print("Info: " + str(info["Info"]))
    #     pause()


class Mob(Character):
    def __init__(self, name, level):
        super().__init__(name, level)
        self.max_health = 100
        self.health = self.max_health
        self.max_mana = 5
        self.mana = self.max_mana
        self.max_stamina = 5
        self.stamina = self.max_stamina
        self.defense = 1
        self.gender = 'Male'
        self.gold = 2
        self.exp = 7

    def melee_attack(self):
        return 5  # TODO Formula will be used after testing
        # return random.randint(self.melee_damage // 2, self.melee_damage)

    def magic_attack(self):
        return 5  # TODO Formula will be used after testing
        # return random.randint(self.magic_damage // 2, self.magic_damage)
