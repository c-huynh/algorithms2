# Homework 6

## 2SAT Problem

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

`python 2sat.py`

*answer = 101100*