# Homework 5

## Travelling Salesman Problem

In this assignment you will implement one or more algorithms for the traveling
salesman problem, such as the dynamic programming algorithm covered in the video
lectures. Here is a data file describing a TSP instance.

tsp.txt

The first line indicates the number of cities. Each city is a point in the plane,
and each subsequent line indicates the x- and y-coordinates of a single city.

The distance between two cities is defined as the Euclidean distance --- that is,
two cities at locations (x, y) and (z, w) have distances sqrt((x - z)^2 + (y - w)^2)
between them.

In the box below, type in the minimum cost of a traveling salesman tour for this
instance, rounded down to the nearest integer.

`python tsp.py`

*answer = 26442*

solution has rounding error