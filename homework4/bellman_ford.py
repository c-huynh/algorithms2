def bellman_ford(graph, n, source):
    """
    Implementation of the Bellman-Ford algorithm.

    Returns: list of shortest paths to each vertex, (with index corresponding to
             vertex) if no negative cycles present

    Returns: None if there are negative cycles
    """

    # initialize all distances from source to infinity
    dist = [float("Inf")] * (n + 1)
    dist[source] = 0

    # determine shortest paths with max n - 1 edges, where n = number of nodes
    for i in range (1, n - 1):
        for u in graph.keys():
            for edge in graph[u]:
                v, w = edge[0], edge[1]
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

    # run cycle once more to detect negative edges
    for u in graph.keys():
        for edge in graph[u]:
            v, w = edge[0], edge[1]
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                return "Negative cycle detected"
    return dist
