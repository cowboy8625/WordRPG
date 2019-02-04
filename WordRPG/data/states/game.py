""" Placeholder state for main 'game' loop """
from collections import deque
import logging

from ... import const
from ...time import Game_Time
from ...common import Point, Table
from ...gui.screen import Screen
from ...state_machine import State
from ...map.map import Map



logging.basicConfig(filename=const.SETTINGS['log_game'], filemode='w',
                    level=const.SETTINGS['logging'])


# TODO: This should be loaded in from a .json at a higher level in the project
# TODO: Need to set a pos from the start map on the new map instead of using
# start position and returning to previous position


class Game(State):
    """ 'Game' state and associated data/methods """
    START_MAP = 'world'
    MOVEMENT = {
        'up' : {'text':'north', 'vec':(0, -1)},
        'down' : {'text':'south', 'vec':(0, 1)},
        'left' : {'text':'west', 'vec':(-1, 0)},
        'right' : {'text':'east', 'vec':(1, 0)},
        }
    BUFFER_START = "WELCOME TO THE WASTELANDS"


    def __init__(self, buffer_size=5):
        """ Initiailize class and super class """
        super(Game, self).__init__()
        #TODO: self.first_time should be True, but disabling it to speed up game launch
        # for development
        self.first_time = False
        self.game_time = Game_Time()

        # initialize maps and map data
        self.maps = self._init_maps()
        self.cur_map = self.maps[self.START_MAP]

        # initialize screen and elements
        self.screen = self._init_screen()
        self.update_map(draw=False)

        # initialize command buffer
        self.BUFFER_SIZE = buffer_size
        self.buffer = deque(['' for i in range(self.BUFFER_SIZE)])
        self.add_to_buffer(self.BUFFER_START)


    def _init_maps(self):
        """ create a 'Map' object using the given image filename and then print
        it to the terminal """
        logging.info('MAPS_DATA:{}'.format(const.MAPS_DATA))
        maps = {k:Map(**v, game_time=self.game_time) for k, v in const.MAPS_DATA.items()}

        return maps


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
        """ updates map and redraws screen """
        # write map frame border
        frame_offset = Point(2, 1)
        frame_size = Point(*self.cur_map.frame_size) + Point(2, 2)
        self.screen.add_frame(size=frame_size, offset=frame_offset,
                              frame_style=0, fgcolor='WHITE', bgcolor='BLACK')

        # write date/time
        date = self.game_time.get_date_string()
        time = self.game_time.get_time_string()
        date_time = f"<< {date} - {time} >>"
        col = Screen.center_offset(date_time, frame_size[0])
        row = frame_offset.row    
        self.screen.write_string(f'{date_time}', offset=(col, row),
                                         fgcolor='WHITE', bgcolor='BLACK')

        # write current biome name
        point = self.cur_map.cur_pos
        cur_tile = self.cur_map.get(point)
        cur_tile_name = f' {cur_tile.name.upper()} - {point} '
        col = Screen.center_offset(cur_tile_name, frame_size[0])
        row = frame_offset.row + frame_size.row - 1
        self.screen.write_string(f'<< {cur_tile_name} >>', offset=(col, row),
                                         fgcolor='WHITE', bgcolor='BLACK')

        # write map to screen
        map_frame = self.cur_map.get_map_frame(as_string=False, color=const.SETTINGS['color'])
        self.screen.write_array(map_frame, offset=(3, 2), format_char=False)

        # write player cursor
        self.screen.write_string('@', offset=(24,12),
                                         fgcolor='WHITE', bgcolor='BLACK')

        if draw:
            self.update_screen()

        # # write map to screen
        # map_frame = self.cur_map.get_map_frame(as_string=True, color=const.SETTINGS['color'])
        # Screen.write(map_frame, pos=Point(4, 3))


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
            self.screen.write_string(text, offset=(3, 24 + i),
                                             transparent=False, fgcolor='WHITE',
                                             bgcolor='BLACK')


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


    def map_transfer(self, map_name, pos):
        new_map = self.maps[map_name]
        self.add_to_buffer(f'ENTERING {map_name.upper()}...')
        self.cur_map = new_map
        self.cur_map.cur_pos = Point(*pos)
        # self.cur_pos = self.cur_map.cur_pos
        # update position on map frame
        self.cur_map.set_map_frame()
        # update the map
        self.update_map()


    def move(self, direction):
        """ Even handler for moving in the game world """
        text = self.MOVEMENT[direction]['text'].upper()
        vec = self.MOVEMENT[direction]['vec']

        cur_pos = self.cur_map.cur_pos
        new_pos = self.cur_map.move(vec)
        new_tile = self.cur_map.get(new_pos)

        if new_pos in self.cur_map.doors:
            door = self.cur_map.doors[new_pos]
            map_name = door['target']
            map_pos = door['enter']
            self.map_transfer(map_name, map_pos)
        elif cur_pos != new_pos:
            self.game_time.add_time(minutes=(15 * new_tile.movement))
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

            for direction, mapped_keys in const.SETTINGS['keymap'].items():
                if key in mapped_keys and direction in self.MOVEMENT:
                    self.move(direction)

        return self
