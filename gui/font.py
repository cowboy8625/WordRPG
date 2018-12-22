""" Module for formatting text

    Notes:
        Fore/Back:
            'BLACK', 'BLUE', 'CYAN', 'GREEN', 'LIGHTBLACK_EX', 'LIGHTBLUE_EX',
            'LIGHTCYAN_EX', 'LIGHTGREEN_EX', 'LIGHTMAGENTA_EX', 'LIGHTRED_EX',
            'LIGHTWHITE_EX', 'LIGHTYELLOW_EX', 'MAGENTA', 'RED', 'RESET',
            'WHITE', 'YELLOW'
        Style:
            'BRIGHT', 'DIM', 'NORMAL', 'RESET_ALL'

"""
from colorama import Fore, Back, Style



def get_formatter(fgcolor = None, bgcolor = None, style = None):
    """ Create formatter using colorama

    Convenience method to get colorama values using string arguement and return
    the string formatter for foreground color, background color, and style

    Arguments:
        fgcolor {str} -- String name of colorama.Fore color
        bgcolor {str} -- String name of colorama.Back color
        style {str} -- String name of colorama.Style
    
    Returns:
        [dict] -- Dictionary congtaining string formatters for 'fgcolor',
                'bgcolor', and 'style'
    """

    results = [ ]
    for a, b in zip([fgcolor, bgcolor, style], [Fore, Back, Style]):
        if isinstance(a, str):
            results.append(getattr( b, a.upper()))
        else:
            results.append('')

    return {'f':results[0],'b':results[1],'s':results[2]}


def add_escape( char, fgcolor = None, bgcolor = None, style = None ):
    """ Create formatter using colorama

    Convenience method to get colorama values using string arguement and return
    the string formatter for foreground color, background color, and style

    Arguments:
        fgcolor {str} -- String name of colorama.Fore color
        bgcolor {str} -- String name of colorama.Back color
        style {str} -- String name of colorama.Style
    
    Returns:
        [dict] -- Dictionary congtaining string formatters for 'fgcolor',
                'bgcolor', and 'style'
    """
    
    a, b, c = [getattr(b, a.upper()) if isinstance(a, str) else '' for a, b in zip([fgcolor, bgcolor, style], [Fore, Back, Style])]
    d, e, f = (Fore.RESET, Back.RESET, Style.RESET_ALL)

    return f'{a}{b}{c}{char}{d}{e}{f}'
