from collections.abc import Callable
from functools import reduce
from scheme.error import BadSpecialForm, NotFunction, NumArgs, TypeMismatch
from scheme.lisp_value import LAtom, LBoolean, LDottedList, LList, LNumber, LString, LispVal

def caliculate(f: Callable[[int, int], int]) -> Callable[[LispVal, LispVal], LispVal]:
    def _inner(a: LispVal, b: LispVal) -> LispVal:
        match (a, b):
            case (LNumber(v1), LNumber(v2)):
                return LNumber(f(v1, v2))
            case _:
                raise TypeMismatch("LNumber", [a,b])

    return _inner

def apply_recursive(f: Callable[[LispVal, LispVal] , LispVal]) -> Callable[[list[LispVal]], LispVal]:
    def _inner(values: list[LispVal]) -> LispVal:
        return reduce(f, values)

    return _inner

def type_check(s: str)->Callable[[LispVal], LispVal]:
    def _inner(value: LispVal)->LispVal:
        match (s, value):
            case ("LString", LString(_)):
                return LBoolean(True)
            case ("LBoolean", LBoolean(_)):
                return LBoolean(True)
            case ("LNumber", LNumber(_)):
                return LBoolean(True)
            case ("LAtom", LAtom(_)):
                return LBoolean(True)
            case _:
                return LBoolean(False)

    return _inner

def equal(s: str)->Callable[[LispVal, LispVal], LispVal]:
    def _inner(a: LispVal, b: LispVal)->LispVal:
        match (s, a, b):
            case ("LString", LString(va), LString(vb)):
                return LBoolean(va == vb)
            case ("LBoolean", LString(va), LString(vb)):
                return LBoolean(va == vb)
            case ("LNumber", LNumber(va), LNumber(vb)):
                return LBoolean(va == vb)
            case ("LAtom", LAtom(va), LAtom(vb)):
                return LBoolean(va == vb)
            case _:
                return LBoolean(False)

    return _inner

ADD = apply_recursive(caliculate(lambda a, b: a + b))
MINUS = apply_recursive(caliculate(lambda a, b: a - b))
MULTIPLE =apply_recursive(caliculate(lambda a, b: a * b))
DEVIDE =apply_recursive(caliculate(lambda a, b: a // b))
MOD =apply_recursive(caliculate(lambda a, b: a % b))

GLOBAL_VARIABLE = { }

def if_expression(pred: LispVal, then_action: LispVal, else_action: LispVal)->LispVal:
    match pred:
        case LBoolean(True):
            return then_action
        case LBoolean(False):
            return else_action
        case _:
            raise TypeMismatch("LBoolean", [pred])


def lisp(val: LispVal) -> LispVal:
    match val:
        ## eval
        case LNumber(_): return val
        case LString(_): return val
        case LBoolean(_): return val
        case LAtom(label):
            return GLOBAL_VARIABLE[label]
        ## caliculate
        case LList([LAtom("+"), *tail]): return ADD(list(map(lisp, tail)))
        case LList([LAtom("-"), *tail]): return MINUS(list(map(lisp, tail)))
        case LList([LAtom("*"), *tail]): return MULTIPLE(list(map(lisp, tail)))
        case LList([LAtom("/"), *tail]): return DEVIDE(list(map(lisp, tail)))
        case LList([LAtom("mod"), *tail]): return MOD(list(map(lisp, tail)))
        ## conditions
        case LList([LAtom("string?"), arg]): return type_check("LString")(lisp(arg))
        case LList([LAtom("string?"), *tail]): raise NumArgs(1, tail)
        case LList([LAtom("number?"), arg]): return type_check("LNumber")(lisp(arg))
        case LList([LAtom("number?"), *tail]): raise NumArgs(1, tail)
        case LList([LAtom("boolean?"), arg]): return type_check("LBoolean")(lisp(arg))
        case LList([LAtom("boolean?"), *tail]): raise NumArgs(1, tail)
        case LList([LAtom("atom?"), arg]): return type_check("LAtom")(lisp(arg))
        case LList([LAtom("atom?"), *tail]): raise NumArgs(1, tail)
        case LList([LAtom("string=?"), arg1, arg2]): return equal("LString")(lisp(arg1), lisp(arg2))
        case LList([LAtom("string=?"), *tail]): raise NumArgs(2, tail)
        case LList([LAtom("number=?"), arg1, arg2]): return equal("LNumber")(lisp(arg1), lisp(arg2))
        case LList([LAtom("number=?"), *tail]): raise NumArgs(2, tail)
        case LList([LAtom("atom=?"), arg1, arg2]): return equal("LAtom")(lisp(arg1), lisp(arg2))
        case LList([LAtom("atom=?"), *tail]): raise NumArgs(2, tail)
        case LList([LAtom("boolean=?"), arg1, arg2]): return equal("LBoolean")(lisp(arg1), lisp(arg2))
        case LList([LAtom("boolean=?"), *tail]): raise NumArgs(2, tail)
        case LList([LAtom("quote"), val]): return val
        case LList([LAtom("if"), pred, then_action, else_action]):
            return if_expression(lisp(pred), lisp(then_action), lisp(else_action))
        case LList([LAtom("set!"), LAtom(v), form]):
            GLOBAL_VARIABLE[v] = lisp(form)
            return lisp(form)
        case LList([LAtom("define"), LAtom(v), form]):
            GLOBAL_VARIABLE[v] = lisp(form)
            return lisp(form)
        case LList([LAtom(v), *_]):
            raise NotFunction(v)
        case LList(_):
            raise
        case LDottedList(_):
            raise
        case _:
            raise BadSpecialForm(val)
