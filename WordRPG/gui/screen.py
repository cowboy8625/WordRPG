""" Module for compositing and drawing various game screens """

import os
from random import randrange

from . import const, main, menu



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
    main.write_to_array(background, screen, col=offset[0], row=offset[0],
                        transparent=True, fgcolor=fgcolor, bgcolor=bgcolor)
    return screen


def _create_frame(screen, cols= 80, rows=40, style=1, offset=(0, 0),
                  fgcolor='CYAN', bgcolor='BLACK'):
    frame = main.create_frame(80, 30, style=style, as_array=True)
    main.write_to_array(frame, screen, col=offset[0], row=offset[0],
                        transparent=True, fgcolor=fgcolor, bgcolor=bgcolor)
    return screen


def title():
    """ tests compositing screens and adding text at a centered offset
    using string formatters and parameters """

    # makes a new empty screen
    screen = main.new_screen(char=' ')

    # creates standard double line frame around whole screen
    _create_frame(screen)

    # draw the game title
    _title = const.SCREENS['title']['array']
    main.write_to_array(_title, screen,
                        transparent=True, col=12, row=6, fgcolor='cyan', bgcolor='magenta')

    # print the screen
    main.draw(screen)


def main_menu():
    """ Creates and draws the Main Menu screen """

    # makes a new empty screen
    screen = main.new_screen(char=' ')

    # creates standard double line frame around whole screen
    _create_frame(screen)

    # draw the game title
    _title = const.SCREENS['title']['array']
    main.write_to_array(_title, screen, transparent=True, col=12, row=6,
                        fgcolor='RED', bgcolor='BLACK')

    # draw the menu
    menu_txt = menu.create_menu_array(menu.main_menu)
    width = menu.get_max_width(menu.main_menu)
    col = main.center_offset(width, const.SCREEN_SIZE[0])
    main.write_to_array(menu_txt, screen, col=col, row=12)

    # draw the footer
    footer = f' {const.FOOTER} '
    col = main.center_offset(footer, const.SCREEN_SIZE[0])
    main.write_to_array(footer, screen, col=col, row=29, fgcolor='RED')

    # print the screen
    main.draw(screen)


def game_menu():
    """ Creates and draws the in-game menu screen """

    # makes a new empty screen
    screen = main.new_screen(char=' ')

    # creates standard double line frame around whole screen
    _create_frame(screen)

    # draw the game title
    _title = const.SCREENS['title']['array']
    main.write_to_array(_title, screen, transparent=True, col=12, row=6,
                        fgcolor='RED', bgcolor='BLACK')

    # draw the menu
    menu_txt = menu.create_menu_array(menu.game_menu)
    width = menu.get_max_width(menu.main_menu)
    col = main.center_offset(width, const.SCREEN_SIZE[0])
    main.write_to_array(menu_txt, screen, col=col, row=12)

    # draw the footer
    footer = f' {const.FOOTER} '
    col = main.center_offset(footer, const.SCREEN_SIZE[0])
    main.write_to_array(footer, screen, col=col, row=29, fgcolor='RED')

    # print the screen
    main.draw(screen)


def new_game():
    """ Creates and draws the New Game screen """

    # makes a new empty screen
    screen = main.new_screen(char=' ')

    # creates standard double line frame around whole screen
    _create_frame(screen)

    # creates the menu text
    menu_txt = menu.create_menu_array(menu.new_game)
    width = menu.get_max_width(menu.new_game)
    col = main.center_offset(width, const.SCREEN_SIZE[0])
    main.write_to_array(menu_txt, screen, col=col, row=12)

    # add footer to screen
    footer = f' {const.FOOTER} '
    col = main.center_offset(footer, const.SCREEN_SIZE[0])
    main.write_to_array(footer, screen, col=col, row=29, fgcolor='RED')

    # print the screen
    main.draw(screen)


def story_test():
    """ tests compositing screens and adding text at a centered offset
    using string formatters and parameters """

    # draw the background and frame
    screen = _create_background(
                    background='scroll',
                    fgcolor='YELLOW', bgcolor='BLACK')

    # draw screen title
    title = 'CHAPTER ONE'
    c = main.center_offset(title, const.SCREEN_SIZE[0])
    main.write_to_array(
            title, screen, col=c, row=2, fgcolor='CYAN', style="BRIGHT")

    # draw story text
    story = const.SCREENS['story_test']['array']
    main.write_to_array(story, screen, col=6, row=6, fgcolor='WHITE')

    # print the screen
    main.draw(screen)


