import sys

from .state_machine.machine import FSM
from .data.states import STATES
from .gui.screen import Screen



def run(start='main_menu'):
    game = FSM(states=STATES,start=start)

    Screen.setup_terminal()

    while True:
        if game.cur_state is None:
            break

        game.on_event('enter_state')
