import pytest
from p.string_parser import StringParser
from p.parser_exception import ParserException

class TestStringParser:
    p = StringParser("hello")
    def test_ok(self):
        (value, stream) = self.p.parse("helloworld")
        assert value == "hello"
        assert stream == "world"

    def test_just_size_stream(self):
        (value, stream) = self.p.parse("hello")
        assert value == "hello"
        assert stream == ""

    def test_raise(self):
        e = ParserException(expect="hello", actual="world")
        with pytest.raises(ParserException, match=e.msg()):
             self.p.parse("worldhello")

    def test_raise_nothing(self):
        e = ParserException(expect="hello", actual="")
        with pytest.raises(ParserException, match=e.msg()):
             self.p.parse("")



