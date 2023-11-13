import pytest
from p.or_parser import OrParser
from p.string_parser import StringParser
from p.any_parser import AnyParser
from p.parser_exception import ParserException
from p.string_parser import StringParser

class TestOrParser:
    def test_ok(self):
        p = OrParser(StringParser("world"), AnyParser())
        (value, stream) = p.parse("helloworld")
        assert value == ('h')
        assert stream == "elloworld"

    def test_raise(self):
        p = OrParser(StringParser("hoge"), StringParser("fuga"))
        e = ParserException.concat(
                ParserException(expect=["hoge"], actual="hell"),
                ParserException(expect=["fuga"], actual="hell")
                )
        with pytest.raises(ParserException, match=e.msg()):
             p.parse("helloworld")

