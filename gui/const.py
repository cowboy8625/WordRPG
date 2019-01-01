""" CONSTANTS for gui module """
import os

from . import main



TITLE = 'WASTELANDS'
VERSION = 1.0
CHAR_SIZE = (8, 16)
# size of terminal for printable characters
FIELD_SIZE = (80,30)
# size of screen for terminal window. Includes padding and extra room for input field
SCREEN_SIZE = (FIELD_SIZE[0], FIELD_SIZE[1])
# screen resolution in pixels
SCREEN_RES = (SCREEN_SIZE[0] * CHAR_SIZE[0], SCREEN_SIZE[1] * CHAR_SIZE[1])
# 1 space of padding inside of frame

HEADER = f'{TITLE} - {VERSION}'
FOOTER = 'COWBOY GAMING - 2018'  # © can cause problems with encoding
# This constant sets color/style formatting on or off
FORMAT_TEXT = True

# build a 'SCREENS' dictionary by loading all .txt files in the 'screens'
# subfolder, and converting them to 2D arrays of characters
DIRNAME = os.path.dirname(__file__)
FILEPATH = os.path.join(DIRNAME, 'screens')
FILENAMES = [os.path.join(FILEPATH, f) for f in os.listdir(FILEPATH) if f.endswith('.txt')]

SCREENS = {}
for f in FILENAMES:
    screen_name = os.path.splitext(os.path.basename(f))[0].lower()
    txt = main.load_txt(f)
    SCREENS[screen_name] = {
        'filename' : f,
        'txt' : txt,
        'array' : main.string_to_char_array(txt),
        }
