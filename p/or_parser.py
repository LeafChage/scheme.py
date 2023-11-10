from p.parser import IParser
from p.parser_exception import ParserException

class OrParser[T](IParser[T]):
    p1: IParser[T]
    p2: IParser[T]

    def __init__(self, p1: IParser[T], p2: IParser[T]) -> None:
        self.p1 = p1
        self.p2 = p2

    def parse(self, stream: str) -> tuple[T, str]:
        try:
            return self.p1.parse(stream)
        except ParserException as e:
            try:
                return self.p2.parse(stream)
            except ParserException as e:
                raise e



