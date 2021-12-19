import numpy as np
import matplotlib.pyplot as plt

def dydx(y,xo,h=0.001):

    return (y(xo+h) - y(xo-h))/(2*h) # derivative


def scarborough(error,n=10):

    eS = 0.5*10**(2-n)*100
    if error < eS: return True
    else: return False


def bisection(y,xN):

    sb = False
    leftX = xN[0]
    rightX = xN[-1]
    print("xl: {:.6f}\txu: {:.6f}\txR: {:.6f}\tabs error: NaN".format(leftX,rightX,( leftX + rightX )/2))

    while not sb: # scarborough
        if y(leftX)*y(rightX)<0: xM = ( leftX + rightX )/2
        else: raise ValueError(f"Chosen interval: {xN} contains no roots!")
        if y(xM)*y(leftX)<0:
            eA = abs((xM - rightX)/(xM+1E-7))*100 # Add 1e-7 to avoid division with Zero error
            rightX = xM
        elif y(xM)*y(rightX)<0:
            eA = abs((xM - leftX)/(xM+1E-7))*100
            leftX = xM
        sb = scarborough(eA)
        print("xl: {:.6f}\txu: {:.6f}\txR: {:.6f}\tabs error: {:.4f}".format(leftX,rightX,xM,eA))

    xBis = (leftX+rightX)/2
    print(f"Bisection: {xBis}")
    return xBis
    

def newtonraphson(y,xN,guess):

    sb = False
    xi = guess  # initial guess
    print("x0: {:.6f}\tabs error: NaN".format(xi))

    while not sb:
        xii = xi - y(xi)/dydx(y,xi)
        eA = abs((xii - xi)/(xii+1E-7))*100
        xi = xii
        sb = scarborough(eA)
        print("xi: {:.6f}\tabs error: {:.4f}".format(xii,eA))

    print(f"Newton-Raphson: {xii}")
    return xii

def fixedpoint(guess):

    g = lambda t: -pow(2.0/3.0*np.exp(t),0.5) # ! needs to be specified ! [SENSITIVE METHOD]
    sb = False
    xi = guess # initial guess

    while not sb:
        xo = xi
        xi = g(xo)
        eA = abs((xi - xo)/(xi+1E-7))*100
        sb = scarborough(eA)
        print("xo: {:.6f}\txi: {:.6f}\tabs error: {:.4f}".format(xo,xi,eA))
    
    print(f"Fixed-point: {xi}")
    return xi

def plot_root(y,xN,xRoot,plotname=""):

    xPlot = np.linspace(xN[0],xN[-1],100) # plot function in given range
    yPlot = [y(i) for i in xPlot]
    plt.figure()
    plt.plot(xPlot,yPlot,color="#6fb1cd")
    plt.plot(xRoot,y(xRoot),"ro",ms=5) # plot root
    plt.axhline(y=0.0,color="#e5958f",ls="--")
    plt.title(plotname)