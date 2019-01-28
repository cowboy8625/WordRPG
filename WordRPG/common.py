""" module for custom container classes """
from collections import namedtuple


# Not sure if this setup is pythonic, but it seems to work
class Point(namedtuple('Point', ['col', 'row'])):
    """ Class for working with a tuple that represents a (col, row) location of
    a cell in a Table object or 2D array
    
    Attributes:
        col
        row
    """

    def __add__(self, point):
        return Point(self.col + point.col, self.row + point.row)


    def __sub__(self, point):
        return Point(self.col - point.col, self.row - point.row)


    def __mul__(self, point):
        return Point(self.col * point.col, self.row * point.row)


    def __iter__(self):
        yield from [self.col, self.row]
  

    def __repr__(self):
        return f'Point({self.col}, {self.row})'


    def __str__(self):
        return f'({self.col}, {self.row})'



class Table:
    """ Class for storing and working with data in a two-dimensional array
    
    Arguements:
        arg {str} -- multi-line string where each line becomes a row and each
                     character becomes a column in that row
        - or -
        arg {list[lists]} -- 2d array (list of lists)
    """
    __slots__ = ['cells']

    def __init__(self, arg):
        if isinstance(arg, str):
            self.cells = Table.from_string(arg)
        elif isinstance(arg, list):
            self.cells = arg


    @staticmethod
    def from_string(string):
        """ Convert a mutli-line string to Table.cells

        Arguments:
            string {str} -- Multi-line string block
        """
        return [list(col) for col in string.splitlines()]


    # @staticmethod
    # def from_list(arg, rows):
    #     """ Creates a new 2D list of lists """
    #     return [[col for col in row] for row in rows]


    # @staticmethod
    # def from_grid(arg):
    #     """ Creates a new Table from 2D list of lists """
    #     return arg.cells


    def to_string(self, attr=None):
        """ Convert Table.cells to multi-line string

        Keyword Arguments:
            attr {str} -- name of attribute to try and get from each element.

        Returns:
            str -- Table as a string
        """
        if isinstance(attr, str):
            rows = [''.join([getattr(col, attr, col) for col in row])
                    for row in self.cells]
        else:
            rows = [''.join([str(col) for col in row]) for row in self.cells]
        return '\n'.join(rows)


    def get_width(self):
        """ Returns the width of the widest row in Table.cells

        Returns:
            int -- number of cells in the widest row
        """
        return max([len(line) for line in self.cells])


    def get(self, pos, default=None):
        """ Gets cell from given (col, row) in Table.cells

        Arguments:
            pos {tuple} -- (col,row) in Table.cells

        Keyword Arguments:
            default -- default element to use in case of IndexError

        Returns:
            return the value of the Table.cell at the given position
        """
        col, row = pos
        try:
            return self.cells[row][col]
        except IndexError:
            return default


    def set(self, pos, arg ):
        """ Replaces cell at given (col, row) in Table.cells

        Arguments:
            pos {tuple} -- (col,row) position in Table.cells

        Returns:
            returns the arg if successful, None otherwise
        """
        col, row = pos
        try:
            self[col][row] = arg
            return arg
        except IndexError:
            return None


    def get_sub(self, size, start, default=None):
        """ Gets a sub-set of the Table.cells

        Arguments:
            size {tuple} -- number of (cols, rows) to get from Table.cells
            start {tuple} -- starting (cols, rows) of the Table

        Keyword Arguments:
            default -- default cell to use in case of IndexError
        """
        cols, rows = size
        start_col, start_row = start
        return [[self.get((col,row), default=default)
                 for col in range(start_col, (start_col + cols))]
                for row in range(start_row, (start_row + rows))]


    def get_neighbors(self, pos, default=None):
        """ Gets neighboring cells at given position in Table.cells

        Arguments:
            pos {tuple} -- (col,row) position of cell in Table.cells

        Keyword Arguments:
            default -- default value to use in case of IndexError

        Returns:
            tuple -- cells to the top, right, bottom, and left of pos
        """
        col, row = pos
        t = self.get((col, row - 1), default=default)
        r = self.get((col + 1, row), default=default)
        b = self.get((col, row + 1), default=default)
        l = self.get((col - 1, row), default=default)
        return t, r, b, l


    def __len__(self):
        return len(self.cells)


    def __repr__(self):
        """ returns representation of Table """
        # abandon all hope ye who enter here
        cells = ',\n'.join(
                [f"     [{','.join([', '.join([str(col) for col in row])])}]"
                for row in self.cells])
        return f'Table(\n{cells}\n    )\n'


    def __str__(self):
        """ returns printable string version of Table """
        return self.to_string()


    def __getitem__(self, index):
        return self.cells[index]


    def __setitem__(self, index, value):
        self.cells[index] = value


    def __delitem__(self, index):
        pass
