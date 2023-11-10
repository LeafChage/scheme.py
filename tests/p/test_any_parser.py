from p.any_parser import AnyParser

class TestAnyParser:
    def test_ok(self):
        p = AnyParser()
        (value, stream) = p.parse("helloworld")
        assert value == "h"
        assert stream == "elloworld"
