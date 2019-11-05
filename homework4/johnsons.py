"""
In this assignment you will implement one or more algorithms for the all-pairs
shortest-path problem. Here are data files describing three graphs:

g1.txt
g2.txt
g3.txt

The first line indicates the number of vertices and edges, respectively. Each
subsequent line describes an edge (the first two numbers are its tail and head,
respectively) and its length (the third number). NOTE: some of the edge lengths
are negative. NOTE: These graphs may or may not have negative-cost cycles.

Your task is to compute the shortest shortest path. Precisely, you must first
identify which, if any, of the three graphs have no negative cycles. For each
such graph, you should compute all-pairs shortest paths and remember the smallest
one (i.e., compute
 
min of u,v E V, d(u, v) where d(u, v) denotes the shortest-path distance from
u to v.

If each of the three graphs has a negative-cost cycle, then enter "NULL" in the
box below. If exactly one graph has no negative-cost cycles, then enter the length
of its shortest shortest path in the box below. If two or more of the graphs have
no negative-cost cycles, then enter the smallest of the lengths of their shortest
shortest paths in the box below.
"""

from bellman_ford import bellman_ford
from djikstra import djikstra

def get_min(A):
    paths = []
    for i in A:
        paths.append(min(i))
    return min(paths)

def load_graph(file):
    graph = {}
    with open(file) as f:
        first_line = f.readline().split()
        n, m = int(first_line[0]), int(first_line[1])
        for i in range(1, n + 1):
            graph[i] = []
        for line in f:
            edge = line.split()
            graph[int(edge[0])].append((int(edge[1]), int(edge[2])))
    f.close()
    return graph, n, m

def johnsons(file):
    """
    Implementation of Johnsons all pairs shortest paths algorithm
    
    Returns: list of list of all path lengths to each node, where index refers 
             to vertex
    """
    graph, n, m = load_graph(file)
    
    # prep graph for bellman ford
    graph[0] = []
    for i in range(1, n + 1):
        graph[0].append((i, 0))

    # determine vertex weights
    print("Running Bellman-Ford...")
    weights = bellman_ford(graph, n, 0)
    if weights == "Negative cycle detected":
        return False

    # create re-weighted graph
    print("Creating re-weighted graph...")
    del graph[0]
    graph_reweighted = {}
    for u in range(1, n + 1):
        if graph_reweighted.get(u) == None:
            graph_reweighted[u] = []
        for v, w in graph[u]:
            graph_reweighted[u].append((v, w + weights[u] - weights[v]))

    # run Djikstra using every vertex as a source
    print("Running Djikstra...")
    all_shortest_paths = [[float("Inf")]] * (n + 1)
    for source in range(1, n + 1):
        if source % 50 == 0:
            print("on vertex # " + str(source))
        all_shortest_paths[source] = djikstra(graph_reweighted, n, source)

    # re-adjust results to show true lengths
    print("Adjusting lengths...")
    for u in range(1, n + 1):
        for v in range(1, n + 1):
            if all_shortest_paths[u][v] != float("Inf"):
                all_shortest_paths[u][v] += weights[v] - weights[u]

    return all_shortest_paths


file = "g1.txt"
all_shortest_paths = johnsons(file)
if all_shortest_paths == False:
    print("Negative cycles detected")
else:
    print(get_min(all_shortest_paths))

# answer g1.txt = False (negative cycles detected)
# answer g2.txt = False (negative cycles detected)
# answer g3.txt = -19
