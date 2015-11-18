from numpy import *                     #import de numpy
from scipy.signal import periodogram    #import du module signal de scipy
from pylab import *                     #import de matplotlib.pylab

Fe=1000                         #fréquence d'échantillonnage
t = arange(0, 0.5, 1/Fe)        #creation de la base temps avec numpy
s = sin(2*pi*10*t)              #creation d'une sinusoide à 10hz
f,Pxx=periodogram(s,Fe)         #calcul de la transformée de Fourier

fig=figure()
fig.patch.set_alpha(0.0)
plot(f,Pxx)                     #Affichage via la fonction plot de Matplotlib
xlabel('Frequence (Hz)')        #définition de l'axe des abscisses
ylabel('Module')                #définition de l'axe des ordonnées
show()                          #affichage des courbes