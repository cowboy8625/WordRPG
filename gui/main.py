""" Main functions for gui-related tasks """
import os
from sys import stdout
import codecs
from collections import deque
import logging

# import textwrap
from colorama import init as colorama_init

# imports from gui module
from . import const
from . import font
from . import cursor



## logging setup
logging.basicConfig(
        filename=r'E:\Python\WordRPG\gui\gui_error.log',
        format='%(levelname)s - %(message)s',
        level=logging.INFO,
        )
logging.debug('debug logging:')



def setup_terminal():
    """ sets the size of the terminal window and clears it before printing"""
    colorama_init( convert = True )
    cols, lines = const.SCREEN_SIZE
    os.system(f"mode con cols={cols} lines={lines}")

    cursor.hide()


def clear():
    """ clear terminal window """
    os.system('cls' if os.name == 'nt' else 'clear')


def make_unicode(text):
    """ Ensures that text is encoded as unicode for error-logging """
    # if type(text) != unicode:
    #     return text.decode('utf-8')
    # else:
    return text.encode( encoding="utf-8")


def draw(screen):
    """ Prints to the output window

    Prints the given 'screen' to the output window.

    **Arguments:**
        :``screen``: `str` Multi-line string to print.
     """
    clear()
    # strdout.write seems to be much faster than print()
    stdout.write(screen)
    #print(screen)


def load_txt(filename, codec = 'utf-8'):
    """ Load .txt file

    Reads in contets of a .txt file into a variable

    Arguments:
        filename {[type]} -- [description]

    Keyword Arguments:
        codec {str} -- [description] (default: {'utf-8'})

    Returns:
        [type] -- [description]
    """

    with codecs.open(filename, encoding = codec)as f:
        return f.read()


def string_to_char_array(_string):
    """ Convert string to 2D array

    Converts a multi-line string into a two-dimensional deque array of string
    characters.

    **Arguments:**

        :``_string``: `str` Multi-line string block

    **Keword Arguments:**

        :``seperator``: `str` Character to split _string by. Default is newline ('\n')
        :``ignore_first``: `bool` If True, ignore the first line of _string.
        :``ignore_last``: `bool` If True, ignore the last line of _string.
    """

    # split text into lines/rows
    _rows = _string.splitlines()

    return [list(col) for col in _rows]


def char_array_to_string(_array ):
    """ Convert array to string

    Converts a two-dimensional deque array of string characters into a
    multi-line string that can be printed to the output window.

    **Arguments:**
        :``_array``: `list` 2D array of characters

    **Keword Arguments:**
        None
    """

    lines = [''.join(char) for char in _array]
    return '\n'.join(lines)


def center_text(text, width, fillchar = ' '):
    """ Centers text

    Centers the given text string in the given 'width' and fills empty space
    with the supplied 'fillchar'. This modifies the original string object.

    Arguments:
        text {str} -- Text to be centered
        width {int} -- Width of the text field to center within

    Keyword Arguments:
        fillchar {str} -- String character to fill empty space (default: {' '})

    Returns:
        str -- New centered and space-filled string
    """

    return text.center( width, fillchar )


def center_offset(text, width):
    """ Get offset to center text

    Gets the offset needed to center the given 'text' string within the given
    'width' of the field. Unlike '.center_text()' this does not modify the
    'text string.

    Arguments:
        text {str} -- string to center
        width {int} -- widgth of the field in characters

    Returns:
        int -- column offset as an int
    """

    return int((width - len(text)) / 2)


def write_character(char,array,col=0,row=0):
    """ write character to a specific [row][col] in the array """
    try:
        array[row][col] = char
    except IndexError:
        err = f".write_character( ) - IndexError \
                Tried to assign {char} to [{col}][{row}] in a \
                {len(array)}x{len(array[0])} array."
        logging.warning(err)


def write_to_array(text, array, col=0, row=0,
                    format_space=False, #format_text=const.FORMAT_TEXT,
                    fgcolor = None, bgcolor = None, style = None, ):
    """ Writes a string to an array

    Arguments:
        text {str} -- string to wrie to the array
        array {deque} -- 2D array of string characters to write to
        col {int} -- column to offset start of arr1

    Keyword Arguments:
        row {int} -- row to offset start of arr1 (default: {0})
    """
    
    kwargs = {'fgcolor':fgcolor, 'bgcolor':bgcolor, 'style':style}

    # writing a string to an array
    if isinstance(text, str):
        logging.info('Writing string to screen_buffer...')

        for c, char in enumerate(text):
            if char != ' ' or format_space:
                char = font.add_escape(char, **kwargs)
            info = f'"{char}" @ col:{col + c}, row:{row}'
            logging.info(make_unicode(info))
            write_character(char, array, col = col + c, row = row)
        return array

    # writing an array to an array
    if isinstance(text, deque) or isinstance(text, list):
        logging.info('Writing array to screen_buffer...')
        for r, line in enumerate(text):
            info = f'{line}'
            logging.info(make_unicode(info))

            for c, char in enumerate(line):
                if char != ' ' or format_space:
                    char = font.add_escape(char, **kwargs)
                info = f'"{char}" @ col:{col + c}, row:{row + r}'
                logging.info(make_unicode(info))
                write_character(char, array, col = col + c, row = row + r)
        return array
