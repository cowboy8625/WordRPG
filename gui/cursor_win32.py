""" Windows sub-module for dealing with the console window cursor """
import sys
import os
import ctypes



class _CursorInfo(ctypes.Structure):
    """ CursorInfo object
    
    Arguments:
        ctypes {[type]} -- [description]
    """
    _fields_ = [("size", ctypes.c_int), ("visible", ctypes.c_byte)]


def hide():
    """ Hide the cursor """
    ci = _CursorInfo()
    handle = ctypes.windll.kernel32.GetStdHandle(-11)
    ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
    ci.visible = False
    ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))


def show():
    """ Show the cursor """
    ci = _CursorInfo()
    handle = ctypes.windll.kernel32.GetStdHandle(-11)
    ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
    ci.visible = True
    ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
