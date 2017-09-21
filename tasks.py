#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from vector import Vector


def task_1():
    """
    Lesson 2.4
    """

    print(f"\n{'Task 1':^79s}")
    print(Vector((8.218, -9.341)) + Vector((-1.129, 2.111)))
    print(Vector((7.119, 8.215)) - Vector((-8.223, 0.878)))
    print(7.41 * Vector((1.671, -1.012, -0.318)))


def task_2():
    """
    Lesson2.6
    """

    print(f"\n{'Task 2':^79s}")
    print(Vector((-0.221, 7.437)).magnitude)
    print(Vector((8.813, -1.331, -6.247)).magnitude)
    print(Vector((5.581, -2.136)).get_normal())
    print(Vector((1.996, 3.108, -4.554)).get_normal())


if __name__ == '__main__':
    task_1()
    task_2()