"""
The file (clustering1.txt) describes a distance function (equivalently, a complete graph with edge
costs). It has the following format:

[number_of_nodes]

[edge 1 node 1] [edge 1 node 2] [edge 1 cost]

[edge 2 node 1] [edge 2 node 2] [edge 2 cost]

...

There is one edge (i, j) for each choice of 1 <= i < j <= n, where n is the number
of nodes.

For example, the third line of the file is "1 3 5250", indicating that the distance
between nodes 1 and 3 (equivalently, the cost of the edge (1,3)) is 5250. You can
assume that distances are positive, but you should NOT assume that they are distinct.

Your task in this problem is to run the clustering algorithm from lecture on this
data set, where the target number k of clusters is set to 4. What is the maximum
spacing of a 4-clustering?
"""

import union_find

def largest_k_clusters(file, k):

    with open(file) as f:
        n_nodes = int(f.readline())

        # initialize subsets for union find
        subsets = {}
        for i in range(1, n_nodes + 1):
            subsets[i] = union_find.Subset(i)

        # create sorted list of edges
        # tuple in the form (cost, node1, node2)
        edges = []
        for line in f:
            edge = [int(x) for x in line.split()]
            edges.append((edge[2], edge[0], edge[1]))
        edges.sort()

        # clustering algorithm based on Kruskal
        n_clusters = n_nodes
        i = 0
        while n_clusters != k: # assumes k < nodes
            subset1 = union_find.find(subsets, edges[i][1])
            subset2 = union_find.find(subsets, edges[i][2])
            if (subset1 != subset2):
                union_find.union(subsets, subset1, subset2)
                n_clusters -= 1
            i += 1

        # determine max spacing (cost of first edge with different subsets)
        for edge in edges:
            subset1 = union_find.find(subsets, edge[1])
            subset2 = union_find.find(subsets, edge[2])
            if (subset1 != subset2):
                max_spacing = edge[0]
                break
    return max_spacing

file = "clustering1.txt"
k = 4
print(largest_k_clusters(file, k)) # answer = 106
