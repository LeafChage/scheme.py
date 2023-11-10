from p.take_parser import TakeParser

class TestTakeParser:
    def test_ok(self):
        p = TakeParser(5)
        (value, stream) = p.parse("helloworld")
        assert value == "hello"
        assert stream == "world"
