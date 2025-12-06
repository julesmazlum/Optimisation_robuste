import time
import matplotlib.pyplot as plt
from mogplex import *
from generator import *

"""
dans ce fichier, on teste nos deux méthodes maxmin et minmax regret sur 10 instances générées par les fonctions dans generator.py, en fonction de N et P.
"""


N = [5, 10, 15]
P = [10, 15, 20]

execution_times_maxmin = {}
execution_times_minmax_regret = {}

for n in N:
    for p in P:
        for i in range(10):
            # mesurer le temps pour maxmin
            start_time_maxmin = time.time()

            a, b, c = generator_maxmin(n, p)
            """
            maxi = True : le problème est une maximisation.
            inf = True : toutes les contraintes sont des inégalités de type <=.
            conti = True : le problème contient 10 variables binaires et 1 variable continue.
            """
            solver(n+1, p+1, a, b, c, maxi=True, inf=True, conti=True)

            end_time_maxmin = time.time()
            execution_time_maxmin = end_time_maxmin - start_time_maxmin
            execution_times_maxmin[(n, p)] = execution_times_maxmin.get((n, p), []) + [execution_time_maxmin]



            # mesurer le temps pour minmax_regret
            start_time_minmax = time.time()

            a, b, c = generator_minmaxregret(n, p)
            """
            maxi = False : le problème est une minimisation.
            inf = False : toutes les contraintes sont des inégalités de type >=.
            conti = True : le problème contient 10 variables binaires et 1 variable continue.
            """
            solver(n+1, p+1, a, b, c, maxi=False, inf=False, conti=True)

            end_time_minmax = time.time()
            execution_time_minmax = end_time_minmax - start_time_minmax
            execution_times_minmax_regret[(n, p)] = execution_times_minmax_regret.get((n, p), []) + [execution_time_minmax]



average_times_maxmin = {key: sum(times) / len(times) for key, times in execution_times_maxmin.items()}
average_times_minmax = {key: sum(times) / len(times) for key, times in execution_times_minmax_regret.items()}

keys = list(average_times_maxmin.keys())  
labels = [f"({n},{p})" for n, p in keys]  
maxmin_times = [average_times_maxmin[key] for key in keys]  
minmax_times = [average_times_minmax[key] for key in keys]  


# tracer le graphique
x = range(len(keys)) 

plt.figure(figsize=(10, 6))
plt.plot(x, maxmin_times, label="maxmin", marker="o")
plt.plot(x, minmax_times, label="minmax regret", marker="x")

plt.xticks(x, labels, rotation=45)
plt.xlabel("(n, p)")
plt.ylabel("temps d'exécution (secondes)")
plt.title("Temps d'exécution pour chaque combinaison (n, p)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
