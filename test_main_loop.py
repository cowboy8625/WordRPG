import sys
from time import sleep, time

# https://pythonhosted.org/pynput/keyboard.html
# https://nitratine.net/blog/post/how-to-make-hotkeys-in-python/?utm_source=pythonanywhere&utm_medium=redirect&utm_campaign=pythonanywhere_organic_redirect
from pynput.keyboard import Key, Listener

# https://pypi.org/project/keyboard/
# import keyboard

# import gui

##------------------------------------------------------------------------------
# copied over from gui sub-module
def clear():
    """ clear terminal window """
    os.system('cls' if os.name == 'nt' else 'clear')


##------------------------------------------------------------------------------

def new_game():
    # keyboard event handlers
    def on_release(key):
        listener.stop()

    # draw the screen
    clear()
    print( 'New Game')
    print( 'press any key to return to main menu')

    with Listener(on_release=on_release) as listener:
        listener.join()

    return main_menu


def load_game():
    # keyboard event handlers
    def on_release(key):
        listener.stop()

    # draw the screen
    clear()
    print( 'Load Game')
    print( 'press any key to return to main menu')

    with Listener(on_release=on_release) as listener:
        listener.join()

    return main_menu


def credits():
    # keyboard event handlers
    def on_release(key):
        listener.stop()

    # draw the screen
    clear()
    print( 'People who made this!')
    print( 'press any key to return to main menu')

    # start loop and keyboard input listener
    with Listener(on_release=on_release) as listener:
        listener.join()

    # return next screen
    return main_menu


def main_menu():
    # if we don't get a valid next screen, progress to quit
    next = None

    # keyboard event handlers
    def on_release(key):            
        try:
            key_pressed = key.char
        except AttributeError:
            key_pressed = key

        if key_pressed == 'q':
            listener.stop()
            next = quit
        elif key_pressed == 'n':
            listener.stop()
            next = new_game
        elif key_pressed == 'c':
            listener.stop()
            next = credits
        elif key_pressed == 'l':
            listener.stop()
            next = load_game

    # draw the screen
    clear()
    print('Main Menu')
    print('(n)new\n(l)oad\n(q)uit\n(c)redits')

    # start loop and keyboard input listener
    # TODO: listen.join() causes this to act like a loop until a key that's
    # handled by on_release is released.
    with Listener(on_release=on_release) as listener:
        listener.join()
    
    # return next screen
    return next


def title():
    # draw the screen
    clear()
    print('Title')

    # pause for 3 seconds and then automatically advance to next screen
    timeout = time() + 1
    while True:
        if time() > timeout:
            break
        
    # return next screen
    return main_menu


def splash():
    # draw the screen
    clear()
    print('Splash Screen')

    # pause for 3 seconds and then automatically advance to next screen
    timeout = time() + 1
    while True:
        if time() > timeout:
            break
        
    # return next screen
    return title


def quit():
    """ function to quit the app """
    print('quitting...')
    sleep(2)
    return sys.exit()
    

def main(): # main game loop
    # always start by setting up the terminal
    gui.main.setup_terminal()

    next_screen = splash
    while True:
        print(f'next_screen : {next_screen}')
        if next_screen is not None:
            next_screen = next_screen()
        else:
            print('got None for next screen')
            sleep(2)
            break
    
    return quit()



if __name__ == '__main__':
    main()