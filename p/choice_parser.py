from collections.abc import Sequence
from functools import reduce
from p.parser import IParser
from p.parser_exception import ParserException

class ChoiceParser[E, O](IParser[E, O]):
    _elements: tuple[IParser[E, O], ...]

    def __init__(self, *elements: IParser[E, O]) -> None:
        self._elements = elements

    def expect(self) -> list[str]:
        result = [];
        for e in self._elements:
            result += e.expect()

        return result

    def parse(self, stream: Sequence[E]) -> tuple[O, Sequence[E]]:
        errors: list[ParserException] = []
        for e in self._elements:
            try:
                return e.parse(stream)
            except ParserException as e:
                errors.append(e)

        def _inner(e1: ParserException, e2: ParserException) -> ParserException:
            return ParserException.concat(e1,e2)

        raise reduce(_inner, errors)


def choice[E, O](*elements: IParser[E, O]) -> IParser[E, O]:
    return ChoiceParser(*elements)
