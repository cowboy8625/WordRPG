# This module is to handle all the print screens for the menus

# All Imports
import os
import textwrap
import time
from colorama import Fore, init
from script.Character import *

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


# Clear Function
def clear():
    if os.name == 'nt':
        _ = os.system('cls')

    else:
        _ = os.system('clear')


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


# This shows who is fighing and there stats
def vs_screen(player, mob=zombie, width=44):
    width = (len(player.char_name) + len(mob.char_name) + 43)         # Width sets how big the screen is no matter
    print('#' * width)                                      # How big the names or stats are
    print(f"#              {player.char_name}  -- VS --  {mob.char_name}               #")
    print('#' * (len(player.char_name) + len(mob.char_name) + 43))


def stat_screen(player, mob=zombie, width=44):
    # Width sets how big the screen is no matter
    width = (len(player.char_name) + len(mob.char_name) + 43)

    left_p_class = f"{player.player_class}    "             # Left side is for player
    right_p_class = f"    {mob.mob_class}"                  # Right side is for Enemy
    line_p_class = left_p_class + ' ' * (width - (
                len(left_p_class) + len(right_p_class))) + right_p_class  # Line puts the Left and Right

    # Sides together and uses width
    left_in_hand = f"Wielding: {player.equipped_weapon.name}    "      # variable to know how many space
    right_in_hand = f"    {mob.equipped_weapon.name} :Wielding"          # to print
    line_in_hand = left_in_hand + ' ' * (width - (len(left_in_hand) + len(right_in_hand))) + right_in_hand

    left_level = f"Level: {player.level}    "
    right_level = f"    {mob.level} :Level"
    line_level = left_level + ' ' * (width - (len(left_level) + len(right_level))) + right_level

    left_exp = f"Exp: {player.exp}    "
    right_exp = f"    {mob.exp_drop} :Exp Drop"
    line_exp = left_exp + ' ' * (width - (len(left_exp) + len(right_exp))) + right_exp

    left_health = f"Health: {player.max_health}\\{player.health}    "
    right_health = f"    {mob.health}/{mob.max_health} :Health"
    line_health = left_health + ' ' * (width - (len(left_health) + len(right_health))) + right_health

    left_armor = f"Armor: {player.equipped_armor.name}    "
    right_armor = f"    {mob.armor} :Armor"
    line_armor = left_armor + ' ' * (width - (len(left_armor) + len(right_armor))) + right_armor

    left_mana = f"Mana: {player.mana}    "
    right_mana = f"    {mob.mana} :Mana"
    line_mana = left_mana + ' ' * (width - (len(left_mana) + len(right_mana))) + right_mana

    left_stamina = f"Stamina: {player.stamina}    "
    right_stamina = f"    {mob.stamina} :Stamina"
    line_stamina = left_stamina + ' ' * (width - (len(left_stamina) + len(right_stamina))) + right_stamina

    left_luck = f"Luck: {player.luck}    "
    right_luck = f"    {mob.luck} :Luck"
    line_luck = left_luck + ' ' * (width - (len(left_luck) + len(right_luck))) + right_luck

    print(line_p_class)
    print(line_in_hand)
    print(line_level)
    print(line_exp)
    print(line_health)
    print(line_armor)
    print(line_mana)
    print(line_stamina)
    print(line_luck)


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
