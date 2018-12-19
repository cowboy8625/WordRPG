# Starting Data November 6, 2018
# Made By Cowboy8625
# Waste Land
__author__ = 'Cowboy8625', 'Cyy', 'BJTMastermind', 'HexTree', 'Byteme8bit', 'Giioke', 'ThePinkChicken'

# Import Modules
import random
import sys
import time

from Mechanics.core_mechanics import *
from script import Screen
from Mechanics.ui_mechanics import *
import ChangeLog


# If True it's the players turn
turn = True


# Main() is the first function
# Gets input from player to either Start Load Help or Exit
def main():
    Screen.main_menu_screen()
    choice = input('\n\nSELECT A NUMBER:> ')

    if choice == '1':
        main_game_loop(char_creation(), opening=True)
    elif choice == '2':  # LOADED AND SAVE
        print('NOT AN OPTION YET')
        time.sleep(2)
        main()
    elif choice == '3':  # Help
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
        pause()
        main()


"""
# Makes a random mob with in the range of the players level
def random_enemy():

    biome_info = Engine.get_tile(x,y)
    spawns = getattr(Biome.World, biome_info[0][2]).spawns
    if not spawns:
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


# This is to set up the fighting system
def combat(mob):
    clear()
    Screen.vs_screen(player_in_game, mob)
    Screen.stat_screen(player_in_game, mob)
    option = input('\n'
                   '(1): Attack\n'
                   '(2): Magic\n'
                   '(3): Use Item\n'
                   '(4): Run\n'
                   'Choose A Number:> ')

    if option == '1':
        attack(mob)

    elif option == '2':
        magic(mob)

    elif option == '3':
        use_item(mob)

    elif option == '4':
        run(mob)


# Attack handles melee and magic attacks
# Unlike most games magic attacks aren't
# Just spells "magic attack" uses the
# Magic of the weapon in hand to deal
# Damage. But spells will be dealt with a
# Different functions

def attack(mob):
    player_melee_attack = random.randint(round(player_in_game.melee_attack / 2),
                                         player_in_game.melee_attack + player_in_game.equipped_weapon.melee_damage)
    player_magic_attack = random.randint(round(player_in_game.magic_attack / 2),
                                         player_in_game.magic_attack + player_in_game.equipped_weapon.magic_damage)
    enemy_attack = random.randint(round(mob.melee_attack / 2), mob.melee_attack)
    clear()
    Screen.vs_screen(player_in_game, mob)
    Screen.stat_screen(player_in_game, mob)
    attack_type = input('\n(1): Melee Attack\n(2): Magic Attack\nChoose A Number:> ')
    if attack_type == '1':
        if player_melee_attack == player_in_game.melee_attack / 2:                          # Player Attack
            print(f"\n{player_in_game.name} {player_in_game.equipped_weapon.action_word}")  # finish me

        else:
            mob.health -= player_melee_attack
            clear()
            print(f'\nYou just dealt {player_melee_attack} damage.')

        pause()

        if mob.health <= 0:
            win(mob)

        if enemy_attack == round(mob.melee_attack / 2):                                     # Mob Attack
            clear()
            print(f'\n{mob.char_name} missed!')

        else:
            player_in_game.health -= enemy_attack
            clear()
            print(f'\n{mob.char_name} just dealt {enemy_attack} damage to you.')

        pause()

        if player_in_game.health <= 0:
            dead(mob)

        else:
            combat(mob)

    elif attack_type == '2':
        if player_magic_attack == player_in_game.magic_attack / 2:                          # Player Attack
            clear()
            print('\nYou Missed!')

        else:
            mob.health -= player_magic_attack
            clear()
            print(f'\nYou just dealt {player_magic_attack} damage.')

        pause()

        if mob.health <= 0:
            win(mob)

        if enemy_attack == round(mob.magic_attack / 2):                                     # Mob Attack
            clear()
            print(f'\n{mob.char_name} missed!')

        else:
            player_in_game.health -= enemy_attack
            clear()
            print(f'\n{mob.char_name} just dealed {enemy_attack} damage to you.')

        pause()

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
        pause()
        main_game_loop()

    else:
        clear()
        print("You Failed To Get Away!")
        pause()
    enemy_attack = random.randint(round(mob.melee_attack / 2), mob.melee_attack)

    if enemy_attack == round(mob.melee_attack / 2):
        clear()
        print(f'\n{mob.char_name} missed!')
    else:
        player_in_game.health -= enemy_attack
        clear()
        print(f'\n{mob.char_name} just dealed {enemy_attack} damage to you.')
    pause()

    if player_in_game.health <= 0:
        dead(mob)
    else:
        combat(mob)


# If you when a fight this function handles what happens
def win(mob):
    clear()
    player_in_game.pures += mob.pures
    player_in_game.exp += mob.exp_gained
    print(f"You just defeated a {mob.char_name}\n"
          f"Gold Looted: {mob.pures}\n"
          f"EXP Gained: {mob.exp_gained}")
    pause()

    if not biome_or_subBiome:
        main_game_loop()

    else:
        sub_map_move()


# If in an unfortunate event the player dies this function is called
def dead(mob):
    print(f'You have died from {mob.char_name}')
    pause()
    main()


def get_resources():
    biome_into = Engine.get_tile(x, y)
    biome_item = getattr(Biome.World, biome_into[2]).resources
    random_item = random.choice(biome_item)
    item = Items.resources[random_item]

    player_in_game.add_to_inventory(item)
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
    if move_to == '1':  # UP
        if sub_y > 0:
            sub_y -= 1
            encounter()
        else:
            print('Looks Like It Dead Ends Here')
            pause()
            main_game_loop()

    elif move_to == '2':  # DOWN
        if sub_y < small:
            sub_y += 1
            encounter()
        else:
            print('Looks Like It Dead Ends Here')
            pause()
            main_game_loop()

    elif move_to == '3':  # RIGHT
        if sub_x > 0:
            sub_x += 1
            encounter()
        else:
            print('Looks Like It Dead Ends Here')
            pause()
            main_game_loop()

    elif move_to == '4':  # LEFT
        if sub_x < small:
            sub_x -= 1
            encounter()
        else:
            print('Looks Like It Dead Ends Here')
            pause()
            main_game_loop()

    elif move_to == '5':
        get_resources()

    elif move_to == '6':
        player_in_game.look_in_inventory()

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
    print(f"Biome Name: {getattr(Biome.World, biome).name}")
    print(f"Resourse: {getattr(Biome.World, biome).resource}")
    print(f"Spawn: {getattr(Biome.World, biome).spawns}")
    print(f"Rarity: {getattr(Biome.World, biome).rarity}")
    # print(f"Enterable: {Biome.world_biomes[biome]['enterable']}")
    print(f"{getattr(Biome.World, biome).info}")
    print("\n----------------------------------------------\n")


    if getattr(Biome.World, biome).enterable is True:
        print(f"Looks likes like we can go futher into the {getattr(Biome.World, biome).name}\nWhat say you?")
        player_input = input("\n(1): Enter\n(2): Move on\nChoose a number:> ")

        if player_input == '1':
            sub_map_move()

    else:
        pause()
        main_game_loop()


"""


