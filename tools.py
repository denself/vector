#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from typing import Iterable


def is_zero(val: int) -> bool:
    return abs(val) < 1e-10


def first_nonzero_index(iterable: Iterable) -> int:
    for k, item in enumerate(iterable):
        if not is_zero(item):
            return k
