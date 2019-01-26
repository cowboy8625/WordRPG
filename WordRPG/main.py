import sys

from .states.machine import FSM, STATES
from . import gui
from .gui.screen import Screen



def run():
    game = FSM(states=STATES,start_state='main_menu')

    Screen.setup_terminal()

    while True:
        if game.cur_state is None:
            break

        game.on_event('enter_state')

    # If we're out of the main loop, then we're quitting the game
    sys.exit()
