"""
The file (edges.txt) describes an undirected graph with integer edge costs. It
has the format:

[number_of_nodes] [number_of_edges]

[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]

[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]

...

For example, the third line of the file is "2 3 -8874", indicating that there is
an edge connecting vertex #2 and vertex #3 that has cost -8874.

You should NOT assume that edge costs are positive, nor should you assume that
they are distinct.

Your task is to run Prim's minimum spanning tree algorithm on this graph.

You should report the overall cost of a minimum spanning tree --- an integer,
which may or may not be negative --- in the box below.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn)
time implementation of Prim's algorithm should work fine. OPTIONAL: For those of
you seeking an additional challenge, try implementing a heap-based version. The simpler approach, which should already give you a healthy speed-up, is to maintain relevant edges in a heap (with keys = edge costs). The superior approach stores the unprocessed vertices in the heap, as described in lecture. Note this requires a heap that supports deletions, and you'll probably need to maintain some kind of mapping between vertices and their positions in the heap.
"""

class min_heap(object):
    def __init__(self, A):
        # heap array has empty first element
        self.heap = self.build_min_heap(A)
        self.size = len(self.heap) - 1

    def heapify(self, A, i):
        # i is the root to heapify from
        n = len(A)
        smallest = i
        l = 2 * i
        r = 2 * i + 1

        if (l < n) and (A[l] < A[smallest]):
            smallest = l
        if (r < n) and (A[r] < A[smallest]):
            smallest = r
        if smallest != i:
            A[i], A[smallest] = A[smallest], A[i]
            self.heapify(A, smallest)

    def build_min_heap(self, A):
        A = [None] + A
        n = len(A)//2
        for i in range(n, 0, -1):
            self.heapify(A, i)
        return A

    def bubble_up(self, i):
        # i is the index of node to bubble up
        parent = i // 2
        while (parent > 0) and (self.heap[parent] > self.heap[i]):
            self.heap[parent], self.heap[i] = \
            self.heap[i], self.heap[parent]
            i = parent
            parent = i // 2

    def insert(self, i):
        # add to end of heap
        self.heap.append(i)
        self.size += 1

        # bubble up to restore heap invariants
        i = self.size
        self.bubble_up(i)

    def extract_min(self):
        if self.size >= 1:
            # swap root and bottom-most, right-most child and remove last element
            child = self.size
            self.heap[1], self.heap[child] = self.heap[child], self.heap[1]
            min = self.heap.pop()
            self.size -= 1

            # restore heap invariants
            self.heapify(self.heap, 1)
            return min
        else:
            return None

    def delete(self, i):
        # i is the index of node to delete
        if self.size >= 1:
            child = heap.size
            self.heap[i], self.heap[child] = self.heap[child], self.heap[i]
            self.heap.pop()

            # restore heap invariants
            if (i != child):
                self.bubble_up(i)
                self.heapify(self.heap, i)
            self.size -= 1

def prim(input_file):
    """
    implementation of Prim's algorithm using a min heap
    """
    graph = {}
    vertices_visited, num_visited = [None], 0
    with open(input_file) as f:
        graph_size = f.readline().split()
        num_vertices = int(graph_size[0])
        num_edges = int(graph_size[1])

        for i in range(1, num_vertices + 1):
            graph[i] = []
            vertices_visited.append(False)
        for line in f:
            i = line.split()
            graph[int(i[0])].append((int(i[2]), int(i[1]))) #(cost, vertex)
            graph[int(i[1])].append((int(i[2]), int(i[0]))) #(cost, vertex)

    # initialize first entry in heap
    initial_entry = []
    for i in graph[1]:
        initial_entry.append((i[0], i[1])) #(cost, vertex)

    # initialize heap
    heap = min_heap(initial_entry)
    vertices_visited[1] = True
    num_visited += 1

    sum = 0
    while num_visited < num_vertices:
        cost, u = heap.extract_min()
        if not vertices_visited[u]:
            vertices_visited[u] = True
            sum += cost
            num_visited += 1
            for w in graph[u]:
                heap.insert((w[0], w[1]))
    return sum

input_file = "edges.txt"
print(prim(input_file))  # answer = -3612829
