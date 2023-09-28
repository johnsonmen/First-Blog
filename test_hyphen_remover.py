import pandas as pd
import numpy as np
import sys
from clean import range_hyphen_remover

epsilon = sys.float_info.epsilon

def test_hyphen_remover_1_2():
    assert(range_hyphen_remover('1–2') - 1.5 < epsilon)

def test_hyphen_remover_1_3():
    assert(range_hyphen_remover('1–3') == 2)

def test_hyphen_remover_10_200():
    assert(range_hyphen_remover('10–200') == 105)

def test_hyphen_remover_float1():
    assert(range_hyphen_remover('1.5–2.5') == 2)

def test_hyphen_remover_float2():
    assert(range_hyphen_remover('34.0–39.2') - 36.6 < epsilon)

def test_hyphen_remover_float3():
    assert(range_hyphen_remover('51.2–54.3') - 52.75 < epsilon)

def test_hyphen_remover_str():
    assert(range_hyphen_remover('40.5') - 40.5 < epsilon)

