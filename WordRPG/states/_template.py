""" Template for making new game states with GUI and event handlers """

from .. import gui
from .states import State



class Template(State):
    def __init__(self):
        """ Initiailize class and super class """
        super(Template, self).__init__()
        self.first_time = True


    def update_screen(self):
        """ Draws the screen """
        gui.main.clear()
        print('THIS IS A TEMPLATE SCREEN')
        print('CREATE A NEW SCREEN IN GUI.SCREEN')
        print('(1) - SUBLOOP 1')
        print('(2) - SUBLOOP 2')
        print('(3) - NEW EVENT')
        print('(ESC) - BACK')


    def sub1(self):
        """ Subloop """
        gui.main.clear()
        print('THIS IS A SUBLOOP')
        print('RETURN TO MAIN LOOP AFTER 3 SECONDS')
        self.pause(pause_time=3)


    def sub2(self):
        """ Subloop """
        print('THIS IS A SUBLOOP')
        print('PRESS KEY TO RETURN TO MAIN LOOP')
        self.wait_for_keypress()


    def on_event(self, event):
        """ Handles events that are delegated to this State. """
        self.update_screen()

        while True:
            key = self.get_key_press()
            if key == '1':
                self.sub1()
                self.update_screen()
            if key == '2':
                self.sub2()
                self.update_screen()
            if key == '3':
                return 'new_state'
            if key == 'esc':
                return 'prev'

        return self
