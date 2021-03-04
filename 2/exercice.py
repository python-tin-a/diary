""" Exercice

- [x] Installer le paquet numpy (avec pip)
- [x] IPython3
- [x] D'importer le module numpy
- [x] De créer un tableau de N valeurs aléatoires entre les bornes A et B
- [x] De multiplier chaque valeur du tableau par K
- [x] Calculer la moyenne des éléments du tableau
- [x] Calculer l'écart type des éléments du tableau
- [x] Calculer la somme des éléments du tableau

"""

import numpy as np
# from numpy import *  (ca c'est caca !)

A = 32
B = 120
N = 1000
K = 12

u = np.random.randint(A, B, N)
u *= K

u.mean()
u.std()
u.sum()
