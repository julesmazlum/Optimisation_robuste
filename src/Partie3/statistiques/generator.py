from graph_generator import *
from matrix_generator import *
from mogplex import *

"""
voici les deux fonctions generator_maxmin et generator_minmaxregret qui permettent de générer les paramètres a, b et c dans le contexte de l'exercice 3. 
vous trouverez deux tests à la fin du fichier pour pouvoir tester ces deux méthodes.
"""

def generator_maxmin(n, p):
    G =  generate_flow_graph(n,0.5,p)
    mat = generate_flow_matrix(G,p)

    # nombre d'arcs/ variables dans G
    nbA = len(G.edges())

    # Matrice des contraintes sur les arcs
    # mat

    # Matrice des contraintes des couts des arcs
    cout = np.random.randint(-100, 0, size=(n, nbA))

    # Matrice des contraintes 
    a = np.vstack((cout, mat))

    # Créer la dernière colonne avec 1 dans les n premières lignes et 0 dans les autres
    last_column = np.zeros((n + p, 1), dtype=int)
    last_column[:n] = 1

    # Ajouter la colonne à la matrice a
    a = np.hstack((a, last_column))


    # Second membre
    b = np.zeros(n + p)
    b[n] = 1
    b[n+1] = 1


    # Fonction objectif
    c = np.zeros(nbA + 1, dtype=int)
    c[-1] = -1

    return a, b, c, nbA

"""a,b,c,nbA = generator_maxmin(3,7)
print(a,b,c)

solver(3+7, nbA+1, a, b, c, maxi=True, nbine=3, inf=False, conti=True)"""


def generator_minmaxregret(n, p):
    G =  generate_flow_graph(n,0.7,p)
    mat = generate_flow_matrix(G,p)

    # nombre d'arcs/ variables dans G
    nbA = len(G.edges())

    # Matrice des contraintes sur les arcs
    # mat

    # Matrice des contraintes des couts des arcs
    cout = np.random.randint(-100, 0, size=(n, nbA))

    # Matrice des contraintes 
    a = np.vstack((cout, mat))

    # Créer la dernière colonne avec 1 dans les n premières lignes et 0 dans les autres
    last_column = np.zeros((n + p, 1), dtype=int)
    last_column[:n] = 1

    # Ajouter la colonne à la matrice a
    a = np.hstack((a, last_column))

    # Calculer les solutions optimales de chque scénario :

    # matrice des contraintes x
    x = mat

    # second membre
    y = np.zeros(p)
    y[0] = 1
    y[1] = 1

    # fonction objectif
    b = np.zeros(n + p)
    for i in range(n):
        z = -cout[i]
        s = solver(n, nbA, x, y, z, maxi=False, nbine=0, inf=None, conti=False)
        b[i] = s[nbA]

    b[n] = 1
    b[n+1] = 1

    # Fonction objectif
    c = np.zeros(nbA + 1, dtype=int)
    c[-1] = 1

    return a, b, c, nbA

"""a,b,c,nbA = generator_minmaxregret(3,7)
print(a,b,c)

solver(3+7, nbA+1, a, b, c, maxi=False, nbine=3, inf=False, conti=True)"""
