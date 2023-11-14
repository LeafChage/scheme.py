from collections.abc import Sequence
from p.parser import IParser
from p.parser_exception import ParserException

class TokenParser[E](IParser[E, E]):
    _target: E

    def __init__(self, t: E) -> None:
        self._target = t

    def expect(self) -> list[str]:
        return [str(self._target)]

    def parse(self, stream: Sequence[E]) -> tuple[E, Sequence[E]]:
        if len(stream) <= 0:
            raise ParserException(expect=self.expect(), actual="EOF")
        else:
            v = stream[0]
            if v == self._target:
                return (self._target, stream[1:])
            else:
                raise ParserException(expect=self.expect(), actual=str(v))


def token[E](t: E) -> IParser[E, E]:
    return TokenParser(t)
