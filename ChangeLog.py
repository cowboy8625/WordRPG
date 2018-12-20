'''
This will grab the changes from CHANGELOG.md and put them in a variable to
be used in the game for the changelog menu.

**Examples:**

    # read in CHANGELOG.md as a python string
    changelog = import_changelog( )

    # reads in CHANGELOG.md and prints it to the terminal
    print_changelog( )

'''

import os
from Mechanics.ui_mechanics import *

FILENAME_CHANGELOG = 'CHANGELOG.md'


def import_change_log():
    '''
    Imports CHANGELOG.md and returns contents as str
    
    **Returns:**
    
        :``str``: changelog as a string
    '''
    
    with open( FILENAME_CHANGELOG, 'r') as f:
        contents = f.read()

    return contents


def clear():
    '''
    Clears the terminal screen

    **Returns:**
    
        :``str``: Result of os.system command
    '''

    return system( 'cls' if name == 'nt' else 'clear' )


def change_log_print():
    '''
    Prints changelog to terminal

    **Returns:**
    
        :``str``: Result of print command
    '''

    change_log = import_change_log( )
    clear( )

    return print( change_log )
