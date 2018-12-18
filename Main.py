# Starting Data November 6, 2018
# Made By Cowboy8625
# Waste Land
__author__ = 'Cowboy8625', 'Cyy', 'BJTMastermind', 'HexTree', 'Byteme8bit','Giioke'

# Import Modules
import os
import random
import sys
import time
# Custom Imports
from Map_Gen import Engine
from Map_Gen import Biome
from script.Character import *
from script import InfoDics, Items, Screen, Story
import ChangeLog

# Global Variables
# These are for the Function char_creation()
player_name = None
player_class_choice = None
player_in_game = None

# Holds pronouns used for player in the story
gender = None

# Only True if hasn't seen opening story
opening = True

# If True it's the players turn
turn = True

# X, Y, SubX, SubY Coordinates:
x = 5
y = 0
sub_x = 0  # For Map in side of biome
sub_y = 0  # ^^       ^^       ^^

# To see if player is in a biome or not
biome_or_subBiome = False

# Map sizes
small = 100
medium = 500
large = 1000

# Downloads modules
def setup():
    if os.path.isfile("Worldmap.db"):
        return
    else:
        if os.name == 'nt':
            os.system("pip3 install colorama > NUL")
            os.system("pip3 install Pandas > NUL")
        else:
            os.system("pip3 install colorama > /dev/null")
            os.system("pip3 install Pandas > /dev/null")
    
# Clears Print Screen
def clear():
    if os.name == 'nt':
        _ = os.system('cls')

    else:
        _ = os.system('clear')


# This maybe fast then retyping input a bunch
def pause():
    input("Press Enter To Continue:> ")


# Main() is the first function
# Gets input from player to either Start Load Help or Exit
def main():
    setup()
    Screen.main_menu_screen()
    choice = input('\n\nSELECT A NUMBER:> ')

    if choice == '1':
        char_creation()
    elif choice == '2':             # LOADED AND SAVE
        print('NOT AN OPTION YET')
        time.sleep(2)
        main()
    elif choice == '3':             # Help
        print('NOT AN OPTION YET')
        time.sleep(2)
        main()
    elif choice == '4':
        ChangeLog.change_log_print()
        pause()
        main()
    elif choice == '5':
        sys.exit()
    else:
        print("Not an Option.")
        input("Press Enter to Continue:> ")
        main()


# Helps is to show player how to fight use items and more
# I think I will also make this accessable in game as well at some point

def game_help():
    pass


