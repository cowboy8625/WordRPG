""" Module for Tile class and tilesets """

from PIL import ImageColor

from .. import const
from ..gui import font



class Tile:
    """
    Base class for a Map Tile

    **Arguments:**

        None

    **Keword Arguments:**
        :``name``:          `str`   name of the tile
        :``resources``:     `list`  list of resources that can be gathered from
                                    this tile. (Default is None)
        :``movement``:      `int`   value that represents how difficult it is
                                    to move into this tile. Higher numbers are
                                    more hazardous tiles. Value of 0 means the
                                    tile is impassable. (Default value is 1)
        :``color``:         `str`   name of a pre-defeind HTML color. color is
                                    used to build a color map key for loading
                                    map images and converting pixels to tile
                                    data. (Default is 'blue')
                                    -- or --
                            `tuple` (r, g, b) color value. 0-255 range.
        :``alpha``:         `str`   alphanumeric character used when drawing the map
        :``symbol``:        `str`   ascii symbol used when drawing the map
        :``description``:   `str`   description of the tile
        :``format``:        `dict`  defines how tile is drawn to screen
        :``visible``:       `bool`  If True, tile is drawn.
                                    (Default is True)
        :``discovered``:    `bool`  If True, tile has been visible at least
                                    once.(Default is False)
        :``connect``:       `bool`  If True, tiles symbol should connect with 
                                    neighboring tiles of same type.
                                    (Default is False.)

    """
    def __init__(self, name='TILE', resources=None, movement=1,
                 color='blue', alpha='?', symbol=' ', font=const.DEF_FONT,
                 description='[TILE DESCRIPTION]',
                 connect=False, connect_style='road',
                 visible=True, discovered=False, **kwargs):
        self.name = name
        self.resources = resources
        self.movement = movement
        self.connect = connect
        self.connect_style = connect_style
        self.alpha = alpha
        self.symbol = symbol
        self.font = font
        self.description = description
        self.visible = visible
        self.discovered = discovered

        self.color = Tile.get_rgb_color(color)
        self.char = self.format_tile()


    @staticmethod
    def get_rgb_color(color):
        """ get rgb color value from color name or tuple """
        if isinstance(color, str):
            return ImageColor.getrgb(color)
        return color


    def format_tile(self, symbol=None, _font=None):
        """ gets tile symbol and escape characters as a string """
        if symbol is None:
            symbol = self.symbol
        if _font is None:
            _font = self.font

        return font.add_escape(symbol, **_font)


    def set_symbol(self, char):
        """ replaces the symbol and re-applies font formatting """
        self.symbol = char
        self.char = font.add_escape(self.symbol, **self.font)


    def __repr__(self):
        """ returns representation of Tile object """
        attr_names = ['name', 'resources', 'movement', 'connect', 'color',
                      'alpha', 'symbol', 'font', 'description', 'visible',
                      'discovered']
        attrs = [f'{n}={str(getattr(self, n))}' for n in attr_names]
        return f'Tile({", ".join(attrs)})\n'


    def __str__(self):
        """ returns printable str for tile """
        return self.symbol
