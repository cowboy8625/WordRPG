from time import sleep

from gui.const import *
from gui.main import MainWindow, setup_terminal
from gui import screens



if __name__ == '__main__':
	setup_terminal( )
	window = MainWindow( )
	window.draw( screens.screen_start )

	sleep( 30 )

	window.draw( screens.screen_class )

	sleep( 3 )

	window.draw( screens.screen_mage, col_frame = Fore.YELLOW )