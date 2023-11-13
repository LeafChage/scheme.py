from typing import Callable
from collections.abc import Sequence
from abc import ABC, abstractmethod

type Self[I, O] = IParser[I, O]

class IParser[Item, Output](ABC):
    @abstractmethod
    def parse(self, stream: Sequence[Item]) -> tuple[Output, Sequence[Item]]:
        pass

    @abstractmethod
    def expect(self) -> list[str]:
        pass

    def and_[Output2](self, p: Self[Item, Output2]) -> Self[Item, tuple[Output, Output2]]:
        from p.and_parser import AndParser
        return AndParser(self, p)

    def or_(self, p: Self[Item, Output]) -> Self[Item, Output]:
        from p.or_parser import OrParser
        return OrParser(self, p)

    def with_[Output2](self, p: Self[Item, Output2]) -> Self[Item, Output2]:
        from p.with_parser import WithParser
        return WithParser(self, p)

    def skip[Output2](self, p: Self[Item, Output2]) -> Self[Item, Output]:
        from p.skip_parser import SkipParser
        return SkipParser(self, p)

    def map[Output2](self, fn: Callable[[Output], Output2]) -> Self[Item, Output2]:
        from p.map_parser import MapParser
        return MapParser(self, fn)

    def debug(self) -> Self[Item, Output]:
        def debug(v: Output) -> Output:
            print(v)
            return v
        return self.map(debug)

