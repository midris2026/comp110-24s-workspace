"""Recursion CQ."""

__author__ = "730569217"


def f(n: int, k: int) -> int:
    """Recursion of multiplication of two integers."""
    if n == 0:
        return 0
    else:
        return k + f(n - 1, k)
    