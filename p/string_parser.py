from p.parser import IParser
from p.parser_exception import ParserException

class StringParser(IParser[str]):
    _target: str

    def __init__(self, t: str) -> None:
        self._target = t

    def parse(self, stream: str) -> tuple[str, str]:
        take = stream[:len(self._target)]
        if take == self._target:
            return (self._target, stream[len(self._target):])
        else:
            raise ParserException(expect=self._target, actual=take)



