import sys
from time import sleep, time

# https://pypi.org/project/keyboard/
import keyboard

import gui



# class Screen():
#     def __init__(self, screen_name, parent, hotkeys={}):
#         self.screen_name = screen_name
#         self.parent = parent

#         self.draw_screen()
        
#         if hotkeys:
#             self.hotkeys = hotkeys
#             self.wait_for_keypress


#     @classmethod
#     def get_key_press(self):
#         while True:
#             key_event = keyboard.read_event()
#             if key_event.event_type == 'up':
#                 return key_event.name


#     @classmethod
#     def get_entry(until='enter'):
#         """Collects keyboard events until the user hits the 'until' key
        
#         Keyword Arguments:
#             until {str} -- Key that stops the event redorder (default: {'enter'})
        
#         Returns:
#             string -- Parsed string entered by user
#         """
#         events = keyboard.record(until=until)
#         generator = keyboard.get_typed_strings(events)
#         string = next(generator)
        
#         return string


#     def draw_screen(self, name, clear=True):
#         """ method that draws the screen """
#         if clear:
#             gui.main.clear()

#         return gui.tests.name()


#     def wait_for_keypress(self):
#         """keyboard event handler"""
#         while True:
#             key = self.get_key_press()
#             if key is not None:
#                 return main_menu
     
#         pass



##------------------------------------------------------------------------------

def get_key_press():
    while True:
        key_event = keyboard.read_event()
        if key_event.event_type == 'up':
            return key_event.name

    # this will return False during a timeout
    return False

##------------------------------------------------------------------------------

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


def help():
    # draw the screen
    gui.main.clear()
    print( 'Help screen')
    print( 'press any key to return to main menu')

    # start loop and keyboard event handler
    while True:
        key = get_key_press()
        if key is not None:
            return main_menu


def credits():
    # draw the screen
    gui.screen.credits()

    # start loop and keyboard event handler
    while True:
        key = get_key_press()
        if key is not None:
            return main_menu


def main_menu():
    # draw the screen
    gui.screen.menu()

    # start loop and keyboard event handler
    while True:
        key = get_key_press()
        if key == 'q':
            return quit(main_menu)
        elif key == 'n':
            return new_game
        elif key == 'c':
            return credits
        elif key == 'l':
            return load_game
        elif key == 'h':
            return help


def splash():
    # draw the screen
    gui.screen.splash()

    # pause for 3 seconds and then automatically advance to next screen
    timeout = time() + 3
    while True:
        if time() > timeout:
            break

    # return next screen
    return main_menu


def quit(prev_screen):
    """ function to quit the app """
    # draw the screen
    gui.main.clear()
    print('Press Q to quit. Press "Esc" to return to main menu.')

    while True:
        key = get_key_press()
        if key == 'q':
            break
        elif key == 'esc':
            return prev_screen

    # returning None forced main loop to exit
    return None


##------------------------------------------------------------------------------

# class GameLoop():
#     def __init__(self, screens):
#         prev_screen = None
#         next_screen = screens[0]

#         self.screens = screens

    


def main(): # main game loop
    # always start by setting up the terminal
    gui.main.setup_terminal()

    prev_screen = None
    next_screen = splash
    while True:
        if next_screen is None:
            break

        prev_screen = next_screen
        next_screen = next_screen()
    
    # If we're out of the main loop, then we're quitting the game
    sys.exit()



if __name__ == '__main__':
    main()
