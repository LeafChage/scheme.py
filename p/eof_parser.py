from collections.abc import Sequence
from p.parser import IParser
from p.parser_exception import ParserException

class EofParser[E](IParser[None, Sequence[E]]):
    def __init__(self) -> None:
        pass

    def expect(self) -> list[str]:
        return ["EOF"]

    def parse(self, stream: Sequence[E]) -> tuple[None, Sequence[E]]:
        if len(stream) == 0:
            return (None, stream)
        else:
            raise ParserException(expect=self.expect(), actual="{}".format(stream[0]))



def eof():
    return EofParser()
