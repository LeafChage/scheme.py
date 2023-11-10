from dataclasses import dataclass

type LispVal = LAtom | LList | LDottedList | LNumber | LString | LBoolean

@dataclass()
class LAtom:
    value: str

@dataclass()
class LList:
    value: list[LispVal]

@dataclass()
class LDottedList:
    value: tuple[list[LispVal], LispVal]

@dataclass()
class LNumber:
    value: int

@dataclass()
class LString:
    value: str

@dataclass()
class LBoolean:
    value: bool
