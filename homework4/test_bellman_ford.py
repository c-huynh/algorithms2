from bellman_ford import *

def test_neg_cycles():
    source = 1
    n = 5 # number of vertices
    graph = {
                1: [(2, 1)],
                2: [(3, 4)],
                3: [(5, -5)],
                4: [(2, -4)],
                5: [(4, 3)]
            }

    assert bellman_ford(graph, n, source) == "Negative cycle detected"

def test_no_neg_cycles():
    answers = [None, 0, 2, 3, 4, 6]
    source = 1
    n = 5 # number of vertices
    graph = {
                1: [(2, 2), (3, 4)],
                2: [(3, 1), (4, 2)],
                3: [(5, 4)],
                4: [(5, 2)],
                5: []
            }

    shortest_paths = bellman_ford(graph, n, source)
    if shortest_paths:
        assert len(shortest_paths) == len(answers)
        for i in range(1, len(shortest_paths)):
            assert shortest_paths[i] == answers[i]
