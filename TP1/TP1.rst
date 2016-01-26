TP1: Régression Linéaire
========================

Dans ce premier TP, nous allons nous familiariser avec la notion de sensibilité. Dans un premier temps, il sera demandé d'afficher la courbe d'étalonnage d'un capteur de distance. Dans un second temps, une régression linéaire sera utilisée pour estimer la sensibilité du capteur. L'écart de sensibilité sera déterminé à partir de ses résultats.

Exercice 1: Analyse d'un capteur de distance
--------------------------------------------

Courbe d'étalonnage
^^^^^^^^^^^^^^^^^^^

Pour obtenir la courbe d'étalonnage d'un capteur de distance, nous réalisons une série de
mesures. Ces mesures sont reportées dans la table :ref:`courbe`.

.. _courbe:

.. table:: Courbe d'étalonnage du capteur de distance

   +--------------+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+------+------+------+------+------+-----+------+------+-----+------+
   |       n      |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10 |  11  |  12  |  13  |  14  |  15  |  16 |  17  |  18  |  19 |  20  |
   +==============+=====+=====+=====+=====+=====+=====+=====+=====+=====+=====+======+======+======+======+======+=====+======+======+=====+======+
   | x[n] (pouce) |0.00 |0.10 |0.20 |0.30 |0.40 |0.50 |0.60 |0.70 |0.80 |0.90 |1.00  | 1.10 |1.20  |1.30  |1.40  |1.50 |1.60  |1.70  |1.80 |1.90  |
   +--------------+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+------+------+------+------+------+-----+------+------+-----+------+
   | y[n] (volts) |0.00 |0.25 |0.51 |0.75 |1.01 |1.24 |1.51 |1.74 |2.01 |2.26 | 2.51 |2.76  |3.02  |3.24  | 3.51 |3.75 |4.00  |4.26  |4.51 |4.75  |
   +--------------+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+------+------+------+------+------+-----+------+------+-----+------+

.. admonition:: Question

    Identifiez le mesurande et la grandeur de sortie.

.. admonition:: Question

   En utilisant la fonction `plot <http://matplotlib.org/examples/pylab_examples/simple_plot.html>`_, développez un script Python permettant d'afficher :math:`y[n]` en fonction de :math:`x[n]` et annotez convenablement votre courbe.

.. tip ::

    Notons que l'utilisation de la fonction plot de Matplotlib n'est pas très adaptée pour l'affichage des courbes d'étalonnage. En effet, cette fonction relie automatiquement les points par des segments de droites, ce qui peut fausser l'interprétation de la courbe d'étalonnage. Pour demander à Python d'afficher uniquement les points, il est possible d'ajouter un troisième argument à la fonction plot

    .. code::

        plot(x,y,'o')


Régression linéaire
^^^^^^^^^^^^^^^^^^^

Nous allons tenter d'approcher la courbe d'étalonnage par une droite d'équation :math:`y=Sx+b`, où S et b sont des paramètres à déterminer.

.. admonition:: Question

    Physiquement, a quoi correspond le paramètre S ? Quel est son unité ?

Pour obtenir S et b, nous allons utiliser l'estimateur des moindres carrés. Les estimées de S et b s'obtiennent alors en minimisant la fonction de coût suivante :

.. math::

   \mathcal{J}(S,b)=\sum_{n=1}^{20}\left(y[n]-(Sx[n]+b)\right)^{2}

Pour réaliser ce type de minimisation, il est possible de procéder de manière classique (recherche des valeurs de S et b annulant la dérivée). Il est alors possible d'établir directement que la fonction de coût est minimisée lorsque

.. math::

   \widehat{S}&=\frac{Na_{12}-a_{1}a_{2}}{Na_{11}-a_{1}^{2}}\label{eq1}\\
   \widehat{b}&=\frac{a_{2}.a_{11}-a_{1}a_{12}}{Na_{11}-a_{1}^{2}}

où

.. math::

   a_{1}&=\sum_{n=1}^{N} x[n],\\
   a_{2}&=\sum_{n=1}^{N} y[n],\\
   a_{11}&=\sum_{n=1}^{N} x^{2}[n]\\
   a_{12}&=\sum_{n=1}^{N} x[n]y[n].


.. admonition:: Question

    Modifiez votre script Python pour qu'il puisse calculer les valeurs S et b à partir de x[n] et y[n]. Votre script utilisera directement la fonction `sum <http://docs.scipy.org/doc/numpy/reference/generated/numpy.sum.html>`_ de Numpy pour le calcul de S et b.

Si les valeurs de S et b sont correctement estimées, la courbe d'équation :math:`y=Sx+b` doit passer à proximité des différents points de mesure.


