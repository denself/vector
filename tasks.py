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
    print(Vector((8.218, -9.341)) + Vector((-1.129, 2.111)))
    print(Vector((7.119, 8.215)) - Vector((-8.223, 0.878)))
    print(7.41 * Vector((1.671, -1.012, -0.318)))


def task_2():
    """
    Lesson2.6
    Magnitude and Normalization of vector
    """

    print(f"\n{'Task 2':^79s}")
    print(Vector((-0.221, 7.437)).magnitude)
    print(Vector((8.813, -1.331, -6.247)).magnitude)
    print(Vector((5.581, -2.136)).get_normal())
    print(Vector((1.996, 3.108, -4.554)).get_normal())

def task_3():
    """
    Lesson 2.8
    Inner product (dot product) and Angle between vectors
    """

    print(f"\n{'Task 3':^79s}")
    print(Vector((7.887, 4.138)) * Vector((-8.802, 6.776)))
    print(Vector((-5.955, -4.904, -1.874)) * Vector((-4.496, -8.755, 7.103)))
    print(Vector((3.183, -7.627)).angle_to(Vector((-2.668, 5.319))))
    print(math.degrees(
        Vector((7.35, 0.221, 5.188)).angle_to(Vector((2.751, 8.259, 3.985)))
    ))


if __name__ == '__main__':
    task_1()
    task_2()
    task_3()