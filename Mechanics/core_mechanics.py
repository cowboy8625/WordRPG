__author__ = "byteme8bit"

# File imports
from script import InfoDics, Screen
from script.Character import *
from Mechanics.ui_mechanics import *

# Module imports
import math


# Rounds the passed attack up by x amount (100, 10, 1, 0.1, 0.01, etc)
def rnd(num_to_round, x=0.01):
    """
    Rounds passed number to specified decimal point
    :param num_to_round: any attack that needs to be rounded
    :param x: value to be rounded to. Default is 0.01, rounding to nearest thousandth.
    :return: returns rounded value
    """
    return math.ceil(num_to_round / x) * x

# Helps is to show player how to fight use items and more
# I think I will also make this accessable in game as well at some point

def game_help():
    pass


# This is where the player chooses what class he will be
def char_creation():
    # This function sets the name of the player
    def player_select_name(__pclass):
        while True:
            a_an = "An" if __pclass[0] in "AEIOU" else "A"
            message = f"{a_an} {__pclass} is a good choice I think. What shall I call you?"
            Screen.display(message)
            option = input("\n\nENTER YOUR NAME:> ")
            if len(option) == 0:
                print('\nYou need to enter a name to continue\n')
            else:
                yes_no = input("Are you Sure You Want To Keep This Name?\n"
                                "(1): Yes\n"
                                "(2): No\n"
                                "Enter A Number:> ")
                if yes_no == '1':
                    return option

    # This set the class for the player
    def player_select_class():
        player_options = ('Mage', 'Warrior', 'Archer', 'Assassin')
        Screen.char_options()

        while True:
            choice = input('\n\n'
                           'SELECT A NUMBER OR TYPE HELP THEN NUMBER:> ')
            if choice in "1234":
                return player_options[int(choice) - 1]
            # lore is the story and it is found in InfoDics
            elif choice[0:4].lower() == 'info':
                lore = InfoDics.info_on_classes[player_options[int(choice[5]) - 1]]
                Screen.display(lore)
                pause()
            else:
                print("Not An Option.")

    def player_select_gender(__pname, __pclass):
        while True:
            message = f"{__pname} the {__pclass}, has a nice ring to\
                     it I think. I know it is obvious but just let me know what gender you are."
            Screen.display(message)
            option = input('\n\n'
                           '(1): Male\n'
                           '(2): Female\n'
                           'Enter A Number:> ')
            if option == '1':
                return 'male'
            elif option == '2':
                return 'female'

    pclass = player_select_class()
    pname = player_select_name(pclass)
    pgender = player_select_gender(pname, pclass)

    # Mage
    if pclass == 'Mage':
        return Player(
            name=pname,
            _class=pclass,
            max_health=80,
            melee_attack=1,
            magic_attack=10,
            max_mana=50,
            max_stamina=10,
            defense=1,
            luck=1,
            gender=pgender,
            gold=0,
            equipped_weapon=Items.weak_staff
        )
    # Warrior
    elif pclass == 'Warrior':
        return Player(
            name=pname,
            _class=pclass,
            max_health=150,
            melee_attack=10,
            magic_attack=0,
            max_mana=5,
            max_stamina=50,
            defense=5,
            luck=0,
            gender=pgender,
            gold=0,
            equipped_weapon=Items.rusty_short_sword
        )
    # Archer
    elif pclass == 'Archer':
        return  Player(
            name=pname,
            _class=pclass,
            max_health=100,
            melee_attack=5,
            magic_attack=0,
            max_mana=50,
            max_stamina=10,
            defense=1,
            luck=5,
            gender=pgender,
            gold=0,
            equipped_weapon=Items.common_hunting_bow
        )
    # Assassin
    elif pclass == 'Assassin':
        return Player(
            name=pname,
            _class=pclass,
            max_health=50,
            melee_attack=20,
            magic_attack=10,
            max_mana=25,
            max_stamina=10,
            defense=2,
            luck=10,
            gender=pgender,
            gold=100,
            equipped_weapon=Items.rusty_dagger
        )
