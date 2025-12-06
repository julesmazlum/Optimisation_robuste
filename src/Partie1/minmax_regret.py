from mogplex import *

# Solution utilisant le minmax regret.
# Le PL est représenté ci dessous.

# Matrice des contraintes
a = [[70, 18, 16, 14, 12, 10, 8, 6, 4, 2, 1],
    [2, 4, 6, 8, 10, 12, 14, 16, 18, 70, 1],
    [-60, -10, -15, -20, -25, -20, -5, -15, -20, -60, 0]]

# Second membre
b = [112, 118, -100]

# Coefficients de la fonction objectif
c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

nbcont = 3
nbvar = 11

"""
maxi = False : le problème est une minimisation.
inf = False : toutes les contraintes sont des inégalités de type >=.
conti = True : le problème contient 10 variables binaires et 1 variable continue.
"""
solver (nbcont, nbvar, a, b, c, maxi=False, inf=False, conti=True)