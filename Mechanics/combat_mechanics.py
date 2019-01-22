__author__ = "byteme8bit"

# File imports
from script import Screen
from script.Character import *

# Module imports


# If you when a fight this function handles what happens
def win(player_in_game, mob):
    clear()
    player_in_game.pures += mob.pures
    player_in_game.exp += mob.exp_gained
    print(f"You just defeated a {mob.name}\n"
          f"Gold Looted: {mob.pures}\n"
          f"EXP Gained: {mob.exp_gained}")
    pause()


def combat(player_in_game, mob):
    clear()
    Screen.vs_screen(player_in_game, mob)
    Screen.stat_screen(player_in_game, mob)

    while player_in_game.health > 0 and mob.health > 0:
        option = input('\n'
                       '(1): Attack\n'
                       '(2): Magic\n'
                       '(3): Use Item\n'
                       '(4): Run\n'
                       'Choose A Number:> ')

        if option == '1':
            # attack(player_in_game, mob)

        elif option == '2':
            pass

        elif option == '3':
            pass

        elif option == '4':
            break
