from gurobipy import Model, GRB, quicksum

def solver_maxOWA(a, budget, c, w_prime):
    m = Model("maxOWA_Linearized")

    # Déclaration des variables de décision
    x = [m.addVar(vtype=GRB.BINARY, lb=0, name=f"x{i+1}") for i in range(len(c))]
    
    # Variables continues r_k pour chaque scénario
    r = [m.addVar(vtype=GRB.CONTINUOUS, lb=0, name=f"r{k+1}") for k in range(len(w_prime))]
    
    # Variables b_{ik} pour l'ordre des performances
    b_vars = [[m.addVar(vtype=GRB.CONTINUOUS, lb=0, name=f"b{i+1},{k+1}") for k in range(len(w_prime))] for i in range(len(a))]
    
    m.update()

    print("\nVariables déclarées :")
    print(f"Nombre de variables binaires x : {len(x)}")
    print(f"Nombre de variables continues r_k : {len(r)}")
    print(f"Taille de la matrice des b_vars : {len(b_vars)} x {len(b_vars[0])}\n")

    # Affichage fonction objectif
    print("Fonction objectif définie :")
    for k in range(len(w_prime)):
        term_r = f"{w_prime[k]} * r[{k}]"
        term_b = " - ".join([f"b_vars[{i}][{k}]" for i in range(len(a))])
        print(f"{term_r} - ({term_b})")

    # Fonction objectif
    obj = quicksum(w_prime[k] * r[k] - quicksum(b_vars[i][k] for i in range(len(a))) for k in range(len(w_prime)))
    m.setObjective(obj, GRB.MAXIMIZE)

    # Contraintes de performance
    for k in range(len(w_prime)):
        for i in range(len(a)):
            m.addConstr(r[k] - b_vars[i][k] <= quicksum(a[i][j] * x[j] for j in range(len(c))), f"Contrainte_{i+1}_{k+1}")

    # Contrainte de budget
    m.addConstr(quicksum(c[j] * x[j] for j in range(len(c))) <= budget, "Contrainte_budget")
    print(f"\nContrainte de budget ajoutée : sum(c[j] * x[j]) <= {budget}")

    m.optimize()

    print("\nSolution optimale :")
    for v in m.getVars():
        print(f"{v.varName} = {v.x}")
    
    print("\nValeur optimale de g(x) : ", m.objVal)

    return r



def solver_minOWA_regret(a, budget, c, w_prime, z_opt):
    m = Model("minOWA_Regrets_Lin")

    # Variables binaires pour sélectionner les projets
    x = [m.addVar(vtype=GRB.BINARY, name=f"x{i+1}") for i in range(len(c))]
    
    # Variables continues pour les regrets triés (r_k)
    r = [m.addVar(vtype=GRB.CONTINUOUS, name=f"r{k+1}") for k in range(len(w_prime))]
    
    m.update()

    # Fonction objectif
    obj = quicksum(w_prime[k] * r[k] for k in range(len(w_prime)))
    m.setObjective(obj, GRB.MINIMIZE)

    # Contraintes pour lier les variables de regrets aux performances (z_i^*)
    for i in range(len(a)):
        regret_expr = z_opt[i] - quicksum(a[i][j] * x[j] for j in range(len(c)))
        m.addConstr(r[i] >= regret_expr, f"Regret_{i+1}")

    # Contrainte pour imposer l'ordre décroissant des regrets
    for i in range(len(w_prime) - 1):
        m.addConstr(r[i] >= r[i + 1], f"Contrainte_ordre_{i+1}")

    # Contrainte de budget
    m.addConstr(quicksum(c[j] * x[j] for j in range(len(c))) <= budget, "Contrainte_budget")

    m.optimize()

    print("\nSolution optimale :")
    for v in m.getVars():
        print(f"{v.varName} = {v.x}")
    
    print("\nValeur optimale de g(x) : ", m.objVal)

    return r


def solver_minOWA_regret_linearized(a, budget, c, w_prime, z_opt):
    m = Model("minOWA_Regrets_Lin")

    # Variables binaires pour sélectionner les projets
    x = [m.addVar(vtype=GRB.BINARY, name=f"x{i+1}") for i in range(len(c))]
    
    # Variables continues pour les regrets (r_k), taille = nombre de scénarios
    r = [m.addVar(vtype=GRB.CONTINUOUS, name=f"r{i+1}") for i in range(len(a))]  
    
    m.update()

    # Fonction objectif
    obj = quicksum(w_prime[i] * r[i] for i in range(len(w_prime)))
    m.setObjective(obj, GRB.MINIMIZE)

    # Contraintes pour lier les variables de regrets aux performances (z_i^*)
    for i in range(len(a)):
        regret_expr = z_opt[i] - quicksum(a[i][j] * x[j] for j in range(len(c)))
        m.addConstr(r[i] >= regret_expr, f"Regret_{i+1}")

    # Contrainte pour imposer l'ordre décroissant des regrets (tri des r_k)
    for i in range(len(r) - 1):
        m.addConstr(r[i] >= r[i + 1], f"Contrainte_ordre_{i+1}")

    # Contrainte de budget
    m.addConstr(quicksum(c[j] * x[j] for j in range(len(c))) <= budget, "Contrainte_budget")

    m.optimize()

    print("\nSolution optimale :")
    for v in m.getVars():
        print(f"{v.varName} = {v.x}")
    
    print("\nValeur optimale de g(x) : ", m.objVal)

    return r
