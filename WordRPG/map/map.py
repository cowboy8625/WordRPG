""" Module for creating and manipulating Maps """
import os
from sys import stdout
from time import sleep
from math import ceil, floor
import logging
import json
from pprint import pprint
from itertools import product

from PIL import ImageColor, Image, ImageOps

from ..common import Point, Table
from .. import const
from .tile import Tile



logging.basicConfig(filename=const.SETTINGS['log_filename'], filemode='w',
                    level=const.SETTINGS['logging'])




class Map(Table):
    """ Base class for a map object

    A map is a 2D array (list of lists) that contain pointers to tile/biome
    data.

    Maps can be parsed from an image where each pixel uses a pre-defined
    RGB value to represent a specific tile or biome

    **Arguments:**
        :``filename``:  `str`   Name of the map image to load and parse

    **Keword Arguments:**
        :``tileset``:   `dict`  Dictionary of keys and 'Tile' objects
    """

    def __init__(self, map_name, pos=(0,0), doors={},
                  tileset='world', visibility=0):
        self.tileset = self.load_tileset(tileset)
        self.map_key = self.get_map_key()
        self.cols, self.rows = self.size = (0, 0)

        # set default cell for out of range indexing
        self.default_cell = self.get_default_tile()

        # create map array from image file
        self.load_map(map_name)

        # initialize doors and their connections to other mapss
        self.doors = doors

        # default visibility radius
        self.visibility_day, self.visibility_night = self.visibility = visibility

        # set current position and Tile
        self.cur_pos = Point(*pos)
        self.cur_tile = self.get(self.cur_pos)

        # create initial map frame
        self.frame_size = const.DEF_MAP_SIZE
        self.set_map_frame(self.frame_size)

        # do initial visiblity check
        self.set_visibility()


    @staticmethod
    def load_tileset(tileset_name):
        """ loads tileset data from a .json file """
        filename = os.path.join(const.PATH_TILESETS, f'{tileset_name}.json')
        with open(filename, encoding='utf-8') as f:
            tileset = json.load(f)
            # pprint(tileset)

        return tileset


    def get_map_key(self):
        """ Builds color : tile map key

        Keyword Arguments:
            tileset {dict} -- dictionary of info about tiles (default: {const.TILESET_WORLD})
        """

        return {Tile.get_rgb_color(values['color']):key
                for key, values in self.tileset.items()}


    def create_tiles(self, pixels):
        """ Creates tiles for the pixels based on the Tileset """

        tiles=[]
        for rgb in pixels:
            if rgb not in self.map_key:
                print(f'{rgb} not in map key!')
                tiles.append(None)
            else:
                key = self.map_key[rgb]
                tile = Tile(name=key, **self.tileset[key])
                tiles.append(tile)
                logging.debug('Tile:{}'.format(repr(tile).encode(encoding="utf-8")))

        return tiles


    def load_map(self, map_name):
        """ Loads an image file and parses it into a map

        Arguments:
            filename {[type]} -- [description]

        Returns:
            [list] -- 'map' array, list of lists containing 'Tile' objects
        """

        filename = os.path.join(const.PATH_MAPS, f'{map_name}.png')
        image = Image.open(filename)

        # update map size based on dimensions of source image
        self.cols, self.rows = self.size = image.size

        # generate color key used to map pixel color to Tiles
        map_key = self.get_map_key()

        # collect image data as a list of rgb pixel values
        pixels = [x for x in list(image.getdata())]

        # loop through list of pixels and convert them to matching Tile in the
        # map's tileset
        tiles = self.create_tiles(pixels)

        # converts list of tiles into an array (2D list of lists) and then
        # generate a Table object as the 'map'
        map_array = [tiles[i:(i + self.cols)]
                     for i in range(0, len(tiles), self.cols)]

        # self.map = Table(map_array)
        self.map = self.cells = map_array

        # replace symbols on connected tiles
        self.connect_tiles()


    def get_default_tile(self):
        """ Create a tile to be used for the border

        'Border' tiles are used for out-of-range indicies when generating a new
        map frame.
        """

        # try to find a Tile in the Tileset that has a 'default' key set to True
        for k, v in self.tileset.items():
            if self.tileset[k].get('default') is True:
                return Tile(name=k, **self.tileset[k])

        # If no default Tile was found, return a Tile from the first Tile in
        # the Tileset dict
        tile_name = self.tileset.keys()[0]
        return Tile(name=tile_name, **self.tileset[tile_name])


    def get_connect_symbol(self, tile, point):
        """ Get a connected 'path' symbol based on neighbor Tiles

        Collects neighboring Tiles at a given point and replaces the Tile symbol
        with one that will connect with all neighboring Tiles of the same name

        Arguments:
            tile_name {str}
                Name of the Tile to connect with other similiar Tiles
            point {Point}
                (col,row) position in the map array

        Notes:
            This method maps binary values to a symbol to determine which should
            be used to connects a Tile to all of it's neighbors of the the same
            tile name.

        Returns:
            [str] -- symbol to use for the path tile at the given position
        """

        t, r, b, l = self.get_neighbors(point)
        key = 0
        if t is not None and t.name == tile.name:
            key += 1
        if b is not None and b.name == tile.name:
            key += 2
        if l is not None and l.name == tile.name:
            key += 4
        if r is not None and r.name == tile.name:
            key += 8

        return const.CONNECT_SYMBOLS[tile.connect_style][key]


    def connect_tiles(self):
        """ Connect 'path' tiles with appropriate symbol

        Loop through each column in each row of the map array and get the
        Tile object.  If the tile's name is 'path', then get a new symbol
        for that tile at that position that connects it to neighboring path
        tiles
        """

        logging.debug('.connect_tiles()')
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                tile = self.map[row][col]

                logging.debug('Tile({}, {}.connect = {}({})'.format(col, row, tile.connect, type(tile.connect)))
                if tile is not None and tile.connect is True:
                    symbol = self.get_connect_symbol(tile, Point(col, row))
                    logging.debug('Get connected symbol:{}'.format(symbol))
                    tile.set_symbol(symbol)


    # def set_visible_tiles(self, range=8):
    #     for tile in self.frame:
    #         distance = Point.distance(self.cur_pos, )


    def get_map(self, as_string=True, symbol=const.SETTINGS['symbol'],
                color=const.SETTINGS['color']):
        """ Gets the map as a string

        Keyword Arguments:
            as_string {bool}    -- If True, output unformatted map Tile symbols
                                   instead of formatted char (default: {False})
            color {bool}        -- If True, output formatted map Tile symbols.
                                   Otherwise, output the raw ASCII symbol.
        """

        if as_string:
            return self.to_string()
        elif symbol is not True:
            return self.to_string(att='alpha')
        elif color is not True:
            return self.to_string(att='symbol')
        else:
            return self.to_string(att='char')


    def set_visibility(self):
        """ sets visiblity on Map Tiles """

        # TODO: Get current visibilty radius based on time of day
        vis_radius = self.visibility_day
        
        # if radius is 0 then all tiles are visible
        all_visible = vis_radius == 0

        self.default_cell.visible = all_visible

        # for row in self:
        #     for tile in row:
        #         tile.visible = all_visible
        
        # if all_visible is True:
        #     return None

        # make sure we're only checking in-range cells
        col, row = self.cur_pos
        min_row = min(row - vis_radius, 0)
        max_row = max(row + vis_radius, self.rows)
        min_col = min(col - vis_radius, 0)
        max_col = max(col + vis_radius, self.cols)
        rows = list(range(min_row, max_row))
        cols = list(range(min_col, max_col))

        # tile symbols used to do a soft falloff of visilbity radius
        gradient = ['▓', '▒', '░']

        # loop through each tile and determine if they are within the visibility
        # radius.
        # For tiles on the edges of the visibility radius, we change their
        # current symbol to render a screen character
        for pos in product(cols, rows):
            point = Point(*pos)
            tile = self.get(Point(*pos))
            distance = int(point.distance(self.cur_pos))

            # if a tile is outside the radius, set the .visible property to True
            # if 'all_visible' is True (visibilty radius is 0)
            if distance > vis_radius:
                tile.visible = all_visible
            # if a tile's distance from current position is between the
            # visibility radisus and 3 units from the edge, we want to change
            # the Tile's symbol to draw a screen character
            elif vis_radius > distance > vis_radius - 3:
                tile.visible = True
                font = {k:v for k, v in tile.font.items()}
                font['fgcolor'] = 'BLACK'
                index = sorted([0, vis_radius - distance, 2])[1]
                symbol = gradient[index]
                tile.char = tile.format_tile(symbol=symbol, _font=font)
            # TODO: This should be refactored so that we're not re-formatting
            # the Tile character every time. Could probably have a sub process
            # that checks to see if the visible state changed
            else:
                tile.visible = True
                tile.char = tile.format_tile()


    def move(self, vec=(0,0)):
        """ Changes current position on Map

        Keyword Arguments:
            vec {tuple} -- (col,row) value to change current position by. (Default is (0,0))

        Returns:
            tuple -- Current (col,row) position on Map
        """

        next_pos = self.cur_pos + Point(*vec)
        next_tile = self.get(next_pos)

        if next_tile.movement > 0:
            self.move_frame(vec)
            sleep(abs(next_tile.movement) * 0.0625)    # pause to give screen time to redraw

        self.set_visibility()

        return self.cur_pos


    def show(self, clear=False, frame=False, symbol=const.SETTINGS['symbol'], color=const.SETTINGS['color']):
        """ Prints the map array to terminal

        Keyword Arguments:
            clear {bool}  -- If True, clear the terminal window before
                                   writing to it. (default: {False})
            frame {bool}        -- If True, output the framed portion of the
                                   map to the terminal (default: {False})
            raw {bool}          -- If True, output unformatted map Tile symbols
                                   instead of formatted char (default: {False})

        Returns:
            [type] -- [description]
        """

        if frame:
            stdout.write(self.get_map_frame(symbol=symbol, color=color))
        else:
            stdout.write(self.get_map(symbol=symbol, color=color))
        stdout.flush()


    def __repr__(self):
        """ returns explicit representation of Map object """
        # attr_names = [slot for slot in self.__slots__]
        attr_names = ['map_name', 'tileset', 'pos', 'doors']
        attrs = [f'{n}={str(getattr(self, n))}' for n in attr_names]
        return f'Map({attrs})'


    def __str__(self):
        """ returns printable string version of Map object """
        # return self.array_to_string(self.map, color=False)
        return self.to_string(attr='symbol')


