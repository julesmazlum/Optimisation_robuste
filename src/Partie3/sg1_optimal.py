from mogplex import *

# Graphe Gauche
# Solution optimale pour le scénario 1.
# Le PL est représenté ci dessous.

# Matrice des contraintes
a = [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
     [1, 0, -1, -1, -1, -1, 0, 0, 0, 0],
     [0, 1, 1, 0, 0, 0, -1, -1, 0, 0],
     [0, 0, 0, 1, 0, 0, 1, 0, -1, 0],
     [0, 0, 0, 0,1, 0, 0, 1, 0, -1]]

# Second membre
b = [1, 1, 0, 0, 0, 0]

# Coefficients de la fonction objectif
c = [4, 5, 2, 1, 2, 7, 5, 2, 3, 5]

nbcont = 6
nbvar = 10

"""
maxi = False : on est en minimisation.
nbine = 0 : il n'y a pas d'inégalités, seulement des égalités.
inf = None : toutes les contraintes sont des égalités (==), donc il n'y a pas d'inégalités.
conti = False : il n'y a que des variables binaires.
"""
solver(nbcont, nbvar, a, b, c, maxi=False, nbine=0, inf=None, conti=False)