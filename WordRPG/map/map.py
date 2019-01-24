from sys import stdout
from copy import deepcopy

from PIL import ImageColor, Image, ImageOps

from ..gui.const import DEF_MAP_SIZE
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

    # define class slots to improve memory effeciency
    # http://book.pythontips.com/en/latest/__slots__magic.html
    __slots__ = ['tileset', 'map_key', 'size', 'cols', 'rows', 'map', 'display_map', 'frame', 'border']



    def __init__(self, filename, tileset=BIOMES):
        self.tileset = tileset
        self.map_key = self.get_map_key(tileset=self.tileset)
        self.cols, self.rows = self.size = (0, 0)

        # create map array from image file
        self.map = self._load_map(filename)

        # create display map with coloroma formatting
        self.display_map = self._get_display_map()

        # create map window
        self.border = self.get_border_tile()
        #self.frame = self.get_map_frame(self.size)



    def get_map_key(self, tileset=BIOMES):
        """ Builds color : tile map key

        Keyword Arguments:
            tileset {[type]} -- [description] (default: {BIOMES})
        """
                
        return {Tile.get_rgb_color(values['color']):key \
                for key, values in tileset.items()}


    def _load_map(self, filename):
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
        return [tiles[i:(i + self.cols)] \
                for i in range(0, len(tiles), self.cols)]


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


    def _get_tile(self, pos):
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
            return None


    def _get_neighbors(self, pos):
        """ Gets neighboring tiles at given position in map array
        
        Arguments:
            pos {tuple} -- (col,row) position in the map array
        
        Returns:
            tuple -- tiles above, right, below, and left of the given pos
        """

        col, row = pos
        t = self._get_tile((col, row - 1))
        r = self._get_tile((col + 1, row))
        b = self._get_tile((col, row + 1))
        l = self._get_tile((col - 1, row))

        return t, r, b, l


    def _get_path_symbol(self, pos):
        """[summary]
        
        Arguments:
            pos {tuple} -- (col,row) position in the map array
        
        Returns:
            [str] -- Symbol to use for the path tile at the given position
        """

        # this uses pseudo binary values to determine which symbol should be
        # used to draw a 'path' tile so that it connects to all neighboring
        # 'path' tiles
        char = {0:'═', 1:'║', 2:'║', 3:'║', 4:'═', 5:'╝', 6:'╗' ,7:'╣', 8:'═',
                9:'╚', 10:'╔', 11:'╠', 12:'═', 13:'╩', 14:'╦', 15:'╬'}

        t, r, b, l = self._get_neighbors(pos)
        key = 0
        if t is not None and t.name == 'path':
            key += 1
        if b is not None and b.name == 'path':
            key += 2
        if l is not None and l.name == 'path':
            key += 4
        if r is not None and r.name == 'path':
            key += 8
        
        return char[key]


    def _connect_path_tiles(self):
        """ Connect 'path' tiles with appropriate symbol """

        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                tile = self.map[row][col]
                if tile.name == 'path':
                    tile.symbol = self._get_path_symbol((col,row))
                    tile.char = tile._get_formatted_char()


    def get_map_frame(self, size, offset=(0,0)):
        """ Gets a portion of the map array

        Gets a portion of the map array so it can be displayed in the game window

        Arguments:
            map_array {list} -- 2D list of lists that holds tile data for map
            size {tuple} -- number of (rows, cols) of the map to return
            offset {tuple} -- starting (row,col) of the segment
        """

        start_col, start_row,  = offset
        cols, rows = size

        map_slice = []
        for row in range(start_row, start_row + rows):
            line = []
            for col in range(start_col, start_col + cols):
                try:
                    tile = self.map[row][col]
                except IndexError:
                    tile = self.border
                line.append(tile)
            map_slice.append(line)

        return map_slice


    def _get_display_map(self, _map=None, discovered=False):
        """ Creates the formatted map for display

        Keywords:
            _map {list} -- 'map' array to display
            discovered {bool} -- If True, only show formatted character for
                                 tiles that have been 'discovered'.
                                 Default is False.

        """

        if _map is None:
            _map = self.map

        self._connect_path_tiles()

        # Go through each row in self.map array and get all of the Tile.char
        # properties (formatted symbol). If the tile has a value of None or the
        # Tile.discovered property is False then the tile is written as an
        # empty space.
        # Then join all of the rows into a single string which can be written
        # to the terminal output
        rows = [''.join(\
                        [tile.char if tile is not None and \
                        ( not discovered or tile.discovered) \
                        else ' ' for tile in row] ) \
                        for row in _map]
        return '\n'.join(rows)


    def show(self, _map=None, discovered=False):
        """ Prints the map array to terminal """

        if _map is None:
            _map = self.map

        map_string = self._get_display_map(_map=_map, discovered=discovered)
        return stdout.write(map_string)


    def __repr__(self):
        """ returns explicit representation of self.map data """
        return self.map


    def _map_to_string(self, _map):
        """ Converts 'map' array to string of tile symbols
        
        Arguments:
            _map {list} -- 'map' array
        
        Note:
            This was broken out into a seperate function from __str__ so that
            it can be used to print map slices from .get_map_frame as well as
            the full self.map

        Returns:
            [str] -- string of tile symbols
        """

        rows = [''.join([tile.symbol for tile in row]) for row in _map]
        return '\n'.join(rows)


    def __str__(self):
        """ returns printable string version of self.map data """

        # Go through each row in self.map array and get all of the Tile.symbol
        # characters.
        # Then join all of the rows into a single string which can be printed
        self._map_to_string(self.map)
