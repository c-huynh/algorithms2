"""
The file (knapsack1.txt) describes a knapsack instance, and it has the following
format:

[knapsack_size][number_of_items]

[value_1] [weight_1]

[value_2] [weight_2]

...

For example, the third line of the file is "50074 659", indicating that the second
item has value 50074 and size 659, respectively.

You can assume that all numbers are positive. You should assume that item weights
and the knapsack capacity are integers.
"""

import numpy as np

def knapsack(file):

    with open(file) as f:
        first_line = f.readline().split()
        w, n = int(first_line[0]), int(first_line[1])

        items = []
        for line in f:
            item = line.split()
            items.append((int(item[0]), int(item[1]))) # (value, weight)
    f.close()

    # dynamic programming implementation
    A = np.zeros((w + 1, n + 1))
    for i in range(1, n + 1):
        for x in range(0, w + 1):
            if items[i - 1][1] > x:
                A[x][i] = A[x][i - 1]
            else:
                A[x][i] = max([A[x][i - 1], \
                               A[x - items[i - 1][1]][i - 1] + items[i - 1][0]])

    return A[w, n]

file = "knapsack1.txt"
print(knapsack(file)) # answer = 2493893
