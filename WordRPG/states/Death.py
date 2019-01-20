""" Placeholder state for 'crafting' """

from ..gui.Screen import const, Screen, setup_terminal
from .States import State



class Death(State):
    def __init__(self):
        """ Initiailize class and super class """
        super(Death, self).__init__()
        self.first_time = True


    def update_screen(self):
        """ Draws the screen """
        Screen.clear()
        print('THIS IS A PLACEHOLDER SCREEN FOR DEATH STATE')
        print('PRESS KEY TO RETURN TO GAME STATE')


    def on_event(self, event, prev_state):
        """ Handles events that are delegated to this State. """
        self.update_screen()
        self.wait_for_keypress()
        return 'game_menu'
