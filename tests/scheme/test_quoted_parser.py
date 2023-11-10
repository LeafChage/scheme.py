from scheme.lisp_value import LAtom, LList, LString
from scheme.parser import quoted

class TestQuotedParser:
    p = quoted()

    def test_ok(self):
        (value, stream) = self.p.parse("'\"hi\" ")
        assert value == LList([LAtom("quote"), LString("hi")])
        assert stream == " "
