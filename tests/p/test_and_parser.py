from p.and_parser import AndParser
from p.any_parser import AnyParser
from p.string_parser import StringParser

class TestAndParser:
    def test_ok(self):
        p = AndParser(StringParser("hello"), AnyParser())
        (value, stream) = p.parse("helloworld")
        assert value == ("hello", 'w')
        assert stream == "orld"
