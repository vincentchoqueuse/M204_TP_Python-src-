TP3: Caractérisation statistique
================================

Dans ce TP, nous allons nous familiariser avec les notions de justesse, fidélité et de précision des capteurs. Ces notions sont intimement liées au domaine des statistiques.

Exercice 1: Mesure du biais et de la variance
---------------------------------------------

Nous disposons de trois capteurs de températures nommés respectivement capteur1, capteur2 et capteur3.  Pour chaque capteur, nous effectuons N mesures (x[0],...x[n-1]) à une température fixe dont la valeur vraie est égale à x. Pour caractériser les performances statiques de nos capteurs, nous allons évaluer les erreurs systématiques et accidentelles. Statistiquement, ces deux erreurs sont quantifiées respectivement par le biais et la variance des mesures.

Soit :math:`\widehat{x}_{n}` la moyenne des mesures c-a-d

.. math ::

    \widehat{x}_{n}&=\frac{1}{N}\sum_{n=0}^{N-1}x[n],

le biais et la variance de x[n] sont respectivement donnés par

.. math ::

    b&=x-\widehat{x}_{n},\\
    \sigma^{2}&=\frac{1}{N}\sum_{n=0}^{N-1}(x[n]-\widehat{x}_{n})^{2}

.. tip::

    Avec Python/Numpy, il est possible de calculer la moyenne via la fonction `mean <http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html>`_ et la variance via la fonction `var <http://docs.scipy.org/doc/numpy/reference/generated/numpy.var.html#numpy.var>`_

Dans ce TP, le comportement de chaque capteur est modélisé par une fonction Python. Les différentes fonctions sont disponibles dans le fichier TP3.py et se nomment respectivement **capteur1**, **capteur2** et **capteur3**. A titre d'illustration, pour réaliser N = 50 mesures avec le capteur1 à la température vraie de 25 dégrées, nous utiliserons l'instruction suivante :

.. code ::

    from TP3 import *
    xn=capteur1(25,50)

où xn est un vecteur comportant les 50 mesures.

.. admonition:: Question

    Affichez la sortie des 3 capteurs lorsque la valeur vraie est égale à 40 degrés et N = 100 mesures.

.. admonition:: Question

    Déterminez le biais et la variance de chaque capteur pour une température vraie égale à x = 40 dégrées. Complétez alors le tableau suivant


.. table:: Erreurs systématiques et accidentelles.

    +-----------+-------+----------+
    |  Capteur  | Biais | Variance |
    +===========+=======+==========+
    | Capteur 1 |       |          |
    +-----------+-------+----------+
    | Capteur 2 |       |          |
    +-----------+-------+----------+
    | Capteur 3 |       |          |
    +-----------+-------+----------+

.. admonition:: Question

    A partir des résultats précédents, quantifiez les performances de chaque capteur en terme de justesse, fidélité et précision.

Exercice 2: Lois aléatoires
---------------------------

Loi Normale, Uniforme et Exponentielle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Un processus aléatoire est caractérisé entièrement par sa distribution aléatoire. Il existe un grand nombre de distributions aléatoires (`voir liste <http://docs.scipy.org/doc/scipy/reference/stats.html>`_). Dans cette partie, nous allons nous focaliser sur trois lois aléatoires:

* une loi `Normale <http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html#scipy.stats.norm>`_ (Gaussienne),
* une loi `Uniforme <http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.uniform.html#scipy.stats.uniform>`_,
* une loi `Exponentielle <http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.expon.html#scipy.stats.expon>`_.

.. tip :: Sous Scipy, il est possible de générer N échantillons suivant une loi Normale en utilisant les instructions suivantes

    .. code ::

        from scipy.stats import norm        	#chargement du module norm de scipy

        x=norm.rvs(loc=10,scale=3,size=100)   	#100 échantillons suivant une loi aleatoire Normale de moyenne loc et d'écart type scale


.. admonition:: Question

    Générez successivement N=10000 échantillons aléatoires suivant

    * une loi normale avec les paramètres loc=10 et scale=10,
    * une loi uniforme avec les paramètres loc=-7.32 et scale=34.64,
    * une loi du exponentielle avec les paramètres loc=0 et scale=10,

    puis déterminez à chaque fois la moyenne et la variance des échantillons.

Comme le montre la question précédente, le biais et la variance ne suffisent pas à caractériser entièrement un processus aléatoire. Dans la suite, nous allons afficher l'histogramme des échantillons pour chaque distribution.

.. tip::

    Sous Matplotlib, l'histogramme s'obtient facilement via les instructions

    .. code::

        from pylab import *
        from scipy.stats import norm

        x=norm.rvs(loc=10,scale=3,size=100)
        hist(x,bins=10,histtype='stepfilled')

.. admonition:: Question

    Affichez les histogrammes des échantillons pour chaque distribution.

Theorème de la limite centrale
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Parmi les trois lois précédentes, la loi Normale a une importance particulière. En effet, il est possible de démontrer que la somme de plusieurs lois aléatoires indépendantes et identiquement distribuées tend vers une loi Normale. Ce théorème est souvent utilisé pour justifier le fait que les composantes aléatoires suivent une loi Gaussienne. Nous allons observer ce phénomène en additionnant plusieurs variables aléatoires toutes issues d'une distribution uniforme.

.. admonition:: Question

    Générez N=1000 échantillons d'une variable aléatoire y[n] dont la distribution suit la somme de L=10 distributions uniformes (loc=0, scale=1) c-a-d

    .. math::

        y[n]=\sum_{l=1}^{10} x_{l}[n]

    où les variables aléatoires xl[n] suivent toutes une loi uniforme. Affichez ensuite l'histogramme de y[n].


Intervalle de confiance
^^^^^^^^^^^^^^^^^^^^^^^

En pratique, l'aspect aléatoire des mesures rend difficile leur interprétation. En effet, le niveau confiance accordé aux mesures dépend directement de la valeur de la variance. Si la variance est élevée, il faudra en effet prendre plus de recul sur les informations fournies par le capteur.

Pour quantifier le niveau de confiance à accorder aux mesures, il est courant d'utiliser la notion d'intervalle de confiance. Mathématiquement, l'intervalle de confiance correspond à l'intervalle comportant X% des valeurs mesurées. Cet intervalle dépend implicitement de la loi aléatoire. Dans la littérature, les intervalles de confiance sont souvent déterminés sous l'hypothèse que la loi aléatoire est une loi Normale.

.. plot:: TP3/intervalle.py

.. admonition:: Question

    Générez N=10000 échantillons suivant une loi Normale de paramètres loc=0 et scale=1. Complétez alors le tableau suivant

.. table::

+-------------+-----+------+
| Intervalle  | Nb  | Nb(%)|
+=============+=====+======+
|    [-1 1]   |     |      |
+-------------+-----+------+
|    [-2 2]   |     |      |
+-------------+-----+------+
|    [-3 3]   |     |      |
+-------------+-----+------+

où Nb correspond au nombres d'échantillons compris dans l'intervalle et Nb(%) correspond au nombre Nb/N exprimé en %.

En pratique, l'intervalle I = [x−3σ, x+3σ] est souvent pris comme intervalle de référence. En effet, cet intervalle contient environ 99.7% des mesures.


Références
----------

.. [Python_pour_les_nuls] http://vincentchoqueuse.github.io/Python-pour-les-nuls.
.. [Numpy] https://docs.scipy.org/doc/numpy/reference/routines.html
.. [Scipy] http://docs.scipy.org/doc/scipy/reference/
.. [Matplotlib] http://matplotlib.org/contents.html