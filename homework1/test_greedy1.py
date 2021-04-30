from greedy import *

def test_no_ties():
    file = "test_greedy1.txt"
    assert greedy1(file) == 109

def test_with_ties():
    file = "test_greedy1_ties.txt"
    assert greedy1(file) == 6837
