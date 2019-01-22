import os
from colorama import init as colorama_init

from WordRPG import gui
from WordRPG.map import Map
from WordRPG.map.tiles import BIOMES



# load map image from relative folder
DIRNAME = os.path.dirname(__file__)
FILEPATH = os.path.join(DIRNAME, 'WordRPG', 'Map', 'images')
TEST_MAP = os.path.join(FILEPATH, 'test_island2.png')


if __name__ == '__main__':
    # test data in BIOMES tileset
    # print(BIOMES)
    # for k, v in BIOMES.items():
    #     print(k, v)

    # create a 'Map' object using the given image filename and then print
    # it to the terminal
    test_world = Map(TEST_MAP)

    # sets up terminal window to expected size
    gui.Screen.setup_terminal(title='MAP TEST', size=(100,50))

    # # prints 2D array of tile symbls
    # print(test_world)

    # # prints the map to the terminal with full formatting
    test_world.show()

    # adding while True loop so terminal stays open until manually closed
    while True:
        pass
