from pylab import *     #importation de pylab pour les graphiques
from numpy import *
from scipy.signal import lti,step

m=0.5
wn=1
K=5

tf=lti([K],[(1/(wn**2)),2*m/wn,1])
t,y=step(tf)

fig=figure()
fig.patch.set_alpha(0.0)

plot(t,y)
xlabel("temps(s)")
ylabel("sortie")
plot([0,14],[K,K],'--',color="k")
text(11, K+0.05, 'Valeur finale')
show()