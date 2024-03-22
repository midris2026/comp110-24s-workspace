"""Mutating functions."""

__author__ = "730569217"


def manual_append(list: list[int], number: int) -> None:
    """Mutate."""
    list.append(number)


def double(numbers: list[int]) -> None:
    """Double the number."""
    i: int = 0 
    while i < len(numbers):
        numbers[i] *= 2
        i += 1
