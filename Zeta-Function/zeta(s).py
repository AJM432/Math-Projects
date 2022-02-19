import numpy as np
import matplotlib.pyplot as plt


# Extending domain of zeta function using eta function
#_____________
def eta(s, terms = 1000):
    return sum([((-1)**(k-1))/(k**s) for k in range(1, terms+1)])


def zeta(s):
    return eta(s)/(1-2**(1-s))
#_____________


# Plotting zeros of zeta function at critical line s=1/2+ti
#_____________
x=[]
y=[]
for complex_point in np.linspace(-100, 100, num=10000):
    zeta_evaluated = zeta(1/2 + complex_point*1j)
    x.append(zeta_evaluated.real)
    y.append(zeta_evaluated.imag)

plt.title("Zeros of Zeta Function")
plt.xlabel("Real")
plt.ylabel("Imag")
plt.plot(x, y)
plt.show()
#_____________
