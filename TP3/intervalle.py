from pylab import *     #importation de pylab pour les graphiques
from numpy import *
from scipy.signal import lti, step
from scipy.stats import norm



N=10000;

x=norm.rvs(loc=10,scale=1,size=N)

n=linspace(6,14,1000)

fig=figure()
fig.patch.set_alpha(0.0)

plot(n, norm.pdf(n,loc=10,scale=1),'r--', label='densité de probabilité')
hist(x,bins=20,histtype='stepfilled',normed=True, label="histogramme")
plot([9,9],[0,0.6],'-',color='r')
plot([11,11],[0,0.6],'-',color='r')
annotate ('', (9,0.45), (11,0.45), arrowprops={'arrowstyle':'<->'})
text(9.5, 0.47, 'Intervalle')
legend()
show()

