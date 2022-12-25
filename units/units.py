from abc import ABC, abstractmethod
from typing import Callable, Self, Type, TypeVar, cast

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


def create_conversion(
    type1: Type[T], type2: Type[U], rate: float
) -> Callable[[T], U]:
    def conversion(x: T) -> U:
        return x * rate  # type: ignore

    return conversion
