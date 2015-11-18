from pylab import *     #importation de pylab pour les graphiques
from numpy import *
from scipy import signal

m=0.5
wn=1
K=1

tf=signal.lti([K],[(1/(wn**2)),2*m/wn,1])
t,y=signal.step(tf)

fig=figure()
fig.patch.set_alpha(0.0)

plot(t,y)
plot([0,14],[K,K],'--',color="k")
annotate ('', (3.6, K-0.01), (3.6, K+0.17), arrowprops={'arrowstyle':'<->'})
text(3.8, 1.08, 'D')
show()