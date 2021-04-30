"""
In this question your task is again to run the clustering algorithm from lecture,
but on a MUCH bigger graph. So big, in fact, that the distances (i.e., edge costs)
are only defined implicitly, rather than being provided as an explicit list.

The format is:

[# of nodes] [# of bits for each node's label]

[first bit of node 1] ... [last bit of node 1]

[first bit of node 2] ... [last bit of node 2]

...

For example, the third line of the file
"0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1" denotes the 24 bits associated
with node #2.

The distance between two nodes u and v in this problem is defined as the Hamming
distance--- the number of differing bits --- between the two nodes' labels.
For example, the Hamming distance between the 24-bit label of node #2 above and
the label "0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1" is 3 (since they differ
in the 3rd, 7th, and 21st bits).

The question is: what is the largest value of k such that there is a k-clustering
with spacing at least 3? That is, how many clusters are needed to ensure that no
pair of nodes with all but 2 bits in common get split into different clusters?
"""

def find_neighbors(node, XOR_results, hamming_points):
    """
    computes all neighbors with distance specified by XOR_results
    key insight: if aXORb = c, aXORc = b
    """
    neighbors = []
    for result in XOR_results:
        if hamming_points[node^result] != False:
            neighbors.append(node^result)
    return neighbors

def hamming_clusters(file):

    with open(file) as f:
        # read data
        first_line = f.readline().split()
        n_nodes, n_bits = int(first_line[0]), int(first_line[1])
        nodes = [] # integer representation of hammings bits
        hamming_points = [False] * pow(2, n_bits) # used to track subset of each node
        for i, line in enumerate(f, 1):
            x = int(line.replace(' ', ''), base=2) 
            nodes.append(x)        
            hamming_points[x] = i
    f.close()

    # determine all possible result of node1 XOR node2 operation
    # that gives a hamming distance of 1 or 2
    XOR_results = []
    for i in range(0, n_bits):
        for j in range(i, n_bits):
            a = 1 << i
            b = 1 << j
            XOR_results.append(a|b)

    names = []
    clusters = 0
    for node in nodes:
        
        # skip node if already processed
        if hamming_points[node] in names:
            continue
            
        queue = [node]
        while queue:
            current = queue.pop()
            subset1 = hamming_points[current]
            neighbors = find_neighbors(current, XOR_results, hamming_points)
            for neighbor in neighbors:
                subset2 = hamming_points[neighbor]
                if subset1 != subset2:
                    queue.append(neighbor)
                    hamming_points[neighbor] = hamming_points[current]
        names.append(hamming_points[node])
        clusters += 1
    return clusters

file = "test_clustering_big.txt"
print(hamming_clusters(file)) # answer: 6118
