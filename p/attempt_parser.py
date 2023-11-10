from p.parser import IParser
from p.parser_exception import ParserException

class AttemptParser[T](IParser[T | None]):
    p: IParser[T | None]
    def __init__(self, p: IParser[T | None]) -> None:
        self.p = p

    def parse(self, stream: str) -> tuple[T | None, str]:
        try:
            return self.p.parse(stream)
        except ParserException:
            return (None, stream)
