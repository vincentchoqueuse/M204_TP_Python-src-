from numpy import *
from pylab import *
from scipy.stats import norm

def capteur1(x,N):
    xn=norm.rvs(loc=x+0.1,scale=0.01,size=N)
    return xn

def capteur2(x,N):
    xn=norm.rvs(loc=x+0.01,scale=0.2,size=N)
    return xn

def capteur3(x,N):
    xn=norm.rvs(loc=x+0.07,scale=0.1,size=N)
    return xn