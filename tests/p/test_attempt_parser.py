from p.attempt_parser import AttemptParser
from p.string_parser import StringParser

class TestAttemptParser:
    def test_ok(self):
        p = AttemptParser(StringParser("world"))
        (value, stream) = p.parse("helloworld")
        assert value == None
        assert stream == "helloworld"
