from p.eof_parser import EofParser

class TestEofParser:
    def test_ok(self):
        p = EofParser()
        (value, stream) = p.parse("")
        assert value == None
        assert stream == ""
