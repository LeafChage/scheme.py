from collections.abc import Callable ,Sequence
from p.parser import IParser

class LazyParser[E, O](IParser[E, O]):
    _fn: Callable[[], IParser[E, O]]

    def expect(self) -> list[str]:
        return []

    def __init__(self, fn: Callable[[], IParser[E, O]]) -> None:
        self._fn = fn

    def parse(self, stream: Sequence[E]) -> tuple[O, Sequence[E]]:
        return self._fn().parse(stream)

def lazy[E, O](fn: Callable[[], IParser[E, O]])-> IParser[E, O]:
    return LazyParser(fn)
