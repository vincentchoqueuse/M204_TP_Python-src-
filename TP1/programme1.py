from pylab import *     #importation de pylab pour les graphiques

x=arange(0,2,0.1)
y=[0.0,0.25,0.51,0.75,1.01,1.24,1.51,1.74,2.01,2.26,2.51,2.76,3.02,3.24,3.51,3.75,4.0,4.26,4.51,4.75]

theta = np.polyfit(x, y, 1) #regression lineaire
yr=theta[0]*x+theta[1]      #mesurande obtenue en effectuant une regression de mesure

fig=figure()
fig.patch.set_alpha(0.0)
plot(x,y,'o',label="points de mesure")
plot(x,yr,label="regression")
legend()