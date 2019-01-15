""" In game menu state """

from .. import gui
from .States import State



class Game_Menu(State):
    def __init__(self):
        """ Initiailize class and super class """
        super(Game_Menu, self).__init__()


    def update_screen(self):
        """ Draws the screen """
        gui.main.clear()
        print('THIS IS PLACEHOLDER FOR IN-GAME MENU STATE')
        print('CREATE A NEW SCREEN IN GUI.SCREEN')
        print('(S) - SAVE GAME')
        print('(L) - LOAD GAME')
        print('(M) - MAIN MENU')
        print()
        print('(ESC) - RETURN TO GAME')


    def on_event(self, event, prev_state):
        """ Handles events that are delegated to this State. """
        self.update_screen()

        while True:
            key = self.get_key_press()
            if key == 'm':
                return 'main_menu'
            if key == 's':
                return 'save_game'
            if key == 'l':
                return 'load_game'
            if key == 'esc':
                return 'game'
