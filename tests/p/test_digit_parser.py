from p.digit_parser import DigitParser

class TestDigitParser:
    def test_ok(self):
        p = DigitParser()
        (value, stream) = p.parse("123hi")
        assert value == '1'
        assert stream == "23hi"
