import pytest
from p.one_of_parser import OneOfParser
from p.parser_exception import ParserException

class TestOneOfParser:
    def test_ok(self):
        p = OneOfParser("123")
        (value, stream) = p.parse("2hello")
        assert value == "2"
        assert stream == "hello"

    def test_raise(self):
        p = OneOfParser("abc")
        e = ParserException(expect=["a", "b", "c"], actual="h")
        with pytest.raises(ParserException, match=e.msg()):
             p.parse("hello")

