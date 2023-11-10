from p.parser import IParser
from p.parser_exception import ParserException
from util.string import String

class OneOfParser(IParser[str]):
    target: list[str]

    def __init__(self, targets: str) -> None:
        self.target = []
        for target in targets[:]:
            self.target.append(target)

    def parse(self, stream: str) -> tuple[str, str]:
        (d, s)  = String.split(stream, 1)
        if d in self.target:
            return (d, s)
        else:
            raise ParserException()



