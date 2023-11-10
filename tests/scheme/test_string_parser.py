from scheme.lisp_value import LString
from scheme.parser import string

class TestStringParser:
    p = string()

    def test_ok(self):
        (value, stream) = self.p.parse("\"hi\" ")
        assert value == LString("hi")
        assert stream == " "
