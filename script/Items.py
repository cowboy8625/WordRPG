##-- This is for all the weapons, armor, potions or any other item type in the game --##


class Item:
       def __init__(self, name, rarity, value):
                self.name = name
                self.rarity = rarity
                self.value = value 


class Weapon(Item):

        def __init__(self, name,  rarity, value, melee_damage, magic_damage, action_word):
                super().__init__(name, rarity, value)
                self.melee_damage = melee_damage
                self.magic_damage = magic_damage
                self.action_word = action_word


class Armor(Item):

        def __init__(self, name,  rarity, value, melee_defence, magic_defence):
                super().__init__(name, rarity, value)
                self.melee_defence = melee_defence
                self.magic_defence = magic_defence


class Spells:

        def __init__(self, magic_damage):
                self.magic_damage = magic_damage



##-- Rarity Tags --##
##-- "Very Common", "Common", "Uncommon", "Rare", "Very Rare", "Epic" --##

##-- items --##
rock = Item("Rock", "Very Common", 1)
wood = Item("Wood", "Very Common", 1)
magic_wood = Item("Magic Wood", "Rare", 10)
bone = Item("Bone", "Common", 1)
flint = Item("Flint", "Common", 1)
clay = Item("Clay", "Common", 1)
herb = Item("Herbs", "Common", 2)
salt = Item("Salt", "Uncommon", 5)
flesh = Item("Flesh", "Very Common", 0)

##-- staffs --##
weak_staff = Weapon("Weak Staff", "Very Common", 5, 1, 10, "expelled")
wooden_staff = Weapon("Wooden Staff", "Common", 6, 2, 15, "expelled")

##-- swords --##
rusty_short_sword = Weapon("Rusty Short Sword", "Very Common", 5, 10, 0, "swung")

##-- bows --##
common_hunting_bow = Weapon("Common Hunting Bow", "Very Common", 3, 10, 0, "shot")  

##-- daggers --##
rusty_dagger = Weapon("Rusty Dagger", "Common", 7, 7, 0, "jabbed")

##-- armor --##
soft_leather_hide = Armor("Soft Leather Hide", "Very Common", 5, 5, 0)

##-- spells --##



##-- All Items, Weapon, & Armor Dictionary's --##
resources = {"Rock": rock, "Wood": wood, "Magic Wood": magic_wood, "Bone": bone, "Flint": flint, "Clay": clay, 
                "Herbs": herb, "Salt": salt, "Flesh": flesh}

staffs = {"Weak Staff": weak_staff, "Wooden Staff": wooden_staff}

swords = {"Rusty Short Sword": rusty_short_sword}

bows = {"Common Hunting Bow": common_hunting_bow}

daggers = {"Rusty Dagger": rusty_dagger}

armor = {"Soft Leather Hide": soft_leather_hide}

spells = {}

print(weak_staff.name)