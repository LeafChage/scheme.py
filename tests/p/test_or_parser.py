from p.any_parser import AnyParser
from p.or_parser import OrParser
from p.string_parser import StringParser

class TestOrParser:
    def test_ok(self):
        p = OrParser(StringParser("world"), AnyParser())
        (value, stream) = p.parse("helloworld")
        assert value == ('h')
        assert stream == "elloworld"
