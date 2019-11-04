"""
The file (knapsack_big.txt) describes a knapsack instance, and it has the following
format:

[knapsack_size][number_of_items]

[value_1] [weight_1]

[value_2] [weight_2]

...

For example, the third line of the file is "50074 834558", indicating that the
second item has value 50074 and size 834558, respectively. As before, you should
assume that item weights and the knapsack capacity are integers.

This instance is so big that the straightforward iterative implemetation uses an
infeasible amount of time and space. So you will have to be creative to compute
an optimal solution. One idea is to go back to a recursive implementation, solving
subproblems --- and, of course, caching the results to avoid redundant work ---
only on an "as needed" basis. Also, be sure to think about appropriate data structures
for storing and looking up solutions to subproblems.
"""

def knapsack_big(file):
    items = []
    subproblems = {}

    # read data
    with open(file) as f:
        first_line = f.readline().split()
        w, n = int(first_line[0]), int(first_line[1])
        for line in f:
            item = line.split()
            items.append((int(item[0]), int(item[1]))) # (value, weight)
    f.close()

    stack = [(n, w)]

    while stack:
        current = stack[-1]
        i, x = current[0], current[1]
        current_value = subproblems.get(current)
        
        # solution already solved
        if current_value != None:
            stack.pop()
            
        # base case
        elif i == 0:
            subproblems[current] = 0
            
        # item is too big for current bag
        elif current[1] < items[i - 1][1]:
            sub_value = subproblems.get((i - 1, x))
            if sub_value == None:
                stack.append((i - 1, x))
            else:
                subproblems[current] = sub_value
        else:
            sub1_value = subproblems.get((i - 1, x))
            if sub1_value == None:
                stack.append((i - 1, x))
            sub2_value = subproblems.get((i - 1, x - items[i - 1][1]))
            if sub2_value == None:
                stack.append((i - 1, x - items[i - 1][1]))
            if (sub1_value != None) and (sub2_value != None):
                subproblems[current] = max([sub1_value, \
                                            sub2_value + items[i - 1][0]])
                stack.pop()

    return subproblems[current]

file = "knapsack_big.txt"
print(knapsack_big(file)) # answer = 4243395
