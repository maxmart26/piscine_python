#!/usr/bin/env python3
"""
tester.py — Compare ft_tqdm et tqdm officiel.
"""

from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm


def main() -> None:
    # ft_tqdm
    for _ in ft_tqdm(range(333)):
        sleep(0.005)
    print()  # même que l'exemple donné

    # tqdm officiel
    for _ in tqdm(range(333)):
        sleep(0.005)
    print()


if __name__ == "__main__":
    main()
