__author__ = "byteme8bit"

# File imports

# Module imports
import math


# Rounds the passed attack up by x amount (100, 10, 1, 0.1, 0.01, etc)
def rnd(num_to_round, x=0.01):
    """
    Rounds passed number to specified decimal point
    :param num_to_round: any attack that needs to be rounded
    :param x: value to be rounded to. Default is 0.01, rounding to nearest thousandth.
    :return: returns rounded value
    """
    return math.ceil(num_to_round / x) * x
