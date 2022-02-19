# Plots the motion of the head of a line segment moving across a point

from matplotlib import pyplot as plt
import numpy as np

# evaluates x_2, equiv to b
def eval_b_positive_root(l, a, c, f):
    return a+abs(l)/(1+(f/(c-a))**2)**(1/2)


# negative solution of quadratic equation for b (not used for now)
def eval_b_negative_root(l, a, c, f):
    return a-abs(l)/(1+(f/(c-a))**2)**(1/2)


# # evaluates y_2, equiv to e
def eval_e(a, b, c, f):
    return (f*(a-b))/(a-c)


# # starting parameters
a = 0  # start of tail of object
l = 47  # length
f = 12  # height of vertical bar that object is resting on
c = (l**2-f**2)**(1/2) # assuming line segment is at a=0 # distance of vertical bar from (0, 0), pythagorean theorem

b_evaluated = eval_b_positive_root(l, a, c, f)
e_evaluated = eval_e(a, b_evaluated, c, f)


# plots parametric equations
b_list = []
e_list = []
num_points_linspace = 1000
# c≠a, only applies to special case of right triangle ACF
for x in np.linspace(a, c-0.0001, num_points_linspace):
    a = x
    b = eval_b_positive_root(l, a, c, f)
    e = eval_e(a, b, c, f)
    b_list.append(b)
    e_list.append(e)

plt.plot(b_list, e_list, label=f"[x=B, y=E], L={l}, F={f}")

# the formula for the turning point graphed as a vertical line
turning_point = eval_b_positive_root(
    l, c-(l**(2/3)*f**(4/3)-f**2)**(1/2), c, f)
# print(turning_point)
plt.plot([turning_point, turning_point], [0, l], label='Critical Point P_x')

plt.xlabel("Horizontal Distance (cm)")
plt.ylabel("Vertical Distance (cm)")
plt.title("Parametric Curve of Line Segment")
plt.legend(loc='lower left')
plt.show()
