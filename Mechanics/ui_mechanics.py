__author__ = "byteme8bit"

# File imports

# Module imports
import os


# Clears Print Screen
def clear():
    if os.name == 'nt':
        _ = os.system('cls')

    else:
        _ = os.system('clear')


# This maybe fast then retyping input a bunch
def pause():
    input("Press Enter To Continue:> ")
