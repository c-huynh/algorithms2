from hamming_clusters import *

# Tests for hamming distance function
def test_hamming_distance1():
    a = "1 1 1 1"
    b = "0 0 0 0"
    assert hamming_distance(a, b) == 4

def test_hamming_distance2():
    a = "1 1 1 1"
    b = "1 1 1 1 "
    assert hamming_distance(a, b) == 0

def test_hamming_distance3():
    a = "1 1 0 1"
    b = "1 1 1 1 "
    assert hamming_distance(a, b) == 1

# Tests for hamming clusters function
def test_hamming_clusters_1():
    file = "test_clustering_big.txt"
    assert hamming_clusters(file) == 989
