"""
In this assignment you will implement one or more algorithms for the traveling
salesman problem, such as the dynamic programming algorithm covered in the video
lectures. Here is a data file describing a TSP instance.

tsp.txt

The first line indicates the number of cities. Each city is a point in the plane,
and each subsequent line indicates the x- and y-coordinates of a single city.

The distance between two cities is defined as the Euclidean distance --- that is,
two cities at locations (x, y) and (z, w) have distances sqrt((x - z)^2 + (y - w)^2)
between them.

In the box below, type in the minimum cost of a traveling salesman tour for this
instance, rounded down to the nearest integer.
"""
import numpy as np
from helpers import *
from math import pow, floor

def shortest_tour(file):
    """
    Implementation of the traveling salesman problem using dyammic programming
    """
    # create adjacency from file
    print("Creating adjacency matrix...")
    n, dists = create_adj_matrix(file)

    # generate all relevant subsets sorted from smallest size to largest
    print("Generating subsets...")
    subsets = get_subsets(n)

    # initialize array to store all sub-problem solutions
    subprobs = np.full((int(pow(2, n)), n), np.inf)
    subprobs[1][0] = 0 # base case (path from source to source)

    # solve relevant subproblems
    print("Solving subproblems...")
    for s in subsets:
        nodes = subset_from_binary(s, n)
        for j in nodes:
            results = []
            if j != 0:
                for k in nodes:
                    if k != j:
                        results.append(subprobs[remove_from_subset(s, j)][k] + \
                                       dists[k][j])
                if results:
                    subprobs[s][j] = min(results)

    # find all path lengths returning to node 0
    print("Returning home...")
    results = []
    for j in range(1, n):
        results.append(subprobs[subsets[-1]][j] + dists[j][0])

    return min(results)

file = "tsp.txt"
print(shortest_tour(file)) # answer = 26442
