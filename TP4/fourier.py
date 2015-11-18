from pylab import *     #importation de pylab pour les graphiques
from numpy import *


f0=10
Fe=1000;

coef_b=[1,0,1/3,0,1/5,0,1/7,0,1/9,0,1/11,0,1/13,0,1/15,0,1/17,0,1/19]
L=len(coef_b)

t=arange(0,0.3,1/Fe)

N=len(t)
x=zeros(N)
for indice in range(L):
    x=x+coef_b[indice]*sin(2*pi*f0*(indice+1)*t)

fig=figure()
fig.patch.set_alpha(0.0)


plot(t,x,label="signal reconstruit")
xlabel('temps (s)')
ylabel('amplitude')

show()
