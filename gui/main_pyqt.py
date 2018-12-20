'''
PySide2.QtCore
PySide2.QtCore.Qt
PySide2.QtGui
PySide2.QtWidgets
'''

import os

import PySide2



class MainWindow( PySide2.QtWidgets.QWidget ):
	"""
	Main Window widget for WORDRPG game
	
	**Arguments:**
	
		None
	
	**Keword Arguments:**
	
		None
	
	**Author:**
	
		Chris Bruce, chris.bruce@dsvolition.com, 12/19/2018
	"""

	# TODO: Need to get relative path here
	# PATH = os.path.dirname(os.path.abspath( __file__ ))
	PATH			= r"C:\Users\chris.bruce\Documents\Python\Personal\WordRPG\gui"
	STYLESHEET	= os.path.join(PATH, 'stylesheet.css')
	WINDOW_SIZE = ( 640, 480 )
	FRAME_SIZE	= ( WINDOW_SIZE[ 0 ] - 24, WINDOW_SIZE[ 1 ] - 24) 
	TITLE			= 'WORDRPG'
	VERSION		= 1.0


	TEST_MAP		= '''
	֍۞۩
	'''

	def __init__( self ):
		super( MainWindow, self ).__init__( )

		self.header = 'WORDRPG'
		
		self._init_stylesheet( )

		#self._init_styles( )
		self._init_gui( )


	def _init_stylesheet( self ):
		with open( self.STYLESHEET ) as _file:
			# _qstring = PySide2.QtCore.QString( _file.read( ) )
			# return _qstring
			
			self.stylesheet = _file.read( )

		self.setStyleSheet( self.stylesheet )

		return self.stylesheet

		
	def _init_gui( self ):
		self.setFixedSize( *self.WINDOW_SIZE )

		self.layout =  PySide2.QtWidgets.QVBoxLayout( )
		self.setLayout( self.layout )
		
		self.frame =  PySide2.QtWidgets.QGroupBox( '{} - v{}'.format( self.TITLE, self.VERSION ) )
		self.frame.setAlignment( PySide2.QtCore.Qt.AlignHCenter )
		self.frame.setFixedSize( *self.FRAME_SIZE )
		self.frame_layout = PySide2.QtWidgets.QVBoxLayout( )
		self.frame.setLayout( self.frame_layout )
		self.layout.addWidget( self.frame )


		self.world_map = PySide2.QtWidgets.QTextEdit( )
		self.world_map.setText( self.TEST_MAP )
		self.frame_layout.addWidget( self.world_map )
		

#if __name__ == 'main':
try:
	_window.destroy( )
except:
	pass

_window = MainWindow( )
_window.show( )
