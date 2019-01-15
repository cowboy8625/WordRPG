from .States import Confirm
from .Main_Menu import Main_Menu
from .Load_Game import Load_Game
from .Save_Game import Save_Game
from .New_Game import New_Game, Character_Class, Character_Gender, Character_Name
from .Game import Game
from .Game_Menu import Game_Menu
from .Combat import Combat
from .Inventory import Inventory
from .Crafting import Crafting
from .Shop import Shop
from .Death import Death



# Initilize states and their classes
STATES = {
    # 'quit':Quit(prev_screen='main_menu'),
    'quit':Confirm('Quit?', 'Are you sure you want to quit?', None),
    'main_menu':Main_Menu(),
    'new_game':New_Game(),
    'character_name':Character_Name(),
    'character_class':Character_Class(),
    'character_gender':Character_Gender(),
    'load_game':Load_Game(),  
    'save_game':Save_Game(),  
    'game':Game(),
    'game_menu':Game_Menu(),
    'inventory':Inventory(),
    'combat':Combat(),
    'shop':Shop(),
    'crafting':Crafting(),
    'death':Death(),
}
