from collections.abc import Sequence
from p.parser import IParser
from p.parser_exception import ParserException

class AttemptParser[E, O](IParser[E, O | None]):
    _p: IParser[E, O]

    def __init__(self, p: IParser[E, O]) -> None:
        self._p = p

    def expect(self) -> list[str]:
        return self._p.expect()

    def parse(self, stream: Sequence[E]) -> tuple[O | None, Sequence[E]]:
        try:
            return self._p.parse(stream)
        except ParserException:
            return (None, stream)

def attempt[E, O](p: IParser[E, O])->IParser[E, O | None]:
    return AttemptParser(p)
