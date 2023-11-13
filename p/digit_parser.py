from p.parser import IParser
from p.parser_exception import ParserException

_digit = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ]

class DigitParser(IParser[str]):
    def __init__(self) -> None:
        pass

    def parse(self, stream: str) -> tuple[str, str]:
        try:
            d = stream[0]
        except IndexError:
            raise ParserException("digit", "EOF")
        else:
            if d in _digit:
                return (d, stream[1:])
            else:
                raise ParserException("digit", d)



