from typing import cast

from unitstools import IntUnit, Unit, create_conversion


class Sec(Unit):
    ...


class Min(Unit):
    ...


class IntMin(IntUnit):
    ...


class IntSec(IntUnit):
    ...


def test_conversion():
    convert = create_conversion(Min, Sec, 60)
    x = Min(1)
    assert convert(x) == 60


def test_int_conversion():
    convert = create_conversion(IntMin, IntSec, 60)
    x = IntMin(1)
    assert convert(x) // 3 == 20
