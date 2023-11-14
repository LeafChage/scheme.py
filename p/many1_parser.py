from collections.abc import Sequence
from p.many_parser import ManyParser
from p.parser import IParser
from p.parser_exception import ParserException

class Many1Parser[E, O](IParser[E, list[O]]):
    _many: IParser[E, list[O]]

    def __init__(self, p: IParser[E, O]) -> None:
        self._many = ManyParser(p)

    def expect(self) -> list[str]:
        return self._many.expect()

    def parse(self, s: Sequence[E]) -> tuple[list[O], Sequence[E]]:
        (result, stream) = self._many.parse(s)
        if len(result) <= 0:
            raise ParserException(self._many.expect(), "")
        else:
            return (result, stream)

def many1[E, O](p: IParser[E, O])-> IParser[E, list[O]]:
    return Many1Parser[E, O](p)
