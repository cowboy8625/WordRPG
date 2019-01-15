""" Module for dymanically building formatted menu arrays with hotkeys """

from . import font



""" 'Menu' dictionary

    Keys:
        text_format     : Dictionary of colorama formatters for menu options
                          and the seperator
        hotkey_format   : Dictionary of colorama formatters for hotkey and
                          their encapsulators
        encap           : Characters to encapsulate the hokey in
        sep             : Characters to place between encapsulated hokey and 
                          the corresponding menu option
        options         : Individual menu options and their associated hotkey
"""

main_menu = {
    'text_format' : {'fgcolor':'CYAN','bgcolor':'BLACK','style':'NORMAL'},
    'hotkey_format' : {'fgcolor':'YELLOW','bgcolor':'BLACK','style':'BRIGHT'},
    'encap' : '()',
    'sep' : ' - ',
    'options' : [
        ('new_game', 'n'), 
        ('load_game', 'l'),
        ('help', 'h'),
        ('credits', 'c'),
        ('quit', 'q'),
    ]
}

new_game = {
    'text_format' : {'fgcolor':'CYAN','bgcolor':'BLACK','style':'NORMAL'},
    'hotkey_format' : {'fgcolor':'YELLOW','bgcolor':'BLACK','style':'BRIGHT'},
    'encap' : '()',
    'sep' : ' - ',
    'options' : [
        ('name', 'n'), 
        ('gender', 'g'),
        # ('race', 'r'),
        ('class', 'c'),
        ('start', 's'),
    ]
}



def create_menu_array(menu, to_upper=True):
    """ Creates a new screen array from supplied menu dictionary
    
    Arguments:
        menu {dict} -- Dictionary for new menu
    
    Keyword Arguments:
        to_upper {bool} -- If True, convert all text to upper-case. (default: {True})
    
    Returns:
        array -- Returns 2D array of formatted characters
    """

    _menu = []

    # convert text to upper case
    for text, hotkey in menu['options']:
        line = []

        if to_upper:
            text, hotkey = text.upper(), hotkey.upper()

        # add formatted hotkey and ecacpsulators to array
        hotkey = f"{menu['encap'][0]}{hotkey}{menu['encap'][1]}"
        for char in hotkey:
            char = font.add_escape(char, **menu['hotkey_format'])
            line.append(char)

        # add formatted seperator and option text
        text = f"{menu['sep']}{text}"
        for char in text:
            char = font.add_escape(char, **menu['text_format'])
            line.append(char)
    
        _menu.append(line)

    return _menu


def get_max_width(menu, option_only=False):
    """ Returns the longest option string in given menu dictionary

    This is a convenience function that can be used to center a block of 
    menu options based on the longest one.
    
    Arguments:
        menu {dict} -- Menu information as a dictionary

    Keyword Arguments:
        option_only {bool} -- If True, only return width of widest option
                              string. Otherwise, include the encapsulators
                              and seperator characters in the total width

    Returns:
        int -- Length of the longest optioon string
    """

    widest = max([len(text) for text, hotkey in menu['options']])

    if option_only:
        return widest
    else:
        return widest + len(menu['encap']) + len(menu['sep'])
