from solver2V2 import solver_maxOWA

# Graphe de gauche
# Matrice des contraintes
a = [[-4, -5, -2, -1, -2, -7, -5, -2, -3, -5],
     [-3, -1, -1, -4, -2, -5, -1, -7, -2, -2],
     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
     [1, 0, -1, -1, -1, -1, 0, 0, 0, 0],
     [0, 1, 1, 0, 0, 0, -1, -1, 0, 0],
     [0, 0, 0, 1, 0, 0, 1, 0, -1, 0]]

# Coût associé à chaque scénario (b)
b = [0, 0, 1, 1, 0, 0, 0, 0]

# Coefficients de la fonction objectif (coût des arcs)
c = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0]

# Poids linéarisés pour maxOWA des regrets
k_values = [2, 4, 8, 16]  # Différentes valeurs pour k dans w' = [k, 1]

# Résolution pour chaque valeur de k
for k in k_values:
    w_prime = [k, 1]  # Vecteur de pondération
    print(f"\n------------- maxOWA (Graphe de gauche) avec k = {k} -------------")
    solver_maxOWA(a, b, c, w_prime)
