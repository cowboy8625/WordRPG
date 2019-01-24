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
                                    more hazardous tiles. Value of -1 means the
                                    tile is impassable. Default value is 1
        :``color``:         `str`   name of a pre-defeind HTML color. color is
                                    used to build a color map key for loading
                                    map images and converting pixels to tile
                                    data. Default is 'blue'
                            `tuple` (r, g, b) color value. 0-255 range.
        :``symbol``:        `str`   character used when drawing the map
        :``description``:   `str`   description of the tile
        :``format``:        `dict`  defines how tile is drawn to screen
        :``discovered``:    `bool`  If True, tile is drawn. Default is False

    """

    # define class slots to improve memory effeciency
    # http://book.pythontips.com/en/latest/__slots__magic.html
    __slots__ = ['name', 'resources', 'movement', 'color', 'symbol', 'char',
                 'description', '_format', 'discovered']



    def __init__(self, name='TILE', resources=None, movement=1,
                 color='blue', symbol=' ', discovered=False,
                 description='[TILE DESCRIPTION]',
                 _format=DEF_FORMAT
                 ):
        self.name = name
        self.resources = resources
        self.movement = movement
        self.color = Tile.get_rgb_color(color)
        self.description = description
        self.symbol = symbol
        self._format = _format
        self.discovered = discovered

        self.char = self._get_formatted_char()

    @staticmethod
    def get_rgb_color(color):
        """ get rgb color value from color name or tuple """
        if isinstance(color, str):
            return ImageColor.getrgb(color)

        return color


    def _get_formatted_char(self):
        """ gets tile symbol and escape characters as a string """
        return font.add_escape(self.symbol, **self._format)


    def __repr__(self):
        """ returns representation of Tile object """
        attrs = [f'{s}={getattr(self, s)}' for s in self.__slots__]
        return f'Tile({", ".join(attrs)})\n'


    def __str__(self):
        """ returns printable str for tile """
        return self.symbol

"""
format key options
    fgcolor/bgcolor:
        'BLACK', 'BLUE', 'CYAN', 'GREEN', 'LIGHTBLACK_EX', 'LIGHTBLUE_EX',
        'LIGHTCYAN_EX', 'LIGHTGREEN_EX', 'LIGHTMAGENTA_EX', 'LIGHTRED_EX',
        'LIGHTWHITE_EX', 'LIGHTYELLOW_EX', 'MAGENTA', 'RED', 'RESET',
        'WHITE', 'YELLOW'
    style:
        'BRIGHT', 'DIM', 'NORMAL', 'RESET_ALL'
"""

BIOMES = {
    'village':{'movement':1, 'color':'red', 'symbol':'±',
            'description':'YOU ARE IN A PEACEFUL VILLAGE',
            'resources':None,
            '_format':{'fgcolor':'BLACK','bgcolor':'WHITE','style':'NORMAL'},
            'discovered':True
            },
    'cave':{'movement':1, 'color':'black', 'symbol':'▄',
            'description':'YOU ARE STANDING AT THE ENTRANCE TO A DEEP, DARK CAVE',
            'resources':None,
            '_format':{'fgcolor':'BLACK','bgcolor':'LIGHTBLACK_EX','style':'NORMAL'},
            },
    'path':{'movement':1, 'color':'white', 'symbol':'·',
            'description':'YOU ARE IN A VILLAGE',
            'resources':None,
            '_format':{'fgcolor':'BLACK','bgcolor':'LIGHTBLACK_EX','style':'NORMAL'},
            'discovered':True
            },
    'farmland':{'movement':2, 'color':'magenta', 'symbol':'≡',
            'description':'YOU ARE IN A VILLAGE',
            'resources':['herb'],
            '_format':{'fgcolor':'LIGHTYELLOW_EX','bgcolor':'GREEN','style':'NORMAL'},
            },
    'beach':{'movement':2, 'color':'khaki', 'symbol':'░',
            'description':'YOU ARE IN A VILLAGE',
            'resources':None,
            '_format':{'fgcolor':'WHITE','bgcolor':'YELLOW','style':'NORMAL'},
            },
    'desert':{'movement':4, 'color':'peru', 'symbol':'░',
            'description':'YOU ARE IN A VILLAGE',
            'resources':None,
            '_format':{'fgcolor':'RED','bgcolor':'YELLOW','style':'NORMAL'},
            },
    'grassland':{'movement':2, 'color':'lawngreen', 'symbol':' ',
            'description':'YOU ARE IN A VILLAGE',
            'resources':None,
            '_format':{'fgcolor':'LIGHTYELLOW_EX','bgcolor':'LIGHTGREEN_EX','style':'NORMAL'},
            },
    'forest':{'movement':3, 'color':'olivedrab', 'symbol':'♣',
            'description':'YOU ARE IN THE FOREST',
            'resources':['wood'],
            '_format':{'fgcolor':'GREEN','bgcolor':'LIGHTGREEN_EX','style':'NORMAL'},
            },
    'deep_forest':{'movement':4, 'color':'darkgreen', 'symbol':'♣',
            'description':'YOU ARE IN THE DEEP, DARK FOREST',
            'resources':None,
            '_format':{'fgcolor':'LIGHTGREEN_EX','bgcolor':'BLACK','style':'NORMAL'},
            },
    'river':{'movement':2, 'color':'cyan', 'symbol':'~',
            'description':'YOU ARE ON THE RIVER',
            'resources':['water', 'fish'],
            '_format':{'fgcolor':'BLUE','bgcolor':'CYAN','style':'NORMAL'},
            },
    'lake':{'movement':3, 'color':'darkcyan', 'symbol':'~',
            'description':'YOU ARE ON A LAKE',
            'resources':['water', 'fish'],
            '_format':{'fgcolor':'CYAN','bgcolor':'BLUE','style':'NORMAL'},
            },
    'swamp':{'movement':5, 'color':'darkolivegreen', 'symbol':'▒',
            'description':'YOU ARE IN THE SWAMP',
            'resources':None,
            '_format':{'fgcolor':'RED','bgcolor':'GREEN','style':'NORMAL'},
            },
    'salt_marsh':{'movement':4, 'color':'darkseagreen', 'symbol':'▒',
            'description':'YOU ARE IN THE SALT MARSH',
            'resources':['fish', 'salt'],
            '_format':{'fgcolor':'GREEN','bgcolor':'BLUE','style':'NORMAL'},
            },
    'alpine_grassland':{'movement':1, 'color':'lightgreen', 'symbol':'░',
            'description':'YOU ARE IN THE ALPINE GRASSLAND',
            'resources':['pine'],
            '_format':{'fgcolor':'WHITE','bgcolor':'LIGHTGREEN_EX','style':'NORMAL'},
            },
    'mountain':{'movement':-1, 'color':'darkslategray', 'symbol':'^',
            'description':'YOU ARE IN THE MOUNTAINS',
            'resources':None,
            '_format':{'fgcolor':'WHITE','bgcolor':'LIGHTBLACK_EX','style':'NORMAL'},
            },
    'ocean':{'movement':-1, 'color':'blue', 'symbol':'~',
            'description':'YOU ARE IN THE OCEAN',
            'resources':None,
            '_format':{'fgcolor':'BLACK','bgcolor':'BLUE','style':'NORMAL'},
            'discovered':True
            },
    }
