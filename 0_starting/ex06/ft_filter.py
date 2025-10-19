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
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable
    for which function(item)
    is true.  If function is None, return the items that are true.
    """
    if function is None:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))
