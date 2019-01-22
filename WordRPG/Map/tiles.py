from PIL import ImageColor

""" Module for formatting text

    Notes:
        Fore/Back:
            'BLACK', 'BLUE', 'CYAN', 'GREEN', 'LIGHTBLACK_EX', 'LIGHTBLUE_EX',
            'LIGHTCYAN_EX', 'LIGHTGREEN_EX', 'LIGHTMAGENTA_EX', 'LIGHTRED_EX',
            'LIGHTWHITE_EX', 'LIGHTYELLOW_EX', 'MAGENTA', 'RED', 'RESET',
            'WHITE', 'YELLOW'
        Style:
            'BRIGHT', 'DIM', 'NORMAL', 'RESET_ALL'

"""



""" Diciontaries for various tilesets are defined here

    '[tile_name]': {[dict]}

    'resource': {list} - list of resources that can be found in this tile
    'movement': {int} - movement cost to move into tile.
                    -1 means tile is
                    impassable
    'description': 'YOU ARE ON THE ROAD',
    'img_color' : (R, G, B) color used in source image
    'symbol' : Ascii symbol used to draw tile in game window
    'format' : {[dict]}
        'fgcolor':'BLACK'
        'bgcolor':'YELLOW'
        'style':'NORMAL'
"""

BIOMES = {
    'village': {
        'resource': None, 
        'movement': 1 ,     # roads are the fastest/safest way to travel
        'description': 'YOU ARE IN A VILLAGE',
        'img_color' : ImageColor.getrgb('red'),
        'symbol' : '±',
        'format' : {'fgcolor':'BLACK','bgcolor':'WHITE','style':'NORMAL'},
        },
    'cave': {
        'resource': None, 
        'movement': 1 ,     # roads are the fastest/safest way to travel
        'description': 'YOU ARE STANDING AT THE ENTRANCE TO A CAVE',
        'img_color' : ImageColor.getrgb('black'),
        'symbol' : '▄',
        'format' : {'fgcolor':'BLACK','bgcolor':'LIGHTBLACK_EX','style':'NORMAL'},
        },
    ## -------------------------------------------------------------------------
    ## passable biomes
    ## -------------------------------------------------------------------------    
    'road': {
        'resource': None, 
        'movement': 1 ,     # roads are the fastest/safest way to travel
        'description': 'YOU ARE ON THE ROAD',
        'img_color' : ImageColor.getrgb('white'),
        'symbol' : '·',
        'format' : {'fgcolor':'BLACK','bgcolor':'LIGHTBLACK_EX','style':'NORMAL'},
        },
    'farmland': {
        'resource' : ['herb'], 
        'movement' : 2 ,
        'description' : 'YOU ARE ON FARMLAND',
        'img_color' : ImageColor.getrgb('magenta'),
        'symbol' : '≡',
        'format' : {'fgcolor':'LIGHTYELLOW_EX','bgcolor':'GREEN','style':'NORMAL'},   
        },
    'beach': {
        'resource' : None, 
        'movement' : 2 ,
        'description' : 'YOU ARE ON THE BEACH',
        'img_color' : ImageColor.getrgb('khaki'),
        'symbol' : '░',
        'format' : {'fgcolor':'WHITE','bgcolor':'YELLOW','style':'NORMAL'},   
        },
    'desert': {
        'resource' : ['grass'], 
        'movement' : 3 ,
        'description' : 'YOU ARE IN THE DESERT',
        'img_color' : (205, 133, 63),   #ImageColor.getrgb('peru'),
        'symbol' : '░',
        'format' : {'fgcolor':'RED','bgcolor':'YELLOW','style':'NORMAL'},   
        },
    'grassland': {
        'resource' : ['grass'], 
        'movement' : 2 ,
        'description' : 'YOU ARE IN GRASSLANDS',
        'img_color' : ImageColor.getrgb('lawngreen'),
        'symbol' : ' ',
        'format' : {'fgcolor':'LIGHTYELLOW_EX','bgcolor':'LIGHTGREEN_EX','style':'NORMAL'},   
        },
    'forest': {
        'resource': ['wood'], 
        'movement': 3 ,
        'description': 'YOU ARE IN THE FOREST',
        'img_color' : ImageColor.getrgb('olivedrab'),
        'symbol' : '♣',     #'▒',
        'format' : {'fgcolor':'GREEN','bgcolor':'LIGHTGREEN_EX','style':'NORMAL'},
        },
    'deep_forest': {
        'resource': ['wood', 'magic_wood'], 
        'movement': 4 ,
        'description': 'YOU ARE IN THE DEEP, DARK FOREST',
        'img_color' : ImageColor.getrgb('darkgreen'),
        'symbol' : '♣',     #'▒',
        'format' : {'fgcolor':'LIGHTGREEN_EX','bgcolor':'BLACK','style':'NORMAL'},
        },
    'river': {
        'resource' : ['water', 'fish'],
        'movement' : 3 ,
        'description' : 'YOU ARE IN A RIVER',
        'img_color' : ImageColor.getrgb('cyan'),
        'symbol' : '~',
        'format' : {'fgcolor':'BLUE','bgcolor':'CYAN','style':'NORMAL'},
        },
    'lake': {
        'resource' : ['water', 'fish'],
        'movement' : 4 ,
        'description' : 'YOU ARE ON A LAKE',
        'img_color' : ImageColor.getrgb('darkcyan'),
        'symbol' : '~',
        'format' : {'fgcolor':'CYAN','bgcolor':'BLUE','style':'NORMAL'},
        },
    'swamp': {
        'resource': None, 
        'movement': 4 ,
        'description': 'YOU ARE IN THE SWAMP',
        'img_color' : ImageColor.getrgb('darkolivegreen'),
        'symbol' : '▒',
        'format' : {'fgcolor':'RED','bgcolor':'GREEN','style':'NORMAL'},
        },
    'salt_marsh': {
        'resource': ['fish', 'salt'], 
        'movement': 3 ,
        'description': 'YOU ARE IN THE SALT MARSH',
        'img_color' : ImageColor.getrgb('darkseagreen'),
        'symbol' : '▒',
        'format' : {'fgcolor':'GREEN','bgcolor':'BLUE','style':'NORMAL'},
        },
    'alpine_grassland': {
        'resource': ['pine'], 
        'movement': 2 ,
        'description': 'YOU ARE IN THE ALPINE GRASSLAND',
        'img_color' : ImageColor.getrgb('lightgreen'),
        'symbol' : '▒',
        'format' : {'fgcolor':'WHITE','bgcolor':'LIGHTGREEN_EX','style':'NORMAL'},
        },
    ## -------------------------------------------------------------------------
    ## impassable boundary biomes
    ## -------------------------------------------------------------------------    
    'mountain': {
        'resource': None,
        'movement': -1 ,
        'description': 'YOU ARE IN THE MOUNTAINS',
        'img_color' : ImageColor.getrgb('darkslategray'),
        'symbol' : '▲',     #'^',
        'format' : {'fgcolor':'WHITE','bgcolor':'LIGHTBLACK_EX','style':'NORMAL'},
        },
    'ocean': {
        'resource': None, 
        'movement': -1 ,
        'description': 'YOU ARE IN THE OCEAN',
        'img_color' : ImageColor.getrgb('blue'),
        'symbol' : '~',
        'format' : {'fgcolor':'BLACK','bgcolor':'BLUE','style':'NORMAL'},
        },
    }
