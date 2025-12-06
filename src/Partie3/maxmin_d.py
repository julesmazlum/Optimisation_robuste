from mogplex import *

# Graphe Droite
# Solution utilisant le maxmin.
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
b = [0, 0, 1, 1, 0, 0, 0, 0, 0]

# Coefficients de la fonction objectif
c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]

nbcont = 9
nbvar = 13

"""
maxi = True : on est en maximisation.
nbine = 2 : il y a 2 inégalités.
inf = False : toutes les inégalités sont du type >=.
conti = True : il y a 12 variables binaires et 1 variable continue.
"""
solver(nbcont, nbvar, a, b, c, maxi=True, nbine=2, inf=False, conti=True)