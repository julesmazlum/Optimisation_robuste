#!/usr/bin/python
# Copyright 2013, Gurobi Optimization, Inc.
from gurobipy import *

"""
Dans une partie de la partie 3, cette fonction va être appelée avec différents paramètres pour résoudre les différents PL.
Le fonctionnement est décrit ci dessous.
"""

def solver(nbcont, nbvar, a, b, c, maxi, nbine, inf, conti) :
    """
    nbcont : le nombre de contraintes du PL.
    nbvar : le nombre de variables dans le PL.
    a : matrice des coefficients des contraintes.
    b : vecteur représentant le second membre des contraintes.
    c : vecteur représentant les coefficients de la fonction objectif.

    maxi (booléen) : si True, le PL est une maximisation ; sinon, une minimisation.
    nbine : le nombre de contraintes avec une inégalité, le reste étant des égalités.
    inf (booléen) : si True, les inégalités des contraintes sont du type <= ; sinon, >=.
    conti (booléen) : si True, les variables sont mixtes : (nbvar-1) variables binaires et 1 variable continue. 
                      Sinon, toutes les variables sont binaires.
    
    dans le cas "conti", les variables doivent être écrites dans l'ordre suivant : les variables binaires x_i puis la variable continue z.

    la fonction retourne le tableau des solutions x* ainsi que la valeur de la fonction objectif.
    """

    # Range of plants and warehouses
    lignes = range(nbcont)
    colonnes = range(nbvar)

    m = Model("mogplex")     
            
    # declaration variables de decision
    x = []
    if conti :
        for i in range(len(colonnes)):
            if i == len(colonnes) - 1:  # si c'est le dernier élément (z)
                x.append(m.addVar(vtype=GRB.CONTINUOUS, lb=0, name="x%d" % (i+1)))
            else:
                x.append(m.addVar(vtype=GRB.BINARY, lb=0, name="x%d" % (i+1)))
    else :
        for i in colonnes:
            x.append(m.addVar(vtype=GRB.BINARY, lb=0, name="x%d" % (i+1)))

    # maj du modele pour integrer les nouvelles variables
    m.update()

    obj = LinExpr();
    obj =0
    for j in colonnes:
        obj += c[j] * x[j]
            
    # definition de l'objectif
    if maxi :
        m.setObjective(obj,GRB.MAXIMIZE)
    else :
        m.setObjective(obj,GRB.MINIMIZE)

    # Definition des contraintes
    for i in lignes:
        if i < nbine:  
            if inf :
                m.addConstr(quicksum(a[i][j] * x[j] for j in colonnes) <= b[i], "ContrainteInf%d" % i)
            else : 
                m.addConstr(quicksum(a[i][j] * x[j] for j in colonnes) >= b[i], "ContrainteInf%d" % i)
        else:  
            m.addConstr(quicksum(a[i][j] * x[j] for j in colonnes) == b[i], "ContrainteEgal%d" % i)


    # Resolution
    m.optimize()

    r = []

    print("")                
    print('Solution optimale:')
    for j in colonnes:
        print('x%d'%(j+1), '=', x[j].x)
        r.append(x[j].x)
    r.append(m.objVal)
    print("")
    print('Valeur de la fonction objectif :', m.objVal)

    return r
