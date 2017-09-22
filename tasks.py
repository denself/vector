#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import math

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
    print(Vector(5.581, -2.136).get_normal())
    print(Vector(1.996, 3.108, -4.554).get_normal())


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


if __name__ == '__main__':
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
