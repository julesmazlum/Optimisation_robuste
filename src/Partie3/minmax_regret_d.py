from mogplex import *

# Graphe Gauche
# Solution utilisant le minmax regret.
# Le PL est représenté ci dessous.

# Matrice des contraintes
a = [[-5, -10, -2, -4, -1, -4, -3, -1, -1, -3, -1, -1, 1],
     [-3, -4, -6, -2, -3, -6, -1, -2, -4, -5, -1, -1, 1],
     [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
     [1, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 1, 0, 0, -1, -1, 1, 0, 0, 0, 0],
     [0, 0, 1, 0, 1, 0, 0, 0, -1, -1, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, -1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, -1, 0]]

# Second membre
b = [5, 6, 1, 1, 0, 0, 0, 0, 0]

# Coefficients de la fonction objectif
c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

nbcont = 9
nbvar = 13

"""
maxi = False : le problème est une minimisation.
nbine = 2 : il y a 2 inégalités.
inf = False : toutes les contraintes sont des inégalités de type >=.
conti = True : le problème contient 10 variables binaires et 1 variable continue.
"""
solver(nbcont, nbvar, a, b, c, maxi=False, nbine=2, inf=False, conti=True)