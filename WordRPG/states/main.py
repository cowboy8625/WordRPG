import sys
from time import sleep, time

import keyboard

from .. import gui

from .FSM import FSM
from .States import Confirm
# from .Game import Game
# from .Combat import Combat
# from .Crafting import Crafting
# from .Shop import Shop
from .Main_Menu import Main_Menu
from .Load_Game import Load_Game
from .New_Game import New_Game
# from .Quit import Quit


# Initilize states and their classes
STATES = {
    # 'quit':Quit(prev_screen='main_menu'),
    'quit':Confirm('Quit?', 'Are you sure you want to quit?', 'main_menu', None),
    'main_menu':Main_Menu(),
    'new_game':New_Game(),
    'load_game':Load_Game(),   
    #'game':Game_Loop(),
    #'combat':Combat(),
    #'shop':Shop(),
    #'crafting':Crafting(),
    #'dead':Dead(),
}



def main():
    game = FSM(states=STATES,start_state='main_menu')

    # main game loop
    gui.main.setup_terminal()
    while True:
        if game.get_state() is None:
            break
        else:
            game.on_event('enter_state')

    # If we're out of the main loop, then we're quitting the game
    sys.exit()
