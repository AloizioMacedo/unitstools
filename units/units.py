from abc import ABC, abstractmethod
from typing import Callable, Self, Type, TypeVar, overload

T = TypeVar("T")
U = TypeVar("U")


class Unit(ABC):
    @abstractmethod
    def __add__(self, other: Self) -> Self:
        ...

    @abstractmethod
    def __mul__(self, k: int | float) -> Self:
        ...

    @abstractmethod
    def __sub__(self, other: Self) -> Self:
        ...

    @abstractmethod
    def __truediv__(self, k: int) -> Self:
        ...


class IntUnit(ABC):
    @abstractmethod
    def __add__(self, other: Self) -> Self:
        ...

    @abstractmethod
    def __mul__(self, k: int) -> Self:
        ...

    @abstractmethod
    def __sub__(self, other: Self) -> Self:
        ...

    @abstractmethod
    def __floordiv__(self, k: int) -> Self:
        ...


def create_conversion(
    type1: Type[T], type2: Type[U], rate: int | float
) -> Callable[[T], U]:
    def conversion(x: T) -> U:
        return x * rate  # type: ignore

    return conversion


@overload
def strip_units(x: IntUnit) -> int:
    ...


@overload
def strip_units(x: Unit) -> int | float:
    ...


def strip_units(x):
    return x  # type: ignore
