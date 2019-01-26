""" Module for creating and manipulating Maps """
import os
from sys import stdout
from time import sleep
from math import ceil, floor

from PIL import ImageColor, Image, ImageOps

from ..gui.const import DEF_MAP_SIZE
from ..grid import Grid
from .tiles import Tile, BIOMES


class Map:
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
    # class slots: http://book.pythontips.com/en/latest/__slots__magic.html
    __slots__ = ['tileset', 'images', 'map_key', 'size', 'cols', 'rows', 'map',
                 'display_map', 'frame_size', 'frame', 'border',
                 'cur_pos', 'cur_tile']

    IMAGES_FILEPATH = os.path.join(os.path.dirname(__file__), 'images')


    def __init__(self, map_name, tileset=BIOMES, pos=(19,18)):
        self.tileset = tileset
        self.map_key = self.get_map_key(tileset=self.tileset)
        self.cols, self.rows = self.size = (0, 0)

        # create map array from image file
        self.load_map(map_name)
        self.border = self.get_border_tile()

        # set current position and Tile
        self.cur_pos = pos
        self.cur_tile = self.get_tile(self.cur_pos)

        # create initial map frame
        self.frame_size = DEF_MAP_SIZE
        self.set_map_frame(self.frame_size)


    def get_map_key(self, tileset=BIOMES):
        """ Builds color : tile map key

        Keyword Arguments:
            tileset {dict} -- dictionary of info about tiles (default: {BIOMES})
        """
        return {Tile.get_rgb_color(values['color']):key \
                for key, values in tileset.items()}


    def load_map(self, map_name):
        """ Loads an image file and parses it into a map

        Arguments:
            filename {[type]} -- [description]

        Returns:
            [list] -- 'map' array, list of lists containing 'Tile' objects
        """
        filename = os.path.join(self.IMAGES_FILEPATH, f'{map_name}.png')
        image = Image.open(filename)

        # update map size based on loaded image
        self.cols, self.rows = self.size = image.size

        # generate color key used to parse map image into a 2D array of tile dicts
        map_key = self.get_map_key()

        # collect image data as a list of rgb pixel values
        pixels = [x for x in list(image.getdata())]

        # loop through list of pixels and convert them to appropriate tile
        # based on the tileset
        tiles = []
        for rgb in pixels:
            if rgb not in self.map_key:
                print(f'{rgb} not in map key!')
                tiles.append(None)
            else:
                key = self.map_key[rgb]
                tiles.append(Tile(name=key, **self.tileset[key]))

        # converts list of tiles into 'map' array (2D list of lists)
        self.map = [tiles[i:(i + self.cols)] \
                for i in range(0, len(tiles), self.cols)]

        # replace symbols on 'path' tiles to make connect paths
        self.connect_path_tiles()


    def get_border_tile(self, tile_name='ocean'):
        """ Create a tile to be used for the border

        Border tiles are used for out-of-range indexes when generating a new
        map frame.

        Keyword Arguments:
            tile_name {str} -- key name of the border Tile to use

        TODO:
            This is hardcoded to use 'ocean' right now, but we might want to
            add a keyword to a tileset dictionary to identify the 'border'
            tile for each tileset
        """
        return Tile(name=tile_name, **self.tileset[tile_name])


    def get_tile(self, pos):
        """ Gets the tile at the given pos in the map array

        Arguments:
            pos {tuple} -- (col,row) position in the map array

        Returns:
            [type] -- [description]
        """
        col, row = pos
        try:
            return self.map[row][col]
        except IndexError:
            return self.border


    def get_neighbors(self, pos):
        """ Gets neighboring tiles at given position in map array

        Arguments:
            pos {tuple} -- (col,row) position in the map array

        Returns:
            tuple -- tiles above, right, below, and left of the given pos
        """
        col, row = pos
        t = self.get_tile((col, row - 1))
        r = self.get_tile((col + 1, row))
        b = self.get_tile((col, row + 1))
        l = self.get_tile((col - 1, row))

        return t, r, b, l


    def get_path_symbol(self, pos):
        """[summary]

        Arguments:
            pos {tuple} -- (col,row) position in the map array

        Notes:
            This method uses binary values to determine which symbol should be
            used to draw a path tile so that it connects to all of it's
            neighboring 'path' tiles

        TODO:
            the tile name 'path' could be passed in as an arguement
            char_map could be passed in as an arguement for different symbols

        Returns:
            [str] -- symbol to use for the path tile at the given position
        """
        char_map = {0:'═', 1:'║', 2:'║', 3:'║', 4:'═', 5:'╝', 6:'╗' ,7:'╣', 8:'═',
                9:'╚', 10:'╔', 11:'╠', 12:'═', 13:'╩', 14:'╦', 15:'╬'}

        t, r, b, l = self.get_neighbors(pos)
        key = 0
        if t is not None and t.name == 'path':
            key += 1
        if b is not None and b.name == 'path':
            key += 2
        if l is not None and l.name == 'path':
            key += 4
        if r is not None and r.name == 'path':
            key += 8

        return char_map[key]


    def connect_path_tiles(self):
        """ Connect 'path' tiles with appropriate symbol

        Loop through each column in each row of the map array and get the
        Tile object.  If the tile's name is 'path', then get a new symbol
        for that tile at that position that connects it to neighboring path
        tiles
        """
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                tile = self.map[row][col]
                if tile.name == 'path':
                    pos = (col,row)
                    symbol = self.get_path_symbol(pos)
                    tile.set_symbol(symbol)


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

        self.frame = [[self.get_tile((col,row)) for col in range(start_col, (start_col + cols))] for row in range(start_row, (start_row + rows))]


    def get_map(self, as_string=True, raw=False):
        """ Gets the map as a string

        Keyword Arguments:
            as_string {bool}    -- If True, output unformatted map Tile symbols
                                   instead of formatted char (default: {False})
            raw {bool}          -- If True, output unformatted map Tile symbols
                                   instead of formatted char (default: {False})
        """
        if as_string:
            return self.array_to_string(self.map, raw=raw)
        elif raw:
            return [[tile.alpha for tile in row] for row in self.map]
        else:
            return [[tile.char for tile in row] for row in self.map]


    def get_map_frame(self, as_string=True, raw=False):
        """ Gets the framed map window as a string

        Keyword Arguments:
            as_string {bool}    -- If True, output unformatted map Tile symbols
                                   instead of formatted char (default: {False})
            raw {bool}          -- If True, output unformatted map Tile symbols
                                   instead of formatted char (default: {False})
        """
        if as_string:
            return self.array_to_string(self.frame, raw=raw)
        elif raw:
            return [[tile.alpha for tile in row] for row in self.frame]
        else:
            return [[tile.char for tile in row] for row in self.frame]


    @staticmethod
    def add_pos(pos1, pos2):
        """ adds (col,row) positions together
        
        Arguments:
            pos1 {tuple} -- tuple of (col,row) position in map
            pos2 {tuple} -- tuple of (col,row) position in map

        TODO:
            Move this over into Grid class
            Might consider using a vetor data class to work with position values
        """
        
        return tuple(sum(x) for x in zip(pos1, pos2))


    def move(self, dir=(0,0)):
        """ Changes current position on Map
        
        Keyword Arguments:
            dir {tuple} -- (col,row) value to change current position by. (Default is (0,0))
        
        Returns:
            tuple -- Current (col,row) position on Map
        """
        next_pos = Map.add_pos(self.cur_pos, dir)
        next_tile = self.get_tile(next_pos)

        if next_tile.movement > 0:
            self.cur_pos = next_pos
            # self.update_map()
            sleep(abs(next_tile.movement) * 0.0625)    # pause to give screen time to redraw

        return self.cur_pos


    def show(self, clear=False, frame=False, raw=False):
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
            stdout.write(self.get_map_frame(raw=raw))
        else:
            stdout.write(self.get_map(raw=raw))
        stdout.flush()


    def __repr__(self):
        """ returns explicit representation of self.map data """
        return self.map


    def array_to_string(self, array, raw=False):
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
        if raw:
            rows = [''.join([tile.alpha for tile in row]) for row in array]
        else:
            rows = [''.join([tile.char for tile in row]) for row in array]

        return '\n'.join(rows)


    def __str__(self):
        """ returns printable string version of self.map data """
        return self.array_to_string(self.map, raw=True)
