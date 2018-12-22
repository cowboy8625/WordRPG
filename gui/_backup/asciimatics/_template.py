import sys

from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
from asciimatics.widgets import Frame, Layout, Background, VerticalDivider
from asciimatics.widgets import Label, TextBox, Button



class HeadFrame( Frame ):
	def __init__( self, screen ):
		super ( HeadFrame, self ).__init__( screen,
														int( screen.height * 0.1 ),
														int( screen.width ),
														has_border = False,
														can_scroll = False,
														has_shadow = False,
														name = "Header Frame")

		# TODO: Look into setting up a custom palette
		self.set_theme( "bright" )

		layout = Layout( [ 1, 1, 1 ] )
		self.add_layout( layout )
		layout.add_widget( Label( "Header" ), 1 )

		self.fix( )


class FootFrame( Frame ):
	def __init__( self, screen ):
		super ( FootFrame, self ).__init__( screen,
														int( screen.height * 0.1 ),
														int( screen.width ),	#* 2 // 3),
														has_border = False,
														can_scroll = False,
														has_shadow = False,
														name = "Footer Frame")

		# TODO: Look into setting up a custom palette
		self.set_theme( "bright" )

		layout = Layout( [ 1, 1, 1 ] )
		self.add_layout( layout )
		layout.add_widget( Label( "Footer" ), 1 )

		self.fix( )


class MainFrame( Frame ):
	def __init__( self, screen ):
		super ( MainFrame, self ).__init__( screen,
														int( screen.height * 0.6 ),
														int( screen.width ),
														has_border = True,
														can_scroll = False,
														has_shadow = False,
														name = "Main Frame")

		self.set_theme( "bright" )

		self._init_main( )
		self._init_nav( )

		self.fix( )

	def _init_main( self ):
		layout = Layout( [ 1 ] )
		self.add_layout( layout )
		layout.add_widget( Label( "Main Body" ), 0 )
		#layout.add_widget( TextBox( "Main Body" ), 0 )

	def _init_nav( self ):
		layout = Layout( [ 1, 1, 1, 1, 1 ] )	# columns that take up 30%, 10%, 10%, 10%, 30% of available width
		self.add_layout( layout )
		layout.add_widget( Button(	"Back", self._back ), 1 )
		layout.add_widget( VerticalDivider( ), 2 )
		layout.add_widget( Button(	"OK", self._accept ), 3 )


	def process_event( self, event ):
		# Events are handled here or passed up to the superclass

		# Pass any other event on to the Frame and contained widgets.
		return super( MainWindow, self ).process_event( event )

	def _back( self ):
		pass

	def _accept( self ):
		pass



def run( screen ):
	effects = [
		Background( screen ),
		HeadFrame( screen ),
		MainFrame( screen ),
		# NavFrame( screen ),
		FootFrame( screen )
	]
	scenes = [ Scene( effects, -1 ) ]
	screen.play( scenes, stop_on_resize = True )


#if __name__ == 'main':
while True:
	try:
		Screen.wrapper( run, unicode_aware = True )
		sys.exit( 0 )
	except ResizeScreenError as e:
		last_scene = e.scene