## -----------------------------------------------------------------------------
## Map 'frame' methods
## -----------------------------------------------------------------------------
    # TODO: Implement as Table class method
    def get_map_frame(self, as_string=True, symbol=const.SETTINGS['symbol'],
                      color=const.SETTINGS['color']):
        """ Gets the framed map window as a string

        Keyword Arguments:
            as_string {bool}    -- If True, output unformatted map Tile symbols
                                   instead of formatted char (default: {False})
            color {bool}        -- If True, output formatted map Tile symbols.
                                   Otherwise, output the raw ASCII symbol.
        """

        if as_string:
            return self.array_to_string(self.frame, symbol=symbol)
        elif symbol is not True:
            return [[tile.alpha for tile in row] for row in self.frame]
        elif color is not True:
            return [[tile.symbol for tile in row] for row in self.frame]
        else:
            # return [[tile.char for tile in row] for row in self.frame]
            return [[tile.char if tile.visible else ' ' for tile in row] for row in self.frame]


    # TODO: Implement as seperate 'Map' object
    def set_map_frame(self, size=None):
        """ Gets a framed portion of the map array

        Gets a framed portion of the whole map array so it can be displayed in
        in a frame on one of the game screens.

        For tiles outside of the range of the map array we use a virtual
        'border' Tile to fill in those empy spaces

        Arguments:
            size {tuple} -- number of (cols, rows) of the map to return
            offset {tuple} -- starting (cols, rows) of the segment
        """

        if size is None:
            size = self.frame_size

        cols, rows = self.frame_size = size
        col, row = self.cur_pos
        # get offset for top-left corner of frame by subtracting half of the
        # frame size from the current position
        start_col, start_row = col - int(ceil(cols / 2)), row - int(floor(rows / 2))
        cols = range(start_col, (start_col + cols))
        rows = range(start_row, (start_row + rows))
        array = [[self.get(Point(col,row)) for col in cols] for row in rows]

        self.frame = Table(array)


    # TODO: Implement as seperate 'Map' object
    def move_frame(self, vec=(0,0)):
        """ Move current position in map and update the map frame

        Keyword Arguments:
            vec {tuple} -- (col,row) value to change current position by. (Default is (0,0))
        """

        self.cur_pos += Point(*vec)
        self.set_map_frame()


    # TODO: Implement as seperate 'Map' object
    def array_to_string(self, array, symbol=const.SETTINGS['symbol'],
                        color=const.SETTINGS['color']):
        """ Converts 'map' array to string of tile symbols

        Arguments:
            _map {list} -- 'map' array

        Note:
            This was broken out into a seperate function from __str__ so that
            it can be used to print map frame as well as the full map

            Go through each row in self.map array and get all of the Tile.symbol
            characters. Then join all of the rows into a single string which
            can be printed to the terminal

        Returns:
            [str] -- string of tile symbol symbols
        """

        if symbol is not True:
            rows = [''.join([tile.alpha for tile in row]) for row in array]
        if color is not True:
            rows = [''.join([tile.symbol for tile in row]) for row in array]
        else:
            rows = [''.join([tile.char for tile in row]) for row in array]

        return '\n'.join(rows)
