from dataclasses import dataclass
from abc import ABC, abstractmethod

type LispVal = LAtom | LList | LDottedList | LNumber | LString | LBoolean

class Showable(ABC):
    @abstractmethod
    def show(self) -> str: pass

@dataclass()
class LAtom(Showable):
    value: str

    def show(self) -> str:
        return self.value

@dataclass()
class LNumber(Showable):
    value: int

    def show(self) -> str:
        return "{}".format(self.value)

@dataclass()
class LString(Showable):
    value: str

    def show(self) -> str:
        return "\"{}\"".format(self.value)

@dataclass()
class LBoolean(Showable):
    value: bool

    def show(self) -> str:
        if self.value:
            return "#t"
        else:
            return "#f"

@dataclass()
class LList(Showable):
    value: list[LispVal]

    def show(self) -> str:
        return "({})".format(" ".join(map(lambda a: a.show(), self.value)))

@dataclass()
class LDottedList(Showable):
    value: tuple[list[LispVal], LispVal]

    def show(self) -> str:
        return "({} . {})".format(
            " ".join(map(lambda a: a.show(), self.value[0])),
            self.value[1].show,
        )

