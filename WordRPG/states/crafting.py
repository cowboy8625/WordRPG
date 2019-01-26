""" Placeholder state for 'crafting' """

from ..gui.screen import const, Screen
from .states import State



class Crafting(State):
    def __init__(self):
        """ Initiailize class and super class """
        super(Crafting, self).__init__()
        self.first_time = True


    def update_screen(self):
        """ Draws the screen """
        Screen.clear()
        print('THIS IS A PLACEHOLDER SCREEN FOR CRAFTING STATE')
        print('PRESS KEY TO RETURN TO MAIN LOOP')


    def on_event(self, event, prev_state):
        """ Handles events that are delegated to this State. """
        self.update_screen()
        self.wait_for_keypress()
        return prev_state
