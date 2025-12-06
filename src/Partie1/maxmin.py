from mogplex import *

# Solution utilisant le maxmin.
# Le PL est représenté ci dessous.

# Matrice des contraintes
a = [[-70, -18, -16, -14, -12, -10, -8, -6, -4, -2, 1],
    [-2, -4, -6, -8, -10, -12, -14, -16, -18, -70, 1],
    [60, 10, 15, 20, 25, 20, 5, 15, 20, 60, 0]]

# Second membre
b = [0, 0, 100]

# Coefficients de la fonction objectif
c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

nbcont = 3
nbvar = 11

"""
maxi = True : le problème est une maximisation.
inf = True : toutes les contraintes sont des inégalités de type <=.
conti = True : le problème contient 10 variables binaires et 1 variable continue.
"""
solver (nbcont, nbvar, a, b, c, maxi=True, inf=True, conti=True)