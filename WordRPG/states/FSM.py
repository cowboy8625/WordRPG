""" Finite State Machine

    Based on this tutorial:
    https://dev.to/karn/building-a-simple-state-machine-in-python

"""
import sys
from time import sleep, time

# import keyboard     # https://pypi.org/project/keyboard/
from .. import keyboard

from .. import gui
from .States import Confirm
from .Main_Menu import Main_Menu
from .Load_Game import Load_Game
from .Save_Game import Save_Game
from .New_Game import New_Game  #, Character_Class, Character_Gender, Character_Name
from .Game import Game
from .Game_Menu import Game_Menu
from .Combat import Combat
from .Inventory import Inventory
from .Crafting import Crafting
from .Shop import Shop
from .Death import Death



# Initilize states
STATES = {
    'main_menu':Main_Menu(),
    'new_game':New_Game(),
    # 'character_name':Character_Name(),
    # 'character_class':Character_Class(),
    # 'character_gender':Character_Gender(),
    'load_game':Load_Game(),  
    'save_game':Save_Game(),  
    'game':Game(),
    'game_menu':Game_Menu(),
    'inventory':Inventory(),
    'combat':Combat(),
    'shop':Shop(),
    'crafting':Crafting(),
    'death':Death(),
    'quit':Confirm(
            'QUIT GAME',
            'ARE YOU SURE YOU WANT TO QUIT?',
            None
            ),
    'return_to_main_menu':Confirm(
            'RETURN TO MAIN MENU',
            'ARE YOU SURE YOU WANT TO RETURN TO MAIN MENU?',
            'main_menu'
            ),
    }

class FSM:
    """
    Very Simple Finite State Machine.
    """

    def __init__(self, states=[], start_state=None):
        """ Initialize the state machine """
        self.states = states

        if start_state is not None:
            self.cur_state = self.states[start_state]
            self.prev_state = self.states[start_state]
        else:
            self.cur_state = states[0]
            self.prev_state = states[0]


    def on_event(self, event):
        """
        This is the main event handler that keeps track of what the previous
        and curent state are and allow us to call the methods in the curent
        state through the FSM.on_event gateway
        """

        # Passing the current self.prev_state as an arg so that we can always
        # return back to the previous screen in the various state event handlers
        # prev_screen can also be passed in as an optional arguement to allow
        # for dialogue windows that draw on top of previous screens
        new_state = self.cur_state.on_event(event, self.prev_state)

        # new_state of None triggers exiting the game
        self.prev_state = self.cur_state

        if new_state is None:
            self.cur_state = None
        elif isinstance(new_state, str):
            self.cur_state = self.states[new_state.lower()]
        else:
            self.cur_state = new_state

        
    def get_states(self):
        """ Return the previous and current State of the finite State machine """
        return self.prev_state, self.cur_state