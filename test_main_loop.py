import sys
from time import sleep, time

# https://pypi.org/project/keyboard/
import keyboard

import gui



def get_key_press():
    while True:
        key_event = keyboard.read_event()
        if key_event.event_type == 'up':
            return key_event.name

    # this will return False during a timeout
    return False


def new_game():
    # draw the screen
    gui.main.clear()
    print( 'New Game')
    print( 'press any key to return to main menu')

    # start loop and keyboard event handler
    while True:
        key = get_key_press()
        if key is not None:
            return main_menu


def load_game():
    # draw the screen
    gui.main.clear()
    print( 'Load Game')
    print( 'press any key to return to main menu')

    # start loop and keyboard event handler
    while True:
        key = get_key_press()
        if key is not None:
            return main_menu


def credits():
    # draw the screen
    gui.main.clear()
    print( 'People who made this!')
    print( 'press any key to return to main menu')

    # start loop and keyboard event handler
    while True:
        key = get_key_press()
        if key is not None:
            return main_menu


def main_menu():
    # draw the screen
    gui.main.clear()
    print('Main Menu')
    print('(n)new\n(l)oad\n(q)uit\n(c)redits')

    # start loop and keyboard event handler
    while True:
        key = get_key_press()
        if key == 'q':
            return quit
        elif key == 'n':
            return new_game
        elif key == 'c':
            return credits
        elif key == 'l':
            return load_game


def title():
    # draw the screen
    gui.main.clear()
    print('Title')

    # pause for 3 seconds and then automatically advance to next screen
    timeout = time() + 3
    while True:
        if time() > timeout:
            break
        
    # return next screen
    return main_menu


def splash():
    # draw the screen
    gui.main.clear()
    print('Splash Screen')

    # pause for 3 seconds and then automatically advance to next screen
    timeout = time() + 3
    while True:
        if time() > timeout:
            break

    # return next screen
    return title


def quit():
    """ function to quit the app """
    # draw the screen
    gui.main.clear()
    print('Press Q to quit. Or any other key to return to main menu.')

    while True:
        key = get_key_press()
        if key == 'q':
            break
        elif key is not None:
            return main_menu

    return sys.exit()


def main(): # main game loop
    # always start by setting up the terminal
    gui.main.setup_terminal()

    next_screen = splash
    while True:
        if next_screen is None:
            break
        else:
            next_screen = next_screen()
    
    # this shouldn't happen, but if it does go to the quit screen
    quit()



if __name__ == '__main__':
    main()
