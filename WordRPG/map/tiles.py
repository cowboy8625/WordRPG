""" Module for Tile class and tilesets """

from PIL import ImageColor

from ..gui import font
from ..gui.const import DEF_FORMAT


class Tile:
    """
    Base class for a Map Tile

    **Arguments:**

        None

    **Keword Arguments:**
        :``name``:          `str`   name of the tile
        :``resources``:     `list`  list of resources that can be gathered from
                                    this tile. Default is None
        :``movement``:      `int`   value that represents how difficult it is
                                    to move into this tile. Higher numbers are
                                    more hazardous tiles. Value of 0 means the
                                    tile is impassable. Default value is 1
        :``color``:         `str`   name of a pre-defeind HTML color. color is
                                    used to build a color map key for loading
                                    map images and converting pixels to tile
                                    data. Default is 'blue'
                                    -- or --
                            `tuple` (r, g, b) color value. 0-255 range.
        :``alpha``:         `str`   alphanumeric character used when drawing the map
        :``symbol``:        `str`   ascii symbol used when drawing the map
        :``description``:   `str`   description of the tile
        :``format``:        `dict`  defines how tile is drawn to screen
        :``discovered``:    `bool`  If True, tile is drawn. Default is False

    """
    # class slots: http://book.pythontips.com/en/latest/__slots__magic.html
    __slots__ = ['name', 'resources', 'movement', 'color', 'alpha', 'symbol',
                 'char', 'description', 'font', 'discovered']



    def __init__(self, name='TILE', resources=None, movement=1,
                 color='blue', alpha='?', symbol=' ', discovered=False,
                 description='[TILE DESCRIPTION]',
                 font=DEF_FORMAT
                 ):
        self.name = name
        self.color = Tile.get_rgb_color(color)
        self.alpha = alpha
        self.symbol = symbol
        self.font = font
        self.char = self.format_tile()
        self.resources = resources
        self.movement = movement
        self.description = description
        self.discovered = discovered


    @staticmethod
    def get_rgb_color(color):
        """ get rgb color value from color name or tuple """
        if isinstance(color, str):
            return ImageColor.getrgb(color)
        return color


    def format_tile(self):
        """ gets tile symbol and escape characters as a string """
        return font.add_escape(self.symbol, **self.font)


    def set_symbol(self, char):
        """ replaces the symbol and re-applies font formatting """
        self.symbol = char
        self.char = font.add_escape(self.symbol, **self.font)


    def __repr__(self):
        """ returns representation of Tile object """
        attrs = [f'{s}={getattr(self, s)}' for s in self.__slots__]
        return f'Tile({", ".join(attrs)})\n'


    def __str__(self):
        """ returns printable str for tile """
        return self.symbol

"""
font options
    fgcolor/bgcolor:
        'BLACK', 'BLUE', 'CYAN', 'GREEN', 'LIGHTBLACK_EX', 'LIGHTBLUE_EX',
        'LIGHTCYAN_EX', 'LIGHTGREEN_EX', 'LIGHTMAGENTA_EX', 'LIGHTRED_EX',
        'LIGHTWHITE_EX', 'LIGHTYELLOW_EX', 'MAGENTA', 'RED', 'RESET',
        'WHITE', 'YELLOW'
    style:
        'BRIGHT', 'DIM', 'NORMAL', 'RESET_ALL'
"""

