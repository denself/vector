#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from typing import Iterable, Union

import math


class Vector:
    def __init__(self, coordinates: Iterable[float]):
        """
        >>> Vector((1, 2, 3))
        Vector((1, 2, 3))
        >>> Vector('test')
        Traceback (most recent call last):
        ...
        AssertionError
        """

        self.coordinates = tuple(coordinates)

        assert all(map(lambda x: isinstance(x, (float, int)),
                       self.coordinates))

        self.dimensions = len(self.coordinates)

    @property
    def magnitude(self) -> float:
        """
        >>> Vector([3, 4]).magnitude
        5.0
        >>> Vector([5, 12]).magnitude
        13.0
        """
        return math.sqrt(sum(map(lambda x: math.pow(x, 2), self.coordinates)))

    def get_normal(self) -> 'Vector':
        """
        >>> Vector((2, 2)).get_normal()
        Vector((0.7071067811865475, 0.7071067811865475))
        >>> Vector((5, -4)).get_normal().magnitude
        1.0
        """
        if self.magnitude == 0:
            return Vector([0] * self.dimensions)
        return self / self.magnitude

    def angle_to(self, other: 'Vector') -> float:
        """
        >>> abs(Vector((0, 1)).angle_to(Vector((1, 0))) - math.pi / 2) < 0.0001
        True
        >>> Vector((1, 2)).angle_to(Vector((1, 2, 3)))
        Traceback (most recent call last):
        ...
        AssertionError
        """
        assert self.dimensions == other.dimensions

        return math.acos(self.get_normal() * other.get_normal())

    def __eq__(self, other: 'Vector') -> bool:
        """
        >>> Vector((1, 2)) == Vector((1, 2))
        True
        >>> Vector((1, 2)) == Vector((2, 2))
        False
        >>> Vector((1, 2)) == Vector((1, 2, 3))
        False
        """
        return self.coordinates == other.coordinates

    def __add__(self, other: 'Vector') -> 'Vector':
        """
        >>> Vector((1, 2)) + Vector((2, 3))
        Vector((3, 5))
        >>> Vector((4, 5)) + Vector((-4, -5))
        Vector((0, 0))
        >>> Vector((1, 2)) + Vector((1, 2, 3))
        Traceback (most recent call last):
        ...
        AssertionError
        """
        assert self.dimensions == other.dimensions

        return Vector(map(sum,
                          zip(self.coordinates, other.coordinates)))

    def __sub__(self, other: 'Vector') -> 'Vector':
        """
        >>> Vector((1, 2)) - Vector((2, 3))
        Vector((-1, -1))
        >>> Vector((4, 5)) - Vector((-4, -5))
        Vector((8, 10))
        >>> Vector((1, 2)) - Vector((1, 2, 3))
        Traceback (most recent call last):
        ...
        AssertionError
        """
        assert self.dimensions == other.dimensions

        return Vector(map(lambda x: x[0]-x[1],
                          zip(self.coordinates, other.coordinates)))

    def __mul__(self, other: Union[float, 'Vector']) -> Union['Vector', float]:
        """
        >>> Vector((1, 2, 3)) * 2
        Vector((2, 4, 6))
        >>> Vector((1, 2, 3)) * 0
        Vector((0, 0, 0))
        >>> Vector((1, 2, 3)) * -1
        Vector((-1, -2, -3))
        >>> Vector((1, 2)) * Vector((1, 2))
        5
        >>> Vector((1, 2)) * Vector((1, 2, 3))
        Traceback (most recent call last):
        ...
        AssertionError
        """
        if isinstance(other, Vector):
            assert self.dimensions == other.dimensions

            return sum(map(lambda x: x[0] * x[1],
                           zip(self.coordinates, other.coordinates)))
        elif isinstance(other, (int, float)):

            return Vector(map(lambda x: x * other, self.coordinates))

        else:
            raise AssertionError

    def __rmul__(self, other: float) -> 'Vector':
        """
        >>> 5 * Vector((1, 1, 1))
        Vector((5, 5, 5))
        """
        return self.__mul__(other)

    def __truediv__(self, other: float) -> 'Vector':
        """
        >>> Vector((4, 5)) / 2
        Vector((2.0, 2.5))
        """

        assert isinstance(other, (int, float))

        return Vector(map(lambda x: x / other, self.coordinates))

    def __str__(self):
        """
        >>> str(Vector((1, 2, 3)))
        'Vector((1, 2, 3))'
        """
        return f"{self.__class__.__name__}({self.coordinates})"

    def __repr__(self):
        """
        >>> Vector((1, 2, 3))
        Vector((1, 2, 3))
        """
        return str(self)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
