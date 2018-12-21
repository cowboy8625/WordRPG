import os
import sys
import codecs
from time import sleep
import textwrap

from .const import *



def setup_terminal( cols = 40, lines = 15):
	""" sets the size of the terminal window and clears it before printing"""
	os.system(f"mode con cols={cols} lines={lines}")
	os.system( 'cls' if os.name == 'nt' else 'clear' )


def load_txt(filename, codec = 'utf-8'):
   """reads in txt file encoded in utf-8"""
   with codecs.open(filename, encoding = codec)as f:
      txt = f.read()

   return txt


def string_to_char_array(_string, seperator = '\n'):
   """
   converts multi-line string into a 2D array of characters
   
   **Arguments:**
   
      :``_string``: `str` Multi-line string block
   
   **Keword Arguments:**
   
      :``seperator``: `str` Character to split _string by. Default is newline ('\n')
      :``ignore_first``: `bool` If True, ignore the first line of _string.
      :``ignore_last``: `bool` If True, ignore the last line of _string.
   
   **Author:**
   
      Chris Bruce, chris.bruce@dsvolition.com, 12/20/2018
   """
   
   _lines = _string.split('\n')
   char_array = deque([ list( line ) for line in _lines ], maxlen = 15)

   return char_array



def char_array_to_string(_array):
   """
   converts 2D array of characters into a multi-line string
   
   **Arguments:**
   
      :``_array``: `list` 2D array of characters
   
   **Keword Arguments:**
   
      None   

   **Author:**
   
      Chris Bruce, chris.bruce@dsvolition.com, 12/20/2018
   """

   lines = [''.join(char) for char in _array]
   _string = '\n'.join(lines)

   return _string

class MainWindow( ):
	"""Main window and text parser for displaying the main window frame and game text
	
	Returns:
		None
	"""

	def __init__( self ):
		self.HEIGHT				= 30					# character height of frame
		self.WIDTH				= 40					# character width of frame
		self.INNER				= self.WIDTH - 2	# character width inside of frame
		self.TITLE				= 'WORDRPG'
		self.VERSION			= 1.0
		self.HEADER				= f'{self.TITLE} - {self.VERSION}'
		self.FOOTER				= 'COWBOY GAMING © 2018'


	def clear( self ):
	   os.system( 'cls' if os.name == 'nt' else 'clear' )


	def center_text( self, text, width, fillchar = ' '  ):
		"""Centers a text string in a given 'width' and fills empty space with given 'fillchar'
		
		Arguments:
			text {str} -- Text to be centered
			width {int} -- Width of the text field to center within
		
		Keyword Arguments:
			fillchar {str} -- String character to fill empty space (default: {' '})
		
		Returns:
			str -- New centered and space-filled string
		"""

		return text.center( width, fillchar )


	def format_contents( self, text, col_text = COL_TEXT, col_frame = COL_FRAME ):
		"""Formats block of raw text as frame contents

		Args:
			text (str): Multiline string of contents to put inside of frame
			fillchar (str, optional): Defaults to ' '. String character to fill empty space
			fillchar (str, optional): Defaults to ' '. String character to fill empty space

		Returns:
			[list]: List of f-strings
		"""

		contents		= [ ]
		lines			= text.splitlines( )

		for line in lines:
			if len( line ) < 1:
				line	= ' ' * ( self.INNER )
			else:
				line	= self.center_text( line, self.INNER )

			contents.append( f"{col_frame}{FRAME[ 'boxV' ]}{col_text}{line}{col_frame}{FRAME[ 'boxV' ]}")

		return contents


	def frame_edge( self, text, lc = 'boxDR', rc = 'boxDL', col_text = COL_HEADER, col_frame = COL_FRAME ):
		"""[summary]
		
		Arguments:
			text {str} -- Text to include in center of frame edge
		
		Keyword Arguments:
			lc {str} -- Name of key in FRAME to use for left corner of frame edge. (default: {'boxDR'})
			rc {str} -- Name of key in FRAME to use for right corner of frame edge. (default: {'boxDL'})
			col_text {colorama.fore} -- Color to use for text (default: {COL_HEADER})
			col_frame {colorama.fore} -- Color to use for frame (default: {COL_FRAME})
		
		Returns:
			str -- Frame edge as a string
		"""

		_text	= f"┤ {text} ├"
		_text	= self.center_text( _text, self.INNER, fillchar = FRAME[ 'boxH' ] )
		_text	= _text.replace( text, f'{col_text}{text}{col_frame}')

		return f"{col_frame}{FRAME[ lc ]}{_text}{col_frame}{FRAME[ rc ]}"


	def build_frame( self, content, col_frame = COL_FRAME ):
		""" Main function to draw the window frame

		Args:
			content (str): Multiline string of contents to put inside of frame
	
		"""

		# top border with header text
		top		= self.frame_edge( self.HEADER,
					'boxDR', 'boxDL',
					col_text		= COL_HEADER,
					col_frame	= col_frame
					)
		contents = [ top ]

		# content parsed from multiline string
		mid		= self.format_contents( content,
					col_text		= COL_TEXT,
					col_frame	= col_frame
					)
		contents += mid

		# bottom border with footer text
		btm		= self.frame_edge( self.FOOTER,
					'boxUR', 'boxUL',
					col_text		= COL_FOOTER,
					col_frame	= col_frame
					)
		contents.append( btm )

		return contents


	def draw( self, content, col_frame = COL_FRAME ):
		""" Main function to draw the screen
		"""

		contents	= self.build_frame( content, col_frame = col_frame )

		self.clear( )
		for line in contents:
			print( line )
