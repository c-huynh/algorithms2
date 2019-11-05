"""
In this assignment you will implement one or more algorithms for the 2SAT problem.
Here are 6 different 2SAT instances:

2sat1.txt
2sat2.txt
2sat3.txt
2sat4.txt
2sat5.txt
2sat6.txt

The file format is as follows. In each instance, the number of variables and the
number of clauses is the same, and this number is specified on the first line of
the file. Each subsequent line specifies a clause via its two literals, with a
number denoting the variable and a "-" sign denoting logical "not". For example,
the second line of the first data file is "-16808 75250", which indicates the
clause !x16808 V x75250.

Your task is to determine which of the 6 instances are satisfiable, and which are
unsatisfiable. In the box below, enter a 6-bit string, where the ith bit should
be 1 if the ith instance is satisfiable, and 0 otherwise. For example, if you
think that the first 3 instances are satisfiable and the last 3 are not, then
you should enter the string 111000 in the box below.
"""

import scc

def load_graph(file):
    graph = {}
    with open(file) as f:

        # initialize graph with positive and negative forms for each variable
        n = int(f.readline())
        for i in range(-1 * n, 0):
            graph[i] = []
        for i in range(1, n + 1):
            graph[i] = []

        # add edges
        for line in f:
            constraint = line.split()
            a, b = int(constraint[0]), int(constraint[1])
            graph[-1 * a].append(b)
            graph[-1 * b].append(a)

    f.close()
    return 2 * n, graph

def is_satisfiable(n, graph):
    """
    Implementation of Kosaraju's SCC algorithm to solve the 2SAT problem.

    1) For each constraint (A or B), decompose into equivalent form:
       (!A -> B) and (!B -> A) where -> is a directed edge in a graph.

    2) Contruct a graph from all constraint edges and find the SCCs of the graph.

    3) If there exists a constraint variable A which lies in the same SCC as !A,
       problem is not satisfiable
    """
    leaders = scc.get_SCC(n, graph)
    for i in range(1, int(n / 2) + 1):
        if leaders[i] == leaders[-1 * i]:
            return False
    return True

files = ["2sat1.txt",
         "2sat2.txt",
         "2sat3.txt",
         "2sat4.txt",
         "2sat5.txt",
         "2sat6.txt"]
for file in files:
    n, graph = load_graph(file)
    print(is_satisfiable(n, graph))

# answer = 101100