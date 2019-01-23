""" 'new_game' state.  Includes character creation. """

from ..gui.screen import const, Screen, setup_terminal
from .states import State



class New_Game(State):
    def __init__(self):
        """ Initiailize class and super class """
        super(New_Game, self).__init__()

        self.screen = self._init_screen()


    def _init_screen(self):
        """ Create the main game screen """
        screen = Screen()

        # creates standard double line frame around whole screen
        screen.add_frame(size=(80, 30), offset=(0, 0),
                    fgcolor='BLUE', bgcolor='BLACK')

        # add menu
        menu = {
            'text_format' : {'fgcolor':'CYAN','bgcolor':'BLACK','style':'NORMAL'},
            'hotkey_format' : {'fgcolor':'YELLOW','bgcolor':'BLACK','style':'BRIGHT'},
            'encap' : '()',
            'sep' : ' - ',
            'options' : [
                ('BOB THE WARRIOR', '1'), 
                ('TIM THE MAGE', '2'),
                # ('race', 'r'),
                ('SUE THE ARCHER', '3'),
                ('PEG THE ASSASSIN', '4'),
                ('start', 's'),
            ]
        }
        screen.add_menu(menu, offset=('center',12))

        screen.add_footer()

        return screen


    def update_screen(self):
        """ Draws the screen """
        self.screen.draw()


    def on_event(self, event, prev_state):
        """ Handles events that are delegated to this State. """
        self.update_screen()

        while True:
            key = self.get_key_press()
            # if key == 'n':
            #     return 'character_name'
            # if key == 'c':
            #     return 'character_class'
            # if key == 'g':
            #     return 'character_gender'
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
