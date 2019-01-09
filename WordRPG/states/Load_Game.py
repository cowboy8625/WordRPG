""" 'load_game' state """

from .. import gui
from .States import Screen



class Load_Game(Screen):
    def __init__(self):
        """ Initiailize class and super class """
        super(Load_Game, self).__init__()


    def update_screen(self):
        """ Draws the screen """
        gui.main.clear()
        print('PLACEHOLDER SCREEN FOR LOAD GAME')
        print('PRESS ANY KEY TO RETURN TO MAIN MENU')


    def on_event(self, event):
        """ Handles events that are delegated to this State. """
        self.update_screen()
        self.wait_for_keypress()
        return 'main_menu'