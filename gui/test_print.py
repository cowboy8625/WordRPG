import os
from time import sleep
import codecs
from collections import deque



def setup_terminal( cols = 40, lines = 16):
    """ sets the size of the terminal window and clears it before printing"""
    #os.system(f"mode con cols={cols} lines={lines}")
    os.system("mode con cols={} lines={}".format(cols, lines))


def load_txt(filename, codec = 'utf-8'):
    """reads in txt file encoded in utf-8"""
    with codecs.open(filename, encoding = codec)as f:
        txt = f.read()

    return txt


def string_to_char_array(_string, seperator = '\n'):
    """
    converts multi-line string into a 2D array of characters

    **Arguments:**

        :``_string``: `str` Multi-line string block

    **Keword Arguments:**

        :``seperator``: `str` Character to split _string by. Default is newline ('\n')
        :``ignore_first``: `bool` If True, ignore the first line of _string.
        :``ignore_last``: `bool` If True, ignore the last line of _string.

    **Author:**

        Chris Bruce, chris.bruce@dsvolition.com, 12/20/2018
    """

    _lines = _string.split('\n')
    char_array = deque([ list( line ) for line in _lines ], maxlen = 15)

    return char_array



def char_array_to_string(_array):
    """
    converts 2D array of characters into a multi-line string

    **Arguments:**

        :``_array``: `list` 2D array of characters

    **Keword Arguments:**

        None   

    **Author:**

        Chris Bruce, chris.bruce@dsvolition.com, 12/20/2018
    """

    lines = [''.join(char) for char in _array]
    _string = '\n'.join(lines)

    return _string
      

# data files
filepath = r'C:\Users\chris.bruce\Documents\Python\Personal\WordRPG\gui\screens'

screen_names = [
    'splash',
    'title',
    'menu_main',
    'file',
    'player',
    'inventory',
    'story',
    'dialogue',
    'shop',
    'combat',
    ]


""" Test stuff below"""
setup_terminal()

# load .txt and convert to 2D array
screens = []
for name in screen_names:
    filename = os.path.join(filepath, '{}.txt'.format(name))
    txt = load_txt(filename)

    screens.append(txt)

# converts multi-line string to 2D array of characters
arrays = []
for screen in screens:
    array = string_to_char_array(screen)
    arrays.append(array)

# converts 2D array of characters to multi-line string
screens = []
for array in arrays:
    screen = char_array_to_string(array)
    screens.append(screen)

# print screens
for x in range(100):
    for screen in screens:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(screen)
        # input('>>>')
        # sleep(3)