""" gui module

  The gui module works by creating and compositing 2D arrays of indivudal string
  characters called a 'screen'.
  
  The maximum dimensions of a screen is 80 columns x 30 rows, which matches the
  terminal output window.

  Screens can also be parsed in from plain text files saved in the 'screens'
  sub-folder.

  Screens can be composited together or have indicies directly overwritten

  Once a final screen array has been created, it is converted to a single string and then
  written to the terminal output window.

"""

from . import const, Screen
