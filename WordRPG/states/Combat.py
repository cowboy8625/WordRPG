""" Placeholder state for 'combat' """

from .. import gui
from .States import State



class Combat(State):
    def __init__(self):
        """ Initiailize class and super class """
        super(Combat, self).__init__()
        self.first_time = True


    def update_screen(self):
        """ Draws the screen """
        gui.main.clear()
        print('THIS IS A PLACEHOLDER SCREEN FOR COMBAT STATE')
        print('PRESS KEY TO RETURN TO MAIN LOOP')


    def on_event(self, event, prev_state):
        """ Handles events that are delegated to this State. """
        self.update_screen()
        self.wait_for_keypress()
        return 'game'
