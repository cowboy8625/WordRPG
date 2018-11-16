##- This will grab the changes from CHANGELOG.md and put them in a variable to
##- be used in the game for the changelog menu.

##-- Import --##

import os

def clear():
    
    if os.name == 'nt':
        _ = os.system('cls')

    else:
        _ = os.system('clear')

def change_log_print():
    with open('CHANGELOG.md', 'r') as f:
        f_contents = f.read()
        clear()
        print(f_contents)

