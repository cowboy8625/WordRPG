from __future__ import division
from asciimatics.effects import BannerText, Print, Scroll
from asciimatics.renderers import ColourImageFile, FigletText, ImageFile
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
import sys



IMG_COWBOY		= r"E:\Python\WordRPG\gui\screen\cowboy_8625.jpg"
IMG_WASTELAND 	= r"E:\Python\WordRPG\gui\screen\wasteland.jpg"
IMG_GROOT 		= r"E:\Python\WordRPG\gui\screen\baby_groot.gif"

COMPANY			= r"COWBOY GAMING © 2018"


def demo(screen):

	scenes = [ ]

	effects = [
		Print(screen, ImageFile( IMG_COWBOY, screen.height - 2,
								colours=screen.colours),
								0,
								stop_frame = 200 ),
		# Print(screen,
		# 		FigletText( COMPANY, font = 'digital' ),
		# 					screen.height // 2 - 3,
		# 					colour = 1,
		# 					bg = 2 if screen.unicode_aware else 0 )
		Print( screen, COMPANY )
	]
	scenes.append(Scene(effects))

	effects = [
		Print(screen,
				FigletText("W A S T E L A N D S",
								font='diamond' if screen.width > 80 else 'banner'),
				screen.height // 2 - 3,
				colour = 1, bg = 2 if screen.unicode_aware else 0 ),
	]
	scenes.append(Scene(effects))


	screen.play(scenes, stop_on_resize=True)


if __name__ == "__main__":
	while True:
		try:
			Screen.wrapper(demo)
			sys.exit(0)
		except ResizeScreenError:
			pass