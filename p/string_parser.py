from p.parser import IParser
from p.parser_exception import ParserException

class StringParser(IParser[str, str]):
    _target: str

    def __init__(self, t: str) -> None:
        self._target = t

    def expect(self) -> list[str]:
        return [self._target]

    def parse(self, stream: str) -> tuple[str, str]:
        take = stream[:len(self._target)]
        if take == self._target:
            return (self._target, stream[len(self._target):])
        else:
            raise ParserException(expect=self.expect(), actual=take)


def string(v: str):
    return StringParser(v)
