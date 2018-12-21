# Program imports
import random

from script import Items
from Mechanics.ui_mechanics import *
from Map_Gen.ParseMap import WorldMap


class Character:
    def __init__(self, name, max_health, melee_attack, magic_attack,
                 max_mana, max_stamina, defense, luck, level=1):
        self.name = name
        self.level = level
        # Stats
        self.max_health = max_health
        self.health = self.max_health
        self.melee_damage = melee_attack
        self.magic_damage = magic_attack
        self.max_mana = max_mana
        self.max_stamina = max_stamina
        self.defense = defense
        self.luck = luck

        # Inventory
        self.equipped_weapon = Items.fist
        self.equipped_armor = None

    def melee_attack(self):
        return random.randint(self.melee_damage // 2, self.melee_damage)

    def magic_attack(self):
        return random.randint(self.magic_damage // 2, self.magic_damage)


class Player(Character):
    def __init__(self, name, _class, max_health, melee_attack, magic_attack,
                 max_mana, max_stamina, defense, luck, gender, gold=0, xp=0,
                 equipped_weapon= Items.fist, equipped_armor=Items.farm_clothing):
        super().__init__(name, max_health, melee_attack, magic_attack,
                         max_mana, max_stamina, defense, luck)
        self._class = _class
        self.gender = gender
        self.gold = gold
        self.xp = xp
        self.equipped_weapon = equipped_weapon
        self.equipped_armor = equipped_armor

        self.inventory = []
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

    def inspect_area(self):
        print("======CALLED=======")
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


"""
# enemy mobs
# Zombies are a close fighter, he needs to be with in 1 block from mob to attack
zombie = Mob(name="Zombie", max_health=100, melee_attack=10, magic_attack=0, max_mana=0, max_stamina=20,
             defense=15, luck=5, mob_class="Undead", gold_drop=10, exp_drop=10, item_drop="Flesh")
yeti = Mob(name="Yeti", max_health=100, melee_attack=10, magic_attack=0, max_mana=0, max_stamina=20,
           defense=15, luck=5, mob_class="Undead", gold_drop=10, exp_drop=10, item_drop="Flesh")
bandit = Mob(name="Bandit", max_health=100, melee_attack=10, magic_attack=0, max_mana=0, max_stamina=20,
             defense=15, luck=5, mob_class="Human", gold_drop=10, exp_drop=10, item_drop="Flesh")
mercenary = Mob(name="Mercenary", max_health=100, melee_attack=10, magic_attack=0, max_mana=0, max_stamina=20,
                defense=15, luck=5, mob_class="Human", gold_drop=10, exp_drop=10, item_drop="Flesh")
skeleton = Mob(name="Skeleton", max_health=100, melee_attack=10, magic_attack=0, max_mana=0, max_stamina=20,
               defense=15, luck=5, mob_class="Undead", gold_drop=10, exp_drop=10, item_drop="Flesh")
golem = Mob(name="Golem", max_health=100, melee_attack=10, magic_attack=0, max_mana=0, max_stamina=20,
            defense=15, luck=5, mob_class="Elemental", gold_drop=10, exp_drop=10, item_drop="Flesh")
witch = Mob(name="Witch", max_health=100, melee_attack=10, magic_attack=0, max_mana=0, max_stamina=20,
            defense=15, luck=5, mob_class="Human", gold_drop=10, exp_drop=10, item_drop="Flesh")
hellHounds = Mob(name="Hell Hounds", max_health=100, melee_attack=10, magic_attack=0, max_mana=0, max_stamina=20,
                 defense=15, luck=5, mob_class="Undead", gold_drop=10, exp_drop=10, item_drop="Flesh")

# animal mobs
dog = Mob(name="Dog", max_health=100, melee_attack=10, magic_attack=0, max_mana=0, max_stamina=20,
          defense=15, luck=5, mob_class="Animal", gold_drop=10, exp_drop=10, item_drop="Flesh")

# bosses
wyrm = Mob(name="Wyrm", max_health=100, melee_attack=10, magic_attack=0, max_mana=0, max_stamina=20,
           defense=15, luck=5, mob_class="Dragon", gold_drop=10, exp_drop=10, item_drop="Dragon Scale",
           special_item_drop="Special Drop")
kraken = Mob(name="Kraken", max_health=100, melee_attack=10, magic_attack=0, max_mana=0, max_stamina=20,
             defense=15, luck=5, mob_class="Dragon", gold_drop=10, exp_drop=10, item_drop="Dragon Scale",
             special_item_drop="Special Drop")

hostile_mobs = {"Zombie": zombie, "Yeti": yeti, "Bandit": bandit, "Mercenary": mercenary, "Skeleton": skeleton,
                "Golem": golem, "Witch": witch,
                "Hell Hounds": hellHounds}

friendly_mobs = {"Dog": dog}

bosses = {"Wyrm": wyrm, "Kraken": kraken}
"""