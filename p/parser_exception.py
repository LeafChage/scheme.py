class ParserException(Exception):
    expect: str
    actual: str

    def __init__(self, expect: str, actual: str) -> None:
        self.expect = expect
        self.actual = actual
        super().__init__(self.msg())

    def msg(self)->str:
        return "expect: {}, actual: {}".format(self.expect, self.actual)
