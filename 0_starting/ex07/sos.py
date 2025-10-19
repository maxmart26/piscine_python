#!/usr/bin/env python3
"""
sos.py — Encode une chaîne en code Morse.

Le programme prend une chaîne (alphanumérique + espaces)
et renvoie son équivalent en code Morse.

Usage :
    ./sos.py "sos"
    ./sos.py "Hello World"

Exemple :
    $ python sos.py "sos" | cat -e
    ... --- ...$
"""

import sys

# Dictionnaire Morse (espaces inclus)
NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",    "B": "-... ",  "C": "-.-. ", "D": "-.. ",
    "E": ". ",     "F": "..-. ",  "G": "--. ",  "H": ".... ",
    "I": ".. ",    "J": ".--- ",  "K": "-.- ",  "L": ".-.. ",
    "M": "-- ",    "N": "-. ",    "O": "--- ",  "P": ".--. ",
    "Q": "--.- ",  "R": ".-. ",   "S": "... ",  "T": "- ",
    "U": "..- ",   "V": "...- ",  "W": ".-- ",  "X": "-..- ",
    "Y": "-.-- ",  "Z": "--.. ",
    "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ",
    "4": "....- ", "5": "..... ", "6": "-.... ", "7": "--... ",
    "8": "---.. ", "9": "----. ",
}


def main():
    """Point d'entrée du programme."""
    try:
        assert len(sys.argv) == 2, "Le programme attend exactement 1 argument."
        text = sys.argv[1]

        # Vérifie que tous les caractères sont valides
        assert all(c.isalnum() or c.isspace() for c in text), \
            "the arguments are bad"

        # Encode chaque caractère avec le dictionnaire (en majuscule)
        morse = "".join([NESTED_MORSE[c.upper()] for c in text])
        print(morse.strip())

    except (AssertionError, KeyError) as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
