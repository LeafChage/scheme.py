from p.parser import IParser
from p.parser_exception import ParserException
from util.string import String

class StringParser(IParser[str]):
    _target: str

    def __init__(self, t: str) -> None:
        self._target = t

    def parse(self, stream: str) -> tuple[str, str]:
        if len(stream) >= len(self._target):
            take = stream[:len(self._target)]
            if take == self._target:
                return String.split(stream, len(self._target))
            else:
                raise ParserException()
        else:
            raise ParserException()



