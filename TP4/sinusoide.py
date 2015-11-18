from pylab import *     #importation de pylab pour les graphiques
from numpy import *


a=1
phi=0
f0=4
Fe=1000;

tmax=0.5

t=arange(0,tmax,1/Fe)
x=sin(2*pi*f0*t)

t2=arange(0,tmax,1/20)
x2=sin(2*pi*f0*t2)

fig=figure()
fig.patch.set_alpha(0.0)


plot(t,x, label="sinusoide à temps continue")
stem(t2,x2,'r',label="sinusoide échantilonnée")
xlabel('temps')
ylabel('amplitude')

annotate ('', (3/20,-0.1), (4/20,-0.1), arrowprops={'arrowstyle':'<->'})
text(3.35/20, -0.2, 'Te')
legend()
show()
