from p.parser import IParser
from p.parser_exception import ParserException

class AnyParser(IParser[str]):
    def __init__(self) -> None:
        pass

    def parse(self, stream: str) -> tuple[str, str]:
        if len(stream) > 0:
            return (stream[0], stream[1:])
        else:
            raise ParserException()


