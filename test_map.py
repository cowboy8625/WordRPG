import os
from time import sleep

from colorama import init as colorama_init

from WordRPG import gui
from WordRPG.map import Map
from WordRPG.map.tiles import BIOMES



# load map image from relative folder
DIRNAME = os.path.dirname(__file__)
FILEPATH = os.path.join(DIRNAME, 'WordRPG', 'Map', 'images')
# TEST_MAP = os.path.join(FILEPATH, 'test_island1.png')
TEST_MAP = os.path.join(FILEPATH, 'test_island2.png')
# TEST_MAP = os.path.join(FILEPATH, 'test_road.png')


if __name__ == '__main__':
    """test data in BIOMES tileset"""
    # print(BIOMES)
    # for k, v in BIOMES.items():
    #     print(k, v)
 
    """ create a 'Map' object using the given image filename and then print
    it to the terminal """
    test_world = Map(TEST_MAP)

    """ prints map as raw tile symbols """
    gui.screen.setup_terminal(title='MAP TEST', size=test_world.size)
    print(test_world)
    sleep(2)

    """ sets up terminal window to expected size and prints the map to the
    terminal with full font formatting """
    gui.screen.setup_terminal(title='MAP TEST', size=test_world.size)
    test_world.show()
    sleep(2)

    """ test map frame """
    size = (40, 20)
    offset = (15, 15)
    test_world.set_map_frame(size, offset=offset)
    gui.screen.setup_terminal(title='MAP FRAME TEST', size=size)
    test_world.show(frame=True, raw=False)
    sleep(2)

    """ test scrolling map frame """
    size = (30, 15)
    gui.screen.setup_terminal(title='MAP FRAME TEST', size=size)
    for r in range(0, 30, 15):
        for c in range(0, 80, 1):
            offset = (c, r)
            test_world.set_map_frame(size, offset=offset)
            test_world.show(frame=True, clear_first=True)
            sleep(1.0 / 15)

    """adding while True loop so terminal stays open until manually closed"""
    while True:
        pass