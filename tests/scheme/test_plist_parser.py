from scheme.lisp_value import LList, LNumber
from scheme.parser import plist

class TestListParser:
    p = plist()

    def test_ok(self):
        (value, stream) = self.p.parse("1 2 3")
        assert value == LList([LNumber(1), LNumber(2), LNumber(3)])
        assert stream == ""
