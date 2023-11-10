from typing import Callable
from p.parser import IParser

class MapParser[T1, T2](IParser[T2]):
    p: IParser[T1]
    fn: Callable[[T1], T2]

    def __init__(self, p: IParser[T1], fn: Callable[[T1], T2]) -> None:
        self.p = p
        self.fn = fn

    def parse(self, stream: str) -> tuple[T2, str]:
        (v1, s) = self.p.parse(stream)
        return (self.fn(v1), s)

