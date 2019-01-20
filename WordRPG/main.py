import sys

from .states.FSM import FSM, STATES
from . import gui
from .gui.Screen import setup_terminal



def run():
    game = FSM(states=STATES,start_state='main_menu')

    setup_terminal()

    while True:
        if game.cur_state is None:
            break

        game.on_event('enter_state')

    # If we're out of the main loop, then we're quitting the game
    sys.exit()
