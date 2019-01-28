""" Module for compositing and drawing various game screens """
import os
from sys import stdout
import codecs

from colorama import init as colorama_init

from . import const, cursor, font



# def setup_terminal(title=const.TITLE, convert_escape=True,
#                    size=const.SCREEN_SIZE, hide_cursor=True):
#     """ sets the size of the terminal window and clears it before printing"""
#     colorama_init(convert=convert_escape)
#     cols, lines = size
#     os.system(f"mode con cols={cols} lines={lines}")
#     os.system("title " + title)

#     if hide_cursor:
#         cursor.hide()



class Screen:
    """ Base class for a 'screen'

    A screen is a 2D array of blocks including a character and any escape
    characters for screen formatting

    """
    def __init__(self, size=const.SCREEN_SIZE):
        self.SCREEN_SIZE = size

        self._init_screen()


    def _init_screen(self, char=' '):
        """ creates a new screen by filling it with given character

        Keyword Arguments:
            char {str} -- String to fill screen with. (default: {'#'})
        """
        cols, rows = self.SCREEN_SIZE
        # line = f'{char}' * cols
        text = '\n'.join([f'{char * cols}' for row in range(rows)])

        # TODO: Implement Table class here
        self.screen = self._string_to_array(text)


    @staticmethod
    def setup_terminal(title=const.TITLE, convert_escape=True,
                       size=const.SCREEN_SIZE, hide_cursor=True):
        """ sets the size of the terminal window and clears it before printing"""
        colorama_init(convert=convert_escape)
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
    def _string_to_array(string):
        """ Convert string to 2D array

        Converts a multi-line string into a two-dimensional deque array of string
        characters.

        **Arguments:**
            :``string``: `str` Multi-line string block
        """
        # split text into lines/rows
        lines = string.splitlines()

        return [list(col) for col in lines]


    @staticmethod
    def array_to_string(array):
        """ Convert array to string

        Converts a two-dimensional deque array of string characters into a
        multi-line string that can be printed to the output window.

        **Arguments:**
            :``array``: `list` 2D array of characters
        """
        lines = [''.join(char) for char in array]
        return '\n'.join(lines)


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
    def _create_frame(size, frame_style=1):
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
        tl = const.FRAME['tl'][frame_style]
        tr = const.FRAME['tr'][frame_style]
        bl = const.FRAME['bl'][frame_style]
        br = const.FRAME['br'][frame_style]
        v = const.FRAME['v'][frame_style]
        h = const.FRAME['h'][frame_style]

        # assemble the final frame string
        frame_string = f'{tl}{h * (cols - 2)}{tr}\n'
        for i in range(0, (rows - 2)):
            frame_string += f'{v}{" " * (cols - 2)}{v}\n'
        frame_string += f'{bl}{h * (cols - 2)}{br}'

        return Screen._string_to_array(frame_string)


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
        filename = os.path.join(const.FILEPATH, f'{screen_name}.txt')
        text = self._load_txt(filename)
        array = self._string_to_array(text)

        if offset[0] == 'center':
            # get offset for center of screen for longest line in screen
            widest = max([len(line) for line in array])
            center = Screen.center_offset(widest, self.SCREEN_SIZE[0])
            offset = (center, offset[1])

        self.write_array_to_screen(array, offset, **format)


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
        frame = self._create_frame(size, frame_style=frame_style)
        self.write_array_to_screen(frame, offset=offset, **format)


    def add_header(self, header=const.HEADER, **format):
        """ Add header to screen

        Keyword Arguments:
            header {[type]} -- [description] (default: {const.HEADER})
            format {[type]} -- [description] (default: {const.DEF_FORMAT})
        """
        header = f' {header} '
        self.add_string_to_screen(header, offset=('center', 0), **format)


    def add_footer(self, footer=const.FOOTER, **format):
        """ Add footer to screen

        Keyword Arguments:
            footer {[type]} -- [description] (default: {const.FOOTER})
            format {[type]} -- [description] (default: {const.DEF_FORMAT})
        """
        footer = f' {footer} '
        self.add_string_to_screen(footer, offset=('center', 29), **format)


    # TODO: Utilize Table.set() class method here
    def write_char_to_screen(self, char, col=0, row=0):
        """ Writes single character to screen

        Writes a single character and escape codes to a specific [row][col] in
        the screen array

        Arguments:
            char {[type]} -- [description]
            array {[type]} -- [description]

        Keyword Arguments:
            col {int} -- [description] (default: {0})
            row {int} -- [description] (default: {0})
        """
        try:
            self.screen[row][col] = char
        except IndexError:
            err = f".write_char_to_screen( ) - IndexError \
                    Tried to assign {char} to [{col}][{row}] in a \
                    {len(self.screen)}x{len(self.screen[0])} array."
            print(err)


    def add_string_to_screen(self, string, offset=(0,0), format_char=True,
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
            self.write_char_to_screen(char, col=col + c, row=row)


    def write_array_to_screen(self, array, offset=(0,0), transparent=False,
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
            width = Screen._get_array_width(array)
            offset = (Screen.center_offset(width, self.SCREEN_SIZE[0]), offset[1])

        col, row = offset
        for r, line in enumerate(array):
            for c, char in enumerate(line):
                if char == ' ' and transparent:
                    continue
                if (char != ' ' and format_char) or format_space:
                    char = font.add_escape(char, **format)
                self.write_char_to_screen(char, col=col + c, row=row + r)


    @staticmethod
    def _get_array_width(array):
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
    def _get_menu_width(menu_dict, option_only=False):
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

        self.write_array_to_screen(array, offset=offset, format_char=False)


    def draw(self, clear_first=False):
        """ Prints current screen to the output window """
        if clear_first:
            self.clear()

        stdout.write(f"\x1b7\x1b[0;0f{self.array_to_string(self.screen)}\x1b8")
        # stdout.write(f'\r\r\r\r\r{self.array_to_string(self.screen)}')
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