.. admonition:: Question

    Modifiez votre script Python pour qu'il puisse afficher les points de mesures et le résultat de la régression linéaire.

Un des gros intérêts du langage Python réside dans la philosophie *batteries included*. En effet, de nombreuses fonctionnalités sont déjà intégrées dans la distribution de base. Par exemple, les regressions linéaires et polynomiale s'obtiennent facilement via la fonction `polyfit <http://docs.scipy.org/doc/numpy/reference/generated/numpy.polyfit.html>`_ intégrée à Numpy.

.. tip :: La fonction polyfit disponible dans Numpy permet d'effectuer une regression polynomiale. A titre d'illustration, la regression linéaire s'obient via les instructions

    .. plot:: TP1/programme1.py
       :include-source:

Écart de linéarité
^^^^^^^^^^^^^^^^^^

Pour quantifier l'écart entre la courbe d'étalonnage et la meilleure droite, nous utilisons un critère nommé écart de linéarité. Ce critère est donné par

.. math::

    |\Delta|&=\max_{n} |y[n]-y_{r}[n]|

où :math:`y_{r}[n]` correspond au mesurande obtenue en effectuant une régression linéaire. En pratique, l'écart de linéarité s'exprime souvent de manière relative par rapport à l'Etendue de Mesure (EM) via l'équation

.. math::

    |\Delta|_{r}(\%)&=\frac{|\Delta|}{EM}\times 100

.. admonition:: Question

    Mesurez l'écart de linéarité :math:`|\Delta|` du capteur de distance puis l'écart de linéarité relatif :math:`|\Delta|_{r}(\%)` lorsque les valeurs minimum et maximum du mesurande sont respectivement égales à 0.00 et 2.00 pouces.


Exercice 2: Analyse d'un capteur de température
------------------------------------------------

Certains capteurs peuvent présenter un comportement linéaire dans une plage de valeurs et un comportement non-linéaire à l'extérieur de cette plage. Lorsque l'on calcule la meilleur droite, il est important de raisonner sur la plage linéaire uniquement.

Nous considérons ici un capteur de température dont la courbe d'étalonnage est spécifié dans la table :ref:`courbe2`.

.. _courbe2:

.. table:: Courbe d'étalonnage du capteur de température

    +--------------+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+------+------+------+------+------+-----+------+------+-----+------+
    |       n      |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10 |  11  |  12  |  13  |  14  |  15  |  16 |  17  |  18  |  19 |  20  |
    +==============+=====+=====+=====+=====+=====+=====+=====+=====+=====+=====+======+======+======+======+======+=====+======+======+=====+======+
    | x[n] (degré) |  0  |  5  | 10  | 15  | 20  | 25  | 30  | 35  | 40  | 45  |  50  |  55  |  60  |  65  |  70  | 75  |  80  |  85  | 90  |  95  |
    +--------------+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+------+------+------+------+------+-----+------+------+-----+------+
    | y[n] (volts) |0.00 |0.32 |0.74 |1.12 |1.42 |1.78 |2.05 |2.40 |2.85 |3.05 | 3.37 | 3.60 |3.92  |4.05  | 4.20 |4.47 |4.63  | 4.74 |4.85 |4.92  |
    +--------------+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+------+------+------+------+------+-----+------+------+-----+------+

.. admonition:: Question

    Développez un script Python permettant d'afficher la courbe d'étalonnage puis déterminez la sensibilité du capteur (avec son unité) sur l'étendue de la plage.

.. admonition:: Question

    Modifiez votre script pour afficher la courbe d'étalonnage ainsi que sa régression linéaire. Évaluez l'écart de linéarité :math:`|\Delta|` puis expliquez pourquoi l'écart de linéarité est si élevé.


Dans le suite, nous allons enlever certains points dans le table :ref:`courbe2` pour améliorer la légitimité de la régression linéaire.

.. admonition:: Question

    Évaluez l'écart de linéarité :math:`|\Delta|` lorsque la régression linéaire est réalisée:

    * sur les 5 premiers échantillons (n=1,2,...,5)
    * sur les 10 premiers échantillons (n=1,2,...,10)
    * sur les 15 premiers échantillons (n=1,2,...,15)

.. admonition:: Question

    A partir de la question précédente, identifiez la zone de linéarité du capteur. Donnez alors la valeur de la sensibilité S du capteur de température.

Réferences
----------

.. [Python_pour_les_nuls] http://vincentchoqueuse.github.io/Python-pour-les-nuls.
.. [Numpy] https://docs.scipy.org/doc/numpy/reference/routines.html
.. [Scipy] http://docs.scipy.org/doc/scipy/reference/
.. [Matplotlib] http://matplotlib.org/contents.html


