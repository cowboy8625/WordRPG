""" Base classes for states

    State - Most abstract base class for all states
    Screen- Base class for all states that update the screen. Includes static
            methods for flow control and keyboard event handling:
                pause()
                get_key_press()
                wait_for_keypress()
                get_entry()
   Menu - Base class for a screen that is a menu with multiple options leading
            to different screens or states on a certain keypress
   Confirm - Base class for confirmation states
"""

from time import sleep, time

# https://pypi.org/project/keyboard/
import keyboard

from .. import gui



class AbstractState:
    """ Abstract base class for 'states' """

    def __init__(self):
        pass


    def on_event(self, event):
        """ Handles events that are delegated to this State. """
        pass


    def __repr__(self):
        """ Leverages the __str__ method to describe the State. """
        return self.__str__()


    def __str__(self):
        """ Returns the name of the State. """
        return self.__class__.__name__



class State(AbstractState):
    """ Abstract class for states that involve drawing/updating the screen """

    def __init__(self):
        super(State, self).__init__()


    @staticmethod
    def pause(pause_time=3):
        """ Pauses for a set amount of time
        
            TODO: Add timeout keyword to wait_for_keypress when keyboard.read_event
                can accept same keyword to allow user to press any key and end the
                method immediately
        """
        timeout = time() + pause_time
        while True:
            if time() > timeout:
                break


    @staticmethod
    def wait_for_keypress(suppress=True):
        """ Waits for any key to be pressed

         TODO: Add timeout keyword to wait_for_keypress when keyboard.read_event
            can accept same keyword to allow user to press any key and end the
            method immediately

        """
        while True:
            key_event = keyboard.read_event()
            if key_event.event_type == 'up':
                break


    @staticmethod
    def get_key_press():
        """ Waits for and returns the name of a key release event

        Note:
            Using event_type 'up' here to only return the event name when a key
            is released, otherwise we end up getting duplicate events when a key
            is pressed and released. I felt waiting for release will feel more 
            correct than triggering the event when the key is pressed. 
        
        Returns:
            string -- Name of the key that has been released
        """
        while True:
            key_event = keyboard.read_event(suppress=True)
            ## only capture key events when key is released.  This prevents 
            ## a second key name event from being captured
            if key_event.event_type == 'up':
                # need to convert key_event.name to lowercase to avoid the event
                # handler being non-responsive if caps-lock is on
                return str(key_event.name).lower()


    @staticmethod
    def get_entry(suppress=True, until='enter'):
        """ Returns a string entered by user

        Listens for and collects keyboard events until the the 'until' key.
        These events are then parsed into a string and returned.
        
        Keyword Arguments:
            until {str} -- Key that stops the event redorder (default: {'enter'})
        
        Returns:
            string -- Parsed string entered by user
        """
        events = keyboard.record(until=until)
        generator = keyboard.get_typed_strings(events)
        string = next(generator)
        
        return string


    def update_screen(self):
        """ Placeholder method """
        pass



class Menu(State):
    """[summary]
    
    Arguments:
        Screen {function} -- Function that draws/updates the screen

    Keywords:
        options {dict} -- dictionary of hotkeys and state events to trigger

    Returns:
        string -- String name of next state event to proceed to
    """

    def __init__(self, screen, options={}):
        """ Initiailize class and super class """
        super(Menu, self).__init__()
        self.screen = screen
        self.options = options


    def update_screen(self):
        """ Draws the screen """
        gui.main.clear()
        self.screen()


    def on_event(self, event):
        """ Handles events that are delegated to this State. """
        self.update_screen()

        while True:
            key = self.get_key_press()
            if key in self.options.keys():
                self.options[key]()

        return self



# class Info(Screen):
#     """ Abstract class for an info screen """
#     def __init__(self, screen, next_state, timeout=None):
#         super(Splash, self).__init__()

#         self.screen = screen
#         self.next_state = next_state


#     def update_screen(self):
#         """ Draws the screen """
#         gui.main.clear()
#         gui.screen.splash()


#     def on_event(self, event):
#         """ Handle events that are delegated to this State. """
#         self.update_screen()
#         if timeout is not None:
#             self.pause(pause_time=3)
#         else:
#             self.wait_for_keypress()

#         return next_state


class Confirm(State):
    """ Abstract class for a confirmation screen """
    def __init__(self, title, message, next_state, accept='y', reject='n'):
        """ Initiailize class and super class """
        super(Confirm, self).__init__()
        self.title = title
        self.message = message
        self.accept = accept
        self.reject = reject
        self.next_state = next_state


    def update_screen(self):
        """ Draws the screen """
        gui.main.clear()
        print(f'{self.message}')


    def on_event(self, event, prev_state):
        """ Handle events that are delegated to this State. """
        self.update_screen()

        while True:
            key = self.get_key_press()
            if key == self.accept:
                return self.next_state
            elif key == self.reject or key == 'esc':
                return prev_state

        return self
