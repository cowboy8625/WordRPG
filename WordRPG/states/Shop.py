""" Placeholder state for 'combat' """
from .. import gui
from .States import State



class Shop(State):
    def __init__(self):
        """ Initiailize class and super class """
        super(Shop, self).__init__()


    def update_screen(self):
        """ Draws the screen """
        gui.main.clear()
        print('THIS IS A PLACEHOLDER SCREEN FOR SHOP STATE')
        print('PRESS KEY TO RETURN TO MAIN LOOP')
   

    def on_event(self, event, prev_state):
        """ Handles events that are delegated to this State. """
        self.update_screen()
        self.wait_for_keypress()
        return prev_state
