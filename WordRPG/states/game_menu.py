""" In game menu state """

from ..gui.screen import const, Screen
from .states import State



class Game_Menu(State):
    def __init__(self):
        """ Initiailize class and super class """
        super(Game_Menu, self).__init__()

        # self.screen = self._init_screen()


    def _create_menu(self, prev_state):
        screen = Screen( )

        if prev_state is not None:
            prev_screen = prev_state.screen
            screen._write_array_to_screen(prev_screen.copy(),
                        format_char=False, format_space=False)

        # creates a frame
        screen.add_frame(size=(40, 10), offset=('center', 10),
                    fgcolor='WHITE', bgcolor='BLACK', transparent=False)

        # add title
        screen.add_string_to_screen(f' GAME MENU ', offset=('center', 10),
                    transparent=False, fgcolor='WHITE', bgcolor='BLACK')

        # add menu
        menu = {
            'text_format' : {'fgcolor':'CYAN','bgcolor':'BLACK','style':'NORMAL'},
            'hotkey_format' : {'fgcolor':'YELLOW','bgcolor':'BLACK','style':'BRIGHT'},
            'encap' : '()',
            'sep' : ' - ',
            'options' : [
                ('save_game', 's'), 
                ('load_game', 'l'),
                ('help', 'h'),
                ('main menu', 'm'),
                ('quit', 'q'),
                ('back to game', 'esc'),
            ]
        }
        screen.add_menu(menu, offset=('center',12))
 
        self.screen = screen
        self.screen.draw()


    def update_screen(self):
        """ Draws the screen """
        self.screen.draw()


    def help(self):
        """ Draws the screen """
        Screen.clear()
        print('PLACEHOLDER FOR IN-GAME HELP SCREEN')
        self.wait_for_keypress()


    def on_event(self, event, prev_state):
        """ Handles events that are delegated to this State. """
        self._create_menu(prev_state)

        while True:
            key = self.get_key_press()
            if key == 'm':
                return 'main_menu'
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
