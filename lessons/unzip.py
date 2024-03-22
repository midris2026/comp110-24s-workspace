"""Splitting a dictionary into two lists."""

__author__ = "730569217"


def get_keys(dict1: dict[str, int]) -> list[str]:
    """List the keys in the dictionary."""
    keys = []
    for key in dict1: 
        keys.append(key)
    return keys


def get_values(dict1: dict[str, int]) -> list[int]:
    """List all the values in dictionary."""
    values = []
    for value in dict1: 
        values.append(dict1[value])
    return values