# main_game_loop() is where all the logic for the player to move about the map
# or any other event while not in a fight
def main_game_loop(player, opening=True):

    if opening:
        Story.intro_story(player.name)
        input("Press Enter to continue: ")
        opening = False

    while True:
        # move_error_msg = 'NEED TO MAKE THE PLAYER TO TELEPORT TO OTHER SIDE OF MAP'
        clear()
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

        """
        # NORTH = 1, SOUTH = 2, EAST = 3, & WEST = 4
        if move_to == '1':  # UP
            if y > 0:
                y -= 1
                encounter()
            else:
                print(move_error_msg)
                pause()
                # main_game_loop()

        elif move_to == '2':  # DOWN
            if y < small:
                y += 1
                encounter()
            else:
                print(move_error_msg)
                pause()
                # main_game_loop()

        elif move_to == '3':  # RIGHT
            if x > 0:
                x += 1
                encounter()
            else:
                print(move_error_msg)
                pause()
                # main_game_loop()

        elif move_to == '4':  # LEFT
            if x < small:
                x -= 1
                encounter()
            else:
                print(move_error_msg)
                pause()
                # main_game_loop()

        elif move_to == '5':
            inspect_area(map_info[0][2])

        elif move_to == '6':
            player_in_game.look_in_inventory()

        elif move_to == '7':
            get_resources()
        """
        if move_to == 'Quit':  # QUIT, I'll take this out after testing
            sys.exit()

        else:
            print("Not an option... Yet ;)")
            pause()


if __name__ == "__main__":
    main()

