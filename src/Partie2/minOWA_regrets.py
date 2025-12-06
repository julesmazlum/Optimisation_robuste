from solver2 import *

# Données d'exemple pour minOWA des regrets
a = [[70, 18, 16, 14, 12, 10, 8, 6, 4, 2],  # utilité dans s1
     [2, 4, 6, 8, 10, 12, 14, 16, 18, 70]]  # utilité dans s2

c = [60, 10, 15, 20, 25, 20, 5, 15, 20, 60]  # coûts des projets
budget = 100  # budget

# Poids linéarisés w' (comme dans l'exemple, w'1 = 2 et w'2 = 1)
w_prime = [2, 1]

z_opt = [112, 118]

# Appel de la fonction de résolution
print("\n------------------------------------------------ minOWA regrets VERSION LINEARISE ------------------------------------------------ ")
solver_minOWA_regret_linearized(a, budget, c, w_prime, z_opt)
print("\n\n------------------------------------------------ minOWA regrets NON LINEARISE ------------------------------------------------ ")
solver_minOWA_regret(a, budget, c, w_prime, z_opt)