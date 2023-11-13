from collections.abc import Sequence
from p.parser import IParser

class WithParser[E, T1, T2](IParser[E, T2]):
    _p1: IParser[E, T1]
    _p2: IParser[E, T2]

    def __init__(self, p1: IParser[E, T1], p2: IParser[E, T2]) -> None:
        self._p1 = p1
        self._p2 = p2

    def expect(self) -> list[str]:
        return self._p1.expect() + self._p2.expect()

    def parse(self, stream: Sequence[E]) -> tuple[T2, Sequence[E]]:
        (_, stream1) = self._p1.parse(stream)
        (v2, stream2) = self._p2.parse(stream1)
        return (v2, stream2)

