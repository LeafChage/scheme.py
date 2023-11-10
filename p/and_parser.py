from p.parser import IParser
from p.parser_exception import ParserException

class AndParser[T1, T2](IParser[tuple[T1, T2]]):
    p1: IParser[T1]
    p2: IParser[T2]

    def __init__(self, p1: IParser[T1], p2: IParser[T2]) -> None:
        self.p1 = p1
        self.p2 = p2

    def parse(self, stream: str) -> tuple[tuple[T1, T2], str]:
        try:
            (v1, stream1) = self.p1.parse(stream)
            (v2, stream2) = self.p2.parse(stream1)
            return ((v1, v2), stream2)
        except ParserException as e:
            raise e

