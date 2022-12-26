from abc import ABC
from typing import Callable, Iterable, Type, TypeVar, Union, overload

TUnit = TypeVar("TUnit", bound="Unit")
TIntUnit = TypeVar("TIntUnit", bound="IntUnit")


class Unit(ABC):
    """Inherit from this class to create units."""

    def __new__(cls: Type[TUnit], x: Union[int, float]) -> TUnit:
        return x  # type: ignore

    def __add__(self: TUnit, other: TUnit) -> TUnit:
        ...

    def __mul__(self: TUnit, k: Union[int, float]) -> TUnit:
        ...

    def __rmul__(self: TUnit, k: Union[int, float]) -> TUnit:
        ...

    def __sub__(self: TUnit, other: TUnit) -> TUnit:
        ...

    def __truediv__(self: TUnit, k: int) -> TUnit:
        ...

    def __lt__(self: TUnit, other: TUnit) -> bool:
        ...

    def __le__(self: TUnit, other: TUnit) -> bool:
        ...

    def __ge__(self: TUnit, other: TUnit) -> bool:
        ...

    def __gt__(self: TUnit, other: TUnit) -> bool:
        ...

    def __int__(self) -> int:
        ...

    def __float__(self) -> float:
        ...


class IntUnit(ABC):
    """Inherit from this class to create units that take integer values."""

    def __new__(cls: Type[TIntUnit], x: int) -> TIntUnit:
        return x  # type: ignore

    def __add__(self: TIntUnit, other: TIntUnit) -> TIntUnit:
        ...

    def __mul__(self: TIntUnit, k: int) -> TIntUnit:
        ...

    def __rmul__(self: TIntUnit, k: int) -> TIntUnit:
        ...

    def __sub__(self: TIntUnit, other: TIntUnit) -> TIntUnit:
        ...

    def __floordiv__(self: TIntUnit, k: int) -> TIntUnit:
        ...

    def __lt__(self: TIntUnit, other: TIntUnit) -> bool:
        ...

    def __le__(self: TIntUnit, other: TIntUnit) -> bool:
        ...

    def __ge__(self: TIntUnit, other: TIntUnit) -> bool:
        ...

    def __gt__(self: TIntUnit, other: TIntUnit) -> bool:
        ...

    def __int__(self) -> int:
        ...

    def __float__(self) -> float:
        ...


_T1 = TypeVar("_T1", bound=Union[IntUnit, Unit])
_T2 = TypeVar("_T2", bound=Union[IntUnit, Unit])

_U = TypeVar("_U", bound=Unit)
_IU = TypeVar("_IU", bound=IntUnit)


def create_conversion(
    type1: Type[_T1], type2: Type[_T2], rate: Union[int, float]
) -> Callable[[_T1], _T2]:
    """Creates a conversion function for the given types.

    Parameters
    ----------
    type1 : Type[_T1]
        Given class inherited from Unit or IUnit to convert from.
    type2 : Type[_T2]
        Given class inherited from Unit or IUnit to convert to.
    rate : int | float
        Multiplier factor for the conversion, i.e. type1 = 60*type2

    Returns
    -------
    Callable[[_T1], _T2]
        Function converting one unit to another.
    """

    def conversion(x: _T1) -> _T2:
        return x * rate  # type: ignore

    return conversion


@overload
def strip_unit(x: IntUnit) -> int:
    ...


@overload
def strip_unit(x: Unit) -> Union[int, float]:
    ...


def strip_unit(x):
    """Strips the unit of the given Unit or IntUnit.

    Parameters
    ----------
    x : Specified value.
        Unit | IntUnit

    Returns
    -------
    int | float
        Float or int representing the value.
    """
    return x  # type: ignore


@overload
def embed_unit(x: int, unit: Type[_IU]) -> _IU:
    ...


@overload
def embed_unit(x: float, unit: Type[_U]) -> _U:
    ...


def embed_unit(x, unit):
    """Sets the given value to a specified unit.

    Parameters
    ----------
    x : int | float
        Specified value.
    unit : Type[Unit] | Type[IntUnit]
        Given class inherited from Unit or IntUnit.

    Returns
    -------
    Unit | IntUnit
        Unit-imbued value.
    """
    return x  # type: ignore


def sum_iter(values: Iterable[_T1]) -> _T1:
    """Calculates sum of unit values in an iterable.

    Parameters
    ----------
    values : list
        Values which bear an unit.

    Returns
    -------
    Type[Unit] | Type[IntUnit]
        Sum of the values.
    """
    return sum(values)  # type: ignore
