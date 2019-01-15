""" Finite State Machine

    Based on this tutorial:
    https://dev.to/karn/building-a-simple-state-machine-in-python

"""
import sys
from time import sleep, time

import keyboard     # https://pypi.org/project/keyboard/

from .. import gui



class FSM:
    """
    Simple finite state machine.
    """

    def __init__(self, states=[], start_state=None):
        """ Initialize the state machine """
        self.states = states
        self.prev_state = None
        if start_state is not None:
            self.cur_state = start_state
        else:
            self.cur_state = states[0]


    def on_event(self, event):
        """
        This is the bread and butter of the state machine. Incoming events are
        delegated to the given states which then handle the event. The result is
        then assigned as the new state.
        """
   
        # Passing the current self.prev_state as an arg so that we can always
        # return back to the previous screen in the various state event handlers
        new_state = self.states[self.cur_state].on_event(event, self.prev_state)

        self.prev_state = self.cur_state
        self.cur_state = new_state


    def get_state(self):
        """ Return the current State of the finite State machine """
        return self.cur_state
