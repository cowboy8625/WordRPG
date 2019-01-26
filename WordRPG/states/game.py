""" Placeholder state for main 'game' loop """
from time import sleep
from collections import deque

from ..gui.screen import const, Screen
from .states import State
from ..map.map import Map


class Game(State):
    # TODO: duplicate data here, but it's easier to check if a key is in 
    # MOVE_KEYS.keys() rather than sort through a list of aliases for now
    MOVE_KEYS = {
        'w' : {'text':'north', 'vec':(0, -1)},
        'up' : {'text':'north', 'vec':(0, -1)},

        's' : {'text':'south', 'vec':(0, 1)},
        'down' : {'text':'south', 'vec':(0, 1)},

        'a' : {'text':'west', 'vec':(-1, 0)},
        'left' : {'text':'west', 'vec':(-1, 0)},

        'd' : {'text':'east', 'vec':(1, 0)},
        'right' : {'text':'east', 'vec':(1, 0)},
    }



    def __init__(self, buffer_size=4):
        """ Initiailize class and super class """
        super(Game, self).__init__()
        self.first_time = False #True

        # initialize maps and map data
        self.maps = self._init_maps(pos=(40,27))
        self.cur_map = self.maps['world']

        # initialize screen and elements
        self.screen = self._init_screen()
        self.update_map(draw=False)

        # initialize command buffer
        self.BUFFER_SIZE = buffer_size
        self.buffer = deque(['' for i in range(self.BUFFER_SIZE)])
        self.add_to_buffer("WELCOME TO THE WASTELANDS")


    def _init_maps(self, pos=(0.0)):
        """ create a 'Map' object using the given image filename and then print
        it to the terminal """
        # maps = {'world':('image':'test_island2', 'pos':19,18}}
        # {name:Map(image_name) for name, image_name in maps.items()}

        return {'world':Map('test_island2', pos=pos)}

    
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
        # get map data
        world_map = self.maps['world']
        world_map.set_map_frame()
        map_frame = world_map.get_map_frame(as_string=False)

        # write map frame border
        frame_offset = (2, 1)
        frame_size = Map.add_pos(world_map.frame_size, (2, 2))
        self.screen.add_frame(size=frame_size, offset=frame_offset,
                              frame_style=0, fgcolor='WHITE', bgcolor='BLACK')

        # write current biome name
        pos = world_map.cur_pos
        cur_tile = world_map.get_tile(pos)
        header = f' {cur_tile.name.upper()} - {pos} '
        col, row = frame_offset
        col = Screen.center_offset(header, frame_size[0])
        self.screen.add_string_to_screen(f'<< {header} >>', offset=(col, row),
                                    fgcolor='WHITE', bgcolor='BLACK')

        # write map to screen
        self.screen._write_array_to_screen(map_frame, offset=(3, 2), format_char=False)

        # write player cursor
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


    def move(self, key):
        """ Even handler for moving in the game world """
        text = self.MOVE_KEYS[key]['text'].upper()
        vec = self.MOVE_KEYS[key]['vec']

        cur_pos = self.maps['world'].cur_pos
        new_pos = self.maps['world'].move(vec)

        if cur_pos != new_pos:
            self.add_to_buffer(f'MOVING {text}...')
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
            if key in self.MOVE_KEYS.keys():
                self.move(key)

        return self
