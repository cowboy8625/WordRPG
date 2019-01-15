""" Placeholder state for main 'game' loop """

from .. import gui
from .States import State



class Game(State):
    def __init__(self):
        """ Initiailize class and super class """
        super(Game, self).__init__()
        self.first_time = True


    def update_screen(self):
        """ Draws the screen """
        gui.main.clear()
        print('THIS IS PLACEHOLDER GAME STATE')
        print('CREATE A NEW SCREEN IN GUI.SCREEN')
        print('(W) - NORTH')
        print('(A) - WEST')
        print('(S) - SOUTH')
        print('(D) - EAST')
        print()
        print('(C) - CRAFTING')
        print('(G) - GATHER RESOURCES')
        print('(I) - INVENTORY')
        print()
        print('(X) - TEST COMBAT')
        print('(K) - TEST DEATH')
        print()
        print('(ESC) - MENU')


    def start(self):
        """ Subloop """
        gui.main.clear()
        print('SARTING NEW GAME')
        print('ENTERING MAIN GAME STATE IN A MOMENT...')
        self.pause(pause_time=2)


    def gather(self):
        """ Subloop """
        print('GATHERING RESOURCES...')
        self.pause(pause_time=1)


    def move(self,dir='north'):
        print(f'MOVING {dir.upper()}...')
        self.pause(pause_time=1)


    def combat(self):
        """ Subloop """
        # This is where any pre-combat functions would be handled before
        # transitioning into the combat state
        print('ENTERING COMBAT...')
        self.pause(pause_time=1)
        return 'combat'


    def death(self):
        """ Subloop """
        # This is where any pre-death functions would be handled before
        # transitioning into the 'death' state
        print('PLAYER IS DEAD...')
        self.pause(pause_time=1)
        return 'death'


    def on_event(self, event, prev_state):
        """ Handles events that are delegated to this State. """
        if event == 'start' or self.first_time:
            self.start()
            self.first_time = False

        self.update_screen()

        while True:
            key = self.get_key_press()
            if key == 'g':
                self.gather()
                self.update_screen()
            if key == 'w' or key == 'up':
                self.move(dir='north')
                self.update_screen()
            if key == 'a' or key == 'left':
                self.move(dir='west')
                self.update_screen()
            if key == 's' or key == 'down':
                self.move(dir='south')
                self.update_screen()
            if key == 'd' or key == 'right':
                self.move(dir='east')
                self.update_screen()
            if key == 'c':
                return 'crafting'
            if key == 'i':
                return 'inventory'
            if key == 'x':
                return self.combat()
            if key == 'k':
                return self.death()
            if key == 'esc':
                return 'game_menu'

        return self