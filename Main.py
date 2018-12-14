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
from Map_Gen import Engine
from Map_Gen import Biome
from script import InfoDics
from script import Items
from script import Map
from script import Mobs
from script import NPC
from script import Screen
from script import Story
import ChangeLog

##-- Globel Varibles --##
player_name = 'X'         ##-- This is for the Funtion char_creation()            --##
player_class_choice = 'X' ##-- This is also for the Funtion char_creation()       --##
player_in_game = 'X'      ##-- Again this is also for the Funtion char_creation() --##
mob = 'X'                 ##-- This varible is to hold the current mob player is fighing --##
gender = 'X'              ##-- This varible sets the pronouns for the story and is set in the function in char_creation() in gender_call() --##
opening = True            ##-- Only True if hasnt seen opening story --##
turn = True               ##-- If True it's the players turn         --##
x = 5                     ##-- Y Coords --##
y = 0                     ##-- X Coords --##
sub_x = 0                 ##-- For Map in side of biome --##
sub_y = 0                 ##--  ^^       ^^       ^^    --##
biome_or_subBiome = False ##-- To see if player is in a biome or not --##
##-- Map sizes --##
small = 100
medium = 500
large = 1000



##-- Clears Print Screen --##

def clear():
    
    if os.name == 'nt':
        _ = os.system('cls')

    else:
        _ = os.system('clear')
##-- This maybe fast then retyping input a bunch --##

def pause():
    
    input("Press Enter To Continue:> ")

##-- Inventory layout --##

class PlayerInventory:

    def __init__(self):

        self.inventory_item_limit = 10 
        self.bag = []
        self.equiped_weapon = ''
        self.equiped_armor = ''
    ##-- Below code is not in use and will change one I start using it --##
    def add_to_inventory(self, add_item): 

        self.add_item = add_item

    def remove_from_inv(self, remove_item):

        self.remove_item = remove_item
    
    def hand_swap(self, requested_item):

        self.requested_item = requested_item

##-- Player Inventory __init__ Call --##

player_inventory = PlayerInventory()

##-- Setting up player classes                                                    --##
##-- The player class handles all the players stat creation                       --##
##-- The Mage, Warrior, Archer and Assassin classes will inherit the Player class --##
class Player:
    
    def __init__(self, name, player_class, max_health, melee_attack, magic_attack,
    max_mana, max_stamina, defense, pures, luck):
        
        self.name = name
        self.player_class = player_class
        self.level = 1
        self.exp = 0
        self.max_health = max_health
        self.health = self.max_health  ##-- Not sure if this is smart but this should only set health to max on making the character --##
        self.melee_attack = melee_attack
        self.magic_attack = magic_attack
        self.max_mana = max_mana
        self.mana = self.max_mana
        self.max_stamina = max_stamina
        self.stamina = self.max_stamina
        self.defense = defense
        self.pures = pures
        self.luck = luck

class Mage(Player):
    pass
    
class Warrior(Player):  
    ##-- Adrenaline Junky --##
    ##-- Lets Warrior the ablity to take 1 hits before death --##
    ##-- Ability can level up as player gets stronger --##
    pass

class Archer(Player):
    pass

class Assassin(Player):
    pass
    
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
        ChangeLog.change_log_print()
        pause()
        main()

    elif choice == '5':
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
        elif choice[0:4].lower() == 'info': 
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
        player_in_game = Mage(player_name,'Mage',max_health=80,melee_attack=1,magic_attack=10,
    max_mana=50, max_stamina=10, defense=1, pures=0, luck=1)
        player_inventory.in_hand = Items.weak_staff
    ##-- Warrior  --##
    elif player_class_choice == 'Warrior':  
        player_in_game = Warrior(player_name,'Warrior',max_health=150,melee_attack=10,magic_attack=0,
    max_mana=5, max_stamina=50, defense=4, pures=0, luck=0)
        player_inventory.in_hand = Items.rusty_short_sword
    ##-- Archer   --##
    elif player_class_choice == 'Archer':  
        player_in_game = Archer(player_name,'Archer',max_health=100,melee_attack=5,magic_attack=0,
    max_mana=50, max_stamina=10, defense=1, pures=0, luck=5)
        player_inventory.in_hand = Items.common_hunting_bow
    ##-- Assassin --##
    elif player_class_choice == 'Assassin': 
        player_in_game = Assassin(player_name,'Assassin',max_health=50,melee_attack=20,magic_attack=10,
    max_mana=25, max_stamina=10, defense=2, pures=100, luck=10)
        player_inventory.in_hand = Items.rusty_dagger

    gender_call()
    ##-- Back to main loop --##           
    main_game_loop()

