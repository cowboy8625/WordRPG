from colorama import init as colorama_init

from WordRPG import gui
from WordRPG.Map import Map
from WordRPG.Map.tiles import BIOMES



if __name__ == '__main__':
    # doing this in a while True loop so that the terminal window stays open
    while True:
        # sets up terminal window to expected size
        gui.Screen.setup_terminal(title='MAP TEST', size=(100,50))

        # create a 'Map' object using the given image filename and then print
        # it to the terminal
        test_map = Map(r"E:\Python\WordRPG\WordRPG\Map\images\test_island2.png")
        test_map.show()
