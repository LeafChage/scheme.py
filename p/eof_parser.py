from p.parser import IParser
from p.parser_exception import ParserException

class EofParser(IParser[None]):
    def __init__(self) -> None:
        pass

    def parse(self, stream: str) -> tuple[None, str]:
        if stream == "":
            return (None, stream)
        else:
            raise ParserException(expect="EOF", actual=stream[0])



