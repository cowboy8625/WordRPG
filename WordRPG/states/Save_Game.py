""" 'load_game' state """

from .. import gui
from .States import State



class Save_Game(State):
    def __init__(self):
        """ Initiailize class and super class """
        super(Save_Game, self).__init__()


    def update_screen(self):
        """ Draws the screen """
        gui.main.clear()
        gui.screen.files(files_info=[{},{},{}], mode='save')


    def on_event(self, event, prev_state):
        """ Handles events that are delegated to this State. """
        self.update_screen()
        self.wait_for_keypress()
        return prev_state
