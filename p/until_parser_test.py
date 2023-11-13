from p.string_parser import StringParser
from p.until_parser import UntilParser

class TestUntilParser:
    def test_ok(self):
        p = UntilParser(StringParser("world"))
        (value, stream) = p.parse("helloworld")
        assert value == ("hello")
        assert stream == "world"
