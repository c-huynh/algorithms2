from hamming_clusters import *

# Tests for hamming clusters function
def test_hamming_clusters_1():
    file = "test_clustering_big.txt"
    assert hamming_clusters(file) == 989
