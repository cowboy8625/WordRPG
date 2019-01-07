""" 'main_menu' state """

import gui
from .States import Screen



class Main_Menu(Screen):
    def __init__(self):
        """ Initiailize class and super class """
        super(Main_Menu, self).__init__()
        self.first_time = True


    def update_screen(self):
        """ Draws the screen """
        gui.main.clear()
        gui.screen.menu()


    def splash(self):
        """ Draws the screen """
        gui.main.clear()
        gui.screen.splash()
        self.pause(pause_time=3)


    def credits(self):
        """ Draws the screen """
        gui.main.clear()
        gui.screen.credits()
        self.wait_for_keypress()


    def help(self):
        """ Draws the screen """
        gui.main.clear()
        gui.screen.help()
        self.wait_for_keypress()
        

    def on_event(self, event):
        """ Handles events that are delegated to this State. """
        if event == 'start' or self.first_time:
            self.splash()
            self.first_time = False

        # update screen and enter main loop for state
        self.update_screen()
        while True:
            key = self.get_key_press()
            if key == 'q':
                return 'quit'
            if key == 'n':
                return 'new_game'
            if key == 'l':
                return 'load_game'
            if key == 'c':
                self.credits()
                self.update_screen()              
            if key == 'h':
                self.help()
                self.update_screen()              

        return self
