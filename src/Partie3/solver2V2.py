from gurobipy import Model, GRB, quicksum

from gurobipy import Model, GRB, quicksum

def solver_maxOWA(a, b, c, w_prime):
    """
    Résout un problème d'optimisation robuste basé sur la méthode maxOWA.
    
    Paramètres :
        a (list of list): Matrice des utilités dans les différents scénarios.
        b (list): Vecteur des coûts associés aux arcs dans chaque scénario.
        c (list): Coûts des arcs dans le graphe.
        w_prime (list): Poids pour la combinaison OWA (par exemple, [2, 1]).
        
    Retourne :
        list: Solution optimale des variables binaires et continues.
    """
    m = Model("maxOWA")

    # Variables binaires pour les arcs sélectionnés
    x = [m.addVar(vtype=GRB.BINARY, name=f"x{i+1}") for i in range(len(c))]
    
    # Variables continues pour les regrets
    r = [m.addVar(vtype=GRB.CONTINUOUS, name=f"r{i+1}") for i in range(len(a))]
    
    # Variables continues pour les b_i,k
    b_vars = [[m.addVar(vtype=GRB.CONTINUOUS, lb=0, name=f"b_{i+1},{k+1}") for k in range(len(w_prime))] for i in range(len(a))]
    
    m.update()

    # Fonction objectif (maximisation des regrets pondérés)
    obj = quicksum(w_prime[k] * r[k] - quicksum(b_vars[i][k] for i in range(len(a))) for k in range(len(w_prime)))
    m.setObjective(obj, GRB.MAXIMIZE)

    # Contraintes pour chaque scénario
    for k in range(len(w_prime)):
        for i in range(len(a)):
            m.addConstr(r[k] - b_vars[i][k] <= quicksum(a[i][j] * x[j] for j in range(len(c))), f"Contrainte_{i+1}_{k+1}")

    # Contraintes sur les coûts des arcs
    for i in range(len(b)):  # Chaque scénario
        m.addConstr(quicksum(b[i][j] * x[j] for j in range(len(c))) <= b[i], f"Contrainte_cout_{i+1}")

    # Optimisation
    m.optimize()

    print("\nSolution optimale :")
    for v in m.getVars():
        print(f"{v.varName} = {v.x}")
    
    print("\nValeur optimale de g(x) : ", m.objVal)

    return r



def solver_minOWA_regret(a, budget, c, w_prime, z_opt):
    """
    Résout un problème d'optimisation basé sur le critère minOWA des regrets.
    
    Le critère minOWA des regrets consiste à minimiser une combinaison pondérée des regrets triés par ordre décroissant.
    
    Paramètres :
        a (list of list): Matrice des utilités dans les différents scénarios.
        budget (float): Budget maximal pour sélectionner les projets.
        c (list): Coûts des projets.
        w_prime (list): Poids pour la combinaison OWA.
        z_opt (list): Valeurs optimales dans chaque scénario pour le regret calculé.

    Retourne :
        list: Valeurs optimales des regrets.
    """
    m = Model("minOWA_Regrets_Lin")

    # Variables binaires pour les projets sélectionnés
    x = [m.addVar(vtype=GRB.BINARY, name=f"x{i+1}") for i in range(len(c))]
    
    # Variables continues pour les regrets triés
    r = [m.addVar(vtype=GRB.CONTINUOUS, name=f"r{k+1}") for k in range(len(w_prime))]
    
    m.update()

    # Définition de la fonction objectif (minimisation des regrets pondérés)
    obj = quicksum(w_prime[k] * r[k] for k in range(len(w_prime)))
    m.setObjective(obj, GRB.MINIMIZE)

    # Contraintes pour lier les variables de regrets aux performances optimales
    for i in range(len(a)):
        regret_expr = z_opt[i] - quicksum(a[i][j] * x[j] for j in range(len(c)))
        m.addConstr(r[i] >= regret_expr, f"Regret_{i+1}")

    # Contrainte pour imposer l'ordre décroissant des regrets
    for i in range(len(w_prime) - 1):
        m.addConstr(r[i] >= r[i + 1], f"Contrainte_ordre_{i+1}")

    # Contrainte de budget total
    m.addConstr(quicksum(c[j] * x[j] for j in range(len(c))) <= budget, "Contrainte_budget")

    m.optimize()

    print("\nSolution optimale :")
    for v in m.getVars():
        print(f"{v.varName} = {v.x}")
    
    print("\nValeur optimale de g(x) : ", m.objVal)

    return r


def solver_minOWA_regret_linearized(a, budget, c, w_prime, z_opt):
    """
    Résout un problème d'optimisation robuste basé sur la version linéarisée du critère minOWA des regrets.
    
    La version linéarisée utilise des variables continues pour représenter les regrets, et impose leur ordre décroissant.
    
    Paramètres :
        a (list of list): Matrice des utilités dans les différents scénarios.
        budget (float): Budget maximal pour sélectionner les projets.
        c (list): Coûts des projets.
        w_prime (list): Poids pour la combinaison OWA.
        z_opt (list): Valeurs optimales dans chaque scénario pour le regret calculé.

    Retourne :
        list: Valeurs optimales des regrets.
    """
    m = Model("minOWA_Regrets_Lin")

    # Variables binaires pour les projets sélectionnés
    x = [m.addVar(vtype=GRB.BINARY, name=f"x{i+1}") for i in range(len(c))]
    
    # Variables continues pour les regrets triés (nombre égal aux scénarios)
    r = [m.addVar(vtype=GRB.CONTINUOUS, name=f"r{i+1}") for i in range(len(a))]  
    
    m.update()

    # Fonction objectif (minimisation des regrets pondérés triés)
    obj = quicksum(w_prime[i] * r[i] for i in range(len(w_prime)))
    m.setObjective(obj, GRB.MINIMIZE)

    # Contraintes pour relier les variables de regrets aux performances optimales par scénario
    for i in range(len(a)):
        regret_expr = z_opt[i] - quicksum(a[i][j] * x[j] for j in range(len(c)))
        m.addConstr(r[i] >= regret_expr, f"Regret_{i+1}")

    # Contrainte pour imposer l'ordre décroissant des regrets (tri des r_k)
    for i in range(len(r) - 1):
        m.addConstr(r[i] >= r[i + 1], f"Contrainte_ordre_{i+1}")

    # Contrainte de budget total
    m.addConstr(quicksum(c[j] * x[j] for j in range(len(c))) <= budget, "Contrainte_budget")

    m.optimize()

    print("\nSolution optimale :")
    for v in m.getVars():
        print(f"{v.varName} = {v.x}")
    
    print("\nValeur optimale de g(x) : ", m.objVal)

    return r
