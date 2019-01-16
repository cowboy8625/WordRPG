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
        gui.screen.game_menu()


    def help(self):
        """ Draws the screen """
        gui.main.clear()
        gui.screen.help()
        self.wait_for_keypress()


    def on_event(self, event, prev_state):
        """ Handles events that are delegated to this State. """
        self.update_screen()

        while True:
            key = self.get_key_press()
            if key == 'm':
                return 'return_to_main_menu'
            if key == 's':
                return 'save_game'
            if key == 'l':
                return 'load_game'
            if key == 'q':
                return 'quit'
            if key == 'esc':
                return 'game'
            if key == 'h':
                self.help()
                self.update_screen()
