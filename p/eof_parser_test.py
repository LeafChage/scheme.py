import pytest
from p.eof_parser import EofParser
from p.parser_exception import ParserException

class TestEofParser:
    p = EofParser()

    def test_ok(self):
        (value, stream) = self.p.parse("")
        assert value == None
        assert stream == ""

    def test_raise(self):
        e = ParserException(expect="EOF", actual="h")
        with pytest.raises(ParserException, match=e.msg()):
             self.p.parse("hello")

