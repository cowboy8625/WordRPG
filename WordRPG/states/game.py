""" Placeholder state for main 'game' loop """
from collections import deque

from ..gui.screen import const, Screen, setup_terminal
from .states import State



class Game(State):
    def __init__(self, buffer_size=4):
        """ Initiailize class and super class """
        super(Game, self).__init__()
        self.first_time = True

        self.screen = self._init_screen()

        # creates initial command buffer
        self.BUFFER_SIZE = buffer_size
        self.buffer = deque(['' for i in range(self.BUFFER_SIZE)])
        self.add_to_buffer("WELCOME TO THE WASTELANDS")

    
    def _init_screen(self):
        """ Create the main game screen """
        screen = Screen()
        screen.load_screen('game', offset=(0,0), fgcolor='WHITE')

        screen.add_header()

        # command menu
        menu = {
            'text_format' : {'fgcolor':'CYAN','bgcolor':'BLACK','style':'NORMAL'},
            'hotkey_format' : {'fgcolor':'YELLOW','bgcolor':'BLACK','style':'BRIGHT'},
            'encap' : '()',
            'sep' : ' - ',
            'options' : [
                ('menu', 'esc'), 
                ('gather resources', 'g'),
                ('inventory', 'i'),
                ('crafting', 'c'),
                ('test combat', 'x'),
                ('test death', 'k'),
            ]
        }
        screen.add_menu(menu, offset=(51,16))

        screen.add_footer()

        return screen


    def update_screen(self):
        """ Updates and redraws the screen """
        self.screen.draw()


    def add_to_buffer(self, text, width=76):
        """ Adds output to command buffer

        Command buffer displays the last 4-5 actions that the player took and
        their results if relevant
        
        Arguments:
            text {str} -- String to add and display in the command buffer
        
        Keyword Arguments:
            width {int} -- Width of line in command buffer so that we can fully
                           overwrite the previous screen line. (default: {76})
        """

        self.buffer.rotate(-1)
        self.buffer[-1]=text

        for i, text in enumerate(self.buffer):
            text = f'> {text}'
            text = f'{text}{" " * (width - len(text))}'
            self.screen.add_string_to_screen(text, offset=(3, 24 + i),
                    transparent=False, fgcolor='WHITE', bgcolor='BLACK')


    def start(self):
        """ Even handler for transitioning into this state the first time """
        Screen.clear()
        print('STARTING NEW GAME')
        print('ENTERING MAIN GAME STATE IN A MOMENT...')
        self.pause(pause_time=1)


    def gather(self):
        """ Even handler for gathering resources """
        self.add_to_buffer(f'GATHERING RESOURCES...')
        self.update_screen()


    def move(self, dir='north'):
        """ Even handler for moving in the game world """
        self.add_to_buffer(f'MOVING {dir.upper()}...')
        self.update_screen()


    def rest(self,):
        """ Even handler for resting """
        self.add_to_buffer(f'YOU REST FOR 4 HOURS.')
        self.update_screen()


    def combat(self):
        """ Even handler for transitioning into 'combat' state """
        # This is where any pre-combat functions would be handled before
        # transitioning into the combat state
        self.add_to_buffer('ENTERING COMBAT...')
        self.update_screen()
        self.pause(pause_time=1)
        return 'combat'


    def death(self):
        """ Even handler for transitioning into 'death' state """
        # This is where any pre-death functions would be handled before
        # transitioning into the 'death' state
        self.add_to_buffer('YOU SLUMP LIFELESSLY TO THE GROUND...')
        self.update_screen()
        self.pause(pause_time=1)
        return 'death'


    def on_event(self, event, prev_state):
        """ Handles events that are delegated to this State. """
        if event == 'start' or self.first_time:
            self.start()
            self.first_time = False

        self.update_screen()
        while True:
            key = self.get_key_press()
            if key == 'g':
                self.gather()
            if key == 'w' or key == 'up':
                self.move(dir='north')
            if key == 'a' or key == 'left':
                self.move(dir='west')
            if key == 's' or key == 'down':
                self.move(dir='south')
            if key == 'd' or key == 'right':
                self.move(dir='east')
            if key == 'r':
                self.rest()
            if key == 'c':
                return 'crafting'
            if key == 'i':
                return 'inventory'
            if key == 'x':
                return self.combat()
            if key == 'k':
                return self.death()
            if key == 'esc':
                return 'game_menu'

        return self
