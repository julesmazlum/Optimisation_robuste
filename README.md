# Projet MOGPL 2024 : Optimisation Robuste dans l'Incertain Total

**Sorbonne Université - Master ANDROIDE (M1)** **Cours :** Modélisation, Optimisation, Graphes et Programmation Linéaire (MOGPL)  

**Auteurs (Groupe 3) :** 
* Jules MAZLUM
* Zahra SIDDIQUE

---

## Description du Projet

Ce projet porte sur la résolution de problèmes d'optimisation combinatoire (Sac à dos et Plus court chemin) dans un contexte d'**incertitude totale**, où les probabilités des scénarios sont inconnues.

L'objectif est de trouver des solutions robustes en utilisant la **Programmation Linéaire (PL)** et le solveur **Gurobi**. Nous avons implémenté et comparé quatre critères de robustesse :

1.  **MaxMin** : Maximiser le pire des cas.
2.  **MinMax Regret** : Minimiser le regret maximum (écart par rapport à l'optimum de chaque scénario).
3.  **MaxOWA** (Ordered Weighted Average) : Maximiser une moyenne pondérée ordonnée (focus sur les scénarios les plus défavorables).
4.  **MinOWA des Regrets** : Minimiser la moyenne pondérée ordonnée des regrets.

## Structure du Répertoire

Le projet est divisé en deux grandes parties correspondant aux problèmes traités.

### Partie 1 : Problème du Sac à Dos (Sélection de projets)
Scripts pour la linéarisation des critères et la résolution du problème de sélection de projets sous contrainte budgétaire.

* `maxmin.py` : Résolution selon le critère MaxMin.
* `minmax_regret.py` : Résolution selon le critère MinMax Regret.
* `s1_optimal.py`, `s2_optimal.py` : Calcul des optimums locaux pour les scénarios 1 et 2 (nécessaire pour le calcul des regrets).
* `maxOWA.py` : Résolution selon le critère MaxOWA linéarisé.
* `minOWA-regrets.py` : Résolution selon le critère MinOWA des regrets linéarisé.
* `solver2.py` : Module utilitaire pour la résolution OWA.

### Partie 2 : Recherche de Chemin Robuste (Graphes)
Application des critères sur deux instances de graphes (Graphe de gauche "g" et Graphe de droite "d").

* **MaxMin** : `maxmin_g.py`, `maxmin_d.py`
* **MinMax Regret** : `minmax_regret_g.py`, `minmax_regret_d.py`
* **MaxOWA** : `maxOWA_g.py`
* **Optimums par scénario** :
    * `sg1_optimal.py`, `sg2_optimal.py` (Graphe de gauche)
    * `sd1_optimal.py`, `sd2_optimal.py` (Graphe de droite)

### Benchmarks et Générateurs
Scripts utilisés pour analyser l'évolution du temps de résolution en fonction de la taille du problème ($n$ scénarios, $p$ projets/sommets).

* `generator.py`, `generator2.py` : Génération d'instances aléatoires.
* `main.py`, `main2.py` : Exécution des tests de performance et génération des graphiques de temps de calcul.

## Prérequis et Installation

Ce projet nécessite **Python 3** et le solveur **Gurobi**.

 **Installer les dépendances Python :**
    ```bash
    pip install gurobipy matplotlib
    ```

## Utilisation

### Exécuter une résolution simple
Pour obtenir la solution optimale d'un critère spécifique (par exemple, MinMax Regret sur le problème du sac à dos) :

```bash
python minmax_regret.py
