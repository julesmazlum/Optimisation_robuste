import networkx as nx
import numpy as np
import random

"""
cette fonction génère une graphe aléatoire avec n scéaniros et p sommets, et avec une densité d.
vous trouverez un tests à la fin du fichier pour pouvoir tester cette fonction.
"""

def generate_flow_graph(n, density, p):
    """
    p : nombre de nœuds
    density : densité des arcs (entre 0.3 et 0.5)
    n : nombre de scénarios
    """
    G = nx.DiGraph()  # graphe orienté

    # ajouter tous les nœuds
    for i in range(p):
        G.add_node(i)

    # choisir source et puits
    source = 0
    sink = p - 1

    # générer les arcs
    possible_arcs = [(i, j) for i in range(p) for j in range(p) if i < j]
    nb_arcs = int(density * len(possible_arcs))
    selected_arcs = random.sample(possible_arcs, nb_arcs)

    for u, v in selected_arcs:
        if u == source or v == sink:  # éviter les arcs "illogiques"
            continue
        G.add_edge(u, v, costs=[random.randint(1, 100) for _ in range(n)])

    # garantir que la source a des arcs sortants
    for v in range(1, p//3):
        if not G.has_edge(source, v):
            G.add_edge(source, v, costs=[random.randint(1, 100) for _ in range(n)])

    # garantir que le puits a des arcs entrants
    for u in range(int(p*0.8), p - 1):
        if not G.has_edge(u, sink):
            G.add_edge(u, sink, costs=[random.randint(1, 100) for _ in range(n)])

    return G


"""G = generate_flow_graph(2,0.5,7)

print("Arcs du graphe :")
for u, v, data in G.edges(data=True):
    print(f"({u} -> {v}) : {data['costs']}")"""