import pytest
from p.any_parser import AnyParser
from p.parser_exception import ParserException
from p.string_parser import StringParser
from p.with_parser import WithParser

class TestWithParser:
    def test_ok(self):
        p = WithParser(StringParser("hello"), AnyParser())
        (value, stream) = p.parse("helloworld")
        assert value == 'w'
        assert stream == "orld"

    def test_raise_first_parser(self):
        p = WithParser(StringParser("hello"), AnyParser())
        e = ParserException(expect=["hello"], actual="world")
        with pytest.raises(ParserException, match=e.msg()):
             p.parse("worldhello")

    def test_raise_second_parser(self):
        p = WithParser(StringParser("hello"), StringParser("aaa"))
        e = ParserException(expect=["aaa"], actual="wor")
        with pytest.raises(ParserException, match=e.msg()):
             p.parse("helloworld")

