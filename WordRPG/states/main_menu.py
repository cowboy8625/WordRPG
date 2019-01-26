""" 'main_menu' state """

from ..gui.screen import const, Screen
from .states import State



class Main_Menu(State):
    def __init__(self):
        """ Initiailize class and super class """
        super(Main_Menu, self).__init__()
        self.first_time = True

        self.screen = self._init_screen()
        self.screen_splash = self._init_screen_splash()
        self.screen_help = self._init_screen_help()
        self.screen_credits = self._init_screen_credits()


    def _init_screen(self):
        """ Creates the main screen (main menu) """
        screen = Screen()

        # creates standard double line frame around whole screen
        screen.add_frame(size=(80, 30), offset=(0, 0),
                    fgcolor='BLUE', bgcolor='BLACK')

        # draw the game title
        screen.load_screen('title', offset=('center',8),
                    fgcolor='RED', bgcolor='LIGHTRED_EX')

        # draw the menu
        menu = {
            'text_format' : {'fgcolor':'CYAN','bgcolor':'BLACK','style':'NORMAL'},
            'hotkey_format' : {'fgcolor':'YELLOW','bgcolor':'BLACK','style':'BRIGHT'},
            'encap' : '()',
            'sep' : ' - ',
            'options' : [
                ('new_game', 'n'), 
                ('load_game', 'l'),
                ('help', 'h'),
                ('credits', 'c'),
                ('quit', 'q'),
            ]
        }
        screen.add_menu(menu, offset=('center',16))

        # draw the footer
        screen.add_footer(fgcolor='RED')

        return screen


    def _init_screen_splash(self):
        """ Creates the splash screen """
        screen = Screen()
        screen.load_screen('splash', offset=('center',2),fgcolor='WHITE')

        text = f'{const.COMPANY}'
        screen.add_string_to_screen(const.COMPANY, offset=('center', 25), fgcolor='RED')

        return screen


    def _init_screen_help(self):
        """ Creates the splash screen """
        screen = Screen()
        screen.load_screen('scroll', offset=('center',1), fgcolor='YELLOW')

        screen.add_string_to_screen('MAIN MENU HELP', offset=('center', 2),
                    fgcolor='CYAN')

        return screen


    def _init_screen_credits(self):
        """ Creates the splash screen """
        screen = Screen()
        screen.load_screen('scroll', offset=(0,1), fgcolor='YELLOW')

        screen.add_string_to_screen('PROJECT CONTRIBUTORS', offset=('center', 2),
                    fgcolor='CYAN')

        screen.load_screen('credits', offset=('center',6), fgcolor='CYAN')

        return screen


    def main_menu(self):
        """ Draws the main menu screen """
        self.screen.draw()


    def splash(self):
        """ Draws the screen """
        self.screen_splash.draw()
        self.pause(pause_time=1)


    def credits(self):
        """ Draws the screen """
        self.screen_credits.draw()
        self.wait_for_keypress()


    def help(self):
        """ Draws the screen """
        self.screen_help.draw()
        self.wait_for_keypress()


    def on_event(self, event, prev_state, prev_screen=None):
        """ Handles events that are delegated to this State. """
        if event == 'start' or self.first_time:
            self.splash()
            self.first_time = False

        # update screen and enter main loop for state
        self.main_menu()
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
                self.main_menu()
            if key == 'h':
                self.help()
                self.main_menu()

        return self
