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

game_menu = {
    'text_format' : {'fgcolor':'CYAN','bgcolor':'BLACK','style':'NORMAL'},
    'hotkey_format' : {'fgcolor':'YELLOW','bgcolor':'BLACK','style':'BRIGHT'},
    'encap' : '()',
    'sep' : ' - ',
    'options' : [
        ('save_game', 's'), 
        ('load_game', 'l'),
        ('help', 'h'),
        ('main menu', 'm'),
        ('quit', 'q'),
        ('back to game', 'esc'),
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
