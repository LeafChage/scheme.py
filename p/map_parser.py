from collections.abc import Sequence
from typing import Callable
from p.parser import IParser

class MapParser[E, O, O2](IParser[E, O2]):
    _p: IParser[E, O]
    _fn: Callable[[O], O2]

    def __init__(self, p: IParser[E, O], fn: Callable[[O], O2]) -> None:
        self._p = p
        self._fn = fn

    def expect(self) -> list[str]:
        return self._p.expect()

    def parse(self, stream: Sequence[E]) -> tuple[O2, Sequence[E]]:
        (v1, s) = self._p.parse(stream)
        return (self._fn(v1), s)


