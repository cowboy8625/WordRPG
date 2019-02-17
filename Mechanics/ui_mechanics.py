__author__ = "byteme8bit"

# File imports

# Module imports
import os


# This shows who is fighing and there stats
def vs_screen(player, mob, width=44):
    width = (len(player.char_name) + len(mob.char_name) + 43)         # Width sets how big the screen is no matter
    print('#' * width)                                      # How big the names or stats are
    print(f"#              {player.char_name}  -- VS --  {mob}               #")
    print('#' * (len(player.char_name) + len(mob.char_name) + 43))


def stat_screen(player, mob, width=44):
    # Width sets how big the screen is no matter
    width = (len(player.char_name) + len(mob.char_name) + 43)

    left_p_class = f"{player.char_class}    "             # Left side is for player
    right_p_class = f"    {mob.char_name}"                  # Right side is for Enemy
    line_p_class = left_p_class + ' ' * (width - (
                len(left_p_class) + len(right_p_class))) + right_p_class  # Line puts the Left and Right

    # Sides together and uses width
    left_in_hand = f"Wielding: {player.equipped_weapon.name}    "      # variable to know how many space
    right_in_hand = f"    None :Wielding"          # to print
    line_in_hand = left_in_hand + ' ' * (width - (len(left_in_hand) + len(right_in_hand))) + right_in_hand

    left_level = f"Level: {player.level}    "
    right_level = f"    Level: {mob.level}"
    line_level = left_level + ' ' * (width - (len(left_level) + len(right_level))) + right_level

    left_exp = f"Exp: {player.exp}    "
    right_exp = f"    Exp reward: {mob.exp}"
    line_exp = left_exp + ' ' * (width - (len(left_exp) + len(right_exp))) + right_exp

    left_health = f"Health: {player.max_health}\\{player.health}    "
    right_health = f"    Health: {mob.max_health}\\{mob.health}"
    line_health = left_health + ' ' * (width - (len(left_health) + len(right_health))) + right_health

    left_armor = f"Armor: {player.equipped_armor.name}    "
    right_armor = f"    TEST :Armor"
    line_armor = left_armor + ' ' * (width - (len(left_armor) + len(right_armor))) + right_armor

    left_mana = f"Mana: {player.mana}    "
    right_mana = f"    Mana: {mob.mana}"
    line_mana = left_mana + ' ' * (width - (len(left_mana) + len(right_mana))) + right_mana

    left_stamina = f"Stamina: {player.stamina}    "
    right_stamina = f"    Stamina: {mob.stamina}"
    line_stamina = left_stamina + ' ' * (width - (len(left_stamina) + len(right_stamina))) + right_stamina

    # left_luck = f"Luck: {player.luck}    "
    # right_luck = f"    TEST :Luck"
    # line_luck = left_luck + ' ' * (width - (len(left_luck) + len(right_luck))) + right_luck

    print(line_p_class)
    print(line_in_hand)
    print(line_level)
    print(line_exp)
    print(line_health)
    print(line_armor)
    print(line_mana)
    print(line_stamina)
    # print(line_luck)


# Clears Print Screen
def clear():
    if os.name == 'nt':
        _ = os.system('cls')

    else:
        _ = os.system('clear')


# This maybe fast then retyping input a bunch
def pause():
    input("Press Enter To Continue:> ")
