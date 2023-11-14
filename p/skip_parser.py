from collections.abc import Sequence
from p.parser import IParser

class SkipParser[E, O1, O2](IParser[E, O1]):
    _p1: IParser[E, O1]
    _p2: IParser[E, O2]

    def __init__(self, p1: IParser[E, O1], p2: IParser[E, O2]) -> None:
        self._p1 = p1
        self._p2 = p2

    def expect(self) -> list[str]:
        return self._p1.expect() + self._p2.expect()

    def parse(self, stream: Sequence[E]) -> tuple[O1, Sequence[E]]:
        (v1, stream1) = self._p1.parse(stream)
        (_, stream2) = self._p2.parse(stream1)
        return (v1, stream2)