BIOMES = {
    'village':{'movement':1, 'color':'red', 'alpha':'V', 'symbol':'±',
            'description':'YOU ARE IN A PEACEFUL VILLAGE',
            'resources':None,
            'font':{'fgcolor':'BLACK','bgcolor':'WHITE','style':'NORMAL'},
            'discovered':True
            },
    'cave':{'movement':1, 'color':'black', 'alpha':'C', 'symbol':'▄',
            'description':'YOU ARE STANDING AT THE ENTRANCE TO A DEEP, DARK CAVE',
            'resources':None,
            'font':{'fgcolor':'BLACK','bgcolor':'LIGHTBLACK_EX','style':'NORMAL'},
            },
    'path':{'movement':1, 'color':'white','alpha':'P', 'symbol':'·',
            'description':'YOU ARE IN A VILLAGE',
            'resources':None,
            'font':{'fgcolor':'LIGHTYELLOW_EX','bgcolor':'LIGHTGREEN_EX','style':'DIM'},
            'discovered':True
            },
    'farmland':{'movement':2, 'color':'magenta', 'alpha':'F', 'symbol':'≡',
            'description':'YOU ARE IN A VILLAGE',
            'resources':['herb'],
            'font':{'fgcolor':'LIGHTYELLOW_EX','bgcolor':'GREEN','style':'NORMAL'},
            },
    'beach':{'movement':2, 'color':'khaki', 'alpha':'B', 'symbol':'░',
            'description':'YOU ARE IN A VILLAGE',
            'resources':None,
            'font':{'fgcolor':'WHITE','bgcolor':'YELLOW','style':'NORMAL'},
            },
    'desert':{'movement':4, 'color':'peru', 'alpha':'D', 'symbol':'░',
            'description':'YOU ARE IN A VILLAGE',
            'resources':None,
            'font':{'fgcolor':'RED','bgcolor':'YELLOW','style':'NORMAL'},
            },
    'grassland':{'movement':2, 'color':'lawngreen', 'alpha':'G', 'symbol':' ',
            'description':'YOU ARE IN A VILLAGE',
            'resources':None,
            'font':{'fgcolor':'LIGHTYELLOW_EX','bgcolor':'LIGHTGREEN_EX','style':'NORMAL'},
            },
    'forest':{'movement':3, 'color':'olivedrab', 'alpha':'T', 'symbol':'O',
            'description':'YOU ARE IN THE FOREST',
            'resources':['wood'],
            'font':{'fgcolor':'GREEN','bgcolor':'LIGHTGREEN_EX','style':'NORMAL'},
            },
    'deep_forest':{'movement':4, 'color':'darkgreen', 'alpha':'P', 'symbol':'O',
            'description':'YOU ARE IN THE DEEP, DARK FOREST',
            'resources':None,
            'font':{'fgcolor':'BLACK','bgcolor':'GREEN','style':'NORMAL'},
            },
    'river':{'movement':2, 'color':'cyan', 'alpha':'R', 'symbol':'~',
            'description':'YOU ARE ON THE RIVER',
            'resources':['water', 'fish'],
            'font':{'fgcolor':'BLUE','bgcolor':'CYAN','style':'NORMAL'},
            },
    'lake':{'movement':3, 'color':'darkcyan', 'alpha':'L', 'symbol':'~',
            'description':'YOU ARE ON A LAKE',
            'resources':['water', 'fish'],
            'font':{'fgcolor':'CYAN','bgcolor':'BLUE','style':'NORMAL'},
            },
    'swamp':{'movement':5, 'color':'darkolivegreen', 'alpha':'S', 'symbol':'▒',
            'description':'YOU ARE IN THE SWAMP',
            'resources':None,
            'font':{'fgcolor':'RED','bgcolor':'GREEN','style':'NORMAL'},
            },
    'salt_marsh':{'movement':4, 'color':'darkseagreen', 'alpha':'X', 'symbol':'▒',
            'description':'YOU ARE IN THE SALT MARSH',
            'resources':['fish', 'salt'],
            'font':{'fgcolor':'GREEN','bgcolor':'BLUE','style':'NORMAL'},
            },
    'alpine_grassland':{'movement':1, 'color':'lightgreen', 'alpha':'A', 'symbol':'░',
            'description':'YOU ARE IN THE ALPINE GRASSLAND',
            'resources':['pine'],
            'font':{'fgcolor':'WHITE','bgcolor':'LIGHTGREEN_EX','style':'NORMAL'},
            },
    'mountain':{'movement':0, 'color':'darkslategray', 'alpha':'M', 'symbol':'^',
            'description':'YOU ARE IN THE MOUNTAINS',
            'resources':None,
            'font':{'fgcolor':'WHITE','bgcolor':'LIGHTBLACK_EX','style':'NORMAL'},
            },
    'ocean':{'movement':0, 'color':'blue', 'alpha':'O', 'symbol':'~',
            'description':'YOU ARE IN THE OCEAN',
            'resources':None,
            'font':{'fgcolor':'BLACK','bgcolor':'BLUE','style':'NORMAL'},
            'discovered':True
            },
    }
