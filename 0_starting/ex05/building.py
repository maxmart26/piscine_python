#!/usr/bin/env python3
"""
building.py — Analyse un texte et compte :
- les lettres majuscules
- les lettres minuscules
- les signes de ponctuation
- les chiffres
- les espaces

Usage :
    python building.py "Votre texte ici"
"""

import sys
import string


def count_characters(text: str) -> dict:
    """
    Compte les majuscules, minuscules, ponctuations, chiffres et espaces dans le texte.

    Args:
        text (str): La chaîne de caractères à analyser.

    Returns:
        dict: Un dictionnaire contenant les comptes.
    """
    counts = {
        "upper": 0,
        "lower": 0,
        "punctuation": 0,
        "digits": 0,
        "spaces": 0
    }

    extra = "–—"
    for char in text:
        if char.isupper():
            counts["upper"] += 1
        elif char.islower():
            counts["lower"] += 1
        elif char.isdigit():
            counts["digits"] += 1
        elif char in string.punctuation or char in extra:
            counts["punctuation"] += 1
        elif char.isspace():
            counts["spaces"] += 1

    return counts


def main():
    """
    Fonction principale du programme.
    Gère les arguments et affiche les résultats.
    """
    try:
        # Vérifie le nombre d’arguments
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")

        # Si aucun argument → demander une entrée
        if len(sys.argv) == 1:
            text = input("What is the text to count?\n")
        else:
            text = sys.argv[1]

        # Analyse du texte
        counts = count_characters(text)
        total = len(text)

        # Affichage formaté
        print(f"The text contains {total} characters:")
        print(f"{counts['upper']} upper letters")
        print(f"{counts['lower']} lower letters")
        print(f"{counts['punctuation']} punctuation marks")
        print(f"{counts['spaces']} spaces")
        print(f"{counts['digits']} digits")

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
