from typing import cast

from units import Unit, create_conversion


class Sec(Unit):
    ...


class Min(Unit):
    ...


def test_conversion():
    convert = create_conversion(Min, Sec, 60)
    x = cast(Min, 1)
    assert convert(x) == 60
