from p.letter_parser import LetterParser

class TestLetterParser:
    def test_ok(self):
        p = LetterParser()
        (value, stream) = p.parse("hi123")
        assert value == 'h'
        assert stream == "i123"
