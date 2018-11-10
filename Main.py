##-- Starting Data November 6, 2018 --##
##-- Made By Cowboy8625             --##
##-- Waste Land                     --##

##-- Import Modules --##
import cmd
import os
import random
import sys
import textwrap
import time

##-- Custom Imports --##
import InfoDics
import Map
import Screen
import Mobs
import Items
import NPC

##-- Globel Varibles --##

player_in_game = ''
opening = True ##-- Only True if hasnt seen opening story --##
turn = True  ##-- If True it's the players turn --##
x = 1
y = 3

##-- Clears PRint Screen --##

def clear():
    
    if os.name == 'nt':
        _ = os.system('cls')

    else:
        _ = os.system('clear')

##-- Inventory layout --##

class PlayerInventory:

    def __init__(self):

        self.can_carry = 10 
        self.on_player = []
        self.in_hand = Items.weapons['short_sword']['damage']

    def add_to_inventory(self, add_item):

        self.add_item = add_item

    def remove_from_inv(self, remove_item):

        self.remove_item = remove_item
    
    def hand_swap(self, requested_item):

        self.requested_item = requested_item

##-- Player Inventory __init__ Call --##

player_inventory = PlayerInventory()

##-- Setting up the players attubuts --##

class Mage:

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.max_health = 80
        self.health = 80
        self.armor = 0
        self.melee_attack = 1
        self.magic_attack = 10
        self.mana = 25
        self.stamina = 10
        self.defense = 1
        self.pures = 0
        self.luck = 5

class Warrior:
    
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.max_health = 150
        self.health = 150
        self.armor = 10
        self.melee_attack = 5
        self.magic_attack = 0
        self.mana = 10
        self.stamina = 20
        self.defense = 1
        self.pures = 0
        self.luck = 0

class Archer:
    
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.max_health = 80
        self.health = 80
        self.armor = 5
        self.melee_attack = 5
        self.magic_attack = 5
        self.mana = 15
        self.stamina = 20
        self.defense = 1
        self.pures = 0
        self.luck = 2

class Assassin:
    
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.max_health = 50
        self.health = 50
        self.armor = 5
        self.melee_attack = 5
        self.magic_attack = 0
        self.mana = 10
        self.stamina = 25
        self.defense = 1
        self.pures = 0
        self.luck = 3

##-- Main() is the first function --##
##-- Gets input from player to either Start Load Help or Exit --##

def main():
    
    while True:
        Screen.main_menu_screen()
        choice = input('\n\nChoose a number:> ')
        
        if choice == '1':
            char_creation()
            break
        
        elif choice == '2':
            print('NOT AN OPTION YET')
            time.sleep(2)

        elif choice == '3':
            game_help()

        elif choice == '4':
            sys.exit()

##-- Helps player know what to do --##

def game_help():
    pass

##-- This is where the player chooses what class he will be --##

def char_creation():
    
    global player_in_game
    player_options = ['Mage', 'Warrior', 'Archer', 'Assassin']
    
    while True:
        
        Screen.char_options()
        
        try:
            
            choice = input('\n\nSELECT A NUMBER OR TYPE HELP:> ')

            if choice[0] in '1234':
                num = int(choice[0]) - 1
                Screen.name_player(player_options[num])
                break

            elif choice[0].lower() == 'i':
                clear()
                try:
                    lore = InfoDics.info_on_classes[player_options[int(choice[5])-1]] ##-- lore is the story and it is found in InfoDics --##
  
                    Screen.display(lore)
                            
                    input("\n\nPress Enter to Continue:> ")
                    continue
                except:
                    print("Invaled Command")

        except:
            print("That's not an option.")

    player_name = input('\n\nENTER YOUR NAME:> ')
    if player_options[num] == 'Mage':
        player_in_game = Mage(player_name)

    elif player_options[num] == 'Warrior':
        player_in_game = Warrior(player_name)

    elif player_options[num] == 'Archer':
        player_in_game = Archer(player_name)

    elif player_options[num] == 'Assassin':
        player_in_game = Assassin(player_name)
    
    main_game_loop()


##-- encounter is to handle if we fight or not --##

