from collections.abc import Sequence
from typing import Any
from p.parser import IParser
from p.parser_exception import ParserException

class UntilParser[E](IParser[E, Sequence[E]]):
    p: IParser[E, Any]

    def __init__(self, p: IParser[E, Any]) -> None:
        self.p = p

    def expect(self) -> list[str]:
        return self.p.expect()

    def parse(self, stream: Sequence[E]) -> tuple[Sequence[E], Sequence[E]]:
        for i in range(0, len(stream)):
            try:
                _ = self.p.parse(stream[i:])
                return (stream[:i], stream[i:])
            except ParserException:
                pass

        raise ParserException(expect=self.expect(), actual="EOF")


def until[E](p: IParser[E, Any])->IParser[E, Sequence[E]]:
    return UntilParser(p)
