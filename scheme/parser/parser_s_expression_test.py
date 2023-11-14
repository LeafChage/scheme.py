from scheme.lisp_value import LList, LNumber
from scheme.parser.parser import s_expression

class TestSExpressionParser:
    p = s_expression()

    def test_ok_list(self):
        (value, stream) = self.p.parse("(1 2 3)")
        assert value == LList([LNumber(1), LNumber(2), LNumber(3)])
        assert stream == ""