def credits():
    """ tests compositing screens and adding text at a centered offset
    using string formatters and parameters """

    # draw the background and frame
    screen = _create_background(
                    background='scroll', offset = (0,1),
                    fgcolor='YELLOW', bgcolor='BLACK')

    # draw screen title
    title = 'PROJECT CONTRIBUTORS'
    c = main.center_offset(title, const.SCREEN_SIZE[0])
    main.write_to_array(title, screen, col=c, row=2, fgcolor='CYAN', style="BRIGHT")

    # draw credits text
    story = const.SCREENS['credits']['array']
    main.write_to_array(story, screen, col=14, row=5, fgcolor='WHITE')

    # print the screen
    main.draw(screen)


def help():
    """ tests compositing screens and adding text at a centered offset
    using string formatters and parameters """

    # draw the background and frame
    screen = _create_background(
                    background='scroll', offset = (0,1),
                    fgcolor='YELLOW', bgcolor='BLACK')

    # draw screen title
    title = 'PLACEHOLDER HELP SCREEN'
    c = main.center_offset(title, const.SCREEN_SIZE[0])
    main.write_to_array(title, screen, col=c, row=2, fgcolor='CYAN', style="BRIGHT")

    # print the screen
    main.draw(screen)


def _file_data_block(index, file_info, screen):
    """ creates file data block

    File screen currently supports 3 file data blocks
    """
    # each frame needs 8 characters of space, starting at row 2
    row = index * 8 + 2

    # draw file frame
    file_frame = const.SCREENS['file_frame']['array']

    # add text from file_info
    filename = f'< SAVE GAME {index + 1} >'
    main.string_to_char_array(filename)
    main.write_to_array(filename, file_frame, col=2, row=0)

    # add character name, class, level
    # TODO: This data should be gotten from file_info arg
    n = f'[NAME]'
    c = f'[CLASS]'
    l = f'[LEVEL]'
    char_text = main.string_to_char_array(f'{n} | {c} | {l}')
    main.write_to_array(char_text, file_frame, col=2, row=1)

    # add timestamp
    # TODO: This data should be gotten from file_info arg
    # TODO: Need to right-justify timestamp to frame border width - 1
    timestamp = f'12:24 - 12/12/2019'
    main.string_to_char_array(filename)
    main.write_to_array(timestamp, file_frame, col=52, row=1)

    # add file details
    # TODO: This data should be gotten from file_info arg
    details_txt = 'OTHER RELEVANT DETAILS IN THE FILE THAT NEED TO BE SHOWN'
    details_txt = main.string_to_char_array(details_txt)
    main.write_to_array(details_txt, file_frame, col=2, row=3)

    # draw the file block to the screen
    main.write_to_array(file_frame, screen,
                        transparent=True, col=3, row=row,
                        fgcolor='WHITE', bgcolor='BLACK'
                        )


def files(files_info=[{},{},{}], mode='load'):
    """ Create file screen

    File screen is used for loading and saving files in the main menu or in
    game menu
    """

    # draw the background and frame
    # makes a new empty screen
    screen = main.new_screen(char=' ')

    # creates standard double line frame around whole screen
    _create_frame(screen)

    # draw the header
    header = f' {mode.upper()} GAME '
    col = main.center_offset(header, const.SCREEN_SIZE[0])
    main.write_to_array(header, screen, col=col, row=0, fgcolor='RED')

    # create each file data block and draw them to screen
    for i, f in enumerate(files_info):
        _file_data_block(i, f, screen)

    # add screen prompt
    text = f'SELECT FILE SLOT TO {mode.upper()}'
    col = main.center_offset(text, const.SCREEN_SIZE[0])
    main.write_to_array(text, screen, col=col, row=27, fgcolor='RED')

    # print the screen
    main.draw(screen)


def game():
    """ Creates and draws the main game screen """

    # draw the background and frame
    screen = _create_background()

    # draw the game title
    _game = const.SCREENS['game']['array']
    main.write_to_array(_game, screen, transparent=True, col=0, row=0,
                        fgcolor='WHITE', bgcolor='BLACK')

    # draw the header
    header = f' {const.HEADER} '
    col = main.center_offset(header, const.SCREEN_SIZE[0])
    main.write_to_array(header, screen, col=col, row=0, fgcolor='RED')

    # draw the menu
    # menu_txt = menu.create_menu_array(menu.game_menu)
    # width = menu.get_max_width(menu.main_menu)
    # col = main.center_offset(width, const.SCREEN_SIZE[0])
    # main.write_to_array(menu_txt, screen, col=col, row=12)

    # draw the footer
    footer = f' {const.FOOTER} '
    col = main.center_offset(footer, const.SCREEN_SIZE[0])
    main.write_to_array(footer, screen, col=col, row=29, fgcolor='RED')

    return screen
