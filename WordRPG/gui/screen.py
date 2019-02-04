""" Module for compositing and drawing various game screens """
import os
from sys import stdout
import codecs

from colorama import init as colorama_init

from .. import const
from . import cursor, font
from ..common import Point, Table



class Screen(Table):
    """ Screen class. Inherets from Table

    A Screen is a 2D array of cells containing an ASCII character and any escape
    characters for color/style formatting

    """

    # characters used to build frames
    FRAME = {
        'tl'    : ['┌','╔'],
        'tr'    : ['┐','╗'],
        'bl'    : ['└','╚'],
        'br'    : ['┘','╝'],
        'v'     : ['│','║'],
        'h'     : ['─','═'],
        'vl'    : ['├','╠'],
        'vr'    : ['┤','╣'],
        'hb'    : ['┴','╩'],
        'ht'    : ['┬','╦'],
        'c'     : ['┼','╬'],
    }



    def __init__(self, size=const.SCREEN_SIZE):
        self.SCREEN_SIZE = size

        super(Screen, self).__init__(self._init_screen())
        self.screen = self.cells

    def _init_screen(self, char=' '):
        """ creates a new screen by filling it with given character

        Keyword Arguments:
            char {str} -- String to fill screen with. (default: {'#'})
        """
        cols, rows = self.SCREEN_SIZE
        # line = f'{char}' * cols
        text = '\n'.join([f'{char * cols}' for row in range(rows)])

        return Screen.from_string(text)


    @staticmethod
    def setup_terminal(title=const.TITLE, convert_escape=True,
                       size=const.SCREEN_SIZE, hide_cursor=True):
        """ sets the size of the terminal window and clears it before printing"""
        colorama_init()     #autoreset=True
        cols, lines = size
        os.system(f"mode con cols={cols} lines={lines}")
        os.system("title " + title)

        if hide_cursor:
            cursor.hide()


    @staticmethod
    def clear():
        """ clear terminal window """
        os.system('cls' if os.name == 'nt' else 'clear')


    @staticmethod
    def make_unicode(text):
        """ Ensures that text is encoded as unicode """
        return text.encode( encoding="utf-8")


    @staticmethod
    def center_string(string, width, fillchar=' '):
        """ Centers string in field of given width

        Centers the given text string in the given 'width' and fills empty space
        with the supplied 'fillchar'. This modifies the original string object.

        Arguments:
            string {str} -- Text to be centered
            width {int} -- Width of the text field to center within

        Keyword Arguments:
            fillchar {str} -- String character to fill empty space (default: {' '})

        Returns:
            str -- New centered and space-filled string
        """
        return string.center(width, fillchar)


    @staticmethod
    def center_offset(text, width):
        """ Get offset to center text

        Gets the offset needed to center the given 'text' string within the
        given 'width' of the field. Unlike '.center_string()' this does not
        'text string.

        Arguments:
            text {str} -- string to center
            width {int} -- widgth of the field in characters

        Returns:
            int -- column offset as an int
        """
        if isinstance(text,int):
            return int((width - text) / 2)

        return int((width - len(text)) / 2)


    @staticmethod
    def create_frame(size, frame_style=1):
        """ Creates a frame

        Arguments:
            cols {[type]} -- [description]
            rows {[type]} -- [description]

        Keyword Arguments:
            style {int} -- [description] (default: {1})

        Returns:
            string -- [description]
        """
        cols, rows = size

        # get frame characters based on style
        tl = Screen.FRAME['tl'][frame_style]
        tr = Screen.FRAME['tr'][frame_style]
        bl = Screen.FRAME['bl'][frame_style]
        br = Screen.FRAME['br'][frame_style]
        v = Screen.FRAME['v'][frame_style]
        h = Screen.FRAME['h'][frame_style]

        # assemble the final frame string
        frame_string = f'{tl}{h * (cols - 2)}{tr}\n'
        for i in range(0, (rows - 2)):
            frame_string += f'{v}{" " * (cols - 2)}{v}\n'
        frame_string += f'{bl}{h * (cols - 2)}{br}'

        return Screen.from_string(frame_string)


    @staticmethod
    def _load_txt(filename, codec='utf-8'):
        """ Load .txt file as the 'screen'

        Reads in contets of a .txt file into a variable

        Arguments:
            filename {[type]} -- [description]

        Keyword Arguments:
            codec {str} -- [description] (default: {'utf-8'})

        Returns:
            [type] -- [description]
        """
        with codecs.open(filename, encoding=codec) as f:
            return f.read()


    # TODO: Utilize Table.from_string() class method here
    def load_screen(self, screen_name, offset=(0,0), **format):
        """ Loads a text file into the screen

        Arguments:
            filename {str} -- name of a .txt file to load as a screen

        Keyword Arguments:
            offset {tuple} -- Offset for the .txt file (default: {(0,0)})
        """
        filename = os.path.join(const.PATH_SCREENS, f'{screen_name}.txt')
        text = self._load_txt(filename)
        array = Screen.from_string(text)

        if offset[0] == 'center':
            # get offset for center of screen for longest line in screen
            widest = max([len(line) for line in array])
            center = Screen.center_offset(widest, self.SCREEN_SIZE[0])
            offset = (center, offset[1])

        self.write_array(array, offset, **format)


    def add_frame(self, size=const.SCREEN_SIZE, offset=(0,0),
                  frame_style=1, **format):
        """ Adds a frame to the screen

        Creates a frame of the given size, style, and format keywords and then
        adds it to the screen array at the given offset col, row

        Arguments:
            size {[type]} -- [description]
            offset {[type]} -- [description]

        Keyword Arguments:
            style {int} -- [description] (default: {1})
        """
        frame = self.create_frame(size, frame_style=frame_style)
        self.write_array(frame, offset=offset, **format)


    def add_header(self, header=const.HEADER, **format):
        """ Add header to screen

        Keyword Arguments:
            header {[type]} -- [description] (default: {const.HEADER})
            format {[type]} -- [description] (default: {const.DEF_FONT})
        """
        header = f' {header} '
        self.write_string(header, offset=('center', 0), **format)


    def add_footer(self, footer=const.FOOTER, **format):
        """ Add footer to screen

        Keyword Arguments:
            footer {[type]} -- [description] (default: {const.FOOTER})
            format {[type]} -- [description] (default: {const.DEF_FONT})
        """
        footer = f' {footer} '
        self.write_string(footer, offset=('center', 29), **format)


    def write_string(self, string, offset=(0,0), format_char=True,
                             format_space=False, transparent=False, **format ):
        """ Writes a string to the screen

        Arguments:
            string {[type]} -- [description]

        Keyword Arguments:
            col {int}           -- [description] (default: {0})
            row {int}           -- [description] (default: {0})
            format_char {bool}  -- If True, add escape characters to all
                                   characters. (default: {False})
            format_space {bool} -- [description] (default: {False})
            transparent {bool}  -- [description] (default: {False})
        """
        if offset[0] == 'center':
            center = Screen.center_offset(string, self.SCREEN_SIZE[0])
            offset = (center, offset[1])

        for c, char in enumerate(string):
            if char == '\t':
                continue
            if char == ' ' and transparent:
                continue
            if (char != ' ' and format_char) or format_space:
                char = font.add_escape(char, **format)

            col, row = offset
            # self.write_char_to_screen(char, col=col + c, row=row)

            # TODO: col, row backwards in offset
            self.set(Point(row, col + c), char)


    def write_array(self, array, offset=(0,0), transparent=False,
                              format_char=True, format_space=False, **format ):
        """ Writes an array to the screen

        Arguments:
            array {list} -- 2D array of characters

        Keyword Arguments:
            col {int} -- [description] (default: {0})
            row {int} -- [description] (default: {0})
            format_char {bool} -- If True, add escape characters to all
                                    characters. (default: {False})
            format_space {bool} -- [description] (default: {False})
            transparent {bool} -- [description] (default: {False})
        """
        # if 'center' is passed in as col offset, then figure out what the
        # correct offset value is based on widest line in the given array
        if offset[0] == 'center':
            width = Screen.get_array_width(array)
            offset = (Screen.center_offset(width, self.SCREEN_SIZE[0]),
                                           offset[1])

        col, row = offset
        for r, line in enumerate(array):
            for c, char in enumerate(line):
                if char == ' ' and transparent:
                    continue
                if (char != ' ' and format_char) or format_space:
                    char = font.add_escape(char, **format)

                self.set(Point(row + r, col + c), char)


    @staticmethod
    def get_array_width(array):
        """ Returns the width of the widest line in the given array

        This is a convenience function that can be used to center an array

        Arguments:
            array {array} -- 2D List of lists

        Returns:
            int -- Length of the longest option string
        """
        return max([len(line) for line in array])


    #TODO: Utlize Table.get_width() method here
    @staticmethod
    def get_menu_width(menu_dict, option_only=False):
        """ Returns the width of the widest option in given menu dictionary

        This is a convenience function that can be used to center a block of
        menu options based on the longest one.

        Arguments:
            menu {dict} -- Menu information as a dictionary

        Keyword Arguments:
            option_only {bool} -- If True, only return width of widest option
                                string. Otherwise, include the encapsulators
                                and seperator characters in the total width

        Returns:
            int -- Length of the longest option string
        """
        widest = max([len(text) for text, hotkey in menu_dict['options']])

        if option_only:
            return widest
        else:
            return widest + len(menu_dict['encap']) + len(menu_dict['sep'])


    def add_menu(self, menu_dict, offset=(0,0), to_upper=True):
        """ Creates a new screen array from supplied menu dictionary

        Arguments:
            menu_dict {dict} -- Dictionary for new menu

        Keyword Arguments:
            to_upper {bool} -- If True, convert all text to upper-case. (default: {True})

        Returns:
            array -- Returns 2D array of formatted characters
        """
        array = []

        # convert text to upper case
        for text, hotkey in menu_dict['options']:
            line = []

            if to_upper:
                text, hotkey = text.upper(), hotkey.upper()

            # add formatted hotkey and ecacpsulators to array
            hotkey = f"{menu_dict['encap'][0]}{hotkey}{menu_dict['encap'][1]}"
            for char in hotkey:
                char = font.add_escape(char, **menu_dict['hotkey_format'])
                line.append(char)

            # add formatted seperator and option text
            text = f"{menu_dict['sep']}{text}"
            for char in text:
                char = font.add_escape(char, **menu_dict['text_format'])
                line.append(char)

            array.append(line)

        self.write_array(array, offset=offset, format_char=False)


    @staticmethod
    def write(string, pos=Point(0,0)):
        """ writes a string to the terminal at given pos """
        for i, line in enumerate(string.splitlines()):
            stdout.write(f"\u001b[{pos.row + i};{pos.col}H{line}")
            stdout.flush()


    def draw(self, as_string=False , clear_first=False):
        """ Prints current screen to the output window """
        if clear_first:
            self.clear()

        stdout.write(f"\u001b[0;0H{self.to_string()}")
        stdout.flush()


    def copy(self):
        """ Prints current screen to the output window """
        return self.screen



##------------------------------------------------------------------------------
## Screens created here
##------------------------------------------------------------------------------

# def story_test():
#     """ tests compositing screens and adding text at a centered offset
#     using string formatters and parameters """

#     # draw the background and frame
#     screen = _create_background(
#                     background='scroll',
#                     fgcolor='YELLOW', bgcolor='BLACK')

#     # draw screen title
#     title = 'CHAPTER ONE'
#     c = main.center_offset(title, const.SCREEN_SIZE[0])
#     main.write_to_array(
#             title, screen, col=c, row=2, fgcolor='CYAN', style="BRIGHT")

#     # draw story text
#     story = const.SCREENS['story_test']['array']
#     main.write_to_array(story, screen, col=6, row=6, fgcolor='WHITE')

#     # print the screen
#     main.draw(screen)


