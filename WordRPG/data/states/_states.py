from ...state_machine import State, Confirm

from .combat import Combat
from .crafting import Crafting
from .death import Death
from .game_menu import Game_Menu
from .game import Game
from .inventory import Inventory
from .file_io import Load_Game, Save_Game
from .main_menu import Main_Menu
from .new_game import New_Game
from .quit import Quit
from .shop import Shop



# Game states
STATES = {
    'main_menu':Main_Menu(),
    'new_game':New_Game(),
    # 'character_name':Character_Name(),
    # 'character_class':Character_Class(),
    # 'character_gender':Character_Gender(),
    'load_game':Load_Game(),  
    'save_game':Save_Game(),  
    'game':Game(),
    'game_menu':Game_Menu(),
    'inventory':Inventory(),
    'combat':Combat(),
    'shop':Shop(),
    'crafting':Crafting(),
    'death':Death(),
    'quit':Confirm(
            'QUIT GAME',
            'ARE YOU SURE YOU WANT TO QUIT?',
            None
            ),
    'return_to_main_menu':Confirm(
            'RETURN TO MAIN MENU',
            'ARE YOU SURE YOU WANT TO RETURN TO MAIN MENU?',
            'main_menu'
            ),
    }
    