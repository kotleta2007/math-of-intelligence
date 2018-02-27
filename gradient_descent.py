# Implementing gradient descent
# 27.02.2018

# We get an N-by-2 matrix of data.
# We want to draw the line of best fit.

# error metric -> Sum of Squares Error

import random

points1 = [(1,2),(2,3),(3,4)]

b_rand = random.random()
m_rand = random.random()

# First, we compute the Error
def compute_error(b, m, points):
    error = 0
    xs = []
    ys = []
    for i in range(0,len(points)):
        xs.append(points[i][0])
        ys.append(points[i][1])

    #for i in range(0,len(points)):
    #    error +=
    print(xs,ys)

compute_error(b_rand,m_rand,points1)
