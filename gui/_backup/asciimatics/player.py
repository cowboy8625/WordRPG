from asciimatics.widgets import Frame, TextBox, Layout, Label, Divider, Text, \
	CheckBox, RadioButtons, Button, PopUpDialog, TimePicker, DatePicker, Background, DropdownList, \
	PopupMenu
from asciimatics.event import MouseEvent
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication, \
	InvalidFields
import sys
import re
import datetime



# TODO: Should pass the 'player' class object in directly
# Initial data for the form
form_character = {
	"name"   	: "STEVE",
	'age'		: "25",
	"gender"	: 2,
	"class" 	: 1
}



class MainWindow( Frame ):
	def __init__( self, screen ):
		super( MainWindow, self ).__init__( screen,
										int( screen.height	),
										int( screen.width ),
										data		= form_character,
										has_border	= True,
										has_shadow	= False,
										name		= "Create Character"
										)
		self._init_gui( )
		self._init_bot_menu( )

		self.fix( )


	def _init_gui( self ):
		# TODO: Look into setting up a custom palette
		# self.set_theme( "default" )
		self.set_theme( "bright" )

		self.layout = Layout( [ 1, 1, 1 ] )
		self.add_layout(self.layout)

		label = Label( "Character Profile:" )
		self.layout.add_widget( label, 1 )

		char_name = Text(
				label 		= "NAME:",
				name 		= "name",
				on_change	= self._on_change,
				validator	= "^[a-zA-Z]*$" )
		self.layout.add_widget( char_name, 1 )
			
		char_age = Text(
				label 		= "AGE:",
				name 		= "age",
				on_change	=self._on_change,
				validator	= "^[0-9]*$" )
		self.layout.add_widget( char_age, 1 )

		# self.layout.add_widget( Divider( height = 2 ), 1 )
		# self.layout.add_widget(Label("Group 2:"), 1)
		char_gender = RadioButtons( [ ( "MALE", 1 ), ( "FEMALE", 2 ) ],
									   label		= "GENDER:",
									   name 		= "gender",
									   on_change	= self._on_change)
		self.layout.add_widget( char_gender, 1 )

		# self.layout.add_widget(CheckBox("Field 1",
		# 						   label="A very silly long name for fields:",
		# 						   name="CA",
		# 						   on_change=self._on_change), 1)
		# self.layout.add_widget(
		# 	CheckBox("Field 2", name="CB", on_change=self._on_change), 1)
		# self.layout.add_widget(
		# 	CheckBox("Field 3", name="CC", on_change=self._on_change), 1)
		
		char_class = DropdownList( [ ( "FIGHTER", 1), ( "MAGE", 2 ), ( "ASSASIN", 3 ) ],
									label 		= "CLASS:",
									name 			= "class",
									on_change	= self._on_change)
		self.layout.add_widget( char_class, 1 )

		self.layout.add_widget( Divider( height = 3 ), 1 )


	def _init_bot_menu( self ):
		layout2 = Layout( [1, 1, 1 ] )
		self.add_layout(layout2)
		layout2.add_widget( Button( "BACK", self._on_back ), 0 )
		layout2.add_widget( Button( "MAIN MENU", self._view ), 1 )
		layout2.add_widget( Button( "OK", self._quit ), 2 )


	def process_event( self, event ):
		# # Handle dynamic pop-ups now.
		# if (event is not None and isinstance(event, MouseEvent) and
		# 		event.buttons == MouseEvent.DOUBLE_CLICK):
		# 	# By processing the double-click before Frame handling, we have absolute coordinates.
		# 	options = [
		# 		("Default", self._set_default),
		# 		("Green", self._set_green),
		# 		("Monochrome", self._set_mono),
		# 		("Bright", self._set_bright),
		# 	]
		# 	if self.screen.colours >= 256:
		# 		options.append(("Red/white", self._set_tlj))
		# 	self._scene.add_effect(PopupMenu(self.screen, options, event.x, event.y))
		# 	event = None

		# Pass any other event on to the Frame and contained widgets.
		return super( MainWindow, self ).process_event( event )


	def _on_change( self ):
		changed = False
		self.save( )

		for key, value in self.data.items( ):
			if key not in form_character or form_character[ key ] != value:
				changed = True
				break

		#self._on_back_button.disabled = not changed


	def _on_back( self ):
		#TODO: return to previous screen
		# self.reset()
		# raise NextScene( )
		pass

	def _view(self):
		# Build result of this form and display it.
		try:
			self.save(validate=True)
			message = "Values entered are:\n\n"
			for key, value in self.data.items():
				message += "- {}: {}\n".format(key, value)
		except InvalidFields as exc:
			message = "The following fields are invalid:\n\n"
			for field in exc.fields:
				message += "- {}\n".format(field)
		self._scene.add_effect(
			PopUpDialog(self._screen, message, ["OK"]))


	def _quit( self ):
		confirm	= PopUpDialog( self._screen, "Are you sure?", [ "Yes", "No" ],
								has_shadow = True, on_close = self._quit_on_yes
								)
		self._scene.add_effect( confirm )
			

	# @staticmethod
	# def _check_email(value):
	# 	m = re.match(r"^[a-zA-Z0-9_\-.]+@[a-zA-Z0-9_\-.]+\.[a-zA-Z0-9_\-.]+$",
	# 				 value)
	# 	return len(value) == 0 or m is not None

	@staticmethod
	def _quit_on_yes(selected):
		# Yes is the first button
		if selected == 0:
			raise StopApplication("User requested exit")



def main( screen, scene ):
	screen.play([Scene([
		Background(screen),
		MainWindow(screen)
	], -1)], stop_on_resize=True, start_scene=scene, )



# if __name__ == 'main':
last_scene = None
while True:
	try:
		Screen.wrapper( main, catch_interrupt = False, arguments = [ last_scene ] )
		sys.exit( 0 )
	except ResizeScreenError as e:
		last_scene = e.scene
