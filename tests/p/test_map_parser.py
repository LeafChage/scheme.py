from p.string_parser import StringParser

class TestMapParser:
    def test_ok(self):
        p = StringParser("hello").map(lambda s: s + " world")
        (value, stream) = p.parse("hellopython")
        assert value == ("hello world")
        assert stream == "python"
