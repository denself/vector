#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from decimal import Decimal
from typing import Union

from tools import first_nonzero_index
from vector import Vector


class Plane:

    def __init__(self,
                 normal_vector: Vector,
                 constant_term: Union[float, str, Decimal]):
        self.dimension = 3

        self.normal_vector = normal_vector
        self.constant_term = Decimal(constant_term)

        base_point_coords = ['0'] * self.dimension
        initial_index = first_nonzero_index(self.normal_vector)
        if initial_index is not None:
            initial_coefficient = self.normal_vector[initial_index]
            base_point_coords[initial_index] = \
                self.constant_term / initial_coefficient
            self.base_point = Vector(*base_point_coords)

    def is_parallel(self, other: 'Plane') -> bool:
        """
        >>> Plane(Vector(1, 2, 3), 5).is_parallel(Plane(Vector(2, 4, 6), 3))
        True
        >>> Plane(Vector(1, 3, 3), 5).is_parallel(Plane(Vector(2, 4, 6), 3))
        False
        """
        return self.normal_vector.is_parallel(other.normal_vector)

    def __eq__(self, other: 'Plane') -> bool:
        """
        >>> Plane(Vector(1, 2, 3), 5) == Plane(Vector(2, 4, 6), 10)
        True
        >>> Plane(Vector(1, 2, 3), 5) == Plane(Vector(2, 4, 6), 9)
        False
        >>> Plane(Vector(1, 3, 3), 5) == Plane(Vector(2, 4, 6), 3)
        False
        """
        if not self.is_parallel(other):
            return False

        helper_vector = self.base_point - other.base_point

        return self.normal_vector.is_orthogonal(helper_vector)

    def __add__(self, other: 'Plane') -> 'Plane':
        """
        >>> Plane(Vector(1, 2, 3), 4) + Plane(Vector(2, 3, 1), 2)
        Plane(Vector(3, 5, 4), 6)
        >>> Plane(Vector(4, 5, 3), 4) + Plane(Vector(-4, -5, 1), 2)
        Plane(Vector(0, 0, 4), 6)
        """
        assert self.dimension == other.dimension

        return Plane(self.normal_vector + other.normal_vector,
                     self.constant_term + other.constant_term)

    def __mul__(self, other: Union[float, Decimal]) -> 'Plane':
        """
        >>> Plane(Vector(1, 2, 3), 1) * 2
        Plane(Vector(2, 4, 6), 2)
        >>> Plane(Vector(1, 2, 3), 1) * 0
        Plane(Vector(0, 0, 0), 0)
        >>> Plane(Vector(1, 2, 3), 1) * -1
        Plane(Vector(-1, -2, -3), -1)
        """
        other = Decimal(other)
        return Plane(self.normal_vector * other, self.constant_term * other)

    def __str__(self):
        class_name = self.__class__.__name__
        return f"{class_name}({self.normal_vector}, {self.constant_term})"

    __repr__ = __str__
