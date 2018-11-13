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
player_name = 'X'         ##-- This is for the Funtion char_creation()            --##
player_class_choice = 'X' ##-- This is also for the Funtion char_creation()       --##
player_in_game = 'X'      ##-- Again this is also for the Funtion char_creation() --##
mob = 'X'                 ##-- This varible is to hold the current mob player is fighing --##
gender = 'X'              ##-- This varible sets the pronouns for the story and is set in the function in char_creation() in gender_call() --##
opening = True            ##-- Only True if hasnt seen opening story --##
turn = True               ##-- If True it's the players turn         --##
x = 1                     ##-- Y Coords --##
y = 3                     ##-- X Coords --##



##-- Clears Print Screen --##

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
        self.in_hand = ''
    ##-- Below code is not in use and will change one I start using it --##
    def add_to_inventory(self, add_item): 

        self.add_item = add_item

    def remove_from_inv(self, remove_item):

        self.remove_item = remove_item
    
    def hand_swap(self, requested_item):

        self.requested_item = requested_item

##-- Player Inventory __init__ Call --##

player_inventory = PlayerInventory()

##-- Setting up the players attubuts or classes --##
##-- Not sure if I did this right.              --##

class Mage:

    def __init__(self, name):
        self.name = name
        self.player_class = 'Mage'
        self.level = 1
        self.exp = 0
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
        self.player_class = 'Warrior'
        self.level = 1
        self.exp = 0
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
        self.player_class = 'Archer'
        self.level = 1
        self.exp = 0
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
        self.player_class = 'Assassin'
        self.level = 1
        self.exp = 0
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
    
    Screen.main_menu_screen()
    choice = input('\n\nSELECT A NUMBER:> ')
    
    if choice == '1':
        char_creation()
    
    elif choice == '2':
        print('NOT AN OPTION YET') ##-- LOADED AND SAVE --##
        time.sleep(2)
        main()

    elif choice == '3':
        print('NOT AN OPTION YET') ##-- Help  --##
        time.sleep(2)
        main()

    elif choice == '4':
        sys.exit()
    else:
        print("Not an Option.")
        input("Press Enter to Continue:> ")
        main()

##-- Helps is to show player how to fight use items and more                --##
##-- I think I will also make this accessable in game as well at some point --##

def game_help():
    pass

##-- This is where the player chooses what class he will be --##

def char_creation():
    global player_in_game
    ##-- This function sets the name of the player --##
    def name_player():
        global player_name
        
        message = f"A {player_class_choice} is a good choice I think. What shall shall I call you?"
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

    ##-- This sets the gender of the character --##

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
    ##-- This set the class for the player --## 
    def class_selection():
        global player_class_choice
        player_options = ('Mage', 'Warrior', 'Archer', 'Assassin')
        Screen.char_options()

        choice = input('\n\nSELECT A NUMBER OR TYPE HELP THEN NUMBER:> ')

        if choice == '1':
            player_class_choice = player_options[int(choice)-1]
        elif choice == '2':
            player_class_choice = player_options[int(choice)-1]
        elif choice == '3':
            player_class_choice = player_options[int(choice)-1]
        elif choice == '4':
            player_class_choice = player_options[int(choice)-1]
        ##-- lore is the story and it is found in InfoDics --##
        elif choice[0:4].lower() == 'help': 
            lore = InfoDics.info_on_classes[player_options[int(choice[5])-1]] 
            Screen.display(lore)      
            input("\n\nPress Enter to Continue:> ")
            class_selection()
        else:
            print("Not An Option.")
            class_selection()

    class_selection()
    name_player()
    ##-- This takes the varibles from the the global varibles that where set in --##
    ##-- class_selection(), gender_call() and name_player() to set the players  --##
    ##-- class to be Mage, Warrior, Archer or Assassin                          --## 
    ##-- Mage     --##
    if player_class_choice == 'Mage':  
        player_in_game = Mage(player_name)
        player_inventory.in_hand = Items.staff['weak_staff']
    ##-- Warrior  --##
    elif player_class_choice == 'Warrior':  
        player_in_game = Warrior(player_name)
        player_inventory.in_hand = Items.swords['rusty_short_sword']
    ##-- Archer   --##
    elif player_class_choice == 'Archer':  
        player_in_game = Archer(player_name)
        player_inventory.in_hand = Items.bow['common_hunting_bow']
    ##-- Assassin --##
    elif player_class_choice == 'Assassin': 
        player_in_game = Assassin(player_name)
        player_inventory.in_hand = Items.staff['rusty_dagger']

    gender_call()
    ##-- Back to main loop --##           
    main_game_loop()

##-- Makes a random mob with in the range of the players level --##

def random_enemy():
    global mob
    mob = Mobs.random_enemy(player_in_game.level)