# This is where the player chooses what class he will be
def char_creation():
    global player_in_game

    # This function sets the name of the player
    def name_player():
        global player_name

        message = f"A {player_class_choice} is a good choice I think. What shall I call you?"
        Screen.display(message)
        option = input("\n\nENTER YOUR NAME:> ")

        if len(option) == 0:
            print('\nYou need to enter a name to continue\n')
            name_player()
        else:
            option1 = input("Are you Sure You Want To Keep This Name?\
             \n(1): Yes\n(2): No\n Enter A Number:> ")

            if option1 == '1':
                player_name = option
            else:
                name_player()

    # This sets the gender of the character
    def gender_call():
        global gender

        message = f"{player_name} the {player_class_choice}, has a nice ring to\
         it I think. I know it is obvious but just let me know what gender you are."

        Screen.display(message)
        option = input('\n\n(1): Male\n(2): Female\nEnter A Number:> ')
        if option == '1':
            gender = 'male'

        elif option == '2':
            gender = 'female'

        else:
            gender_call()
        Story.set_gender(gender)

    # This set the class for the player
    def class_selection():
        global player_class_choice
        player_options = ('Mage', 'Warrior', 'Archer', 'Assassin')
        Screen.char_options()

        choice = input('\n\nSELECT A NUMBER OR TYPE HELP THEN NUMBER:> ')

        if choice == '1':
            player_class_choice = player_options[int(choice) - 1]
        elif choice == '2':
            player_class_choice = player_options[int(choice) - 1]
        elif choice == '3':
            player_class_choice = player_options[int(choice) - 1]
        elif choice == '4':
            player_class_choice = player_options[int(choice) - 1]
        # lore is the story and it is found in InfoDics
        elif choice[0:4].lower() == 'info':
            lore = InfoDics.info_on_classes[player_options[int(choice[5]) - 1]]
            Screen.display(lore)
            input("\n\nPress Enter to Continue:> ")
            class_selection()
        else:
            print("Not An Option.")
            class_selection()

    class_selection()
    name_player()
    ##-- Mage     --##
    if player_class_choice == 'Mage':  
        player_in_game = Mage(char_name=player_name, player_class='Mage',max_health=80,melee_attack=1,magic_attack=10,
    max_mana=50, max_stamina=10, defense=1, pures=0, luck=1)
        player_in_game.equipped_weapon = Items.weak_staff
    ##-- Warrior  --##
    elif player_class_choice == 'Warrior':  
        player_in_game = Warrior(char_name=player_name, player_class='Warrior',max_health=150,melee_attack=10,magic_attack=0,
    max_mana=5, max_stamina=50, defense=4, pures=0, luck=0)
        player_in_game.equipped_weapon = Items.rusty_short_sword
    ##-- Archer   --##
    elif player_class_choice == 'Archer':  
        player_in_game = Archer(char_name=player_name, player_class='Archer',max_health=100,melee_attack=5,magic_attack=0,
    max_mana=50, max_stamina=10, defense=1, pures=0, luck=5)
        player_in_game.equipped_weapon = Items.common_hunting_bow
    ##-- Assassin --##
    elif player_class_choice == 'Assassin': 
        player_in_game = Assassin(char_name=player_name,player_class='Assassin',max_health=50,melee_attack=20,magic_attack=10,
    max_mana=25, max_stamina=10, defense=2, pures=100, luck=10)
        player_in_game.equipped_weapon = Items.rusty_dagger

    gender_call()

    # Back to main loop
    main_game_loop()


# Makes a random mob with in the range of the players level
def random_enemy():
    biome_info = Engine.get_tile(x,y)
    spawns = Biome.world_biomes[biome_info[0][2]]['spawns']
    if spawns == ["None"]:
        return None
    random_mob = random.choice(spawns)
    return hostile_mobs[random_mob]


# Encounter is to handle if we fight or not
# This probably needs some work
# I will work on this more once I get the
# Map done
def encounter():
    # num is subject to change as I add possible encounters
    num = random.randint(1, 1000)
    mob = random_enemy()
    clear()
    if mob is not None:
        print(f"You ran in a {mob.char_name} on the path.")
    pause()
    # combat()

    if biome_or_subBiome is False:
        main_game_loop()

    else:
        sub_map_move()


# This Function is to level up the player
# Needs to add more stats and change the
# the player levels up
def level_up(player):
#     player.level += 1
#     player.max_health = player.max_health + player.level
#     player.armor = player.armor + player.level
#     player.mana = player.mana + player.level
#     player.stamina = player.stamina + player.level
#     player.luck = player.luck + player.level
    
    player.level += 1
    choices = []
    skills = {"1": "HP", "2": "Armour", "3": "Mana", "4": "Stamina", "5": "Luck"}
    rows, columns = os.popen('stty size', 'r').read().split()
    for num in range(3):
        option = ""
        while option not in ["1", "2", "3", "4", "5"]:
            clear()
            print(f"Congrats! You have leveled up! You have {num+1} skill points available!")
            option = input("How would you like to use your skill point\n(1): HP\n(2): Armour\n(3): Mana\n(4): Stamina\n(5): Luck\nChoose A Number:>") 
        choices.append(option)
    print(f"Player skills increased ({skills[choices[0]]}, {skills[choices[1]]}, {skills[choices[2]]})")
    for i in choices:
        if i == "1":
            player.max_health = player.max_health + player.level
        if i == "2":
            player.armor = player.armor + player.level
        if i == "3":
            player.mana = player.mana + player.level
        if i == "4":
            player.stamina = player.stamina + player.level
        else:
            player.luck = player.luck + player.level
            

