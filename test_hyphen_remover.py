import pandas as pd
import numpy as np
import sys
from clean import range_hyphen_remover

epsilon = sys.float_info.epsilon

def test_hyphen_remover_1_2():
    '''
    tests function range_hyphen_remover with int bounds and float output
    input: string '1–2'
    output: float 1.5
    '''
    assert(range_hyphen_remover('1–2') - 1.5 < epsilon)

def test_hyphen_remover_1_3():
    '''
    tests function range_hyphen_remover with int bounds and output
    input: string '1–3'
    output: int 2
    '''
    assert(range_hyphen_remover('1–3') == 2)

def test_hyphen_remover_float1():
    '''
    tests function range_hyphen_remover with float bounds and int output
    '''
    assert(range_hyphen_remover('1.5–2.5') == 2)

def test_hyphen_remover_float2():
    '''
    tests function range_hyphen_remover with float bounds and output
    input: string '34.0–39.2'
    output: float 36.6
    '''
    assert(range_hyphen_remover('34.0–39.2') - 36.6 < epsilon)

def test_hyphen_remover_float3():
    '''
    tests function range_hyphen_remover with float bounds and output
    input: string '51.2–54.3'
    output: float 52.75
    '''
    assert(range_hyphen_remover('51.2–54.3') - 52.75 < epsilon)

def test_hyphen_remover_str():
    '''
    tests function range_hyphen_remover with float input and output
    input: string '40.5'
    output: float 40.5
    '''
    assert(range_hyphen_remover('40.5') - 40.5 < epsilon)

