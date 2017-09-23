#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import math

from line import Line, GeometryException
from vector import Vector


def task_1():
    """
    Lesson 2.4
    Basic functions:
    - Adding and subtraction of vectors
    - Scalar multiplication
    """

    print(f"\n{'Task 1':^79s}")
    print(Vector(8.218, -9.341) + Vector(-1.129, 2.111))
    print(Vector(7.119, 8.215) - Vector(-8.223, 0.878))
    print(7.41 * Vector(1.671, -1.012, -0.318))


def task_2():
    """
    Lesson2.6
    Magnitude and Normalization of vector
    """

    print(f"\n{'Task 2':^79s}")
    print(f'{Vector(-0.221, 7.437).magnitude:.3}')
    print(f'{Vector(8.813, -1.331, -6.247).magnitude:.3}')
    print(Vector(5.581, -2.136).get_unit_vector())
    print(Vector(1.996, 3.108, -4.554).get_unit_vector())


def task_3():
    """
    Lesson 2.8
    Inner product (dot product) and Angle between vectors
    """

    print(f"\n{'Task 3':^79s}")
    print(f'{Vector(7.887, 4.138) * Vector(-8.802, 6.776):.3f}')
    print(
        f'{Vector(-5.955, -4.904, -1.874) * Vector(-4.496, -8.755, 7.103):.3f}')
    print(f'{Vector(3.183, -7.627).angle_to(Vector(-2.668, 5.319)):.3f}')
    print(f'''{math.degrees(
        Vector(7.35, 0.221, 5.188).angle_to(Vector(2.751, 8.259, 3.985))
    ):.3f}''')


def task_4():
    """
    Lesson 2.10
    Parallelism and Orthogonality
    """
    print(f"\n{'Task 4':^79s}")
    print(Vector('-7.579', '-7.88')
          .is_parallel(Vector('22.737', '23.64')))
    print(Vector('-7.579', '-7.88')
          .is_orthogonal(Vector('22.737', '23.64')))

    print(Vector('-2.029', '9.97', '4.172')
          .is_parallel(Vector('-9.231', '-6.639', '-7.245')))
    print(Vector('-2.029', '9.97', '4.172')
          .is_orthogonal(Vector('-9.231', '-6.639', '-7.245')))

    print(Vector('-2.328', '-7.284', '-1.214')
          .is_parallel(Vector('-1.821', '1.072', '-2.94')))
    print(Vector('-2.328', '-7.284', '-1.214')
          .is_orthogonal(Vector('-1.821', '1.072', '-2.94')))

    print(Vector('2.118', '4.827').is_parallel(Vector(0, 0)))
    print(Vector('2.118', '4.827').is_orthogonal(Vector(0, 0)))


def task_5():
    """
    Lesson 2.12
    Vector projections
    """
    print(f"\n{'Task 5':^79s}")
    print(Vector('3.039', '1.879').project_on(Vector('0.825', '2.036'))[0])
    print(Vector('-9.88', '-3.264', '-8.159')
          .project_on(Vector('-2.155', '-9.353', '-9.473'))[1])
    print(Vector('3.009', '-6.172', '3.692', '-2.51')
          .project_on(Vector('6.404', '-9.144', '2.759', '8.718')))


def task_6():
    """
    Lesson 2.14
    Cross-product
    """
    print(f"\n{'Task 6':^79s}")
    print(Vector('8.462', '7.893', '-8.187')
          .cross_product(Vector('6.984', '-5.975', '4.778')))
    print(Vector('-8.987', '-9.838', '5.031')
          .cross_product(Vector('-4.268', '-1.861', '-8.866')).magnitude)
    print(Vector('1.5', '9.547', '3.691')
          .cross_product(Vector('-6.007', '0.124', '5.772')).magnitude / 2)


def task_7():
    """
    Lesson 3.4
    Intersections of lines
    """
    print(f"\n{'Task 7':^79s}")
    print(Line(Vector('4.046', '2.836'), '1.21')
          .get_intersection(Line(Vector('10.115', '7.09'), '3.025')))
    print(Line(Vector('7.204', '3.182'), '8.68')
          .get_intersection(Line(Vector('8.172', '4.114'), '9.883')))
    print(Line(Vector('1.182', '5.562'), '6.744')
          .get_intersection(Line(Vector('1.773', '8.343'), '9.525')))



if __name__ == '__main__':
    Vector.precision = 4
    # task_1()
    # task_2()
    # task_3()
    # task_4()
    # task_5()
    # task_6()

    task_7()
