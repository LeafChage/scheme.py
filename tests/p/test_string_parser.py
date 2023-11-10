from p.string_parser import StringParser

class TestStringParser:
    def test_ok(self):
        p = StringParser("hello")
        (value, stream) = p.parse("helloworld")
        assert value == "hello"
        assert stream == "world"

    def test_just_size_stream(self):
        p = StringParser("hello")
        (value, stream) = p.parse("hello")
        assert value == "hello"
        assert stream == ""
