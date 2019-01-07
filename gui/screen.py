""" Module for compositing and drawing various game screens """

import os
from random import randrange

from . import const, main



DIRNAME = os.path.dirname(__file__)
FILEPATH = os.path.join(DIRNAME, 'screens')



def blank():
    """ tests creating an empty screen and drawing it """
    screen = main.new_screen(char=' ')
    # print the screen
    main.draw(screen)


def filled():
    """ tests creating an filled screen and drawing it """
    screen = main.new_screen(char='#')
    # print the screen
    main.draw(screen)


def splash():
    """ tests compositing screens and adding text at a centered offset
    using string formatters and parameters """
    screen = main.new_screen(char=' ')

    # _splash = create_splash()
    _splash = const.SCREENS['splash']['array']
    main.write_to_array(_splash, screen, col=20, row=2,
                        transparent=True, fgcolor='WHITE', bgcolor='BLACK')

    text = f'{const.COMPANY}'
    start = main.center_offset(text, const.SCREEN_SIZE[0])
    main.write_to_array(text, screen, col=start, row=25, fgcolor='RED', style='BRIGHT')

    # print the screen
    main.draw(screen)


def _create_background(background='frame', offset=(0, 0),
                       fgcolor='CYAN', bgcolor='BLACK'):
    """ creates a new screen with a given background screen """
    screen = main.new_screen(char=' ')
    background = const.SCREENS[background]['array']
    main.write_to_array(background, screen, col=offset[0], row=offset[1],
                        transparent=True, fgcolor=fgcolor, bgcolor=bgcolor)

    return screen


def title():
    """ tests compositing screens and adding text at a centered offset
    using string formatters and parameters """

    screen = _create_background()

    _title = const.SCREENS['title']['array']
    main.write_to_array(_title, screen,
                        transparent=True, col=12, row=6, fgcolor='cyan', bgcolor='magenta')

    # print the screen
    main.draw(screen)


def menu():
    """ tests compositing screens and adding text at a centered offset
    using string formatters and parameters """

    screen = _create_background()

    _title = const.SCREENS['title']['array']
    main.write_to_array(_title, screen,
                        transparent=True, col=12, row=6, fgcolor='RED', bgcolor='BLACK')

    row_start = 12
    MAIN_MENU = [
        '(N) - NEW GAME',
        '(L) - LOAD GAME',
        '(H) - HELP',
        '(C) - CREDITS',
        '(Q) - QUIT'
        ]
    c = main.center_offset(max(MAIN_MENU), const.SCREEN_SIZE[0])
    for i, line in enumerate(MAIN_MENU):
        r = row_start + i
        main.write_to_array(line, screen, col=c, row=r, fgcolor='YELLOW', style='BRIGHT')

    footer = f' {const.FOOTER} '
    start = main.center_offset(footer, const.SCREEN_SIZE[0])
    main.write_to_array(footer, screen, col=start, row=29, fgcolor='RED')

    # print the screen
    main.draw(screen)
    

def story_test():
    """ tests compositing screens and adding text at a centered offset
    using string formatters and parameters """

    screen = _create_background(
                    background='scroll',
                    fgcolor='YELLOW', bgcolor='BLACK')

    title = 'CHAPTER ONE'
    c = main.center_offset(title, const.SCREEN_SIZE[0])
    main.write_to_array(
            title, screen, col=c, row=2, fgcolor='CYAN', style="BRIGHT")

    story = const.SCREENS['story_test']['array']
    main.write_to_array(story, screen, col=6, row=6, fgcolor='WHITE')

    # print the screen
    main.draw(screen)


def credits():
    """ tests compositing screens and adding text at a centered offset
    using string formatters and parameters """

    screen = _create_background(
                    background='scroll', offset = (0,1),
                    fgcolor='YELLOW', bgcolor='BLACK')

    title = 'PROJECT CONTRIBUTORS'
    c = main.center_offset(title, const.SCREEN_SIZE[0])
    main.write_to_array(title, screen, col=c, row=2, fgcolor='CYAN', style="BRIGHT")

    story = const.SCREENS['credits']['array']
    main.write_to_array(story, screen, col=14, row=5, fgcolor='WHITE')

    # print the screen
    main.draw(screen)


def help():
    """ tests compositing screens and adding text at a centered offset
    using string formatters and parameters """

    screen = _create_background(
                    background='scroll', offset = (0,1),
                    fgcolor='YELLOW', bgcolor='BLACK')

    title = 'PLACEHOLDER HELP SCREEN'
    c = main.center_offset(title, const.SCREEN_SIZE[0])
    main.write_to_array(title, screen, col=c, row=2, fgcolor='CYAN', style="BRIGHT")

    # print the screen
    main.draw(screen)
