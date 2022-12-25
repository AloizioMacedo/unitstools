from abc import ABC, abstractmethod
from typing import Callable, Iterable, Self, Type, TypeVar, overload


class Unit(ABC):
    """Inherit from this class to create units."""

    @abstractmethod
    def __add__(self, other: Self) -> Self:
        ...

    @abstractmethod
    def __mul__(self, k: int | float) -> Self:
        ...

    @abstractmethod
    def __rmul__(self, k: int | float) -> Self:
        ...

    @abstractmethod
    def __sub__(self, other: Self) -> Self:
        ...

    @abstractmethod
    def __truediv__(self, k: int) -> Self:
        ...

    @abstractmethod
    def __lt__(self, other: Self) -> bool:
        ...

    @abstractmethod
    def __le__(self, other: Self) -> bool:
        ...

    @abstractmethod
    def __ge__(self, other: Self) -> bool:
        ...

    @abstractmethod
    def __gt__(self, other: Self) -> bool:
        ...


class IntUnit(ABC):
    """Inherit from this class to create units that take integer values."""

    @abstractmethod
    def __add__(self, other: Self) -> Self:
        ...

    @abstractmethod
    def __mul__(self, k: int) -> Self:
        ...

    @abstractmethod
    def __rmul__(self, k: int) -> Self:
        ...

    @abstractmethod
    def __sub__(self, other: Self) -> Self:
        ...

    @abstractmethod
    def __floordiv__(self, k: int) -> Self:
        ...

    @abstractmethod
    def __lt__(self, other: Self) -> bool:
        ...

    @abstractmethod
    def __le__(self, other: Self) -> bool:
        ...

    @abstractmethod
    def __ge__(self, other: Self) -> bool:
        ...

    @abstractmethod
    def __gt__(self, other: Self) -> bool:
        ...


_T1 = TypeVar("_T1", bound=IntUnit | Unit)
_T2 = TypeVar("_T2", bound=IntUnit | Unit)

_U = TypeVar("_U", bound=Unit)
_IU = TypeVar("_IU", bound=IntUnit)


def create_conversion(
    type1: Type[_T1], type2: Type[_T2], rate: int | float
) -> Callable[[_T1], _T2]:
    """Creates a conversion function for the given types.

    :param type1: Given class inherited from Unit or IUnit to convert from.
    :type type1: Type[Unit] | Type[IntUnit]
    :param type2: Given class inherited from Unit or IUnit to convert to.
    :type type2: Type[Unit] | Type[IntUnit]
    :param rate: Multiplier factor for the conversion, i.e. type1 = 60*type2
    :type rate: int, float
    :return: Function converting one unit to another.
    :rtype: Callable[T1, T2]"""

    def conversion(x: _T1) -> _T2:
        return x * rate  # type: ignore

    return conversion


@overload
def strip_unit(x: IntUnit) -> int:
    ...


@overload
def strip_unit(x: Unit) -> int | float:
    ...


def strip_unit(x):
    """Strips the unit of the given Unit or IUnit.

    :param x: Specified value.
    :type x: Unit | IntUnit
    :return: Float or int representing the value.
    :rtype: int | float"""
    return x  # type: ignore


@overload
def embed_unit(x: int, unit: Type[_IU]) -> _IU:
    ...


@overload
def embed_unit(x: float, unit: Type[_U]) -> _U:
    ...


def embed_unit(x, unit):
    """Sets the given value to a specified unit.

    :param x: Specified value.
    :type x: int | float
    :param unit: Given class inherited from Unit or IUnit.
    :type unit: Type[Unit] | Type[IntUnit]
    :return: Unit-imbued value.
    :rtype: Unit | IntUnit"""
    return x  # type: ignore


def sum_iter(values: Iterable[_T1]) -> _T1:
    """Calculates sum of unit values in an iterable.

    :param values: Values which bear an unit.
    :type values: list
    :return: Sum of the values.
    :rtype: Type[Unit] | Type[IntUnit]"""
    return sum(values)  # type: ignore
