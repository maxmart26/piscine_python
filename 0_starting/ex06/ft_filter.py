#!/usr/bin/env python3
"""
ft_filter.py — Recode du filtre intégré `filter()`.

Cette fonction retourne un itérable contenant les éléments pour
lesquels la fonction donnée renvoie True.

Usage:
    ft_filter(function, iterable)
"""

def ft_filter(function, iterable):
    """
    Imitation de la fonction filter().
    Retourne un itérateur contenant les éléments de 'iterable'
    pour lesquels 'function(item)' est True.
    """
    if function is None:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))
