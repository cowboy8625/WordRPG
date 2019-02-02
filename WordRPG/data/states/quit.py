""" 'quit' state """

from ...gui.screen import const, Screen
from ...state_machine import Confirm



class Quit(Confirm):
    def __init__(self, title, message, next_state, prev_screen=None, accept='y', reject='n'):
        """ Initiailize class and super class """
        super(Quit, self).__init__(title, message, next_state, accept='y', reject='n')
        self.title = title
        self.message = message
        self.accept = accept
        self.reject = reject
        self.next_state = next_state

    
    def _init_screen(self, prev_screen):
        # if prev_screen is None:
        #     screen = prev_screen
        # else:
        #     screen = Screen()

        screen = Screen()

        # creates standard double line frame around whole screen
        screen.add_frame(size=(30, 20), offset=('center', 0),
                    fgcolor='BLUE', bgcolor='BLACK')

        # draw the game title
        screen.load_screen('title', offset=('center', 8),
                    fgcolor='RED', bgcolor='BLACK')

        # add title and text
        # draw the menu
        menu = {
            'text_format' : {'fgcolor':'CYAN','bgcolor':'BLACK','style':'NORMAL'},
            'hotkey_format' : {'fgcolor':'YELLOW','bgcolor':'BLACK','style':'BRIGHT'},
            'encap' : '()',
            'sep' : ' - ',
            'options' : [
                ('quit', 'n'), 
                ('load_game', 'l'),
                ('help', 'h'),
                ('credits', 'c'),
                ('quit', 'q'),
            ]
        }
        screen.add_menu(menu, offset=('center',16))




    def update_screen(self):
        """ Draws the screen """
        Screen.clear()
        print(f'{self.message}')
