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
