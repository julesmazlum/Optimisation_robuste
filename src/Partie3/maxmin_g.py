from mogplex import *

# Graphe Gauche
# Solution utilisant le maxmin.
# Le PL est représenté ci dessous.

# Matrice des contraintes
a = [[-4, -5, -2, -1, -2, -7, -5, -2, -3, -5, 1],
     [-3, -1, -1, -4, -2, -5, -1, -7, -2, -2, 1],
     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
     [1, 0, -1, -1, -1, -1, 0, 0, 0, 0, 0],
     [0, 1, 1, 0, 0, 0, -1, -1, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 1, 0, -1, 0, 0],
     [0, 0, 0, 0,1, 0, 0, 1, 0, -1, 0]]

# Second membre
b = [0, 0, 1, 1, 0, 0, 0, 0]

# Coefficients de la fonction objectif
c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]

nbcont = 8
nbvar = 11

"""
maxi = True : on est en maximisation.
nbine = 2 : il y a 2 inégalités.
inf = False : toutes les inégalités sont du type >=.
conti = True : il y a 10 variables binaires et 1 variable continue.
"""
solver(nbcont, nbvar, a, b, c, maxi=True, nbine=2, inf=False, conti=True)