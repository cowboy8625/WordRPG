""" WordRPG constants and game data """
import os
import logging


##------------------------------------------------------------------------------
## Project constants
##------------------------------------------------------------------------------

NAME = 'WASTELANDS'
VERSION = 0.2
YEAR = 2019
COMPANY = 'COWBOY GAMING'

TITLE = f'{NAME}(ver.{VERSION}) - {COMPANY} - ©{YEAR}'
HEADER = f'{NAME} - {VERSION}'
FOOTER = f'{COMPANY} - ©{YEAR}'  # © can cause problems with encoding

##------------------------------------------------------------------------------
## Filepaths and filenames
##------------------------------------------------------------------------------

PATH_ROOT = os.path.dirname(__file__)
PATH_MAPS = os.path.join(PATH_ROOT, 'map', 'images')
PATH_TILESETS = os.path.join(PATH_ROOT, 'map', 'tilesets')
PATH_SCREENS = os.path.join(PATH_ROOT, 'gui', 'text_screens')

##------------------------------------------------------------------------------
## GUI related constants
##------------------------------------------------------------------------------

# pixel size of characters in terminal
CHAR_SIZE = (8, 16)
# size of terminal in (cols, rows) of printable characters
SCREEN_SIZE = (80, 30)
# screen resolution in pixels
SCREEN_RES = (SCREEN_SIZE[0] * CHAR_SIZE[0], SCREEN_SIZE[1] * CHAR_SIZE[1])
# default size of map window in main game screen
# note, these should be an odd number so we can have a 'player' character in
# the center of the screen
DEF_MAP_SIZE = (41, 21)

# This constant sets color/style formatting on or off
FORMAT_TEXT = True
# These are the default colorama font color/styling values
DEF_FONT = {'fgcolor':'WHITE','bgcolor':'BLACK','style':'NORMAL'}

# CONNECT_SYMBOLS = {0:'═', 1:'║', 2:'║', 3:'║', 4:'═', 5:'╝', 6:'╗' ,7:'╣',
#                    8:'═', 9:'╚', 10:'╔', 11:'╠', 12:'═', 13:'╩', 14:'╦', 15:'╬'}

CONNECT_SYMBOLS ={
    'path':{0:'─', 1:'│', 2:'│', 3:'│', 4:'─', 5:'┘', 6:'┐' ,7:'┤', 8:'─',
            9:'└', 10:'┌', 11:'├', 12:'─', 13:'┴', 14:'┬', 15:'┼'},
    'road':{0:'═', 1:'║', 2:'║', 3:'║', 4:'═', 5:'╝', 6:'╗' ,7:'╣', 8:'═',
            9:'╚', 10:'╔', 11:'╠', 12:'═', 13:'╩', 14:'╦', 15:'╬'},
    'fence':{0:'┬', 1:'│', 2:'│', 3:'│', 4:'┬', 5:'┤', 6:'┐' ,7:'┤', 8:'┬',
            9:'├', 10:'┌', 11:'├', 12:'┬', 13:'┼', 14:'┬', 15:'┼'},
    }


##------------------------------------------------------------------------------
## User Settings
##------------------------------------------------------------------------------

# TODO: starting to implement a settings menu for development and game options
# eventually this should be managed as an extrnal .json file so we can save/load
# them in game
SETTINGS = {
    # 'start_state':'main_menu',        # normal start_state
    'start_state':'game',
    'symbol':True,
    'color':True,
    'logging':logging.ERROR,
    'log_map':os.path.join(PATH_ROOT, 'map.log'),
    'log_game':os.path.join(PATH_ROOT, 'game.log'),    
    }

# ToDo: duplicate data here, but it's easier to check if a key is in
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

##------------------------------------------------------------------------------
## Map data
##------------------------------------------------------------------------------

MAPS_DATA = {
    'world':{
        'map_name':'test_island2', 'tileset':'world', 'visibility':(0,12),
        'pos':(40,27),
        'doors':{
            (54,25):{'target':'cave_river', 'enter':(2,13)},
            (42,28):{'target':'village_port', 'enter':(20,11)},
            (44,32):{'target':'ship', 'enter':(42,21)},
            # (25,35):'cave_desert',
            # (57,12):'cave_swamp',
            # (74,9):'cave_forest',
            # (69,30):'cave_lake',
            # (85,21):'cave_alpine',
            # (84,47):'cave_beach',
            # (18,19):'village_desert',
            # (36,14):'village_forest',
        }
    },
    'cave_river':{
        'map_name':'test_cave2', 'tileset':'cave', 'visibility':(6,6),
        'pos':(54,47),
        'doors':{
            (1,13):{'target':'world', 'enter':(53,25)},
        }
    },
    'village_port':{
        'map_name':'test_village1', 'tileset':'village', 'visibility':(0,12),
        'pos':(20,11),
        'doors':{
            (20,1):{'target':'world', 'enter':(42,27)},
            (20,20):{'target':'world', 'enter':(42,29)},
            (1,11):{'target':'world', 'enter':(41,28)},
        }
    },
    'ship':{
        'map_name':'test_ship1', 'tileset':'world', 'visibility':(0,12),
        'pos':(42,19),
        'doors':{
            (42,19):{'target':'world', 'enter':(44,31)},
            (42,19):{'target':'world', 'enter':(44,31)},
        }
    }
}