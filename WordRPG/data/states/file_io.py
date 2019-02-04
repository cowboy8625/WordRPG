""" 'load_game' state """

from ...gui.screen import const, Screen
from ...state_machine import State



class Load_Game(State):
    # this is test data block. Need to collect this from various game objects
    FILE_DATA = [
        {
            'name':'PLAYER78',
            'class':'WARRIOR',
            'level':10,
            'timestamp':f'12:24 - 12/12/2019',
        }
    ]


    def __init__(self):
        """ Initiailize class and super class """
        super(Load_Game, self).__init__()

        self.screen = self._init_screen()


    def _init_screen(self, mode='load'):
        screen = Screen()

        # creates standard double line frame around whole screen
        screen.add_frame(size=(80, 30), offset=(0, 0),
                    fgcolor='BLUE', bgcolor='BLACK')

        # add title
        screen.write_string('LOAD GAME', offset=('center', 2),
                    fgcolor='CYAN')

        # create each file data block and draw them to screen
        # for i, file_info in enumerate(FILE_DATA):
        #     file_block = self.add_data_block(i, file_info)

        # add screen prompt
        screen.write_string(f'SELECT FILE SLOT TO {mode.upper()}', offset=('center', 2),
                    fgcolor='CYAN')

        return screen


    # def add_data_block(index, file_info):
    #     """ creates file data block

    #     File screen currently supports 3 file data blocks
    #     """
    #     # each frame needs 8 characters of space, starting at row 2
    #     row = index * 8 + 2

    #     # draw file frame
    #     file_frame = const.SCREENS['file_frame']['array']

    #     # add text from file_info
    #     filename = f'< SAVE GAME {index + 1} >'
    #     main.string_to_char_array(filename)
    #     main.write_to_array(filename, file_frame, col=2, row=0)

    #     # add character name, class, level
    #     # TODO: This data should be gotten from file_info arg
    #     n = f'[NAME]'
    #     c = f'[CLASS]'
    #     l = f'[LEVEL]'
    #     char_text = main.string_to_char_array(f'{n} | {c} | {l}')
    #     main.write_to_array(char_text, file_frame, col=2, row=1)

    #     # add timestamp
    #     # TODO: This data should be gotten from file_info arg
    #     # TODO: Need to right-justify timestamp to frame border width - 1
    #     timestamp = f'12:24 - 12/12/2019'
    #     main.string_to_char_array(filename)
    #     main.write_to_array(timestamp, file_frame, col=52, row=1)

    #     # add file details
    #     # TODO: This data should be gotten from file_info arg
    #     details_txt = 'OTHER RELEVANT DETAILS IN THE FILE THAT NEED TO BE SHOWN'
    #     details_txt = main.string_to_char_array(details_txt)
    #     main.write_to_array(details_txt, file_frame, col=2, row=3)

    #     # draw the file block to the screen
        
    #     main.write_to_array(file_frame, screen,
    #                         transparent=True, col=3, row=row,
    #                         fgcolor='WHITE', bgcolor='BLACK'
    #                         )


    def files(files_info=[{},{},{}], mode='load'):
        """ Create file screen

        File screen is used for loading and saving files in the main menu or in
        game menu
        """
        screen = Screen()

        # creates standard double line frame around whole screen
        screen.add_frame(size=(80, 30), offset=(0, 0),
                    fgcolor='BLUE', bgcolor='BLACK')

        # add title
        screen.write_string('LOAD GAME', offset=('center', 2),
                    fgcolor='CYAN')

        # create each file data block and draw them to screen
        # for i, f in enumerate(files_info):
        #     file_data_block(i, f, screen)

        # add screen prompt
        screen.write_string(f'SELECT FILE SLOT TO {mode.upper()}', offset=('center', 2),
                    fgcolor='CYAN')

        text = f'SELECT FILE SLOT TO {mode.upper()}'
        col = main.center_offset(text, const.SCREEN_SIZE[0])
        main.write_to_array(text, screen, col=col, row=27, fgcolor='RED')

        return screen



    def update_screen(self):
        """ Draws the screen """
        self.screen.draw()


    def on_event(self, event, prev_state):
        """ Handles events that are delegated to this State. """
        self.update_screen()
        self.wait_for_keypress()     
        return 'game'   #prev_state



class Save_Game(State):
    def __init__(self):
        """ Initiailize class and super class """
        super(Save_Game, self).__init__()

        self.screen = self._init_screen()


    def _init_screen(self):
        screen = Screen()
        screen.load_screen('scroll', offset=('center',1), fgcolor='YELLOW')

        screen.write_string('SAVE GAME', offset=('center', 2),
                    fgcolor='CYAN')

        return screen
        

    def update_screen(self):
        """ Draws the screen """
        self.screen.draw()


    def on_event(self, event, prev_state):
        """ Handles events that are delegated to this State. """
        self.update_screen()
        self.wait_for_keypress()
        return 'game'   #prev_state
