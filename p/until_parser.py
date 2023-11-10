from p.parser import IParser
from p.parser_exception import ParserException

class UntilParser[T](IParser[str]):
    p: IParser[T]

    def __init__(self, p: IParser[T]) -> None:
        self.p = p

    def parse(self, stream: str) -> tuple[str, str]:
        for i in range(0, len(stream)):
            try:
                _ = self.p.parse(stream[i:])
                return (stream[:i], stream[i:])
            except ParserException:
                pass

        raise ParserException()


