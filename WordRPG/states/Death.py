""" Placeholder state for 'crafting' """

from ..gui.Screen import const, Screen, setup_terminal
from .States import State



class Death(State):
    def __init__(self):
        """ Initiailize class and super class """
        super(Death, self).__init__()
        self.first_time = True
        self.screen = self._init_screen()


    def _init_screen(self):
        screen = Screen()
        screen.load_screen('tombstone', offset=('center',2), fgcolor='WHITE')
        screen.add_string_to_screen('YOU ARE DEAD', offset=('center', 27),
                    fgcolor='RED')
        return screen
        

    def update_screen(self):
        """ Draws the screen """
        self.screen.draw()


    def on_event(self, event, prev_state):
        """ Handles events that are delegated to this State. """
        self.update_screen()
        self.wait_for_keypress()
        return 'game_menu'
