""" Linux sub-module for dealing with the console window cursor """
import sys
import os



def hide():
    """ Hide the cursor """
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()


def show():
    """ Show the cursor """
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()
