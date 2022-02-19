# Finds roots of a function given f(x) and f'(x)
import math


def f(x):
    return math.sin(x)


# must define the derivative of f(x)
def derivative_f(x):
    return math.cos(x)


def next_alpha(a_n):
    return (a_n*derivative_f(a_n)-f(a_n))/(derivative_f(a_n))


alpha=2 # initial arbitrary value
num_iterations = 10
# alpha gets closer to root of f(x)
for a in range(num_iterations):
    print(alpha)
    alpha = next_alpha(alpha)
