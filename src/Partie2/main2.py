import time
from solver2 import *
from generator2 import *

N = [5, 10, 15]   # Nombre de projets
P = [10, 15, 20]  # Nombre de scénarios

"""
GENERATOR = 0 : pour performances maxOWA
GENERATOR = 1 : pour performances minOWA des regrets avec linéarisation
"""

GENERATOR = 0

execution_times = {}

for n in N:
    for p in P:
        for i in range(10):  # 10 instances par combinaison (n, p)
            start_time = time.time()
            if(GENERATOR == 0):
                a, c, budget = generator_maxOWA(n, p)
                solver_maxOWA(a, budget, c, w_prime=[2, 1])

            elif(GENERATOR == 1):
                a, c, budget, z_opt = generator_minOWA_regret(n, p)
                solver_minOWA_regret_linearized(a, budget, c, w_prime=[2, 1], z_opt=z_opt)
            
            else:
                print(f"Erreur : Valeur de GENERATOR invalide ({GENERATOR}). Utilisez 0, 1 ou 2.")
                break
                
            end_time = time.time()
            execution_time = end_time - start_time
            execution_times[(n, p)] = execution_times.get((n, p), []) + [execution_time]

for key, times in execution_times.items():
    avg_time = sum(times) / len(times)
    print(f"Temps moyen pour (n={key[0]}, p={key[1]}): {avg_time:.4f} secondes")