##-- Makes a random mob with in the range of the players level --##

def random_enemy():
    global mob
    biome_info = Engine.get_tile(x,y) 
    spawns = Biome.world_biomes[biome_info[0][2]]['spawns']
    random_mob = random.choice(spawns)
    mob = Mobs.hostail_mobs[random_mob]
    # mob = Mobs.random_enemy(player_in_game.level)

##-- Encounter is to handle if we fight or not --##
##-- This probably needs some work             --##
##-- I will work on this more once I get the   --##
##-- Map done                                  --##

def encounter():
    
    ##-- num is subject to change as I add possible encounters --##
    
    num = random.randint(1, 1000)
    random_enemy()
    clear()
    print(f"You ran in a {mob.name} on the path.")
    pause()
    combat()
    if biome_or_subBiome == False:
        main_game_loop()
    else:
        sub_map_move()
    

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

    player_melee_attack = random.randint(round(player_in_game.melee_attack / 2), player_in_game.melee_attack + player_inventory.in_hand.melee_damage)
    player_magic_attack = random.randint(round(player_in_game.magic_attack / 2), player_in_game.magic_attack + player_inventory.in_hand.magic_damage)    
    enemy_attack = random.randint(round(mob.melee_attack / 2), mob.melee_attack)
    clear()
    Screen.vs_screen(player_in_game, mob)
    Screen.stat_screen(player_in_game,player_inventory, mob)
    attack_type = input('\n(1): Melee Attack\n(2): Magic Attack\nChoose A Number:> ')
    if attack_type == '1':
        if player_melee_attack == player_in_game.melee_attack / 2: ##-- Player Attack --##
            print(f"\n{player_in_game.name} {player_inventory.in_hand.action_word}")  ##-- finish me --##
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
            clear()
            print('\nYou Missed!')
        else:
            mob.health -= player_magic_attack
            clear()       
            print(f'\nYou just dealed {player_magic_attack} damage.')

        input('\nPress Enter To Continue:> ')
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
    print("not working yet. Sorry!")
    pause()
    attack()

##-- Handles the use of potions or and other usable item --##
##-- In combat or out                                    --##
def use_item():
    print("not working yet. Sorry!")
    pause()
    attack()

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
    if biome_or_subBiome == False:
        main_game_loop()
    else:
        sub_map_move()
##-- If in an unfortunate event the player dies this function is called --##
 
def dead():
    print(f'You have died from {mob.name}')
    pause()
    main()


def get_resouces():
    print("not working yet. Sorry!")
    pause()
    attack()


def look_in_inventory():
    print(player_inventory.bag)
    print(player_inventory.inventory_item_limit)
    pause()
    if biome_or_subBiome == False:
        main_game_loop()
    else:
        sub_map_move()


def sub_map_move():
    global biome_or_subBiome, x, y, sub_x, sub_y
    clear()
    biome_or_subBiome = True
    map_info = Engine.get_tile(x,y)

    sub_map_info = Engine.get_subTile(x,y,sub_x,sub_y)
    Engine.update_subTile(x,y,sub_x,sub_y,True)
    Screen.display(f"Biome in: {sub_map_info[0][4]}    Room: {sub_map_info[0][5]}")
    if sub_x == map_info[0][8] and sub_y == map_info[0][9]:
        options = "Which way do you want to move?\n\n(1): North\n(2): South\n(3): East\n(4): West\n(5): Look For Resources\n(6): Inventory\n(7): Exit\nInput a Number:>  "
    else:
        options = "Which way do you want to move?\n\n(1): North\n(2): South\n(3): East\n(4): West\n(5): Look For Resources\n(6): Inventory\nInput a Number:>  "


    move_to = input(options)
    ##-- NORTH = 1, SOUTH = 2, EAST = 3, & WEST = 4
    if move_to == '1':  ##-- UP --##
        if sub_y > 0:
            sub_y -= 1
            encounter()
        else:
            print('Looks Like It Dead Ends Here')
            pause()
            main_game_loop()
    
    elif move_to == '2':  ##-- DOWN --##
        if sub_y < small:
            sub_y += 1
            encounter()
        else:
            print('Looks Like It Dead Ends Here')
            pause()
            main_game_loop()

    elif move_to == '3':  ##-- RIGHT --##
        if sub_x > 0:
            sub_x += 1
            encounter()
        else:
            print('Looks Like It Dead Ends Here')
            pause()
            main_game_loop()

    elif move_to == '4':  ##-- LEFT --##
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

    elif move_to == 'Quit':  ##-- QUIT, I'll take this out after testing --## 
        sys.exit()


