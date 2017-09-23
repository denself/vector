#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from typing import Tuple, Iterable, Union

from decimal import Decimal

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

        self.normal_vector = normal_vector
        self.constant_term = Decimal(constant_term)
        self.base_point = None

        base_point_coords = ['0'] * self.dimension
        initial_index = self._first_nonzero_index(self.normal_vector)
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

    def is_equal(self, other: 'Line') -> bool:
        """
        >>> Line(Vector(2, 3), 5).is_equal(Line(Vector(4, 6), 10))
        True
        >>> Line(Vector(2, 3), 5).is_equal(Line(Vector(4, 5), 10))
        False
        """
        if not self.is_parallel(other):
            return False

        middle_vector = self.base_point - other.base_point

        return self.normal_vector.is_orthogonal(middle_vector)

    def get_intersection(self, other: 'Line') -> Vector:
        """
        >>> Line(Vector(3, 3), 6).get_intersection(Line(Vector(3, -3), 3))
        Vector(1.5, 0.5)
        >>> Line(Vector(2, 3), 5).get_intersection(Line(Vector(4, 6), 10))
        Traceback (most recent call last):
        ...
        line.LinesEqualException: Infinite amount of intersection points
        >>> Line(Vector(2, 3), 5).get_intersection(Line(Vector(4, 6), 3))
        Traceback (most recent call last):
        ...
        line.LinesParallelException: No intersection points
        """
        if self.is_equal(other):
            raise LinesEqualException("Infinite amount of intersection points")
        if self.is_parallel(other):
            raise LinesParallelException("No intersection points")

        a, b = self.normal_vector
        c, d = other.normal_vector
        k1, k2 = self.constant_term, other.constant_term

        return Vector((d * k1 - b * k2) / (a * d - b * c),
                      (a * k2 - c * k1) / (a * d - b * c))

    @staticmethod
    def _first_nonzero_index(iterable: Iterable) -> int:
        for k, item in enumerate(iterable):
            if not abs(item) < 1e-10:
                return k

    def __str__(self):
        """
        >>> Line(Vector(2, 3), 1)
        Line(2x_0+3x_1=1)
        """
        class_name = self.__class__.__name__
        initial_index = self._first_nonzero_index(self.normal_vector)

        def to_coef(value, index: int):
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
            output = ''.join(to_coef(v, i) for i, v in enumerate(self.normal_vector))
            if output.startswith('+'):
                output = output[1:]

            constant = round(self.constant_term)
            if constant % 1 == 0:
                constant = int(constant)

            output += f'={constant}'

        return f'{class_name}({output})'

    __repr__ = __str__


if __name__ == '__main__':
    print(Line(Vector(-2, 3), 5))
