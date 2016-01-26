
TP2: Dynamique des systèmes
===========================

Dans ce TP, nous allons analyser la dynamique des capteurs. Cette dynamique est le plus souvent quantifiée au moyen de la réponse indicielle (réponse à une entrée de type échelon). En particulier, la réponse indicielle permet de quantifier le temps de réponse et le premier dépassement du système.

.. tip :: Dans ce TP; il est conseillé d'utiliser l'environnement *ipython*


Exercice 1: Analyse de la dynamique d'un capteur de déplacement
-----------------------------------------------------------------------

Les capteurs de déplacement mesurent la distance parcourue par un objet. Ils peuvent également servir à mesurer la hauteur et la largeur d'un objet.

La fonction **reponse_capteur** disponible dans le fichier TP2.py simule le comportement d'un capteur de déplacement passif. La réponse du capteur à un échelon d'amplitude unitaire s'obtient de la manière suivante

.. code ::

    from TP2 import *
    t,v=reponse_capteur(1)
    plot(t,v)

où l'argument de la fonction correspond à l'amplitude du déplacement en m (ici 1m), *v* correspond au vecteur contenant la réponse indicielle et *t* correspond au vecteur temps.

.. admonition:: Question

    Affichez la réponse indicielle pour un déplacement de 10 mm.


Mesure de la valeur finale
^^^^^^^^^^^^^^^^^^^^^^^^^^

La valeur finale correspond à la dernière valeur de la réponse indicielle.

.. plot:: TP2/valeur_finale.py

.. tip::

    Avec Numpy, le dernier élement d'un vecteur s'obtient en spécifiant comme index -1.

.. admonition:: Question

    Déterminez la valeur finale, vf.



Mesure du temps de réponse: Technique graphique
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dans cette partie, nous allons utiliser une technique graphique pour la détermination du temps de réponse à :math:`\pm 5 \%`. Pour déterminer le temps de réponse, nous allons tout d'abord superposer deux droites sur la figure de la réponse indicielle. Ces deux droites auront respectivement pour équation :

.. math ::
    y &= 0.95 \times vf\\
    y &= 1.05 \times vf

.. plot:: TP2/tr.py

.. tip::

    Pour tracer la droite située à :math:`+ 5 \%` de la valeur finale sous Matplotlib, nous utiliserons l'instruction suivante:

    .. code ::

        plot([t[0],t[-1]],[0.95*vf,0.95*vf])


.. admonition:: Question

    Tracez les droites situées à :math:`+\pm 5 \%` de la valeur finale puis déduisez-en le temps de réponse du capteur.


Mesure du temps de réponse: Technique directe
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tip::

    Pour déterminer le temps de réponse à :math:`\pm 5 \%` directement, il est possible d'utiliser directement la méthodologie suivante

    .. code ::

        vect_tr=where((v>1.05*vf)|( v<0.95*vf))[0] #Identification des éléments pour lesquelles la réponse indicielle est supérieure ou égale à 1.05 × vf OU inférieure ou égale à 0.95 × vf
        index_tr=vect_tr[-1]                        #Récupération du dernier élément du vecteur
        tr=t[index_tr]                              #Recherche du temps tr situé à l'index index_tr

.. admonition:: Question

    Déterminez le temps de réponse en utilisant la méthodologie précédente.

Dans le plupard des cas, la dynamique d'un système peut être approché par la dynamique soit d'un système de premier ordre ou d'un système de second ordre.

Exercice 2: Analyse des systèmes de premier ordre
-------------------------------------------------

Un système de premier ordre est décrit par une équation différentielle du type :

.. math ::

    v(t)+\tau \frac{dv(t)}{dt}=Ke(t)

où e(t) et v(t) correspondent respectivement à l'entrée et à la sortie du système. Le paramètre :math:`\tau` correspond à la constante de temps du système (en seconde) et K représente le gain statique.

Pour simuler un système décrit par une équation différentielle en Python, il faut spécifier sa fonction de transfert dans le domaine de Laplace. La fonction de transfert d'un premier ordre est donnée par

.. math ::

    F(p)=\frac{K}{1+\tau p}

