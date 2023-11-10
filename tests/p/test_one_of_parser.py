from p import one_of

class TestOneOfParser:
    def test_ok(self):
        p = one_of("123")
        (value, stream) = p.parse("2hello")
        assert value == "2"
        assert stream == "hello"
