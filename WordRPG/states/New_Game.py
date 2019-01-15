""" 'new_game' state.  Includes character creation. """

from .. import gui
from .States import State



class New_Game(State):
    def __init__(self):
        """ Initiailize class and super class """
        super(New_Game, self).__init__()


    def update_screen(self):
        """ Draws the screen """
        gui.main.clear()
        gui.screen.new_game()


    def on_event(self, event, prev_state):
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
            if key == 's':
                return 'game'
            if key == 'esc':
                return 'main_menu'

        return self



class Character_Name(State):
    def __init__(self):
        """ Initiailize class and super class """
        super(Character_Name, self).__init__()


    def update_screen(self):
        """ Draws the screen """
        gui.main.clear()
        print('PLACEHOLDER SCREEN FOR ENTERING CHARACTER NAME')
        print('PRESS ANY KEY TO RETURN TO NEW CHARACTER SCREEN.')


    def on_event(self, event, prev_state):
        """ Handles events that are delegated to this State. """
        self.update_screen()
        self.wait_for_keypress()
        return 'new_game'



class Character_Gender(State):
    def __init__(self):
        """ Initiailize class and super class """
        super(Character_Gender, self).__init__()


    def update_screen(self):
        """ Draws the screen """
        gui.main.clear()
        print('PLACEHOLDER SCREEN FOR SELECTING CHARACTER GENDER')
        print('PRESS ANY KEY TO RETURN TO NEW CHARACTER SCREEN.')


    def on_event(self, event, prev_state):
        """ Handles events that are delegated to this State. """
        self.update_screen()
        self.wait_for_keypress()
        return 'new_game'



class Character_Class(State):
    def __init__(self):
        """ Initiailize class and super class """
        super(Character_Class, self).__init__()


    def update_screen(self):
        """ Draws the screen """
        gui.main.clear()
        print('PLACEHOLDER SCREEN FOR SELECTING CHARACTER CLASS')
        print('PRESS ANY KEY TO RETURN TO NEW CHARACTER SCREEN.')


    def on_event(self, event, prev_state):
        """ Handles events that are delegated to this State. """
        self.update_screen()
        self.wait_for_keypress()
        return 'new_game'
