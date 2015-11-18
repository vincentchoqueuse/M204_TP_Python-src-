from numpy import *
from scipy import signal
from pylab import *


def reponse_capteur(entree):
    K=250
    m=0.35
    wn=2000

    tf=signal.lti([entree*K],[(1/(wn**2)),2*m/wn,1])
    
    t,y=signal.step(tf)
    return t,y


def show_tr():
    t,y=reponse_capteur(1)
    plot([0,0.010],[200,200])
    plot(t,y)
