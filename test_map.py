import os
from time import sleep

from WordRPG.gui.screen import Screen
from WordRPG.map import Map



if __name__ == '__main__':
    """ create a 'Map' object using the given image filename and then print
    it to the terminal """
    test_world = Map('test_island2')

    """ prints map as raw tile symbols """
    Screen.setup_terminal(title='MAP TEST', size=test_world.size)
    print(test_world)
    sleep(2)

    """ sets up terminal window to expected size and prints the map to the
    terminal with full font formatting """
    Screen.setup_terminal(title='MAP TEST', size=test_world.size)
    test_world.show()
    sleep(2)

    """ test map frame """
    size = (40, 20)
    offset = (15, 15)
    test_world.set_map_frame(size, offset=offset)
    Screen.setup_terminal(title='MAP FRAME TEST', size=size)
    test_world.show(frame=True, raw=False)
    sleep(2)

    """ test scrolling map frame """
    size = (80, 30)
    Screen.setup_terminal(title='MAP FRAME TEST', size=size)
    for r in range(0, 30, 15):
        for c in range(0, 80, 1):
            offset = (c, r)
            test_world.set_map_frame(size, offset=offset)
            test_world.show(frame=True, clear=True, raw=True)
            sleep(1.0 / 30)

    """ test scrolling map frame """
    size = (80, 30)
    Screen.setup_terminal(title='MAP FRAME TEST', size=size)
    for r in range(0, 30, 15):
        for c in range(0, 80, 1):
            offset = (c, r)
            test_world.set_map_frame(size, offset=offset)
            test_world.show(frame=True, clear=True,)
            sleep(1.0 / 30)

    """adding while True loop so terminal stays open until manually closed"""
    while True:
        pass