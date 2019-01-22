import os
from colorama import init as colorama_init

from WordRPG import gui
from WordRPG.Map import Map
from WordRPG.Map.tiles import BIOMES



# get list of .txt filenames in the 'screens' subfolder
DIRNAME = os.path.dirname(__file__)
FILEPATH = os.path.join(DIRNAME, 'WordRPG', 'Map', 'images')
TEST_MAP = os.path.join(FILEPATH, 'test_island2.png')


if __name__ == '__main__':
    # sets up terminal window to expected size
    gui.Screen.setup_terminal(title='MAP TEST', size=(100,50))

    # create a 'Map' object using the given image filename and then print
    # it to the terminal
    test_map = Map(TEST_MAP)
    test_map.show()

    # adding while True loop so terminal stays open until manually closed
    while True:
        pass
