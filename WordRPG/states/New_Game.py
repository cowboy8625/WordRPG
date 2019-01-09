""" 'new_game' state.  Includes character creation. """

from .. import gui
from .States import Screen



class New_Game(Screen):
    def __init__(self):
        """ Initiailize class and super class """
        super(New_Game, self).__init__()


    def update_screen(self):
        """ Draws the screen """
        gui.main.clear()
        print('PLACEHOLDER CREATE CHARACTER SCREEN')
        print('(N) - CHARACTER NAME')
        print('(C) - CHARACTER CLASS')
        print('(G) - CHARACTER GENDER')
        print('(A) - ACCEPT')
        print('(ESC) - MAIN MENU')


    def on_event(self, event):
        """ Handles events that are delegated to this State. """
        self.update_screen()

        while True:
            key = self.get_key_press()
            if key == 'n':
                return 'character_name'
            if key == 'c':
                return 'character_class'
            if key == 'g':
                return 'character_gender'
            if key == 'a':
                return 'accept'
            if key == 'esc':
                return 'main_menu'

        return self



class Character_Name(Screen):
    def __init__(self):
        """ Initiailize class and super class """
        super(Character_Name, self).__init__()


    def update_screen(self):
        """ Draws the screen """
        gui.main.clear()
        print('PLACEHOLDER SCREEN FOR ENTERING CHARACTER NAME')
        print('PRESS ANY KEY TO RETURN TO NEW CHARACTER SCREEN.')


    def on_event(self, event):
        """ Handles events that are delegated to this State. """
        self.update_screen()
        self.wait_for_keypress()
        return 'new_game'



class Character_Gender(Screen):
    def __init__(self):
        """ Initiailize class and super class """
        super(Character_Gender, self).__init__()


    def update_screen(self):
        """ Draws the screen """
        gui.main.clear()
        print('PLACEHOLDER SCREEN FOR SELECTING CHARACTER GENDER')
        print('PRESS ANY KEY TO RETURN TO NEW CHARACTER SCREEN.')


    def on_event(self, event):
        """ Handles events that are delegated to this State. """
        self.update_screen()
        self.wait_for_keypress()
        return 'New_Game'



class Character_Class(Screen):
    def __init__(self):
        """ Initiailize class and super class """
        super(Character_Class, self).__init__()


    def update_screen(self):
        """ Draws the screen """
        gui.main.clear()
        print('PLACEHOLDER SCREEN FOR SELECTING CHARACTER CLASS')
        print('PRESS ANY KEY TO RETURN TO NEW CHARACTER SCREEN.')


    def on_event(self, event):
        """ Handles events that are delegated to this State. """
        self.update_screen()
        self.wait_for_keypress()
        return 'New_Game'