##-- Encounter is to handle if we fight or not --##
##-- This probably needs some work             --##

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
##-- Needs to add more stats and change the  --##
##-- the player levels up                    --##

def level_up(player):
    

    player.level += 1
    player.max_health = player.max_health + player.level
    player.armor = player.armor + player.level
    player.mana = player.mana + player.level
    player.stamina = player.stamina + player.level
    player.luck = player.luck + player.level


##-- This is to set up the fighting system --##

def combat():

    clear()
    Screen.vs_screen(player_in_game, mob)
    Screen.stat_screen(player_in_game, player_inventory, mob)
    option = input('\n(1): Attack\n(2): Magic\n(3): Use Item\n(4): Run\nChoose A Number:> ')

    if option == '1':
        attack()

    elif option == '2':
        magic()

    elif option == '3':
        use_item()

    elif option =='4':
        run()
##-- Attack handles melee and magic attacks --##
##-- Unlike most games magic attacks aren't --##
##-- Just spells "magic attack" uses the    --##
##-- Magic of the weapon in hand to deal    --##
##-- Damage. But spells will be delt with a --##
##-- Different functions                    --##
def attack():

    player_melee_attack = random.randint(round(player_in_game.melee_attack / 2), player_in_game.melee_attack + player_inventory.in_hand['melee_damage'])
    player_magic_attack = random.randint(round(player_in_game.magic_attack / 2), player_in_game.magic_attack + player_inventory.in_hand['magic_damage'])    
    enemy_attack = random.randint(round(mob.melee_attack / 2), mob.melee_attack)
    clear()
    Screen.vs_screen(player_in_game, mob)
    Screen.stat_screen(player_in_game,player_inventory, mob)
    attack_type = input('\n(1): Melee Attack\n(2): Magic Attack\nChoose A Number:> ')
    if attack_type == '1':
        if player_melee_attack == player_in_game.melee_attack / 2: ##-- Player Attack --##
            print(f"\n{player_in_game.name} {player_inventory.in_hand['action']}")  ##-- finish me --#############################
        else:
            mob.health -= player_melee_attack
            clear()       
            print(f'\nYou just dealed {player_melee_attack} damage.')

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
    
    elif attack_type == '2':

        if player_magic_attack == player_in_game.magic_attack / 2: ##-- Player Attack --##
            print('\nYou Missed!')
        else:
            mob.health -= player_magic_attack
            clear()       
            print(f'\nYou just dealed {player_magic_attack} damage.')

        input('\nPess Enter To Continue:> ')
        if mob.health <= 0:
            win()
        
        if enemy_attack == round(mob.magic_attack / 2):  ##--  Mob Attack --##
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

##-- Handles Spell Attacks and Healing or what ever else I can dream up --##
def magic():
    pass

##-- Handles the use of potions or and other usable item --##
##-- In combat or out                                    --##
def use_item():
    pass

##-- Run or Flee is to get away from the enemy in a fight --##
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

##-- If you when a fight this function handles what happens --##

def win():
    clear()
    player_in_game.pures += mob.pures
    player_in_game.exp += mob.exp_gained
    message = f"You just defeated a {mob.name}\nGold Looted: {mob.pures}\nEXP Gained: {mob.exp_gained}"
    print(message)
    input('\nPess Enter To Continue:> ')
    main_game_loop()

##-- If in an unfortunate event the player dies this function is called --##
 
def dead():
    print(f'You have died from {mob.name}')

##-- main_game_loop() is where all the logic for the player to move about the map --##
##-- or any other event while not in a fight                                      --##

def main_game_loop():
    
    ##-- This is for navigating the map --##
    global opening, x, y

    if opening == True:
        Story.intro_story(player_in_game.name)
        #Screen.display(InfoDics.story_line['Intro'])
        input("Press Enter to continue: ")
        opening = False

    Screen.display(f"Location: {Map.map[(x, y)]['name']}")
    move_to = input("Which way do you want to travel?\n\n(1): North\n(2): South\n(3): East\n(4): West\n(5): Quit\nInput a Number:>  ")
    ##-- NORTH = 1, SOUTH = 2, EAST = 3, & WEST = 4
    if move_to == '1':  ##-- UP --##
        y -= 1
        encounter()
    
    elif move_to == '2':  ##-- DOWN --##
        y += 1
        encounter()

    elif move_to == '3':  ##-- RIGHT --##
        x += 1
        encounter()
    
    elif move_to == '4':  ##-- LEFT --##
        x -= 1
        encounter()
    
    elif move_to == '5':  ##-- QUIT, I'll take this out after testing --## 
        sys.exit()

    else:
        print("That is undiscovered area, we best stay on the map.")
        print("you have been teleported home")
        y = 1
        x = 1
        input("Press Enter to continue: ")
        main_game_loop()
    

main()
