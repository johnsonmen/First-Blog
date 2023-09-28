import pandas as pd
import numpy as np


def range_hyphen_remover(range_value):
    '''
    This function removes the hyphen from the range of values with a hyphen and returns the average of the bounds
    Input - range value - a string with a hyphen
    Output - the average of the two numbers in the range
    '''
    if '–' in range_value:
        range_value = range_value.split('–')
        return (float(range_value[0]) + float(range_value[1])) / 2
    else:
        return float(range_value)
