""" Placeholder state for main 'game' loop """
from time import sleep
from collections import deque

from ..gui.screen import const, Screen
from .states import State
from ..map.map import Map


class Game(State):
    MOVE_KEYS = {
        'w' : 'north', 'up' : 'north',
        'a' : 'west', 'left' : 'west',
        's' : 'south', 'down' : 'south',
        'd' : 'east', 'right' : 'east',
    }

    def __init__(self, buffer_size=4):
        """ Initiailize class and super class """
        super(Game, self).__init__()
        self.first_time = True

        self.maps = self._init_maps()
        self.cur_map = self.maps['world']
        self.pos = (19, 18)

        self.screen = self._init_screen()

        self.update_map(draw=False)

        # creates initial command buffer
        self.BUFFER_SIZE = buffer_size
        self.buffer = deque(['' for i in range(self.BUFFER_SIZE)])
        self.add_to_buffer("WELCOME TO THE WASTELANDS")


    def _init_maps(self):
        """ create a 'Map' object using the given image filename and then print
        it to the terminal """
        # maps = {'world':('image':'test_island2', 'pos':19,18}}
        # {name:Map(image_name) for name, image_name in maps.items()}

        return {'world':Map('test_island2')}

    
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


    def update_map(self, draw=True):
        world_map = self.maps['world']
        world_map.set_map_frame(offset=self.pos)
        map_frame = world_map.get_map_frame(as_string=False)


        # write map frame to screen
        self.screen._write_array_to_screen(map_frame, offset=(3, 2), format_char=False)

        # biome name
        cur_tile = world_map.get_tile(self.pos)
        self.screen.add_string_to_screen(f'< {cur_tile.name} - {cur_tile.movement} >', offset=(16,1),
                                    fgcolor='WHITE', bgcolor='BLACK')

        # player cursor
        self.screen.add_string_to_screen('@', offset=(24,12),
                                    fgcolor='WHITE', bgcolor='BLACK')

        if draw:
            self.update_screen()


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

        if dir == 'north':
            dir = (0, -1)
        if dir == 'south':
            dir = (0, 1)
        if dir == 'east':
            dir = (1, 0)
        if dir == 'west':
            dir = (-1, 0)

        new_pos = self.maps['world'].move(dir)

        if self.pos != new_pos:
            self.pos = new_pos
            self.update_map()


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
            if key in self.MOVE_KEYS.keys():
                self.move(dir=self.MOVE_KEYS[key])
            if key == 'g':
                self.gather()
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
