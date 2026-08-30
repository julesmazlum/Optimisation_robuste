# MOGPL — Optimisation Robuste dans l'Incertain Total

Projet L3 Informatique 2023-2024 — UE Modélisation, Optimisation, Graphes et Programmation Linéaire (MOGPL), Sorbonne Université. Auteurs : Jules MAZLUM, Zahra SIDDIQUE (Groupe 3).

## Description / Sujet

Ce projet porte sur la résolution de problèmes d'optimisation combinatoire (sac à dos et plus court chemin) dans un contexte d'**incertitude totale**, où les probabilités des scénarios sont inconnues.

L'objectif est de trouver des solutions robustes en utilisant la programmation linéaire (PL) et le solveur **Gurobi**. Quatre critères de robustesse sont implémentés et comparés :

1. **MaxMin** : maximiser le pire des cas.
2. **MinMax Regret** : minimiser le regret maximum (écart par rapport à l'optimum de chaque scénario).
3. **MaxOWA** (Ordered Weighted Average) : maximiser une moyenne pondérée ordonnée (focus sur les scénarios les plus défavorables).
4. **MinOWA des Regrets** : minimiser la moyenne pondérée ordonnée des regrets.

## Structure du dépôt

Le problème du sac à dos (critères MaxMin / MinMax Regret / MaxOWA / MinOWA des regrets) est traité dans `src/Partie1/` et `src/Partie2/` ; la recherche de chemin robuste sur graphes est traitée dans `src/Partie3/`.

```text
.
├── src/
│   ├── Partie1/                        Sac à dos — critères MaxMin, MinMax Regret
│   │   ├── generator.py                Génération d'instances aléatoires
│   │   ├── main.py                     Tests de performance et graphiques (MaxMin, MinMax Regret)
│   │   ├── maxmin.py                   Résolution selon le critère MaxMin
│   │   ├── minmax_regret.py            Résolution selon le critère MinMax Regret
│   │   ├── mogplex.py                  Module utilitaire (modélisation PL)
│   │   ├── s1_optimal.py               Optimum local du scénario 1
│   │   └── s2_optimal.py               Optimum local du scénario 2
│   ├── Partie2/                        Sac à dos — critères MaxOWA, MinOWA des regrets
│   │   ├── generator2.py               Génération d'instances aléatoires
│   │   ├── main2.py                    Tests de performance et graphiques (MaxOWA, MinOWA)
│   │   ├── maxOWA.py                   Résolution selon le critère MaxOWA linéarisé
│   │   ├── minOWA_regrets.py           Résolution selon le critère MinOWA des regrets linéarisé
│   │   ├── plot.py                     Génération des graphiques de temps de calcul
│   │   └── solver2.py                  Module utilitaire pour la résolution OWA
│   └── Partie3/                        Recherche de chemin robuste (graphe de gauche « g » et de droite « d »)
│       ├── maxmin_g.py, maxmin_d.py                 MaxMin (gauche / droite)
│       ├── minmax_regret_g.py, minmax_regret_d.py   MinMax Regret (gauche / droite)
│       ├── maxOWA_g.py, minOWA_g.py                 MaxOWA / MinOWA (gauche)
│       ├── sg1_optimal.py, sg2_optimal.py           Optimums, graphe de gauche
│       ├── sd1_optimal.py, sd2_optimal.py           Optimums, graphe de droite
│       ├── mogplex.py, solver2V2.py                 Modules utilitaires
│       └── statistiques/                            Résultats statistiques générés
├── projetmogpl24.pdf                   Énoncé du sujet
└── GR3_MAZLUM_SIDDIQUE.pdf             Rapport du projet
```

## Installation / Prérequis

Python 3 et le solveur Gurobi.

```bash
pip install gurobipy matplotlib
```

## Utilisation

Depuis le dossier de la partie concernée, exécuter la résolution d'un critère spécifique, par exemple MinMax Regret sur le problème du sac à dos :

```bash
cd src/Partie1
python minmax_regret.py
```

Les scripts `main.py` (`Partie1/`) et `main2.py` (`Partie2/`) lancent les benchmarks comparant les critères sur des instances de tailles croissantes.

## Résultats principaux

- Les benchmarks (`main.py`, `main2.py`) génèrent des graphiques de temps de résolution en fonction de la taille des instances (nombre de scénarios *n*, nombre de projets/sommets *p*).
- Ces graphiques permettent de comparer l'efficacité des quatre critères de robustesse (MaxMin, MinMax Regret, MaxOWA, MinOWA des regrets) sur le problème du sac à dos et sur les deux instances de graphes étudiées.
- Le détail est présenté dans le rapport `GR3_MAZLUM_SIDDIQUE.pdf`.

## Auteurs

- Jules MAZLUM
- Zahra SIDDIQUE
