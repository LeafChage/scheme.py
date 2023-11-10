from p.parser import IParser
from p.parser_exception import ParserException

class ChoiceParser[T](IParser[T]):
    elements: tuple[IParser[T], ...]

    def __init__(self, *elements: IParser[T]) -> None:
        self.elements = elements

    def parse(self, stream: str) -> tuple[T, str]:
        for e in self.elements:
            try:
                return e.parse(stream)
            except ParserException:
                continue

        raise ParserException()

