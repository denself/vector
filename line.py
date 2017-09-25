#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from decimal import Decimal
from typing import Union

from tools import is_zero, first_nonzero_index, to_decimal
from vector import Vector


class GeometryException(Exception):
    """"""


class LinesParallelException(GeometryException):
    """"""


class LinesEqualException(GeometryException):
    """"""


class Line:
    precision = None

    def __init__(self,
                 normal_vector: Vector,
                 constant_term: Union[int, float, str, Decimal]):

        self.dimension = 2

        self.normal_vector: Vector = normal_vector
        self.constant_term = to_decimal(constant_term)
        self.base_point = None

        base_point_coords = ['0'] * self.dimension
        initial_index = first_nonzero_index(self.normal_vector)
        if initial_index is not None:
            initial_coefficient = self.normal_vector[initial_index]
            base_point_coords[initial_index] = \
                self.constant_term / initial_coefficient
            self.base_point = Vector(*base_point_coords)

    def is_parallel(self, other: 'Line') -> bool:
        """
        >>> Line(Vector(2, 3), 5).is_parallel(Line(Vector(4, 6), 3))
        True
        >>> Line(Vector(2, 3), 5).is_parallel(Line(Vector(4, 5), 3))
        False
        """
        return self.normal_vector.is_parallel(other.normal_vector)

    def __eq__(self, other: 'Line') -> bool:
        """
        >>> Line(Vector(2, 3), 5) == Line(Vector(4, 6), 10)
        True
        >>> Line(Vector(2, 3), 5) == Line(Vector(4, 5), 10)
        False
        """
        if not self.normal_vector:
            if other.normal_vector:
                return False
            else:
                diff = self.constant_term - other.constant_term
                return is_zero(diff)
        elif not other.normal_vector:
            return False

        if not self.is_parallel(other):
            return False

        middle_vector = self.base_point - other.base_point

        return self.normal_vector.is_orthogonal(middle_vector)

    def get_intersection(self, other: 'Line') -> Union['Line', Vector, None]:
        """
        >>> Line(Vector(3, 3), 6).get_intersection(Line(Vector(3, -3), 3))
        Vector(1.5, 0.5)
        >>> Line(Vector(2, 3), 5).get_intersection(Line(Vector(4, 6), 10))
        Line(2x_0+3x_1=5)
        >>> Line(Vector(2, 3), 5).get_intersection(Line(Vector(4, 6), 3))

        """
        if self == other:
            return self
        if self.is_parallel(other):
            return None

        a, b = self.normal_vector
        c, d = other.normal_vector
        k1, k2 = self.constant_term, other.constant_term

        return Vector((d * k1 - b * k2) / (a * d - b * c),
                      (a * k2 - c * k1) / (a * d - b * c))

    def __str__(self):
        """
        >>> Line(Vector(2, 3), 1)
        Line(2x_0+3x_1=1)
        """
        class_name = self.__class__.__name__
        initial_index = first_nonzero_index(self.normal_vector)

        def to_coeff(value, index: int):
            value = round(value, self.precision)
            if not value % 1:
                value = int(value)

            if not value:
                return ''

            result = f'{value:+}x_{index}'
            return result

        if initial_index is None:
            output = '0'

        else:
            output = ''.join(to_coeff(v, i) for i, v in
                             enumerate(self.normal_vector))
            if output.startswith('+'):
                output = output[1:]

            constant = round(self.constant_term)
            if constant % 1 == 0:
                constant = int(constant)

            output += f'={constant}'

        return f'{class_name}({output})'

    __repr__ = __str__
