"""Summing the elements of a list using different loops."""

__author__ = "730569217"


def w_sum(vals: list[float]) -> float:
    """While loop."""
    index = 0
    total = 0.0
    while index < len(vals):
        total += vals[index]
        index += 1
    return total


def f_sum(vals: list[float]) -> float:
    """For in loop."""
    total = 0.0
    for amount in vals:
        total += amount
    return total


def f_range_sum(vals: list[float]) -> float:
    """Range loop."""
    total = 0.0 
    for i in range(len(vals)):
        total += vals[i]
    return total






        
