import pytest
from p.letter_parser import LetterParser, _letter
from p.parser_exception import ParserException

class TestLetterParser:
    p = LetterParser()
    def test_ok(self):
        (value, stream) = self.p.parse("hi123")
        assert value == 'h'
        assert stream == "i123"

    def test_raise(self):
        e = ParserException(expect=_letter, actual="1")
        with pytest.raises(ParserException, match=e.msg()):
             self.p.parse("123")

    def test_raise_nothing(self):
        e = ParserException(expect=_letter, actual="EOF")
        with pytest.raises(ParserException, match=e.msg()):
             self.p.parse("")



