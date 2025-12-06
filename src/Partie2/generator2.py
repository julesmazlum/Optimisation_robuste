import numpy as np

def generator_maxOWA(n, p):
    """
    Génère les paramètres pour une instance de maxOWA avec n scénarios et p projets.
    
    n : nombre de scénarios
    p : nombre de projets
    
    Retourne :
    - a : matrice des utilités (n x p)
    - c : coûts des projets (p éléments)
    - budget : budget total, fixé à 50% du coût total des projets
    """
    # matrice des utilités pour chaque projet et scénario (valeurs entre 1 et 100)
    a = np.random.randint(1, 101, size=(n, p))

    # coûts des projets (valeurs entre 1 et 100)
    c = np.random.randint(1, 101, size=p)

    # budget comme 50% de la somme des coûts des projets
    budget = 0.5 * np.sum(c)

    return a, c, budget

def generator_minOWA_regret(n, p):
    """
    Génère les paramètres pour une instance de minOWA des regrets avec n scénarios et p projets.
    
    n : nombre de scénarios
    p : nombre de projets
    
    Retourne :
    - a : matrice des utilités (n x p)
    - c : coûts des projets (p éléments)
    - budget : budget total, fixé à 50% du coût total des projets
    - z_opt : valeurs optimales z_i* pour chaque scénario (calculées comme les utilités maximales possibles)
    """
    # 1. Générer la matrice des utilités pour chaque projet et scénario (valeurs entre 1 et 100)
    a = np.random.randint(1, 101, size=(n, p))

    # 2. Générer les coûts des projets (valeurs entre 1 et 100)
    c = np.random.randint(1, 101, size=p)

    # 3. Calculer le budget comme 50% de la somme des coûts des projets
    budget = 0.5 * np.sum(c)

    # 4. Calculer z_opt (les valeurs optimales de référence pour chaque scénario)
    z_opt = []
    for i in range(n):
        # Sélectionner les projets avec le budget total pour maximiser la valeur dans chaque scénario
        z_opt.append(np.max(a[i]))  # Choisir la meilleure utilité possible pour le scénario i

    return a, c, budget, z_opt
