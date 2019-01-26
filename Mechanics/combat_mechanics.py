__author__ = "byteme8bit"

# File imports
from script import Screen
from Mechanics.ui_mechanics import clear, pause, vs_screen, stat_screen

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


# Mob "AI"
def mob_ai(player, mob):
    pass


def attack(player_in_game, mob):
    """
    Handles one attack choice by player and the mob currently being fought
    :param player_in_game: Player's character
    :param mob: Mob currently being fought
    :return:
    """

    clear()
    vs_screen(player_in_game, mob)
    stat_screen(player_in_game, mob)
    attack_type = input('(1): Melee Attack\n'
                        '(2): Magic Attack\n'
                        'Choose A Number:> ')

    if attack_type == '1':
        melee_damage = player_in_game.melee_attack()
        mob.health -= melee_damage
        clear()
        print(f'You just dealt {melee_damage} damage.')

        pause()

    elif attack_type == '2':
        magic_damage = player_in_game.magic_attack()
        mob.health -= magic_damage
        clear()
        print(f'You just dealt {magic_damage} damage.')

        pause()

    if mob.health <= 0:  # If mob is dead
        win(player_in_game, mob)

    else:  # If mob is still alive
        mob_damage = mob.melee_attack()
        player_in_game.health -= mob_damage
        clear()
        print(f"{mob.charname} dealt {mob_damage} damage to you.")

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
            attack(player_in_game, mob)

        elif option == '2':
            pass

        elif option == '3':
            pass

        elif option == '4':
            break
