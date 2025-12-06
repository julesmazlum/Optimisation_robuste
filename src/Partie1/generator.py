import numpy as np
from mogplex import *

"""
voici les deux fonctions generator_maxmin et generator_minmaxregret qui permettent de générer les paramètres a, b et c dans le contexte de l'exercice 1. 
vous trouverez deux tests à la fin du fichier pour pouvoir tester ces deux méthodes.
"""

def generator_maxmin(n,p) :
    """
    cette fonction prend en paramètre :
        n : le nombre de scénarios
        p : le nombre de projets
    et crée aléatoirement les paramètres a, b et c pour pouvoir résoudre un PL avec un solver dans un contexte de maxmin.
    """

    # Générer la matrice n x p, qui représente les utilités dans [-100, 0]
    a = np.random.randint(-100, 1, size=(n, p))

    # Ajouter une colonne de 1 à la fin de la matrice a, qui représente la colonne des z
    a = np.hstack((a, np.ones((n, 1))))

    # Ajouter une ligne en bas avec les n premières valeurs qui represente les cout dans [0, 100] et la dernière valeur à 0 pour le z
    last_row = np.append(np.random.randint(0, 101, p), 0)
    a = np.vstack((a, last_row))

    # Créer un tableau b de taille n+1, avec des zéros sur les n premier elements 
    # et le dernier élément égal à 50% de la somme de la dernière ligne de a : le budget
    b = np.zeros(n + 1)
    b[-1] = 0.5 * np.sum(last_row)

    # Créer un tableau c de taille n+1, avec les n premiers éléments à 0 (les x_i) et le dernier élément à 1 (z) : la fonction objectif
    c = np.zeros(p + 1)
    c[-1] = 1

    return a, b, c

def generator_minmaxregret(n,p) :
    """
    cette fonction prend en paramètre :
        n : le nombre de scénarios
        p : le nombre de projets
    et crée aléatoirement les paramètres a, b et c pour pouvoir résoudre un PL avec un solver dans un contexte de minmax regret.
    """

    # Générer la matrice n x p, qui représente les utilités dans [0, 100]
    a = np.random.randint(0, 101, size=(n, p))

    # Ajouter une colonne de 1 à la fin de la matrice a, qui représente la colonne des z
    a = np.hstack((a, np.ones((n, 1))))

    # Ajouter une ligne en bas avec les n premières valeurs qui represente les cout dans [-100, 0] et la dernière valeur à 0 pour le z
    last_row = np.append(np.random.randint(-100, 1, p), 0)
    a = np.vstack((a, last_row))

    # Second membre
    # Pour le second membre on doit calculer, la solution optimale de chaque ligne de a pour chaque ligne de b
    b = []
    x = -a[-1].reshape(1, -1)           #x : équivalent de la matrice des contraintes. Elle ne change pas c'est toujours la dernière ligne de a donc les contraintes sur le couts mais le signe est opposé.
    x = np.delete(x, -1, axis=1)        #on enlève le dernier élément car c'est z, pas besoin ici
    y = -(0.5 * np.sum(last_row))       #y : equivalent ddu second memebre, ici c'est le budget qui est également fixe
    y = np.array([y])
    z = []                              #z : équivalent de la fonction objectif.
    for i in range(n):                  #Pour les n projets
        z = a[i]                        #on prend la ligne du projet i dans a
        z = np.delete(z, -1)            #on enlève le dernier élément z
        """
        maxi = True car on est en maximisation
        inf = True car toutes les contraines sont des inégalités de type <=
        conti = False, car on a 10 variables binaires
        """
        s = solver (1, p, x, y, z, maxi=True, inf=True, conti=False)    #et on trouve la solution optimale pour chaque ligne de a
        b.append(s[p])                  #et on l'insere dans b le second membre

    b.append(float(-y[0]))              #on fini par ajouter le budget 

    # Créer un tableau c de taille n+1, avec les n premiers éléments à 0 (les x_i) et le dernier élément à 1 (z) : la fonction objectif
    c = np.zeros(p + 1)
    c[-1] = 1

    return a, b, c


# Tests

a, b, c = generator_maxmin(2, 10)
print("generator_maxmin : \n a :\n", a, "\n b :\n", b,"\n c :\n", c,)

a, b, c = generator_minmaxregret(2, 10)
print("generator_minmaxregret : \n a :\n", a, "\n b :\n", b,"\n c :\n", c,)