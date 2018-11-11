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
import Story
import Map
import Screen
import Mobs
import Items
import NPC

##-- Globel Varibles --##

player_in_game = ''
mob = ''
opening = True ##-- Only True if hasnt seen opening story --##
turn = True    ##-- If True it's the players turn         --##
x = 1          ##-- Y Coords --##
y = 3          ##-- X Coords --##



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
    while len(player_name) == 0:
        player_name = input('\n\nENTER YOUR NAME:> ')

        if len(player_name) == 0:
            print("You need a name!")
            input("\nEnter to continue:> ")
    
    if player_options[num] == 'Mage':
        player_in_game = Mage(player_name)

    elif player_options[num] == 'Warrior':
        player_in_game = Warrior(player_name)

    elif player_options[num] == 'Archer':
        player_in_game = Archer(player_name)

    elif player_options[num] == 'Assassin':
        player_in_game = Assassin(player_name)
    
    main_game_loop()

##-- Makes a random mob with in the range of the players level --##


def random_enemy():
    global mob
    mob = Mobs.random_enemy(player_in_game.level)

##-- encounter is to handle if we fight or not --##

def encounter():
    
    num = random.randint(1, 6)
    random_enemy()

    if num is 1:
        clear()
        Screen.display("You see a Deer/Animal.")
        input("Press Enter to continue: ")
        combat()
    
    elif num is 2:
        clear()
        Screen.display("You came accoss some treaser")
        input("Press Enter to continue: ")
        main_game_loop()

    elif num is 3:
        clear()
        Screen.display("A mob attacks you!")
        input("Press Enter to continue: ")
        combat()

    elif num is 4:
        clear()
        Screen.display("You see a person aproching! Do you hide?")
        input("Press Enter to continue: ")
        main_game_loop()

    elif num is 5:
        clear()
        Screen.display('Some bandits attack you')
        input("Press Enter to continue: ")
        combat()

    elif num is 6:
        clear()
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


##-- This is to set up the fighting system --##

def combat():
    #clear()

    Screen.vs_screen(player_in_game, mob)
    Screen.stat_screen(player_in_game, mob)
    option = input('\n(1): Attack\n(2): Use Item\n(3): Run\nChoose A Number:> ')

    if option == '1':
        attack()

    elif option == '2':
        use_item()

    elif option =='3':
        run()

def attack():

    player_attack = random.randint(round(player_in_game.melee_attack / 2), player_in_game.melee_attack + player_inventory.in_hand)
    enemy_attack = random.randint(round(mob.melee_attack / 2), mob.melee_attack)
    clear()
    Screen.vs_screen(player_in_game, mob)
    Screen.stat_screen(player_in_game, mob)
    if player_attack == player_in_game.melee_attack / 2: ##-- Player Attack --##
        print('\nYou Missed!')
    else:
        mob.health -= player_attack
        clear()       
        print(f'\nYou just dealed {player_attack} damage.')

    input('\nPess Enter To Continue:> ')
    if mob.health <= 0:
        win()
    
    if enemy_attack == round(mob.melee_attack / 2):  ##--  Mob Attack --##
        clear()
        print(f'\n{mob.name} missed!')
    else:
        player_in_game.health -= enemy_attack
        clear()
        print(f'\n{mob.name} just dealed {enemy_attack} damage to you.')
    input('\nPess Enter To Continue:> ')
    if player_in_game.health <= 0:
        dead()
    else:
        combat()
    
def use_item():
    pass

def run():
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
        print(f'\n{mob.name} missed!')
    else:
        player_in_game.health -= enemy_attack
        clear()
        print(f'\n{mob.name} just dealed {enemy_attack} damage to you.')
    input('\nPess Enter To Continue:> ')
    if player_in_game.health <= 0:
        dead()
    else:
        combat()

def win():
    pass

def dead():
    pass

def main_game_loop():
    
    ##-- This is for navigating the map --##
    global opening, x, y

    if opening == True:
        Story.intro_story(player_in_game.name)
        #Screen.display(InfoDics.story_line['Intro'])
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
# player_in_game = Warrior('Quoth')
# random_enemy()
# print(mob.name, mob.health)
# mob.health -= (player_in_game.melee_attack + player_inventory.in_hand)
# print(mob.name, mob.health)
main()
