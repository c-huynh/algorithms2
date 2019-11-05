import min_heap as mh

def djikstra(graph, n, source):
    """
    Implementation of Djikstra's algorithm with a min heap

    Returns: list of shortest paths to each vertex, (with index corresponding to
             vertex)
    """
    shortest_paths = [float("Inf")] * (n + 1)
    heap = mh.min_heap([(0, source)])
    while heap.size > 0:
        path_length, v = heap.extract_min()
        if shortest_paths[v] == float("Inf"):
            shortest_paths[v] = path_length
            for edge in graph[v]:
                w, edge_length = edge[0], edge[1]
                if shortest_paths[w] == float("Inf"):
                    heap.insert((path_length + edge_length, w))
    return shortest_paths
