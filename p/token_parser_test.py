import pytest
from p.parser_exception import ParserException
from p.token_parser import TokenParser

class TestTokenParser:
    p = TokenParser(1)
    def test_ok(self):
        (value, stream) = self.p.parse([1,2,3,4,5])
        assert value == 1
        assert stream == [2,3,4,5]

    def test_raise(self):
        e = ParserException(expect=["1"], actual="5")
        with pytest.raises(ParserException, match=e.msg()):
             self.p.parse([5,4,3,2,1])

    def test_raise_nothing(self):
        e = ParserException(expect=["1"], actual="")
        with pytest.raises(ParserException, match=e.msg()):
             self.p.parse([])



