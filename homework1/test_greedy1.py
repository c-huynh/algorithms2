from greedy1 import *

def test_no_ties():
    file = "test_greedy1.txt"
    assert greedy(file) == 109

def test_with_ties():
    file = "test_greedy1_ties.txt"
    assert greedy(file) == 6837
