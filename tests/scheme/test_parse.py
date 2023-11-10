from scheme.lisp_value import LString
from scheme.parser import parse

class TestParser:
    p = parse()

    def test_ok(self):
        (value, stream) = self.p.parse("\"hi\"")
        assert value == LString("hi")
        assert stream == ""
