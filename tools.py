#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from typing import Iterable

from decimal import Decimal


def is_zero(val: int) -> bool:
    return abs(val) < 1e-10


def to_decimal(val) -> Decimal:
    res = Decimal(val)
    if is_zero(res):
        res = Decimal('0')
    return res


def first_nonzero_index(iterable: Iterable) -> int:
    for k, item in enumerate(iterable):
        if not is_zero(item):
            return k
