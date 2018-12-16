import os
import sys
from time import sleep
import textwrap

from .const import *


class MainWindow():
    """[summary]

    Returns:
        [type]: [description]
    """

    def __init__(self):
        self.HEIGHT = 14  # character height of frame
        self.WIDTH = 64  # character width of frame
        self.INNER = self.WIDTH - 2  # character width inside of frame
        self.TITLE = 'WORDRPG'
        self.VERSION = 1.0
        self.HEADER = f'{self.TITLE} - {self.VERSION}'
        self.FOOTER = 'COWBOY GAMING © 2018'

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def center_text(self, text, width, fillchar=' '):
        """[summary]

        Args:
            text (str): Text to be centered
            width (int): [Character width of the field to center text in
            fillchar (str, optional): Defaults to ' '. String character to fill empty space with.

        Returns:
            str: New centered and padded string
        """

        return text.center(width, fillchar)

    def format_contents(self, text, col_text=COL_TEXT, col_frame=COL_FRAME):
        """Formats block of raw text as frame contents

        Args:
            text (str): Multiline string of contents to put inside of frame

        Returns:
            [list]: List of f-strings
        """

        contents = []
        lines = text.splitlines()

        for line in lines:
            if len(line) < 1:
                line = ' ' * (self.INNER)
            else:
                line = self.center_text(line, self.INNER)

            contents.append(f"{col_frame}{FRAME['boxV']}{col_text}{line}{col_frame}{FRAME['boxV']}")

        return contents

    def frame_edge(self, text, lc='boxDR', rc='boxDL', col_text=COL_HEADER, col_frame=COL_FRAME):
        """Builds the top or bottom line of the window frame

        Args:
            text (str): Text to include in middle of frame edge
            lc (str, optional): Defaults to 'boxDR'. Name of key in FRAME to use for left corner of frame edge.
            rc (str, optional): Defaults to 'boxDL'. Name of key in FRAME to use for right corner of frame edge.
            col_text (colorama.fore, optional): Defaults to const.COL_HEADER. Color to use for text
            col_frame (colorama.fore, optional): Defaults to const.COL_FRAME. Color to use for frame

        Returns:
            str: string of frame edge
        """

        _text = f"┤ {text} ├"
        _text = self.center_text(_text, self.INNER, fillchar=FRAME['boxH'])
        _text = _text.replace(text, f'{col_text}{text}{col_frame}')

        return f"{col_frame}{FRAME[lc]}{_text}{col_frame}{FRAME[rc]}"

    def build_frame(self, content, col_frame=COL_FRAME):
        """ Main function to draw the window frame

        Args:
            content (str): Multiline string of contents to put inside of frame

        """

        # top border with header text
        top = self.frame_edge(self.HEADER,
                              'boxDR', 'boxDL',
                              col_text=COL_HEADER,
                              col_frame=col_frame
                              )
        contents = [top]

        # content parsed from multiline string
        mid = self.format_contents(content,
                                   col_text=COL_TEXT,
                                   col_frame=col_frame
                                   )
        contents += mid

        # bottom border with footer text
        btm = self.frame_edge(self.FOOTER,
                              'boxUR', 'boxUL',
                              col_text=COL_FOOTER,
                              col_frame=col_frame
                              )
        contents.append(btm)

        return contents

    def draw(self, content, col_frame=COL_FRAME):
        """ Main function to draw the screen
        """

        contents = self.build_frame(content, col_frame=col_frame)

        self.clear()
        for line in contents:
            print(line)
