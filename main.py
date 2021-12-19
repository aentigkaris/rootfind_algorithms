"""
Bisection, Newton-Raphson & Fixed-point root finding algorithms and root plotting.

Ntigkaris E. Alexandros
"""

from functions import bisection,newtonraphson,fixedpoint,plot_root
import numpy as np
import matplotlib.pyplot as plt

def main():

    y = lambda x: 2*np.exp(x) - 3*x**2
    xN = [-1,1]

    rootBisection = bisection(y,xN)
    plot_root(y,xN,rootBisection,"Bisection: y=2exp(x)-3x^2")

    rootNewton = newtonraphson(y,xN,guess=0.1)
    plot_root(y,xN,rootNewton,"Newton: y=2exp(x)-3x^2")

    # 2*exp(x) - 3*x^2 = 0
    # => x^2 = (2/3)*exp(x)
    # => x = - sqrt[(2/3)*exp(x)]
    # => x = g(x)
    # -0.603744 = g(-0.603744)

    xtest = np.linspace(-10,10,1000)
    y1test = xtest
    y2test = -pow(2.0/3.0 * np.exp(xtest),0.5)
    plt.figure()
    plt.plot(xtest,y1test,color="red")
    plt.plot(xtest,y2test,color="blue")
    plt.axvline(x=rootNewton,ls="--",color="green")
    plt.title("Fixed point method explanation")
    plt.legend(["y=x","y=-sqrt[(2/3)*exp(x)]"])

    rootFixed = fixedpoint(guess=-0.2)
    plot_root(y,xN,rootFixed,"FixedPoint: y=2exp(x)-3x^2")
    plt.show()

main()