# This is to set up the fighting system
def combat(mob):
    clear()
    Screen.vs_screen(player_in_game, mob)
    Screen.stat_screen(player_in_game, mob)
    option = input('\n(1): Attack\n(2): Magic\n(3): Use Item\n(4): Run\nChoose A Number:> ')

    if option == '1':
        attack(mob)

    elif option == '2':
        magic(mob)

    elif option == '3':
        use_item(mob)

    elif option =='4':
        run(mob)
# Attack handles melee and magic attacks
# Unlike most games magic attacks aren't
# Just spells "magic attack" uses the
# Magic of the weapon in hand to deal
# Damage. But spells will be dealt with a
# Different functions

def attack(mob):
    
    player_melee_attack = random.randint(round(player_in_game.melee_attack / 2), player_in_game.melee_attack + player_in_game.equipped_weapon.melee_damage)
    player_magic_attack = random.randint(round(player_in_game.magic_attack / 2), player_in_game.magic_attack + player_in_game.equipped_weapon.magic_damage)
    enemy_attack = random.randint(round(mob.melee_attack / 2), mob.melee_attack)
    clear()
    Screen.vs_screen(player_in_game, mob)
    Screen.stat_screen(player_in_game, mob)
    attack_type = input('\n(1): Melee Attack\n(2): Magic Attack\nChoose A Number:> ')
    if attack_type == '1':
        if player_melee_attack == player_in_game.melee_attack / 2: ##-- Player Attack --##
            print(f"\n{player_in_game.name} {player_in_game.equipped_weapon.action_word}")  ##-- finish me --##
        else:
            mob.health -= player_melee_attack
            clear()
            print(f'\nYou just dealed {player_melee_attack} damage.')

        input('\nPess Enter To Continue:> ')
        if mob.health <= 0:
            win(mob)
        if enemy_attack == round(mob.melee_attack / 2):  ##--  Mob Attack --##
            clear()
            print(f'\n{mob.char_name} missed!')
        else:
            player_in_game.health -= enemy_attack
            clear()
            print(f'\n{mob.char_name} just dealed {enemy_attack} damage to you.')
        input('\nPress Enter To Continue:> ')
        if player_in_game.health <= 0:
            dead(mob)
        else:
            combat(mob)
    elif attack_type == '2':
        if player_magic_attack == player_in_game.magic_attack / 2:  ##-- Player Attack --##
            clear()
            print('\nYou Missed!')
        else:
            mob.health -= player_magic_attack
            clear()
            print(f'\nYou just dealed {player_magic_attack} damage.')

        input('\nPress Enter To Continue:> ')
        if mob.health <= 0:
            win(mob)
        if enemy_attack == round(mob.magic_attack / 2):  ##--  Mob Attack --##
            clear()
            print(f'\n{mob.char_name} missed!')
        else:
            player_in_game.health -= enemy_attack
            clear()
            print(f'\n{mob.char_name} just dealed {enemy_attack} damage to you.')
        input('\nPess Enter To Continue:> ')
        if player_in_game.health <= 0:
            dead(mob)
        else:
            combat(mob)

# Handles Spell Attacks and Healing or what ever else I can dream up
def magic(mob):
    print("not working yet. Sorry!")
    pause()
    attack(mob)

# Handles the use of potions or and other usable item
# In combat or out                                 --##
def use_item(mob):
    print("not working yet. Sorry!")
    pause()
    attack(mob)

