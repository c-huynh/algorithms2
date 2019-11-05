from djikstra import *

def test_djikstra():
    answers = [float("Inf"), 0, 2, 3, 4, 6]
    source = 1
    n = 5
    graph = {
                1: [(2, 2), (3, 4)],
                2: [(3, 1), (4, 2)],
                3: [(5, 4)],
                4: [(5, 2)],
                5: []
            }

    shortest_paths = djikstra(graph, n, source)
    for i in range(n + 1):
        assert shortest_paths[i] == answers[i]
