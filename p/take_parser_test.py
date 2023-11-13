import re
import pytest
from p.parser_exception import ParserException
from p.take_parser import TakeParser

class TestTakeParser:
    def test_ok(self):
        p = TakeParser(5)
        (value, stream) = p.parse("helloworld")
        assert value == "hello"
        assert stream == "world"

    def test_raise(self):
        p = TakeParser(5)
        e = ParserException(expect=["*****"], actual="hel")
        with pytest.raises(ParserException, match=re.escape(e.msg())):
             p.parse("hel")

