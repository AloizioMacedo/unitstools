from abc import ABC, abstractmethod
from typing import Callable, Self, Type, TypeVar, overload


class Unit(ABC):
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
    def conversion(x: _T1) -> _T2:
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


@overload
def embed_unit(x: int, unit: Type[_IU]) -> _IU:
    ...


@overload
def embed_unit(x: float, unit: Type[_U]) -> _U:
    ...


def embed_unit(x, unit):
    return x  # type: ignore
