TP4: Introduction au traitement du signal
=========================================

Dans ce TP, nous allons nous familiariser avec les bases du traitement du signal. Le traitement du signal est un discipline qui trouve ses racines dans les travaux de `Joseph Fourier <https://en.wikipedia.org/wiki/Joseph_Fourier>`_, scientifique du siècle des Lumières. Joseph Fourier a montré qu'il était possible d'exprimer n'importe quel signal comme la somme de plusieurs sinusoïdes. Cette décomposition est particulièrement utilisée lorsqu'il s'agit d'analyser des signaux.

Exercice 1: Signal sinusoidal
-----------------------------

Un signal sinusoidal est un signal continu défini par l'équation

.. math ::

    x(t)&=a\sin(2\pi f_{0} t+\phi)

où a, phi et f0 correspondent respectivement à l'amplitude, la phase et la fréquence de la sinusoïde.


Génération du signal
^^^^^^^^^^^^^^^^^^^^

.. plot:: TP4/sinusoide.py

Lorsque nous travaillons avec des outils numériques, la base temps t n'est pas continue mais discrete. La façon la plus simple de discretiser la base temps consiste à prélever un échantillon du signal continu tous les Te secondes. Le nombre Te est appelé période d'échantillonnage. La fréquence d’échantillonnage Fe est définie par

.. math::

    Fe=\frac{1}{Te}


.. tip::

    Sous Numpy, il est possible de générer facilement une version discretisée de la base temps en utilisant les instructions:

    .. code ::

        from numpy import *

        Fe=100  #Fréquence d'échantillonnage.
        t=arange(0,1,1/Fe)  #vecteur allant de 0 à 1 par pas de Te=1/Fe.

.. admonition:: Question

    Générez un signal sinusoidal échantillonné ayant comme paramètres a=1, phi=0 et f0=10. La fréquence d'échantillonnage sera fixée à Fe=1000 Hz. Affichez ensuite le signal avec Matplotlib.


Influence de la fréquence d'échantillonnage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Intuitivement, nous pouvons penser qu'une bonne restitution de la sinusoïde nécessite nécessairement une fréquence d'échantillonnage Fe élevée. Nous allons voir que cela dépend en fait du ratio Fe/f0.


.. admonition:: Question

    En modifiant votre programme précédent, complétez le tableau suivant.

.. table::

    +-----------+--------------+-------------------+-----------------+
    |     Fe    | Fréquence f0 | Période T0 réelle | Période mesurée |
    +===========+==============+===================+=================+
    |   1000Hz  |    10 Hz     |                   |                 |
    +-----------+--------------+-------------------+-----------------+
    |   1000Hz  |   500 Hz     |                   |                 |
    +-----------+--------------+-------------------+-----------------+
    |   1000Hz  |   990 Hz     |                   |                 |
    +-----------+--------------+-------------------+-----------------+


* La deuxième ligne du tableau illustre la valeur limite du ratio Fe/f0. Lorsque Fe=2f0, l'échantillonnage n'est pas capable de "capturer" le mouvement de la sinusoïde. Ce phénomène est similaire à celui observable dans cette `vidéo <https://www.youtube.com/watch?v=jQDjJRYmeWg>`_.
* La dernière ligne du tableau montre que la fréquence de la sinusoïde est repliée lorsque Fe<2f0. Nous parlons alors de **repliement du spectre** (aliasing). Ce phénomène est similaire à celui observable dans cette `vidéo <https://www.youtube.com/watch?v=jHS9JGkEOmA>`_.

Ces résultats sont formalisés par le **théorème de Shannon**.

.. important::

    Pour échantillonner correctement un signal dont la fréquence maximale est fmax, il faut nécessairement respecter la condition

    .. math ::

        Fe> 2f_{max}

A titre d'exemple, comme la fréquence maximale perceptible par l'oreille est d'environ fmax=20kHz, la fréquence d'échantillonnage utilisée dans les supports numériques audios est généralement égale à 44.1KHz.

Exercice 2: Décomposition en série de Fourier
---------------------------------------------

Fourier a démontré qu'il était possible de décomposer un signal périodique de fréquence f0 en une somme de plusieurs sinusoïdes de fréquence kf0. Mathématiquement, n'importe quel signal périodique s(t) peut donc s'exprimer sous la forme:

