from typing import Callable
from abc import ABC, abstractmethod

type Self[T] = IParser[T]

class IParser[T](ABC):
    @abstractmethod
    def parse(self, stream: str) -> tuple[T, str]:
        pass

    def and_[U](self, p: Self[U]) -> Self[tuple[T, U]]:
        from p.and_parser import AndParser
        return AndParser(self, p)

    def or_(self, p: Self[T]) -> Self[T]:
        from p.or_parser import OrParser
        return OrParser(self, p)

    def map[U](self, fn: Callable[[T], U]) -> Self[U]:
        from p.map_parser import MapParser
        return MapParser(self, fn)

    def debug(self) -> Self[T]:
        def debug(v: T) -> T:
            print(v)
            return v
        return self.map(debug)

