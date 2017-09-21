#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import math
from decimal import Decimal, getcontext
from typing import Union


getcontext().prec = 30


class Vector:
    def __init__(self, *coordinates: Union[float, str]):

        self.coordinates = tuple([Decimal(x) for x in coordinates])

        self.dimensions = len(self.coordinates)

    @property
    def magnitude(self) -> Decimal:
        """
        >>> Vector(3, 4).magnitude
        Decimal('5')
        >>> Vector(5, 12).magnitude
        Decimal('13')
        """
        return Decimal.sqrt(sum(map(lambda x: x * x, self.coordinates)))

    def get_normal(self) -> 'Vector':
        """
        >>> abs(Vector(-2, 2).get_normal().magnitude - 1) < 0.00001
        True
        >>> abs(Vector(5, -4).get_normal().magnitude - 1) < 0.000001
        True
        """
        if self.magnitude == 0:
            return Vector(*([0] * self.dimensions))
        return self / self.magnitude

    def angle_to(self, other: 'Vector') -> Decimal:
        """
        >>> abs(float(Vector(0, 1).angle_to(Vector(1, 0))) - math.pi / 2) < 0.1
        True
        >>> Vector(2, 4).angle_to(Vector(4, 8))
        Decimal('0')
        >>> Vector(1, 2).angle_to(Vector(1, 2, 3))
        Traceback (most recent call last):
        ...
        AssertionError
        """
        assert self.dimensions == other.dimensions

        return Decimal(math.acos(self.get_normal() * other.get_normal()))

    def is_parallel(self, other: 'Vector') -> bool:
        """
        >>> Vector(1, 2).is_parallel(Vector(2, 4))
        True
        >>> Vector(1, 2).is_parallel(Vector(2, 5))
        False
        >>> Vector(0, 0).is_parallel(Vector(2, 5))
        True
        >>> Vector(1, 2).is_parallel(Vector(0, 0))
        True
        >>> Vector(0, 2).is_parallel(Vector(2, 4))
        False

        """
        assert self.dimensions == other.dimensions

        if not any(self.coordinates):
            return True

        if not any(other.coordinates):
            return True

        pairs = zip(self.coordinates, other.coordinates)

        k = None

        for self_x, other_x in pairs:
            if self_x == 0 and other_x == 0:
                continue

            if self_x and not other_x:
                return False

            if k is None:
                k = self_x / other_x
                continue

            if self_x / other_x != k:
                return False

        return True

    def is_orthogonal(self, other: 'Vector') -> bool:
        """
        >>> Vector(2, 4).is_orthogonal(Vector(-4, 2))
        True
        >>> Vector(2, 4).is_orthogonal(Vector(-4, 3))
        False
        >>> Vector(0, 0).is_orthogonal(Vector(-4, 3))
        True
        >>> Vector(2, 4).is_orthogonal(Vector(0, 0))
        True
        """
        return self * other == 0

    def __eq__(self, other: 'Vector') -> bool:
        """
        >>> Vector(1, 2) == Vector(1, 2)
        True
        >>> Vector(1, 2) == Vector(2, 2)
        False
        >>> Vector(1, 2) == Vector(1, 2, 3)
        False
        """
        return self.coordinates == other.coordinates

    def __add__(self, other: 'Vector') -> 'Vector':
        """
        >>> Vector(1, 2) + Vector(2, 3)
        Vector(3, 5)
        >>> Vector(4, 5) + Vector(-4, -5)
        Vector(0, 0)
        >>> Vector(1, 2) + Vector(1, 2, 3)
        Traceback (most recent call last):
        ...
        AssertionError
        """
        assert self.dimensions == other.dimensions

        return Vector(*map(sum,
                           zip(self.coordinates, other.coordinates)))

    def __sub__(self, other: 'Vector') -> 'Vector':
        """
        >>> Vector(1, 2) - Vector(2, 3)
        Vector(-1, -1)
        >>> Vector(4, 5) - Vector(-4, -5)
        Vector(8, 10)
        >>> Vector(1, 2) - Vector(1, 2, 3)
        Traceback (most recent call last):
        ...
        AssertionError
        """
        assert self.dimensions == other.dimensions

        return Vector(*map(lambda x: x[0]-x[1],
                           zip(self.coordinates, other.coordinates)))

    def __mul__(self, other: Union[float, 'Vector']) \
            -> Union['Vector', Decimal]:
        """
        >>> Vector(1, 2, 3) * 2
        Vector(2, 4, 6)
        >>> Vector(1, 2, 3) * 0
        Vector(0, 0, 0)
        >>> Vector(1, 2, 3) * -1
        Vector(-1, -2, -3)
        >>> Vector(1, 2) * Vector(1, 2)
        Decimal('5')
        >>> Vector(1, 2) * Vector(1, 2, 3)
        Traceback (most recent call last):
        ...
        AssertionError
        """
        if isinstance(other, Vector):
            assert self.dimensions == other.dimensions

            return sum(map(lambda x: x[0] * x[1],
                           zip(self.coordinates, other.coordinates)))
        elif isinstance(other, (int, float, Decimal)):

            return Vector(*map(lambda x: x * Decimal(other), self.coordinates))

        else:
            raise AssertionError

    def __rmul__(self, other: float) -> 'Vector':
        """
        >>> 5 * Vector(1, 1, 1)
        Vector(5, 5, 5)
        """
        return self.__mul__(other)

    def __truediv__(self, other: float) -> 'Vector':
        """
        >>> Vector(4, 5) / 2
        Vector(2, 2.5)
        """

        assert isinstance(other, (int, float, Decimal))

        other = Decimal(other)

        return Vector(*map(lambda x: x / other, self.coordinates))

    def __str__(self):
        """
        >>> str(Vector(1, 2, 3))
        'Vector(1, 2, 3)'
        """
        s = ', '.join(f'{x:.3}' for x in self.coordinates)
        return f"{self.__class__.__name__}({s})"

    def __repr__(self):
        """
        >>> Vector(1, 2, 3)
        Vector(1, 2, 3)
        """
        return str(self)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
