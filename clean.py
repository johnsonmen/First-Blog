import pandas as pd
import numpy as np


def range_hyphen_remover(range_value):
    '''
    removes the hyphen from a range value and returns the average of the bounds
    input: range value - a string with a hyphen
    output: value - the average of the upperbounds and lowerbounds in the range
    '''
    if '–' in range_value:
        range_value = range_value.split('–')
        value = float(range_value[0]) + float(range_value[1]) / 2
    else:
        value float(range_value)
    return value
