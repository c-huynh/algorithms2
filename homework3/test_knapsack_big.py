from knapsack_big import *

def test1():
    file = "test_knapsack1.txt"
    assert knapsack_big(file) == 8

def test2():
    file = "knapsack1.txt"
    assert knapsack_big(file) == 2493893
