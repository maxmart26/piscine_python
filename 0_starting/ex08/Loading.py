#!/usr/bin/env python3
"""
Loading.py — ft_tqdm : barre de progression façon tqdm,
via un générateur (yield).
"""

from __future__ import annotations

import sys
import time
from typing import Generator


def _format_time(seconds: float) -> str:
    """Formate un nombre de secondes en mm:ss."""
    if seconds < 0 or seconds == float("inf"):
        return "??:??"
    m, s = divmod(int(seconds + 0.5), 60)
    return f"{m:02d}:{s:02d}"


def _safe_rate(done: int, elapsed: float) -> float:
    """Renvoie un débit it/s sans division par zéro."""
    return done / elapsed if elapsed > 1e-12 else float("inf")


def ft_tqdm(lst: range) -> Generator[int, None, None]:
    """
    ft_tqdm(lst: range) -> iterator

    Imite (approximativement) le rendu de tqdm pour un `range`.
    Affiche une barre du type :
    " 42%|██████▌....................| 140/333 [00:00<00:01, 214.73it/s]"

    Notes :
    - Utilise `yield` pour rester paresseux (lazy) comme tqdm.
    - Se focalise sur les éléments essentiels (%, barre, compteur,
    elapsed, ETA, it/s).
    - Prévu pour un objet `range` (total connu).
    """
    total = len(lst)
    if total == 0:
        # Rien à itérer : montrer une barre vide puis terminer
        sys.stdout.write("  0%| | 0/0 [00:00<00:00, 0.00it/s]\r")
        sys.stdout.flush()
        sys.stdout.write("\n")
        return

    bar_len = 30  # longueur de la barre (tqdm ≈ 28,
    # on prend 30 pour la lisibilité)
    start = time.time()

    for idx, item in enumerate(lst, start=1):
        # Mesures temps
        elapsed = max(time.time() - start, 0.0)
        rate = _safe_rate(idx, elapsed)  # it/s
        remain = (total - idx) / rate if rate != float("inf") else float("inf")

        # Barre
        frac = idx / total
        filled = int(bar_len * frac + 0.0000001)
        bar = "█" * filled + " " * (bar_len - filled)

        # Pourcentage & compteur
        percent = int(frac * 100)
        left = _format_time(remain)
        spent = _format_time(elapsed)

        # Ligne de statut (proche de tqdm)
        # Ex: " 42%|██████▌               | 140/333 [00:00<00:01, 214.73it/s]"
        line = (
            f"{percent:3d}%|{bar}| {idx}/{total} "
            f"[{spent}<{left}, "
            f"{(f'{rate:.2f}' if rate != float('inf') else '∞')}it/s]"
        )

        # Impression en place
        sys.stdout.write("\r" + line)
        sys.stdout.flush()

        # Yield l'élément
        yield item

    # Fin : s'assurer que la barre est à 100% et aller à la ligne
    elapsed = max(time.time() - start, 0.0)
    rate = _safe_rate(total, elapsed)
    left = _format_time(0.0)
    spent = _format_time(elapsed)
    bar = "█" * bar_len
    line = (
        f"100%|{bar}| {total}/{total} "
        f"[{spent}<{left}, "
        f"{(f'{rate:.2f}' if rate != float('inf') else '∞')}it/s]"
    )
    sys.stdout.write("\r" + line + "\n")
    sys.stdout.flush()
