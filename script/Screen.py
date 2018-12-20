# This module is to handle all the print screens for the menus

# All Imports
import os
import textwrap
import time
from colorama import Fore, init
from Mechanics.ui_mechanics import *

init(convert=True)

# Font Colors
white = Fore.WHITE
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE
magenta = Fore.MAGENTA
light_red = Fore.LIGHTRED_EX
cyan = Fore.CYAN


# Main Menu I have Ideas for a better more custom and reusable screen
def main_menu_screen():
    first = light_red + 'WELECOME TO THE WASTE LAND' + cyan
    num1 = green + '1' + cyan
    num2 = green + '2' + cyan
    num3 = green + '3' + cyan
    num4 = green + '4' + cyan
    num5 = green + '5' + cyan
    start = yellow + 'START' + cyan
    load = yellow + 'LOAD' + cyan
    help_ = yellow + 'HELP' + cyan
    change_log = yellow + 'CHANGE LOG' + cyan
    quit = yellow + 'QUIT' + cyan
    l1 = red + "SELECT A NUMBER TO CONTINE" + cyan
    l2 = red + "Copy Write 2018" + cyan
    l3 = red + "Writen by Cowboy Gaming" + cyan

    line1 = f"{cyan}####################################################################################################"
    line2 = f"#-                                   {first}                                   -#"
    line3 = "#-                                                                                                -#"
    line4 = f"#-                                           ({num1}): {start}                                           -#"
    line5 = f"#-                                           ({num2}): {load}                                            -#"
    line6 = f"#-                                           ({num3}): {help_}                                            -#"
    line7 = f"#-                                           ({num4}): {change_log}                                      -#"
    line8 = f"#-                                           ({num5}): {quit}                                            -#"
    line9 = f"#-                                                                                                -#"
    line10 = f"#-                                   {l1}                                   -#"
    line11 = f"#-                                       {l2}                                          -#"
    line12 = f"#-                                  {l3}                                       -#"
    line13 = f"####################################################################################################"

    lines = [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12, line13]

    clear()

    for i in lines:
        print(i)


# This This is the menu for the character set up
def char_options():
    first = light_red + 'SELECT A CLASS TO BE' + cyan
    num1 = green + '1' + cyan
    num2 = green + '2' + cyan
    num3 = green + '3' + cyan
    num4 = green + '4' + cyan
    mage = yellow + 'MAGE' + cyan
    warrior = yellow + 'WARRIOR' + cyan
    archer = yellow + 'ARCHER' + cyan
    assassin = yellow + 'ASSASSIN' + cyan
    l1 = red + "SELECT A NUMBER TO CONTINE OR" + cyan
    l2 = red + "TYPE 'INFO' THEN SPACE AND A NUMBER, FOR INFORMATION ON CLASS" + cyan
    l3 = red + "EXSAMPLE: INFO 1" + cyan

    line1 = f"{cyan}####################################################################################################"
    line2 = f"#-                                       {first}                                     -#"
    line3 = "#-                                                                                                -#"
    line4 = f"#-                                           ({num1}): {mage}                                            -#"
    line5 = f"#-                                           ({num2}): {warrior}                                         -#"
    line6 = f"#-                                           ({num3}): {archer}                                          -#"
    line7 = f"#-                                           ({num4}): {assassin}                                        -#"
    line8 = f"#-                                                                                                -#"
    line9 = f"#-                                   {l1}                                -#"
    line10 = f"#-                     {l2}              -#"
    line11 = f"#-                                           {l3}                                     -#"
    line12 = f"####################################################################################################"

    lines = [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12]

    clear()

    for i in lines:
        print(i)


# This is for the start of the story and to get the players name
def name_player(player_class):
    line1 = '#' * len(player_class) + '#' * 30
    line2 = '#- ' + f'So you want to be a {player_class} hu?' + ' -#'
    line3 = '#- ' + 'What shall I call you?' + (' ' * len(player_class)) + '   -#'
    line4 = '#' * len(player_class) + '#' * 30

    lines = [line1, line2, line3, line4]

    clear()

    for i in lines:
        print(i)


# This is for the main story line and to update the player what is happening
# Needs work but we can come back to it when we get to adding story          NOT IN USE

def main_game_screen(story):
    line1 = '#' * len(story) + '#' * 30
    line2 = f'# {story} #'
    line3 = '#' * len(story) + '#' * 30

    lines = [line1, line2, line3]

    clear()

    for i in lines:
        print(i)

"""






"""
def display(on_screen, width=44):
    # width = 44 max width is 208
    side = round(((width / 2) / 2) - 1)
    middle = round(width / 2)
    top_bottom = '#' * width
    space = '#' + ' ' * (width - 2) + '#'
    center_text = textwrap.wrap(on_screen, middle)

    left = '#' + (' ' * side)
    right = (' ' * side) + '#'

    clear()
    print(cyan + top_bottom)
    print(space)
    print(space)

    for i in center_text:
        print(cyan + left + white + i + cyan + ' ' * (middle - len(i)) + right)

    print(space)
    print(space)
    print(top_bottom)


def type_to_screen(message):
    add_one_letter = []
    for i in message:
        if len(add_one_letter) == 0:
            add_one_letter.append(i)
        else:
            add_one_letter.append(add_one_letter.pop(0) + i)
        time.sleep(0.02)
        display(add_one_letter[0])


def menu_display(top, middle, bottom):
    top_bottom_border = "#"
    left_side_border = "#-"
    right_side_border = "-#"
    space = " " * 3

    print()

    for line in top:
        print(left_side_border + space + line + space + right_side_border)

    for line in middle:
        print(left_side_border + space + line + space + right_side_border)

    for line in bottom:
        print(left_side_border + space + line + space + right_side_border)
