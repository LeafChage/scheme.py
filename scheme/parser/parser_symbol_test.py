from scheme.parser.parser import symbol

class TestSymbolParser:
    def test_ok(self):
        (value, stream) = symbol().parse("!")
        assert value == "!"
        assert stream == ""

