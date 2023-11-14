import re
import pytest
from p.any_parser import AnyParser
from p.parser_exception import ParserException

class TestAnyParser:
    def test_ok(self):
        p = AnyParser()
        (value, stream) = p.parse("helloworld")
        assert value == "h"
        assert stream == "elloworld"

    def test_raise(self):
        p = AnyParser()
        e = ParserException(expect=["*"], actual="EOF")
        with pytest.raises(ParserException, match=re.escape(e.msg())):
             p.parse("")

