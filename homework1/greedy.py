"""
The file (jobs.txt) describes a set of jobs with positive and integral weights and lengths.
It has the format:

[number_of_jobs]

[job_1_weight] [job_1_length]

[job_1_weight] [job_1_length]

...

For example, the third line of the file is "74 59", indicating that the second
job has weight 74 and length 59.

You should NOT assume that edge weights or lengths are distinct.
"""

def greedy1(file):
    """
    Greedy algorithm based on decreasing values of weight - length
    """
    order = []
    with open(file) as f:
        next(f)
        for line in f:
            i = line.split()
            # order is a list of tuples with values (w - l, w, l)
            order.append((int(i[0])-int(i[1]), int(i[0]), int(i[1])))
    order.sort(reverse=True)
    finishing_time = 0
    sum = 0
    for job in order:
        finishing_time += job[2]
        sum += job[1] * finishing_time

    return sum
    
def greedy2(file):
    """
    Greedy algorithm based on decreasing values of weight/length
    """
    order = []
    with open(file) as f:
        next(f)
        for line in f:
            i = line.split()
            # order is a list of tuples with values (w/l, w, l)
            order.append((int(i[0])/int(i[1]), int(i[0]), int(i[1])))
    order.sort(reverse=True)
    finishing_time = 0
    sum = 0
    for job in order:
        finishing_time += job[2]
        sum += job[1] * finishing_time

    return sum

# assignment solution
input_file = "jobs.txt"

print(greedy1(input_file)) # answer = 69119377652
print(greedy2(input_file)) # answer = 67311454237
