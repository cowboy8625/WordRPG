import sys

from .states.FSM import FSM
from .states.const import STATES
from . import gui



def run():
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
