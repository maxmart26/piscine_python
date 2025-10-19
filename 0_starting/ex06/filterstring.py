#!/usr/bin/env python3
"""
filterstring.py — Programme principal de la Partie 2.

Ce script prend deux arguments :
  1. une chaîne de caractères S
  2. un entier N

Il affiche la liste des mots de S dont la
longueur est strictement supérieure à N.

Utilisation :
    ./filterstring.py "Hello world Python piscine" 5
Résultat :
    ['Python', 'piscine']
"""

import sys
from ft_filter import ft_filter


def main():
    """Point d'entrée principal du programme."""
    try:
        # Vérification du nombre d'arguments
        assert len(sys.argv) == 3
        "Le programme attend exactement 2 arguments."

        s = sys.argv[1]
        n = int(sys.argv[2])  # Convertit le 2e argument en entier

        # Vérifie que s est bien une chaîne
        assert isinstance(s, str), "Le premier argument doit être une chaîne."

        # Découpe la phrase en mots
        words = [word for word in s.split()]  # list comprehension ✅

        # Filtrage avec lambda et ft_filter ✅
        longer_words = ft_filter(lambda word: len(word) > n, words)

        # Affiche la liste résultante
        print(list(longer_words))

    except (ValueError, AssertionError) as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
