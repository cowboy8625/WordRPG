""" Finite State Machine

    Based on this tutorial:
    https://dev.to/karn/building-a-simple-state-machine-in-python

"""
import sys
from time import sleep, time

# import keyboard     # https://pypi.org/project/keyboard/
import keyboard



class Machine:
    """
    Very Simple Finite State Machine.
    """

    def __init__(self, states=[], start=None):
        """ Initialize the state machine """
        self.states = states

        if start is not None:
            self.cur_state = self.states[start]
            self.prev_state = self.states[start]
        else:
            self.cur_state = states[0]
            self.prev_state = states[0]


    def on_event(self, event):
        """
        This is the main event handler that keeps track of what the previous
        and curent state are and allow us to call the methods in the curent
        state through the FSM .on_event gateway
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