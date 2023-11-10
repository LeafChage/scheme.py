import pytest

from p.digit_parser import DigitParser
from p.many1_parser import Many1Parser
from p.parser_exception import ParserException

class TestMany1Parser:
    def test_ok(self):
        p = Many1Parser(DigitParser())
        (value, stream) = p.parse("123hi")
        assert value == ["1","2","3"]
        assert stream == "hi"

    def test_nothing(self):
        p = Many1Parser(DigitParser())
        with pytest.raises(ParserException):
             p.parse("hi")

