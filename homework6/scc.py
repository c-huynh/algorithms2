def get_ordered_vertices(n, graph):
    """
    Returns a list where values represent the nodes and index represents
    finishing times (of Kosaraju's algorithm)
    """

    # create a reversed graph
    rev_graph = {}
    for u in graph:
        rev_graph[u] = []
    for u in graph:
        for v in graph[u]:
            rev_graph[v].append(u)

    ordered_vertices = []
    times_visited = {}
    for u in rev_graph:
        times_visited[u] = 0

    for i in sorted(rev_graph, reverse=True):
        if times_visited[i] == 0:
            stack = [i]
            while stack:
                v = stack[-1]

                # node visted for first time
                # add all unvisited adjacent vertices to stack
                if times_visited[v] == 0:
                    times_visited[v] += 1
                    for w in rev_graph[v]:
                        if times_visited[w] == 0:
                            stack.append(w)

                # node visited once before
                # record finishing time
                elif times_visited[v] == 1:
                    times_visited[v] += 1
                    ordered_vertices.append(v)
                    stack.pop()

                # every time after second visit
                else:
                    stack.pop()
    return ordered_vertices

def get_SCC(n, graph):
    """
    Returns a dictionary where the key corresponds to the vertex and the value
    corresponds to the leader vertex of that node's SCC group
    """
    order = get_ordered_vertices(n, graph)
    leaders = {}
    for u in graph:
        leaders[u] = None

    while order:
        # search nodes in decreasing order as per Kosaraju's Algorithm
        i = order.pop()
        stack = []
        if leaders[i] == None: # i becomes the leader
            stack = [i]
        while stack:
            v = stack.pop()
            if leaders[v] == None:
                leaders[v] = i
            for w in graph[v]:
                if leaders[w] == None:
                    stack.append(w)
    return leaders
