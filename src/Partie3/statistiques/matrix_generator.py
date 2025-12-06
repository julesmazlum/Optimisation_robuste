from graph_generator import *

"""
cette fonction génère la matrice de contrainte sur les arcs du graphe G, avec p sommets.
vous trouverez un tests à la fin du fichier pour pouvoir tester cette fonction.
"""

def generate_flow_matrix(G, p):
    """
    Matrice des contraintes sur le flot
    Génère une matrice de flots qui respecte les contraintes :
    - arcs sortants de la source (1ère ligne) = 1
    - arcs entrants au puits (dernière ligne) = 1
    - pour les autres sommets, arcs entrants = 1, arcs sortants = -1
    """
    # initialiser une matrice vide
    flow_matrix = np.zeros((p, len(G.edges())), dtype=int)

    # lister les arcs dans l'ordre
    arcs = list(G.edges())

    # remplir la matrice
    for i in range(p):
        for idx, (u, v) in enumerate(arcs):
            if i == u:  # arc sortant du sommet i
                flow_matrix[i, idx] = -1
            if i == v:  # arc entrant au sommet i
                flow_matrix[i, idx] = 1

    # ajuster la source (ligne 0) : seulement les arcs sortants
    flow_matrix[0, :] = [1 if u == 0 else 0 for u, v in arcs]

    # ajuster le puits (ligne p-1) : seulement les arcs entrants
    flow_matrix[-1, :] = [1 if v == p - 1 else 0 for u, v in arcs]

    last_line = flow_matrix[-1, :]
    flow_matrix = np.delete(flow_matrix, -1, axis=0)
    flow_matrix = np.insert(flow_matrix, 1, last_line, axis=0)

    return flow_matrix


"""G = generate_flow_graph(1,0.5,7)

print("Arcs du graphe :")
for u, v, data in G.edges(data=True):
    print(f"({u} -> {v}) : {data['costs']}")

mat = generate_flow_matrix(G,7)
print(mat)"""