# Run or Flee is to get away from the enemy in a fight
def run(mob):
    running = random.randint(1, 3)

    if running == 1:
        clear()
        print("You have successfully ran away!")
        input('\nPess Enter To Continue:> ')
        main_game_loop()

    else:
        clear()
        print("You Failed To Get Away!")
        input('\nPess Enter To Continue:> ')
    enemy_attack = random.randint(round(mob.melee_attack / 2), mob.melee_attack)

    if enemy_attack == round(mob.melee_attack / 2):
        clear()
        print(f'\n{mob.char_name} missed!')
    else:
        player_in_game.health -= enemy_attack
        clear()
        print(f'\n{mob.char_name} just dealed {enemy_attack} damage to you.')
    input('\nPess Enter To Continue:> ')

    if player_in_game.health <= 0:
        dead(mob)
    else:
        combat(mob)


# If you when a fight this function handles what happens
def win(mob):
    clear()
    player_in_game.pures += mob.pures
    player_in_game.exp += mob.exp_gained
    message = f"You just defeated a {mob.char_name}\nGold Looted: {mob.pures}\nEXP Gained: {mob.exp_gained}"
    print(message)
    input('\nPress Enter To Continue:> ')
    if not biome_or_subBiome:
        main_game_loop()

    else:
        sub_map_move()

# If in an unfortunate event the player dies this function is called
def dead(mob):
    print(f'You have died from {mob.char_name}')
    pause()
    main()


def get_resouces():
    biome_into = Engine.get_tile(x, y)
    biome_item = Biome.world_biomes[biome_into[2]]['resource']
    random_item = random.choice(biome_item)
    item = Items.resources[random_item]

    player_in_game.add_to_inventory(item)
    pause()

    if biome_or_subBiome is False:
        main_game_loop()

    else:
        sub_map_move()


def look_in_inventory():
    clear()
    print(f"Current Inventory: {player_in_game.inventory}")
    print(f"Inventory Limit: {player_in_game.inventory_limit}")
    pause()

    if biome_or_subBiome is False:
        main_game_loop()

    else:
        sub_map_move()


def sub_map_move():
    global biome_or_subBiome, x, y, sub_x, sub_y
    clear()
    biome_or_subBiome = True
    map_info = Engine.get_tile(x, y)
    sub_map_info = Engine.get_subTile(x, y, sub_x, sub_y)
    Engine.update_subTile(x, y, sub_x, sub_y, True)
    Screen.display(f"Biome in: {sub_map_info[0][4]}    Room: {sub_map_info[0][5]}")

    if sub_x == map_info[0][8] and sub_y == map_info[0][9]:
        options = "Which way do you want to move?\n\n" \
                  "(1): North\n" \
                  "(2): South\n" \
                  "(3): East\n" \
                  "(4): West\n" \
                  "(5): Look For Resources\n" \
                  "(6): Inventory\n" \
                  "(7): Exit\n" \
                  "Input a Number:>  "

    else:
        options = "Which way do you want to move?\n\n" \
                  "(1): North\n" \
                  "(2): South\n" \
                  "(3): East\n" \
                  "(4): West\n" \
                  "(5): Look For Resources\n" \
                  "(6): Inventory\n" \
                  "Input a Number:>  "

    move_to = input(options)

    # NORTH = 1, SOUTH = 2, EAST = 3, & WEST = 4
    if move_to == '1':              # UP
        if sub_y > 0:
            sub_y -= 1
            encounter()
        else:
            print('Looks Like It Dead Ends Here')
            pause()
            main_game_loop()

    elif move_to == '2':            # DOWN
        if sub_y < small:
            sub_y += 1
            encounter()
        else:
            print('Looks Like It Dead Ends Here')
            pause()
            main_game_loop()

    elif move_to == '3':            # RIGHT
        if sub_x > 0:
            sub_x += 1
            encounter()
        else:
            print('Looks Like It Dead Ends Here')
            pause()
            main_game_loop()

    elif move_to == '4':            # LEFT
        if sub_x < small:
            sub_x -= 1
            encounter()
        else:
            print('Looks Like It Dead Ends Here')
            pause()
            main_game_loop()

    elif move_to == '5':
        get_resouces()

    elif move_to == '6':
        look_in_inventory()

    elif move_to == '7' and sub_x == map_info[0][8] and sub_y == map_info[0][9]:
        main_game_loop()

    elif move_to == 'Quit':  # QUIT, I'll take this out after testing
        sys.exit()


