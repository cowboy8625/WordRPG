import Items

class Character:
    def __init__(self, name=None, max_health=1, health=1, melee_attack=None, magic_attack=None,
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

    
character = Character()
print(character.health)
character.max_health = 100
print("Max Health is", character.max_health)
character.set_health()
print(character.health)

