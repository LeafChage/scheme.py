from functools import wraps
import scheme.eval.eval as e
from scheme.lisp_value import LAtom, LBoolean, LList, LNumber, LString

class TestEval:
    def test_eval_number_ok(self):
        assert e.lisp(LNumber(1)) == LNumber(1)

    def test_eval_string_ok(self):
        assert e.lisp(LString("hello")) == LString("hello")

    def test_eval_boolean_ok(self):
        assert e.lisp(LBoolean(True)) == LBoolean(True)
        assert e.lisp(LBoolean(False)) == LBoolean(False)

    def test_eval_fn_add_ok(self):
        assert e.lisp(LList([LAtom("+"), LNumber(1), LNumber(2)])) == LNumber(3)

    def test_eval_fn_multiple_ok(self):
        assert e.lisp(LList([LAtom("+"), LNumber(1), LNumber(2)])) == LNumber(3)

    def test_eval_fn_is_string_ok(self):
        assert e.lisp(LList([LAtom("string?"), LString("hi")])) == LBoolean(True)

    def test_eval_fn_define_get_ok(self):
        assert e.lisp(LList([LAtom("define"), LAtom("hi"), LString("hi")])) == LString("hi")
        assert e.lisp(LAtom("hi")) == LString("hi")



