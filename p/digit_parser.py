from p.parser import IParser
from p.parser_exception import ParserException

_digit = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ]

class DigitParser(IParser[str,str]):
    def __init__(self) -> None:
        pass

    def expect(self) -> list[str]:
        return _digit

    def parse(self, stream: str) -> tuple[str, str]:
        try:
            d = stream[0]
        except IndexError:
            raise ParserException(self.expect(), "EOF")
        else:
            if d in _digit:
                return (d, stream[1:])
            else:
                raise ParserException(self.expect(), d)


def digit():
    return DigitParser()