.. tip::

    En python, la déclaration d'une fonction de transfert s'obtient en utilisant la fonction `lti <http://docs.scipy.org/doc/scipy-0.16.0/reference/generated/scipy.signal.lti.html>`_ du module signal de Scipy. Une fois déclarée, il est possible de simuler la réponse du système à un échelon unitaire (réponse indicielle) en utilisant la fonction *step* du module signal. Par exemple, l'affichage de la réponse indicielle d'un système de premier ordre de gain statique K=0.5 et de constante de temps :math:`\tau=3` s'obtient via les instructions suivantes


    .. code ::

        from scipy.signal import lti,step        # chargement des fonctions lti et step du module signal de Scipy
        ft=lti([0.5], [3, 1])    # déclaration de la fonction de transfert
        t,yout=step(ft)          # Réponse Indicielle (RI)
        plot(t,yout)                    # affichage de la RI


Dans la suite de cet exercice, nous allons considerer un capteur de température dont le comportement est décrit par un système de premier ordre de paramètres **K = 0.23** et **tau=0.004 s**.



.. admonition:: Question

    Affichez la réponse indicielle du capteur. Déterminez alors la valeur finale puis le temps de réponse à :math:`\pm 5%`.

.. admonition:: Question

    En généralisant la méthodologie utilisée à la question précédente, déterminez le temps nécessaire pour obtenir 63% de la valeur finale, 86% de la valeur finale. Completez alors le tableau suivant:

.. table::

    +-------+---------+------------+
    |       |    tr   |   tr/tau   |
    +=======+=========+============+
    |  63%  |         |            |
    +-------+---------+------------+
    |  86%  |         |            |
    +-------+---------+------------+
    |  95%  |         |            |
    +-------+---------+------------+


Exercice 3: Analyse des systèmes de second ordre
------------------------------------------------

Un système de second ordre est décrit par une équation différentielle du type :

.. math ::

    v(t)+\left(\frac{2m}{\omega_{n}}\right) \frac{dv(t)}{dt}+\left(\frac{1}{\omega_{n}^{2}}\right) \frac{d^{2}v(t)}{dt^{2}}=Ke(t)

où K, m et wn et v(t) correspondent respectivement au gain statique, à l'amortissement et à la pulsation propre (en rad/s) du système.

Dans la suite de cet exercice, nous allons considerer un capteur dont le comportement est décrit par un système de second ordre de paramètres **K = 1.5**, **m = 0.5** et **wn=10 rad/s**.

.. admonition:: Question

    Déterminez la fonction de transfert F(p) du capteur puis affichez sa réponse indicielle.

.. admonition:: Question

    Déterminez la valeur finale ainsi que le temps de réponse du système à :math:`\pm 5%`.

.. plot:: TP2/programme2.py

Pour m < 1, la réponse indicielle présente un dépassement (voir figure ci-dessus). La valeur du premier dépassement D dépend de la valeur finale du système, vf. En pratique, nous préférons utiliser la notion de premier dépassement relatif et exprimer cette valeur en pourcent. Le premier dépassement relatif est alors défini par


.. math::

    D_r(\%) &= \frac{D}{vf}\times 100

où D correspond à la valeur du premier dépassement (absolu).


.. admonition:: Question

    Pour le capteur défini précedemment, déterminez la valeur du premier dépassement relatif, Dr(%).

Les valeurs du temps de réponse, tr, et du premier dépassement relatif, Dr(%), dépendent des paramètres m et ωn du système. Nous allons dans la question suivante évaluer les performances de plusieurs capteurs ayant des paramètres m différents.


.. admonition:: Question

    Complétez le tableau suivant :

.. table::

    +-------------+-----+-----+---------------+---------+
    |             |  wn |  m  |  tr (+/- 5%)  |  Dr(%)  |
    +=============+=====+=====+===============+=========+
    |  Capteur 1  |  10 | 0.3 |               |         |
    +-------------+-----+-----+---------------+---------+
    |  Capteur 2  |  10 | 0.5 |               |         |
    +-------------+-----+-----+---------------+---------+
    |  Capteur 3  |  10 | 0.7 |               |         |
    +-------------+-----+-----+---------------+---------+
    |  Capteur 4  |  10 |  1  |               |         |
    +-------------+-----+-----+---------------+---------+
    |  Capteur 5  |  10 | 1.3 |               |         |
    +-------------+-----+-----+---------------+---------+
    |  Capteur 6  |  10 | 1.6 |               |         |
    +-------------+-----+-----+---------------+---------+



Réferences
----------

.. [Python_pour_les_nuls] http://vincentchoqueuse.github.io/Python-pour-les-nuls.
.. [Numpy] https://docs.scipy.org/doc/numpy/reference/routines.html
.. [Scipy] http://docs.scipy.org/doc/scipy/reference/
.. [Matplotlib] http://matplotlib.org/contents.html