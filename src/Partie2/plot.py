import matplotlib.pyplot as plt

# Résultats pour maxOWA (GENERATOR = 0)
times_maxOWA = {
    (5, 10): 0.0100,
    (5, 15): 0.0078,
    (5, 20): 0.0106,
    (10, 10): 0.0092,
    (10, 15): 0.0133,
    (10, 20): 0.0153,
    (15, 10): 0.0107,
    (15, 15): 0.0139,
    (15, 20): 0.0234
}

# Résultats pour minOWA regrets linéarisé (GENERATOR = 1)
times_minOWA_regret = {
    (5, 10): 0.0031,
    (5, 15): 0.0051,
    (5, 20): 0.0037,
    (10, 10): 0.0026,
    (10, 15): 0.0054,
    (10, 20): 0.0042,
    (15, 10): 0.0035,
    (15, 15): 0.0065,
    (15, 20): 0.0053
}

n_values = [5, 10, 15]
p_values = [10, 15, 20]

fig, ax = plt.subplots(figsize=(10, 6))

times_maxOWA_list = [times_maxOWA[(n, p)] for n in n_values for p in p_values]
ax.plot(range(len(times_maxOWA_list)), times_maxOWA_list, marker='o', label='maxOWA', linestyle='-')

times_minOWA_list = [times_minOWA_regret[(n, p)] for n in n_values for p in p_values]
ax.plot(range(len(times_minOWA_list)), times_minOWA_list, marker='s', label='minOWA des regrets', linestyle='--')

positions = [f"({n}, {p})" for n in n_values for p in p_values]
ax.set_xticks(range(len(positions)))
ax.set_xticklabels(positions, rotation=45)

ax.set_title("Comparaison des temps d'exécution pour maxOWA et minOWA regrets linéarisés ")
ax.set_xlabel("(n, p) - Combinaison de projets et scénarios")
ax.set_ylabel("Temps moyen (secondes)")
ax.legend()

plt.tight_layout()
plt.show()


# --------- Graphique 1: Temps en fonction de p ---------
plt.figure(figsize=(10, 5))
for n in n_values:
    maxOWA_times = [times_maxOWA[(n, p)] for p in p_values]
    minOWA_times = [times_minOWA_regret[(n, p)] for p in p_values]

    plt.plot(p_values, maxOWA_times, marker='o', label=f'maxOWA (n={n})')
    plt.plot(p_values, minOWA_times, marker='s', linestyle='--', label=f'minOWA regrets (n={n})')

plt.title("Temps d'exécution en fonction du nombre de scénarios (p)")
plt.xlabel("Nombre de scénarios (p)")
plt.ylabel("Temps moyen (secondes)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# --------- Graphique 2: Temps en fonction de n ---------
plt.figure(figsize=(10, 5))
for p in p_values:
    maxOWA_times = [times_maxOWA[(n, p)] for n in n_values]
    minOWA_times = [times_minOWA_regret[(n, p)] for n in n_values]

    plt.plot(n_values, maxOWA_times, marker='o', label=f'maxOWA (p={p})')
    plt.plot(n_values, minOWA_times, marker='s', linestyle='--', label=f'minOWA regrets (p={p})')

plt.title("Temps d'exécution en fonction du nombre de projets (n)")
plt.xlabel("Nombre de projets (n)")
plt.ylabel("Temps moyen (secondes)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()