# The Inspect function checks the biome for the player to see if it has anything
# is interesting and of value.
# Biome, Tell player about the area they are in
# Rarity, Tell player how rare the biome is
# Enterable, Tells the player if you can explore the area any more
# Spawnable Mobs, Tells player what mobs can spawn in area
# Items that can be obtained for crafting
# Coords for area
# Time of day..... maybe
def inspect_area(biome):
    clear()
    print(f"Biome Name: {Biome.world_biomes[biome]['name']}")
    print(f"Resourse: {Biome.world_biomes[biome]['resource']}")
    print(f"Spawn: {Biome.world_biomes[biome]['spawns']}")
    print(f"Rarity: {Biome.world_biomes[biome]['rarity']}")
    # print(f"Enterable: {Biome.world_biomes[biome]['enterable']}")
    print(f"{Biome.world_biomes[biome]['info']}")
    print("\n----------------------------------------------\n")

    if Biome.world_biomes[biome]['enterable'] is True:
        print(f"Looks likes like we can go futher into the {Biome.world_biomes[biome]['name']}\nWhat say you?")
        player_input = input("\n(1): Enter\n(2): Move on\nChoose a number:> ")
        if player_input == '1':
            sub_map_move()

    else:
        pause()
        main_game_loop()


# main_game_loop() is where all the logic for the player to move about the map
# or any other event while not in a fight
def main_game_loop():
    # This is for navigating the map
    global opening, x, y, sub_x, sub_y, biome_or_subBiome

    biome_or_subBiome = False

    if os.path.getsize('Worldmap.db') == 12288:
        Engine.map_builder()
    # while os.path.getsize('Worldmap.db') != 10000:
    #     print('Loading...........')

    if opening:
        Story.intro_story(player_in_game.char_name)
        input("Press Enter to continue: ")
        opening = False

    map_info = Engine.get_tile(x, y)
    sub_x = map_info[0][8]
    sub_y = map_info[0][9]
    Engine.update_tile(x, y, True)
    Screen.display(f"Location: {map_info[0][3]}")

    move_to = input(
        "Which way do you want to travel?\n\n"
        "(1): North\n"
        "(2): South\n"
        "(3): East\n"
        "(4): West\n"
        "(5): Inspect Area\n"
        "(6): Inventory\n"
        "(7): Look For Resources\n"
        "Input a Number:>  ")

    # NORTH = 1, SOUTH = 2, EAST = 3, & WEST = 4
    if move_to == '1':              # UP
        if y > 0:
            y -= 1
            encounter()
        else:
            print('NEED TO MAKE THE PLAYER TO TELEPORT TO OTHER SIDE OF MAP')
            pause()
            main_game_loop()

    elif move_to == '2':            # DOWN
        if y < small:
            y += 1
            encounter()
        else:
            print('NEED TO MAKE THE PLAYER TO TELEPORT TO OTHER SIDE OF MAP')
            pause()
            main_game_loop()

    elif move_to == '3':            # RIGHT
        if x > 0:
            x += 1
            encounter()
        else:
            print('NEED TO MAKE THE PLAYER TO TELEPORT TO OTHER SIDE OF MAP')
            pause()
            main_game_loop()

    elif move_to == '4':            # LEFT
        if x < small:
            x -= 1
            encounter()
        else:
            print('NEED TO MAKE THE PLAYER TO TELEPORT TO OTHER SIDE OF MAP')
            pause()
            main_game_loop()

    elif move_to == '5':
        inspect_area(map_info[0][2])

    elif move_to == '6':
        look_in_inventory()

    elif move_to == '7':
        get_resouces()

    elif move_to == 'Quit':         # QUIT, I'll take this out after testing
        sys.exit()

    else:
        print("Not an option.")
        pause()
        main_game_loop()


Engine.make_map_datebase()

main()
