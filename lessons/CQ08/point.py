"""CQ08."""
from __future__ import annotations
__author__ = "730569217"


class Point:
    """Assigning point class."""

    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Point class."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Mutating to multiple x and y by the factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Not mutating to create a new point."""
        nxpoint = self.x * factor
        nypoint = self.y * factor
        npoint: Point = Point(nxpoint, nypoint)
        return npoint