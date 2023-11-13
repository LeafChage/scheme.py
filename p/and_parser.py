from collections.abc import Sequence
from p.parser import IParser

class AndParser[E, O, O2](IParser[E, tuple[O, O2]]):
    _p1: IParser[E, O]
    _p2: IParser[E, O2]

    def __init__(
            self,
            p1: IParser[E, O],
            p2: IParser[E, O2]
        ) -> None:

        self._p1 = p1
        self._p2 = p2

    def expect(self) -> list[str]:
        return self._p1.expect() + self._p2.expect()

    def parse(self, stream: Sequence[E]) -> tuple[tuple[O, O2], Sequence[E]]:
        (v1, stream1) = self._p1.parse(stream)
        (v2, stream2) = self._p2.parse(stream1)
        return ((v1, v2), stream2)

