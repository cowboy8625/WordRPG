""" common module for working with Arrays (2D list of lists) """

class Grid:
    __slots__ = ['cells']

    def __init__(self, arg):
        if isinstance(arg, str):
            self.cells = Grid.from_string(arg)
        elif isinstance(arg, list):
            self.cells = Grid.from_list(arg)
        elif isinstance(arg, tuple):
            cols, rows = arg
            self.cells = [[None for col in range(cols)] for row in range(rows)]


    @staticmethod
    def from_string(string):
        """ Convert a mutli-line string to Grid.cells

        Arguments:
            string {str} -- Multi-line string block
        """
        return [list(col) for col in string.splitlines()]


    @staticmethod
    def from_list(arg):
        return [[col for col in row] for row in arg]


    def to_string(self, attr=None):
        """ Convert Grid.cells to multi-line string

        Keyword Arguments:
            attr {str} -- name of attribute to try and get from each element.

        Returns:
            str -- Grid as a string
        """
        if isinstance(attr, str):
            rows = [''.join([getattr(col, attr, col) for col in row])
                    for row in self.cells]
        else:
            rows = [''.join([col for col in row]) for row in self.cells]
        return '\n'.join(rows)


    def get_width(self):
        """ Returns the width of the widest row in Grid.cells

        Returns:
            int -- number of cells in the widest row
        """
        return max([len(line) for line in self.cells])


    def get(self, pos, default=None):
        """ Gets cell from given (col, row) in Grid.cells

        Arguments:
            pos {tuple} -- (col,row) in Grid.cells

        Keyword Arguments:
            default -- default element to use in case of IndexError

        Returns:
            return the value of the Grid.cell at the given position
        """
        col, row = pos
        try:
            return self.cells[row][col]
        except IndexError:
            return default


    def set(self, arg, pos):
        """ Replaces cell at given (col, row) in Grid.cells

        Arguments:
            pos {tuple} -- (col,row) position in Grid.cells

        Returns:
            returns the arg if successful, None otherwise
        """
        col, row = pos
        try:
            self.cells[row][col] = arg
            return arg
        except IndexError:
            return None


    def get_sub(self, size, start, default=None):
        """ Gets a sub-set of the Grid.cells

        Arguments:
            size {tuple} -- number of (cols, rows) to get from Grid.cells
            start {tuple} -- starting (cols, rows) of the Grid

        Keyword Arguments:
            default -- default cell to use in case of IndexError
        """
        cols, rows = size
        start_col, start_row = start
        return [[self.get((col,row), default=default)
                 for col in range(start_col, (start_col + cols))]
                for row in range(start_row, (start_row + rows))]


    def get_neighbors(self, pos, default=None):
        """ Gets neighboring cells at given position in Grid.cells

        Arguments:
            pos {tuple} -- (col,row) position of cell in Grid.cells

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


    def __repr__(self):
        """ returns representation of Grid """
        string = ''
        string.join([','.join([f'[{col}]' for col in row]) for row in self.cells])
        string = 'Grid(\n{string})'
        return string


    def __str__(self):
        """ returns printable string version of Grid """
        return self.to_string()
