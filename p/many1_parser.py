from p.many_parser import ManyParser
from p.parser import IParser
from p.parser_exception import ParserException

class Many1Parser[T](IParser[list[T]]):
    many: IParser[list[T]]

    def __init__(self, p: IParser[T]) -> None:
        self.many = ManyParser(p)

    def parse(self, s: str) -> tuple[list[T], str]:
        (result, stream) = self.many.parse(s)
        if len(result) <= 0:
            raise ParserException()
        else:
            return (result, stream)
