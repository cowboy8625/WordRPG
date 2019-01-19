""" CONSTANTS for gui module """
import os

from . import main



NAME = 'WASTELANDS'
VERSION = 1.0
YEAR = 2018
COMPANY = 'COWBOY GAMING'
TITLE = f'{NAME}(ver.{VERSION}) - {COMPANY} - ©{YEAR}'
HEADER = f'{NAME} - {VERSION}'
FOOTER = f'{COMPANY} - ©{YEAR}'  # © can cause problems with encoding


CHAR_SIZE = (8, 16)
# size of terminal for printable characters
FIELD_SIZE = (80,30)
# size of screen for terminal window. Includes padding and extra room for input field
SCREEN_SIZE = (FIELD_SIZE[0], FIELD_SIZE[1])
# screen resolution in pixels
SCREEN_RES = (SCREEN_SIZE[0] * CHAR_SIZE[0], SCREEN_SIZE[1] * CHAR_SIZE[1])
# 1 space of padding inside of frame

# This constant sets color/style formatting on or off
FORMAT_TEXT = True

# get list of .txt filenames in the 'screens' subfolder
DIRNAME = os.path.dirname(__file__)
FILEPATH = os.path.join(DIRNAME, 'screens')
FILENAMES = []
for f in os.listdir(FILEPATH):
    if f.endswith('.txt'):
        FILENAMES.append(os.path.join(FILEPATH, f))

# build a 'SCREENS' dictionary by loading all .txt files in the 'screens'
# subfolder, and converting them to 2D arrays of characters
SCREENS = {}
for f in FILENAMES:
    screen_name = os.path.splitext(os.path.basename(f))[0].lower()
    txt = main.load_txt(f)
    SCREENS[screen_name] = {
        'filename' : f,
        'txt' : txt,
        'array' : main.string_to_char_array(txt),
        }

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
