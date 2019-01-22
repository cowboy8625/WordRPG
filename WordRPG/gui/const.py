""" CONSTANTS for gui module """
import os



NAME = 'WASTELANDS'
VERSION = 1.0
YEAR = 2018
COMPANY = 'COWBOY GAMING'
TITLE = f'{NAME}(ver.{VERSION}) - {COMPANY} - ©{YEAR}'
HEADER = f'{NAME} - {VERSION}'
FOOTER = f'{COMPANY} - ©{YEAR}'  # © can cause problems with encoding

# default pixel size of characters
CHAR_SIZE = (8, 16)
# size of terminal for printable characters
SCREEN_SIZE = (80,30)
# screen resolution in pixels
SCREEN_RES = (SCREEN_SIZE[0] * CHAR_SIZE[0], SCREEN_SIZE[1] * CHAR_SIZE[1])
# default size of map window in main game screen
DEF_MAP_SIZE = (41, 21)


# This constant sets color/style formatting on or off
FORMAT_TEXT = True
DEF_FORMAT = {'fgcolor':'WHITE','bgcolor':'BLACK','style':'NORMAL'}


# get list of .txt filenames in the 'screens' subfolder
DIRNAME = os.path.dirname(__file__)
FILEPATH = os.path.join(DIRNAME, 'screens')


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
