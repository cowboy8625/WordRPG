##-- Starting Data November 6, 2018 --##
##-- Made By Cowboy8625             --##
##-- Waste Land                     --##


##-- Import Modules --##
import os, sys, random, time, cmd, textwrap
import Screen
import InfoDics
import Map

##-- Globel Varibles --##

player_in_game = ''

##-- Clears PRint Screen --##

def clear():
    
    if os.name == 'nt':
        _ = os.system('cls')

    else:
        _ = os.system('clear')

##-- Setting up the players attubuts --##

class Player:

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.max_health = 100
        self.heath = 100
        self.armor = 0
        self.melee_attack = 0
        self.magic_attack = 0
        self.mama = 0
        self.stamina = 0
        self.deffence = 0
        self.pures = 0
        self.luck = 0

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
                    lore = InfoDics.info_on_classes[player_options[int(choice[5])-1]]
  
                    letter_count = 0  ##-- This keeps count of how many words have been printed so the word dont get split on the screen --##

                    for i in lore:
                        letter_count += 1
                        sys.stdout.write(i)
                        sys.stdout.flush()
                        time.sleep(0.02)
                        if letter_count >= 100 and i == ' ':
                            letter_count = 0
                            print('\n')
                            
                    input("\n\nPress Enter to Continue:> ")
                    continue
                except:
                    print("Invaled Command")

        except:
            print("That's not an option.")

    player_name = input('\n\nENTER YOUR NAME:> ')
    player_in_game = Player(player_name)
    main_game_loop()

##-- This is for navigating the map --##

    

##-- encounter is to handle if we fight or not --##

def encounter():

    random.randint(1, 6)

def main_game_loop():
    ##-- This is for navigating the map --##
    x = 1
    y = 1
    while True:
        try:
            Screen.main_game_screen(InfoDics.story_line['Intro'])

            move_to = input("Which way do you want to travel?\n\n(1): North\n(2): South\n(3): East\n(4): West\n5): Quit\nInput a Number:>  ")
            ##-- NORTH = 1, SOUTH = 2, EAST = 3, & WEST = 4
            if move_to == '1':  ##-- UP --##
                y += 1
                print(f"Location: {Map.map[(x, y)]['name']}")
                input("Press Enter to continue: ")
                encounter()
            
            elif move_to == '2':  ##-- DOWN --##
                y -= 1
                print(f"Location: {Map.map[(x, y)]['name']}")
                input("Press Enter to continue: ")
                encounter()

            elif move_to == '3':  ##-- RIGHT --##
                x += 1
                print(f"Location: {Map.map[(x, y)]['name']}")
                input("Press Enter to continue: ")
                encounter()
            
            elif move_to == '4':  ##-- LEFT --##
                x -= 1
                print(f"Location: {Map.map[(x, y)]['name']}")
                input("Press Enter to continue: ")
                encounter()
            
            elif move_to == '5':  ##-- QUIT, I'll take this out after testing --## 
                break

        except:
            print("That is undiscover area. We best stay on the map.")
            input("Press Enter to continue: ")

    





main()