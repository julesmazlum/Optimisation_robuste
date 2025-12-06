from solver2 import solver_maxOWA

# Données d'exemple pour maxOWA
a = [[70, 18, 16, 14, 12, 10, 8, 6, 4, 2], # utilité dans s1
     [2, 4, 6, 8, 10, 12, 14, 16, 18, 70]] # utilité dans s2

# Coefficients de la fonction objectif
c = [60, 10, 15, 20, 25, 20, 5, 15, 20, 60]

budget = 100

# Poids linéarisés w' (comme dans l'exemple, w'1 = 1 et w'2 = 1)
w_prime = [2, 1]


# Résolution avec la fonction solver_OWA
print("\n------------------------------------------------ maxOWA ------------------------------------------------ ")
solver_maxOWA(a, budget, c, w_prime)
