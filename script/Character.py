from script import Items


class Character:
    def __init__(self, char_name, max_health, melee_attack, magic_attack,
                 max_mana, max_stamina, defense, luck, level=1):
        self.char_name = char_name
        self.level = level
        # Stats
        self.max_health = max_health
        self.health = self.max_health
        self.melee_attack = melee_attack
        self.magic_attack = magic_attack
        self.max_mana = max_mana
        self.mana = self.max_mana
        self.max_stamina = max_stamina
        self.stamina = self.max_stamina
        self.defense = defense
        self.luck = luck
        # Inventory
        self.inventory = []
        self.inventory_limit = 10
        self.equipped_weapon = Items.fist
        self.equipped_armor = None

    # Add given item to inventory
    # Returns True if successful (available space in inventory)
    def add_to_inventory(self, item):
        if len(self.inventory) < self.inventory_limit:
            self.inventory.append(item)
            return True
        else:
            return False

    # Remove item at given position of inventory
    # Note that we can not currently remove an item via its 'identity' because Item does not have an equality override
    # Returns True if item was present
    def remove_from_inventory(self, pos):
        del self.inventory[pos]


# The player class handles all the players stat creation
class Player(Character):
    def __init__(self, max_health, melee_attack, magic_attack,
                 max_mana, max_stamina, defense, luck, player_class, pures, char_name):
        super(Player, self).__init__(char_name, max_health, melee_attack, magic_attack,
                 max_mana, max_stamina, defense, luck)
        self.player_class = player_class
        self.pures = pures
        self.exp = 0
        # Inventory
        self.equipped_armor = Items.farm_clothing


# The Mage, Warrior, Archer and Assassin classes inherit the Player class
class Mage(Player):
    pass


class Warrior(Player):
    # Adrenaline Junky
    # Lets Warrior the ablity to take 1 hits before death
    # Ability can level up as player gets stronger
    pass


class Archer(Player):
    pass


class Assassin(Player):
    pass


class Mob(Character):
    def __init__(self, char_name, max_health, melee_attack, magic_attack, max_mana, max_stamina, defense, luck,
                 mob_class, gold_drop, exp_drop, item_drop, special_item_drop=None):
        super(Mob, self).__init__(char_name, max_health, melee_attack, magic_attack,
                 max_mana, max_stamina, defense, luck)
        self.mob_class = mob_class
        # Drops
        self.gold_drop = gold_drop
        self.exp_drop = exp_drop
        self.item_drop = item_drop
        self.special_item_drop = special_item_drop

    def level_up(self):
        pass


# enemy mobs
# Zombies are a close fighter, he needs to be with in 1 block from mob to attack
zombie = Mob(char_name="Zombie", max_health=100, melee_attack=10, magic_attack=0, max_mana=0, max_stamina=20,
             defense=15, luck=5, mob_class="Undead", gold_drop=10, exp_drop=10, item_drop="Flesh")
yeti = Mob(char_name="Yeti", max_health=100, melee_attack=10, magic_attack=0, max_mana=0, max_stamina=20,
             defense=15, luck=5, mob_class="Undead", gold_drop=10, exp_drop=10, item_drop="Flesh")
bandit = Mob(char_name="Bandit", max_health=100, melee_attack=10, magic_attack=0, max_mana=0, max_stamina=20,
             defense=15, luck=5, mob_class="Human", gold_drop=10, exp_drop=10, item_drop="Flesh")
mercenary = Mob(char_name="Mercenary", max_health=100, melee_attack=10, magic_attack=0, max_mana=0, max_stamina=20,
             defense=15, luck=5, mob_class="Human", gold_drop=10, exp_drop=10, item_drop="Flesh")
skeleton = Mob(char_name="Skeleton", max_health=100, melee_attack=10, magic_attack=0, max_mana=0, max_stamina=20,
             defense=15, luck=5, mob_class="Undead", gold_drop=10, exp_drop=10, item_drop="Flesh")
golem = Mob(char_name="Golem", max_health=100, melee_attack=10, magic_attack=0, max_mana=0, max_stamina=20,
             defense=15, luck=5, mob_class="Elemental", gold_drop=10, exp_drop=10, item_drop="Flesh")
witch = Mob(char_name="Witch", max_health=100, melee_attack=10, magic_attack=0, max_mana=0, max_stamina=20,
             defense=15, luck=5, mob_class="Human", gold_drop=10, exp_drop=10, item_drop="Flesh")
hellHounds = Mob(char_name="Hell Hounds", max_health=100, melee_attack=10, magic_attack=0, max_mana=0, max_stamina=20,
             defense=15, luck=5, mob_class="Undead", gold_drop=10, exp_drop=10, item_drop="Flesh")

# animal mobs
dog = Mob(char_name="Dog", max_health=100, melee_attack=10, magic_attack=0, max_mana=0, max_stamina=20,
             defense=15, luck=5, mob_class="Animal", gold_drop=10, exp_drop=10, item_drop="Flesh")

# bosses
wyrm = Mob(char_name="Wyrm", max_health=100, melee_attack=10, magic_attack=0, max_mana=0, max_stamina=20,
           defense=15, luck=5, mob_class="Dragon", gold_drop=10, exp_drop=10, item_drop="Dragon Scale",
           special_item_drop="Special Drop")
kraken = Mob(char_name="Kraken", max_health=100, melee_attack=10, magic_attack=0, max_mana=0, max_stamina=20,
           defense=15, luck=5, mob_class="Dragon", gold_drop=10, exp_drop=10, item_drop="Dragon Scale",
           special_item_drop="Special Drop")

hostile_mobs = {"Zombie": zombie, "Yeti": yeti, "Bandit": bandit, "Mercenary": mercenary, "Skeleton": skeleton,
                "Golem": golem, "Witch": witch,
                "Hell Hounds": hellHounds}

friendly_mobs = {"Dog": dog}

bosses = {"Wyrm": wyrm, "Kraken": kraken}