# Program imports
import random

from script import Items, Screen
from Mechanics.core_mechanics import rnd
from Mechanics.ui_mechanics import *


class Character:
    def __init__(self, name, max_health, melee_attack, magic_attack,
                 max_mana, max_stamina, defense, luck, level=1):
        self.name = name
        self.level = level
        # Stats
        self.max_health = max_health
        self.health = self.max_health
        self.melee_attack = melee_attack
        self.magic_attack = magic_attack
        self.max_mana = max_mana
        self.max_stamina = max_stamina
        self.defense = defense
        self.luck = luck

        # Inventory
        self.equipped_weapon = Items.fist
        self.equipped_armor = None


class Player(Character):
    def __init__(self, name, _class, max_health, melee_attack, magic_attack,
                 max_mana, max_stamina, defense, luck, gender, gold=0, xp=0,
                 equipped_weapon= Items.fist, equipped_armor=Items.farm_clothing):
        super().__init__(self, name, max_health, melee_attack, magic_attack,
                         max_mana, max_stamina, defense, luck)
        self._class = _class
        self.gender = gender
        self.gold = gold
        self.xp = xp
        self.equipped_weapon = equipped_weapon
        self.equipped_armor = equipped_armor

        self.inventory = []
        self.inventory_limit = 10

        
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