#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from typing import Iterable


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

    def __mul__(self, other: float) -> 'Vector':
        """
        >>> Vector((1, 2, 3)) * 2
        Vector((2, 4, 6))
        >>> Vector((1, 2, 3)) * 0
        Vector((0, 0, 0))
        >>> Vector((1, 2, 3)) * -1
        Vector((-1, -2, -3))
        >>> Vector((1, 2)) * Vector((1, 2))
        Traceback (most recent call last):
        ...
        AssertionError
        """

        assert isinstance(other, (int, float))

        return Vector(map(lambda x: x * other, self.coordinates))

    def __rmul__(self, other: float) -> 'Vector':
        """
        >>> 5 * Vector((1, 1, 1))
        Vector((5, 5, 5))
        """
        return self.__mul__(other)

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

