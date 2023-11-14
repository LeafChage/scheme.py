from dataclasses import dataclass
from abc import ABC, abstractmethod

class Showable(ABC):
    @abstractmethod
    def show(self) -> str:
        pass

@dataclass()
class LispVal(Showable):
    pass

@dataclass()
class LAtom(LispVal):
    value: str

    def show(self) -> str:
        return self.value

@dataclass()
class LNumber(LispVal):
    value: int

    def show(self) -> str:
        return "{}".format(self.value)

@dataclass()
class LString(LispVal):
    value: str

    def show(self) -> str:
        return "\"{}\"".format(self.value)

@dataclass()
class LBoolean(LispVal):
    value: bool

    def show(self) -> str:
        if self.value:
            return "#t"
        else:
            return "#f"

@dataclass()
class LList(LispVal):
    value: list[LispVal]

    def show(self) -> str:
        return "({})".format(" ".join(map(lambda a: a.show(), self.value)))

@dataclass()
class LDottedList(LispVal):
    value: tuple[list[LispVal], LispVal]

    def show(self) -> str:
        return "({} . {})".format(
            " ".join(map(lambda a: a.show(), self.value[0])),
            self.value[1].show,
        )

