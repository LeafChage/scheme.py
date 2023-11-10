from p.parser import IParser
from p.parser_exception import ParserException
from util.string import String

class TakeParser(IParser[str]):
    length: int

    def __init__(self, n: int) -> None:
        self.length = n

    def parse(self, stream: str) -> tuple[str, str]:
        if len(stream) >= self.length:
            return String.split(stream, self.length)
        else:
            raise ParserException()



