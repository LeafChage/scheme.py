from p.parser import IParser

class SkipParser(IParser[None]):
    p: IParser

    def __init__(self, p: IParser) -> None:
        self.p = p

    def parse(self, s: str) -> tuple[None, str]:
        (_, stream) = self.p.parse(s)
        return (None, stream)

