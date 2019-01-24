from sys import stdout
from copy import deepcopy

from PIL import ImageColor, Image, ImageOps

from ..gui.const import DEF_MAP_SIZE
from ..gui.screen import Screen
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
    __slots__ = ['tileset', 'map_key', 'size', 'cols', 'rows', 'map',
                 'display_map', 'frame_size', 'frame', 'border']



    def __init__(self, filename, tileset=BIOMES):
        self.tileset = tileset
        self.map_key = self.get_map_key(tileset=self.tileset)
        self.cols, self.rows = self.size = (0, 0)

        # create map array from image file
        self.load_map(filename)
        self.border = self.get_border_tile()

        # create map frame
        self.frame_size = DEF_MAP_SIZE
        self.set_map_frame(self.frame_size)



    def get_map_key(self, tileset=BIOMES):
        """ Builds color : tile map key

        Keyword Arguments:
            tileset {[type]} -- [description] (default: {BIOMES})
        """

        return {Tile.get_rgb_color(values['color']):key \
                for key, values in tileset.items()}


    def load_map(self, filename):
        """ Loads an image file and parses it into a map

        Arguments:
            filename {[type]} -- [description]

        Returns:
            [list] -- 'map' array, list of lists containing 'Tile' objects
        """

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


    def set_map_frame(self, size, offset=(0,0), raw=False):
        """ Gets a framed portion of the map array

        Gets a framed portion of the whole map array so it can be displayed in
        in a frame on one of the game screens.

        For tiles outside of the range of the map array we use a virtual
        'border' Tile to fill in those empy spaces

        Arguments:
            size {tuple} -- number of (cols, rows) of the map to return
            offset {tuple} -- starting (cols, rows) of the segment
        """

        cols, rows = self.frame_size = size
        start_col, start_row = offset

        # map_frame = []
        # for row in range(start_row, (start_row + rows)):
        #     line = [self.get_tile((col,row)) \
        #             for col in range(start_col, (start_col + cols))]

        #     map_frame.append(line)
        # self.frame = map_frame

        self.frame = [[self.get_tile((col,row)) for col in range(start_col, (start_col + cols))] for row in range(start_row, (start_row + rows))]

        # if raw:
        #     rows = [''.join([self.get_tile((col,row))
        #             for col in range(start_col, (start_col + cols))]) for row in range(start_row, (start_row + rows))]
        # else:
        #     rows = [''.join([tile.char for tile in range(start_col, (start_col + cols))]) for row in range(start_row, (start_row + rows))]
        # map_frame = '\n'.join(rows)



    def show(self, frame=False, clear_first=False, raw=False):
        """ Prints the map array to terminal """

        if clear_first:
            Screen.clear()
        if frame:
            return stdout.write(self.array_to_string(self.frame, raw=raw))
        else:
            return stdout.write(self.array_to_string(self.map, raw=raw))


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