##-- The Inspect function checks the biome for the player to see if it has anything --##
##-- is interesting and of value.                                                   --## 
##-- Biome, Tell player about the area they are in                                  --##
##-- Rarity, Tell player how rare the biome is                                      --##
##-- Enterable, Tells the player if you can explore the area any more               --##
##-- Spawnable Mobs, Tells player what mobs can spawn in area                       --##
##-- Items that can be obtained for crafting                                        --##
##-- Coords for area                                                                --##
##-- Time of day..... maybe                                                         --##
def inspect_area(biome):
    
    clear()
    print(f"Biome Name: {Biome.world_biomes[biome]['name']}")
    print(f"Resourse: {Biome.world_biomes[biome]['resource']}")
    print(f"Spawn: {Biome.world_biomes[biome]['spawns']}")
    print(f"Rarity: {Biome.world_biomes[biome]['rarity']}")
    #print(f"Enterable: {Biome.world_biomes[biome]['enterable']}")
    print(f"{Biome.world_biomes[biome]['info']}")
    print("\n----------------------------------------------\n")

    if Biome.world_biomes[biome]['enterable'] == True:
        print(f"Looks likes like we can go futher into the {Biome.world_biomes[biome]['name']}\nWhat say you?")
        player_input = input("\n(1): Enter\n(2): Move on\nChoose a number:> ")
        if player_input == '1':
            sub_map_move()
    else:
        pause()
        main_game_loop()


##-- main_game_loop() is where all the logic for the player to move about the map --##
##-- or any other event while not in a fight                                      --##

def main_game_loop():
    
    ##-- This is for navigating the map --##
    global opening, x, y, sub_x, sub_y, biome_or_subBiome
    biome_or_subBiome = False
    if os.path.getsize('Worldmap.db') == 12288:
        Engine.map_builder()
    # while os.path.getsize('Worldmap.db') != 10000:
    #     print('Loading...........')
    if opening == True:

        Story.intro_story(player_in_game.name)
        input("Press Enter to continue: ")
        opening = False
    map_info = Engine.get_tile(x,y)
    sub_x = map_info[0][8]
    sub_y = map_info[0][9]
    Engine.update_tile(x,y,True)
    Screen.display(f"Location: {map_info[0][3]}")
    move_to = input("Which way do you want to travel?\n\n(1): North\n(2): South\n(3): East\n(4): West\n(5): Inspect Area\n(6): Inventory\n(7): Look For Resources\nInput a Number:>  ")
    ##-- NORTH = 1, SOUTH = 2, EAST = 3, & WEST = 4
    if move_to == '1':  ##-- UP --##
        if y > 0:
            y -= 1
            encounter()
        else:
            print('NEED TO MAKE THE PLAYER TO TELEPORT TO OTHER SIDE OF MAP')
            pause()
            main_game_loop()
    
    elif move_to == '2':  ##-- DOWN --##
        if y < small:
            y += 1
            encounter()
        else:
            print('NEED TO MAKE THE PLAYER TO TELEPORT TO OTHER SIDE OF MAP')
            pause()
            main_game_loop()

    elif move_to == '3':  ##-- RIGHT --##
        if x > 0:
            x += 1
            encounter()
        else:
            print('NEED TO MAKE THE PLAYER TO TELEPORT TO OTHER SIDE OF MAP')
            pause()
            main_game_loop()

    elif move_to == '4':  ##-- LEFT --##
        if x < small:
            x -= 1
            encounter()
        else:
            print('NEED TO MAKE THE PLAYER TO TELEPORT TO OTHER SIDE OF MAP')
            pause()
            main_game_loop()

    elif move_to == '5':
        inspect_area(map_info[0][2])

    elif move_to == 'Quit':  ##-- QUIT, I'll take this out after testing --## 
        sys.exit()

Engine.make_map_datebase()
Engine.make_sub_map_table()
# if os.path.getsize('Worldmap.db') == 0:
#     Engine.map_builder()
main()
