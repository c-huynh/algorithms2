from prim import *

def test_prim():
    input = "test_prim.txt"
    assert prim(input) == -86

def test_prim_negatives():
    input = "test_prim_negatives.txt"
    assert prim(input) == 2
