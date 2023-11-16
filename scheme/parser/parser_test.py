from scheme.lisp_value import LString
from scheme.parser.parser import parser

class TestParser:
    def test_ok(self):
        assert parser("\"hi\"") == LString("hi")
