type Self = ParserException

class ParserException(Exception):
    _expect: list[str]
    _actual: str

    @staticmethod
    def concat(e1: Self, e2:Self) -> Self:
        expects = e1.expect + e2.expect
        return ParserException(
            expects,
            "|".join([e1.actual, e2.actual]),
        )

    @property
    def expect(self)->list[str]:
        return self._expect

    @property
    def actual(self)->str:
        return self._actual

    def __init__(self, expect: list[str], actual: str) -> None:
        self._expect = expect
        self._actual = actual
        super().__init__(self.msg())


    def msg(self)->str:
        return "expect: {}, actual: {}".format("|".join(self.expect), self.actual)
