from mogplex import *

# Solution optimale pour le scénario 1.
# Le PL est représenté ci dessous.

# Matrice des contraintes
a = [[60, 10, 15, 20, 25, 20, 5, 15, 20, 60]]

# Second membre
b = [100]

# Coefficients de la fonction objectif
c = [70, 18, 16, 14, 12, 10, 8, 6, 4, 2]

nbcont = 1
nbvar = 10

"""
maxi = True : le problème est une maximisation.
inf = True : toutes les contraintes sont des inégalités de type <=.
conti = False : il n’y a que des variables binaires.
"""
solver (nbcont, nbvar, a, b, c, maxi=True, inf=True, conti=False)