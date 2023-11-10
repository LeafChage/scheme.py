from scheme.lisp_value import LNumber
from scheme.parser import number

class TestNumberParser:
    p = number()

    def test_ok(self):
        (value, stream) = self.p.parse("123")
        assert value == LNumber(123)
        assert stream == ""
