#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from typing import Iterable, Union

from plane import Plane
from tools import first_nonzero_index
from vector import Vector


class LinearSystem:

    def __init__(self,
                 *planes: Union[Plane, Vector]):

        self.planes = list(planes)
        self.dimension = self.planes[0].dimension
        for p in self.planes[1:]:
            assert p.dimension == self.dimension,\
                'All planes in the system should live in the same dimension'

    def swap_rows(self, index1, index2):
        """
        >>> p0 = Plane(Vector('1','1','1'), '1')
        >>> p1 = Plane(Vector('0','1','0'), '2')
        >>> p2 = Plane(Vector('1','1','-1'), '3')
        >>> p3 = Plane(Vector('1','0','-2'), '2')
        >>> s = LinearSystem(p0, p1, p2, p3)
        >>> s.swap_rows(0,1)
        >>> s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3
        True
        >>> s.swap_rows(1,3)
        >>> s[0] == p1 and s[1] == p3 and s[2] == p2 and s[3] == p0
        True
        >>> s.swap_rows(3,1)
        >>> s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3
        True
        """
        self[index1], self[index2] = self[index2], self[index1]

    def multiply_coefficient_and_row(self, coefficient, index):
        """
        >>> p0 = Plane(Vector('1','1','1'), '1')
        >>> p1 = Plane(Vector('0','1','0'), '2')
        >>> p2 = Plane(Vector('1','1','-1'), '3')
        >>> p3 = Plane(Vector('1','0','-2'), '2')
        >>> s = LinearSystem(p1, p0, p2, p3)
        >>> s.multiply_coefficient_and_row(1, 0)
        >>> s.multiply_coefficient_and_row(-1, 2)
        >>> s.multiply_coefficient_and_row(10,1)
        >>> s[0] == p1
        True
        >>> s[1] == Plane(Vector('10','10','10'), '10')
        True
        >>> s[2] == Plane(Vector('-1','-1','1'), '-3')
        True
        >>> s[3] == p3
        True
        """
        self[index] = self[index] * coefficient

    def add_multiple_times_row_to_row(self, coefficient, index_to_add,
                                      index_to_be_added):
        """
        >>> p0 = Plane(Vector('10','10','10'), '10')
        >>> p1 = Plane(Vector('0','1','0'), '2')
        >>> p2 = Plane(Vector('-1','-1','1'), '-3')
        >>> p3 = Plane(Vector('1','0','-2'), '2')
        >>> s = LinearSystem(p1, p0, p2, p3)
        >>> s.add_multiple_times_row_to_row(0,0,1)
        >>> s[0] == p1
        True
        >>> s[1] == Plane(Vector('10','10','10'), '10')
        True
        >>> s[2] == Plane(Vector('-1','-1','1'), '-3')
        True
        >>> s[3] == p3
        True
        >>> s.add_multiple_times_row_to_row(1,0,1)
        >>> s[0] == p1
        True
        >>> s[1] == Plane(Vector('10','11','10'), '12')
        True
        >>> s[2] == Plane(Vector('-1','-1','1'), '-3')
        True
        >>> s[3] == p3
        True

        >>> s.add_multiple_times_row_to_row(-1,1,0)
        >>> s[0] == Plane(Vector('-10','-10','-10'), '-10')
        True
        >>> s[1] == Plane(Vector('10','11','10'), '12')
        True
        >>> s[2] == Plane(Vector('-1','-1','1'), '-3')
        True
        >>> s[3] == p3
        True
        """
        scaled_row = self[index_to_add] * coefficient
        self[index_to_be_added] = self[index_to_be_added] + scaled_row

    def indices_of_first_nonzero_term_in_each_row(self):
        num_equations = len(self)

        indices = [-1] * num_equations

        for i, p in enumerate(self):
            index = first_nonzero_index(p.normal_vector)
            if index is None:
                continue
            indices[i] = index

        return indices

    def __len__(self):
        return len(self.planes)

    def __iter__(self):
        return iter(self.planes)

    def __getitem__(self, i):
        return self.planes[i]

    def __setitem__(self, i, x):
        assert x.dimension == self.dimension,\
            'All planes in the system should live in the same dimension'

        self.planes[i] = x

    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret

