from scheme.lisp_value import LString
from scheme.parser.parser import parser

class TestParser:
    p = parser()

    def test_ok(self):
        (value, stream) = self.p.parse("\"hi\"")
        assert value == LString("hi")
        assert stream == ""
