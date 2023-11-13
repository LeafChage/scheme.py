from collections.abc import Sequence
from p.parser import IParser
from p.parser_exception import ParserException

class TakeParser[E](IParser[E, Sequence[E]]):
    _length: int

    def __init__(self, n: int) -> None:
        self._length = n

    def expect(self) -> list[str]:
        return ['*'*self._length]

    def parse(self, stream: str) -> tuple[str, str]:
        if len(stream) >= self._length:
            return (stream[:self._length], stream[self._length:])
        else:
            raise ParserException(
                expect=self.expect(),
                actual=stream[:self._length]
            )


def take[E](n: int):
    return TakeParser[E](n)
