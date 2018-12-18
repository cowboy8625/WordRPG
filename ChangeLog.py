"""
This will grab the changes from CHANGELOG.md and put them in a variable to
be used in the game for the changelog menu.

**Examples:**

	# read in CHANGELOG.md as a python string
	changelog = import_changelog( )

	# reads in CHANGELOG.md and prints it to the terminal
	print_changelog( )

"""

from os import system, name


FILENAME_CHANGELOG = 'CHANGELOG.md'


def import_changelog( ):
	"""
	Imports CHANGELOG.md and returns contents as str
	
	**Returns:**
	
		:``str``: changelog as a string
	"""

	with open( FILENAME_CHANGELOG', 'r') as f:
		contents = f.read()

	return changelog


def clear( ):
	"""
	Clears the terminal screen

	**Returns:**
	
		:``str``: Resultof os.system command
	"""

	return os.system( 'cls' if os.name == 'nt' else 'clear' )
    

def print_changelog( ):
	"""
	Prints changelog to terminal

	**Returns:**
	
		:``str``: Result of print command
	"""

	change_log = import_change_log( )
	clear( )

	return print( change_log )
