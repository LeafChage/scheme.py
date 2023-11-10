from p.parser import IParser
from p.parser_exception import ParserException

class ManyParser[T](IParser[list[T]]):
    p: IParser[T]

    def __init__(self, p: IParser[T]) -> None:
        self.p = p

    def parse(self, s: str) -> tuple[list[T], str]:
        result = []
        next_stream = s
        while(True):
            try:
                (v, stream) = self.p.parse(next_stream)
                result.append(v)
                next_stream = stream
                if next_stream == "": return (result, "")
            except ParserException:
                return (result, next_stream)

