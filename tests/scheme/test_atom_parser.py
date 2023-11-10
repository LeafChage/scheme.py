from scheme.lisp_value import LAtom, LBoolean
from scheme.parser import atom

class TestAtomParser:
    p = atom()

    def test_atom(self):
        (value, stream) = self.p.parse("hi ")
        assert value == LAtom("hi")
        assert stream == " "

    def test_true(self):
        (value, stream) = self.p.parse("#t ")
        assert value == LBoolean(True)
        assert stream == " "

    def test_false(self):
        (value, stream) = self.p.parse("#f ")
        assert value == LBoolean(False)
        assert stream == " "

