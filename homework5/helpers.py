"""
Helper functions for the traveling salesman algorithm Implementation
"""

import numpy as np
import math

def create_adj_matrix(file):
    """
    Creates an adjacency matrix of distances between nodes.
    """
    with open(file) as f:
        n = int(f.readline())     # n is number of nodes
        pts = []                  # stores the (x, y) coordinates of each node
        for line in f:
            point = line.split()
            pts.append((int(float(point[0])), int(float(point[1]))))
    f.close()
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                matrix[i][j] = math.sqrt(pow(pts[i][0] - pts[j][0], 2) + \
                                         pow(pts[i][1] - pts[j][1], 2))
    return n, matrix

def remove_from_subset(s, k):
    """
    Removes a node from a subset
    s = an integer that represents the binary mask of a subset
    k = the kth bit (node) to be removed from the subset - assumes the nodes
    are named starting from 0 to n - 1, where n is the total number of nodes
    """
    return s & ~ (1 << k)

def subset_from_binary(s, n):
    """
    s = an integer that represents the binary mask of a subset
    n = total number of nodes
    Assuming nodes are named from 0 to n - 1.
    Returns a list L, of nodes that the binary mask represents.
    """
    L = []
    for i in range(n):
        if (s >> i) % 2 == 1:
            L.append(i)
    return L

def subset_to_binary(L, n):
    """
    L = list, subset of all nodes (names are ordered from 0 to n - 1)
    n = total number of nodes
    Returns integer s, that represents the binary mask of L
    """
    s = 0
    for i in L:
        s |= (1 << i)
    return s

def get_subsets(n):
    """
    Returns a list of subsets (in binary representation) sorted from smallest
    subset size to largest
    only subsets containing the first node is returned
    n = number of vertices
    """
    # sort subsets by number of set bits in its binary mask
    subsets = [(set_bits(i), i) for i in range(0, pow(2, n)) if i % 2 == 1]
    return [i[1] for i in sorted(subsets)]

def set_bits(i):
    """
    Returns the number of set bits in the binary form of integer i
    """
    n = 0
    while i != 0:
        if i % 2 == 1:
            n += 1
        i >>= 1
    return n

# file = "test_tsv.txt"
# create_adj_matrix(file)

# s = 21
# k = 4
# print(remove_from_subset(s, k))

# s = 21
# n = 6
# print(subset_from_binary(s, n))

# L = [0, 2, 4]
# n = 6
# print(subset_to_binary(L, n))

# i = 0
# print(count_set_bits(i))
# print(get_subsets(4))
