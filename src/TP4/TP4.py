from numpy import *
from pylab import *
from scipy.signal import *
from scipy.stats import norm

Fe=1000
t=arange(0,1,1/Fe)
b=norm.rvs(loc=0,scale=0.9,size=len(t))

def signal1():
    x=sawtooth(2*pi*10*t,0)+b
    return t,x

def signal2():
    x=square(2*pi*100*t)+b
    return t,x

def signal3():
    x=sin(2*pi*30*t)+b
    return t,x

