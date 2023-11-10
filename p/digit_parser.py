from p.parser import IParser
from p.parser_exception import ParserException
from util.string import String

digit = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ]

class DigitParser(IParser[str]):
    def __init__(self) -> None:
        pass

    def parse(self, stream: str) -> tuple[str, str]:
        (d, s)  = String.split(stream, 1)
        if d in digit:
            return (d, s)
        else:
            raise ParserException()