.. math::

    s(t)&=a_{0}+\sum_{k=1}^{\infty} a_{k}\cos(2\pi k f_{0}t)+\sum_{k=1}^{\infty} b_{k}\sin(2\pi k f_{0}t)

.. plot:: TP4/fourier.py

Le tableau suivant présente la valeur des coefficients ak et bk pour plusieurs signaux périodiques.

.. table ::

    +--------------+----+----+-----+-----+-----+-----+-----+-----+-----+-----+
    |     Signal   | ak | b1 |  b2 |  b3 |  b4 |  b5 |  b6 |  b7 | b8  | b9  |
    +==============+====+====+=====+=====+=====+=====+=====+=====+=====+=====+
    |     Carré    |  0 | 1  |  0  | 1/3 |  0  | 1/5 |  0  | 1/7 |  0  | 1/9 |
    +--------------+----+----+-----+-----+-----+-----+-----+-----+-----+-----+
    | Triangulaire |  0 | 1  |  0  |-1/9 |  0  |1/25 |  0  |-1/49|  0  | 1/81|
    +--------------+----+----+-----+-----+-----+-----+-----+-----+-----+-----+
    | Dent de Scie |  0 | 1  |-1/2 | 1/3 |-1/4 | 1/5 |-1/6 | 1/7 |-1/8 | 1/9 |
    +--------------+----+----+-----+-----+-----+-----+-----+-----+-----+-----+

.. admonition:: Question

    Avec Numpy, synthétisez un signal carré, triangulaire puis dent de scie à partir de leur décomposition en série de Fourier (avec f0=10Hz et Fe=1000Hz)

La décomposition en série de Fourier peut être généralisée au cas des signaux non-périodiques. Dans ce cas, le signal est décomposé en une somme d'exponentielles complexes:

.. math::

    x(t)=\int_{-\infty}^{\infty}X(f)e^{2j\pi ft}df

où X(f) correspond à la **transformée de Fourier** du signal x(t).

Exercice 3: Analyse spectrale
-----------------------------

La transformée de Fourier est très utilisée pour l'analyse des signaux. Cette transformée permet de mettre en valeur des éléments de notre signal difficilement visualisables dans le domaine temporel.

Mathématiquement, la transformée de Fourier d'un signal x(t) s'exprime sous la forme

.. math::

    X(f)=\int_{-\infty}^{\infty}x(t)e^{-2j\pi ft}dt

La plupart des langages de programmation intègre des fonctionnalités pour la calcul de la transformée de Fourier via des algorithmes rapides. Ces algorithmes sont couramment nommés FFT (Fast Fourier Transform). Dans cette exercice, nous allons illustrer l’intérêt de cette transformée.


.. tip::

    En python, il est possible d'afficher le module de la transformée de Fourier d'un signal sinusoidal en utilisant la fonction *periodogram* du module signal de Scipy.

    .. plot:: TP4/show_fourier.py
        :include-source:

Le fichier TP4.py contient différents signaux nommés respectivement signal1, signal2 et signal 3. Derrière chaque signal se cache un signal périodique de type sinusoidal, carré ou dent de scie dont la fréquence fondamentale est inconnue. Pour extraire un signal, il suffit de lancer les instructions

.. code::

    from TP4 import *

    t,x=signal1()   #generation du signal 1


.. admonition:: Question

    Afficher les trois signaux dans le domaine temporel puis affichez le module de leur transformée de Fourier. Complétez alors le tableau suivant

.. table ::

    +--------------+--------------+---------------------------------------------+
    |    Signal    | Fréquence f0 |   Type (Sinusoidal | Carré | Dent de scie)  |
    +==============+==============+=============================================+
    |   Signal 1   |              |                                             |
    +--------------+--------------+---------------------------------------------+
    |   Signal 2   |              |                                             |
    +--------------+--------------+---------------------------------------------+
    |   Signal 3   |              |                                             |
    +--------------+--------------+---------------------------------------------+




Références
----------

.. [Python_pour_les_nuls] http://vincentchoqueuse.github.io/Python-pour-les-nuls.
.. [Numpy] https://docs.scipy.org/doc/numpy/reference/routines.html
.. [Scipy] http://docs.scipy.org/doc/scipy/reference/
.. [Matplotlib] http://matplotlib.org/contents.html