__author__ = "byteme8bit"

# File imports

# Module imports
from script.Character import Player, Mob
from Mechanics.combat_mechanics import combat
from script import Items

player = Player(name='Steve',
                char_class='Warrior',
                level=1,
                max_mana=5,
                max_stamina=50,
                defense=5,
                gender='Male',
                gold=0,
                equipped_weapon=Items.rusty_short_sword
                )

enemy = Mob('Butthead', level=1)

combat(player, enemy)