def encounter():
    
    num = random.randint(1, 6)

    if num is 1:
        Screen.display("You see a Deer/Animal.")
        input("Press Enter to continue: ")
        combat('animal')
    
    elif num is 2:
        Screen.display("You came accoss some treaser")
        input("Press Enter to continue: ")
        main_game_loop()

    elif num is 3:
        Screen.display("A mob attacks you!")
        input("Press Enter to continue: ")
        combat('random mob')

    elif num is 4:
        Screen.display("You see a person aproching! Do you hide?")
        input("Press Enter to continue: ")
        main_game_loop()

    elif num is 5:
        Screen.display('Some bandits attack you')
        input("Press Enter to continue: ")
        combat('human')

    elif num is 6:
        Screen.display(" This area is infested with blah blah")
        input("Press Enter to continue: ")
        main_game_loop()

##-- This Function is to level up the player --##

def level_up(player):
    

    player.level += 1
    player.max_health = player.max_health + player.level
    player.armor = player.armor + player.level
    player.mana = player.mana + player.level
    player.stamina = player.stamina + player.level
    player.luck = player.luck + player.level
    # print(f"Level: {player.level}")
    # print(f"Health: {player.max_health}")
    # print(f"Armor: {player.armor}")
    # print(f"Mana: {player.mana}")
    # print(f"Stamina: {player.stamina}")
    # print(f"Luck: {player.luck}")

##-- This is to set up the fighting system --##

def combat(combat_choice):
    m = []

    mob = Mobs.random_enemy(player_in_game.level)
    m.append(mob)

    def in_combat(player, mob): ##-- This will handle all the combat --##
                                ##-- Takes to argument               --## 
        global turn ##-- If True it's the players turn --##
        while True:
            Screen.combat_screen(player_in_game, m[0])
            player_move = input('\n\n(1): Melee Attack\n(2): Magic Attack\n(3): Run\nChoose A Number:> ')

            if player_move == '1':  ##-- Handles Melee Attacks
                attacker = player.melee_attack + player_inventory.in_hand
                deffender = mob.defense - mob.armor

                mob.health -= attacker - deffender

            elif player_move == '2':        ##-- Handles Magic Attacks --##
                attacker = player.magic_attack + player_inventory.in_hand
                deffender = mob.defense - mob.armor

                mob.health -= attacker - deffender           

            elif player_move == '3':

                sys.exit()
        
    
    if combat_choice == 'random mob':
        in_combat(player_in_game, m[0])
        input("Press Enter to continue: ")
        main_game_loop()
        
    elif combat_choice == 'animal':
        in_combat(player_in_game, m[0])
        input("Press Enter to continue: ")
        main_game_loop()

    elif combat_choice == 'human':
        in_combat(player_in_game, m[0])
        input("Press Enter to continue: ")
        main_game_loop()

def main_game_loop():
    
    ##-- This is for navigating the map --##
    global opening, x, y

    if opening == True:
        Screen.display(InfoDics.story_line['Intro'])
        input("Press Enter to continue: ")
        opening = False

    while True:
        
        try:
            
            Screen.display(f"Location: {Map.map[(x, y)]['name']}")
            move_to = input("Which way do you want to travel?\n\n(1): North\n(2): South\n(3): East\n(4): West\n(5): Quit\nInput a Number:>  ")
            ##-- NORTH = 1, SOUTH = 2, EAST = 3, & WEST = 4
            if move_to == '1':  ##-- UP --##
                y -= 1
                print(f"Location: {Map.map[(x, y)]['name']}")
                input("Press Enter to continue: ")
                encounter()
                break
            
            elif move_to == '2':  ##-- DOWN --##
                y += 1
                print(f"Location: {Map.map[(x, y)]['name']}")
                input("Press Enter to continue: ")
                encounter()
                break

            elif move_to == '3':  ##-- RIGHT --##
                x += 1
                print(f"Location: {Map.map[(x, y)]['name']}")
                input("Press Enter to continue: ")
                encounter()
                break
            
            elif move_to == '4':  ##-- LEFT --##
                x -= 1
                print(f"Location: {Map.map[(x, y)]['name']}")
                input("Press Enter to continue: ")
                encounter()
                break
            
            elif move_to == '5':  ##-- QUIT, I'll take this out after testing --## 
                break

        except Exception as e:
            print(e)
            print("That is undiscovered area, we best stay on the map.")
            print("you have been teleported home")
            y = 1
            x = 1
    
        input("Press Enter to continue: ")

        clear()
    





main()
