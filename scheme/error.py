from abc import ABC, abstractmethod
from scheme.lisp_value import LispVal
from p import ParserException

class Showable(ABC):
    @abstractmethod
    def show(self) -> str:
        pass

class LispError(Exception, Showable):
    pass

class TypeMismatch(LispError):
    expected: str
    actual: list[LispVal]

    def __init__(self, expected: str, actual: list[LispVal]) -> None:
        self.expected = expected
        self.actual = actual
        super().__init__(self.show())

    def show(self) -> str:
        return "Invalid type: expected {}, found {}".format(
            self.expected,
            " ".join(map(lambda a: a.show(), self.actual))
        )

class LispParserError(LispError):
    e: ParserException

    def __init__(self, e: ParserException) -> None:
        self.e = e
        super().__init__(self.show())

    def show(self) -> str:
        return "parser error at: {}".format(self.e)

class NotFunction(LispError):
    fn: str

    def __init__(self, fn: str) -> None:
        self.fn  = fn
        super().__init__(self.show())

    def show(self) -> str:
        return "this is not a function: {}".format(self.fn)

class NumArgs(LispError):
    expected: int
    actual: list[LispVal]

    def __init__(self, expected: int, actual: list[LispVal]) -> None:
        self.expected = expected
        self.actual = actual
        super().__init__(self.show())

    def show(self) -> str:
        return "Expected {} args; found values {}".format(
            self.expected,
            " ".join(map(lambda a: a.show(), self.actual))
        )


# showError :: LispError -> String
# showError (UnboundVar message varname)  = message ++ ": " ++ varname
# showError (BadSpecialForm message form) = message ++ ": " ++ show form
