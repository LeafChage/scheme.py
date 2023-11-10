from util.string import String

class TestString:
    def test_ok(self):
        (before, after) = String.split("hello world", 5)
        assert before == "hello"
        assert after == " world"

    def test_just_size(self):
        (before, after) = String.split("hello", 5)
        assert before == "hello"
        assert after == ""
