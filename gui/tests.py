""" Some test screen-building functions """

import os
from random import randrange

from . import const, main



DIRNAME = os.path.dirname(__file__)
FILEPATH = os.path.join(DIRNAME, 'screens')


def draw_screen(screen):
    """ draws the given screen to the terminal output window

    Arguments:
        screen {str|list} -- screen as a raw string or 2D array of characters
    """

    if isinstance(screen, str):
        main.draw(screen)
    else:
        screen = main.char_array_to_string(screen)
        main.draw(screen)


def fill_screen(char = '#'):
    """ creates a new screen by filling with given character

    Keyword Arguments:
        char {str} -- String to fill screen with. (default: {'#'})

    Returns:
        list -- 2D array of string characters
    """

    cols, rows = const.FIELD_SIZE
    line = f'{char}' * cols
    text = f'{line}\n' * rows

    return main.string_to_char_array(text)


def empty():
    """ tests creating an empty screen and drawing it """
    screen = fill_screen(char=' ')
    # print the screen
    draw_screen(screen)


def fill():
    """ tests creating an filled screen and drawing it """
    screen = fill_screen(char='#')
    # print the screen
    draw_screen(screen)


def logo():
    """ tests drawing a raw txt screen """
    _splash = const.SCREENS['splash']['txt']

    draw_screen(_splash)


def splash( company = 'COMBOY GAMING', year = '2018' ):
    """ tests compositing screens and adding text at a centered offset
    using string formatters and parameters """
    screen = fill_screen(char=' ')

    # _splash = create_splash()
    _splash = const.SCREENS['splash']['array']
    main.write_to_array(_splash, screen, col = 20, row = 2, fgcolor = 'white', bgcolor = 'black')

    text = f'<<  {company} - {year}  >>'
    start = main.center_offset(text, const.SCREEN_SIZE[0])
    main.write_to_array(text, screen, col = start, row = 25, fgcolor = 'red')

    # print the screen
    draw_screen(screen)


def menu():
    """ tests compositing screens and adding text at a centered offset
    using string formatters and parameters """

    screen = fill_screen(char=' ')

    frame = const.SCREENS['frame']['array']
    main.write_to_array(frame, screen, col=0, row=0, fgcolor='cyan', bgcolor='blue')

    header = f'> {const.HEADER} <'
    start = main.center_offset(header, const.SCREEN_SIZE[0])
    main.write_to_array(header, screen, col = start, row = 0, fgcolor = 'red')

    # print the screen
    draw_screen(screen)


def title():
    """ tests compositing screens and adding text at a centered offset
    using string formatters and parameters """

    screen = fill_screen(char=' ')

    frame = const.SCREENS['frame']['array']
    main.write_to_array(frame, screen, col=0, row=0, fgcolor='cyan', bgcolor='blue')

    _title = const.SCREENS['title']['array']
    main.write_to_array(_title, screen, col = 12, row = 6, fgcolor='cyan', bgcolor='magenta')

    # print the screen
    draw_screen(screen)


def random_words():
    """ tests compositing screens and multiple string objects at random
    locations on the screen """

    screen = fill_screen(char=' ')

    frame = const.SCREENS['frame']['array']
    main.write_to_array(frame, screen, col=0, row=0, fgcolor='cyan', bgcolor='blue')

    text = 'WORDS'
    col, rows = const.FIELD_SIZE
    # put text in random places
    col_max = col - len(text)
    for _ in range( 30 ):
        rand_col = randrange( 0, col_max)
        rand_row = randrange( 0, rows)
        main.write_to_array(text, screen, col = rand_col, row = rand_row)

    # print the screen
    draw_screen(screen)
