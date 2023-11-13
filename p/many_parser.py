from collections.abc import Sequence
from p.parser import IParser
from p.parser_exception import ParserException

class ManyParser[E, O](IParser[E, list[O]]):
    _p: IParser[E, O]

    def __init__(self, p: IParser[E, O]) -> None:
        self._p = p

    def expect(self) -> list[str]:
        return self._p.expect()

    def parse(self, s: Sequence[E]) -> tuple[list[O], Sequence[E]]:
        try:
            (v, stream) = self._p.parse(s)
        except ParserException:
            return ([], s)
        else:
            (v1, stream2) = self.parse(stream)
            return ([v] + v1, stream2)


def many[E, O](p: IParser[E, O])-> IParser[E, list[O]]:
    return ManyParser[E, O](p)
