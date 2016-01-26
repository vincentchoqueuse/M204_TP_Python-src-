from TP2 import *


t,y=reponse_capteur(10)
vf=y[-1]

print("la valeur est %f" % vf)



plot(t,y)
plot([0,t[-1]],[vf,vf])  #afficher la valeur finale
show()