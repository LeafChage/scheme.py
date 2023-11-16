from collections.abc import Callable
from functools import reduce
from scheme.error import NotFunction, NumArgs, TypeMismatch
from scheme.lisp_value import LAtom, LBoolean, LDottedList, LList, LNumber, LString, LispVal

def lisp(val: LispVal) -> LispVal:
    match val:
        case LNumber(_):
            return val
        case LString(_):
            return val
        case LBoolean(_):
            return val
        case LAtom(_):
            return val
        case LList([LAtom(v), *tail]):
            return apply(v, list(map(lisp, tail)))
        case LList(_):
            raise
        case LDottedList(_):
            raise
        case _:
            raise

def unpack_num(val: LispVal)->int:
    match val:
        case LNumber(v):
            return v
        case _:
            # unexpected type
            raise

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

def type_check(s: str)->Callable[[list[LispVal]], LispVal]:
    def _inner(values: list[LispVal])->LispVal:
        if len(values) != 1:
            raise NumArgs(1, values)

        match (s, values[0]):
            case ("LString", LString(_)):
                return LBoolean(True)
            case ("LBoolean", LBoolean(_)):
                return LBoolean(True)
            case ("LNumber", LNumber(_)):
                return LBoolean(True)
            case ("LAtom", LAtom(_)):
                return LBoolean(True)
            case _:
                print(s, values)
                return LBoolean(False)

    return _inner

def equal(s: str)->Callable[[list[LispVal]], LispVal]:
    def _inner(values: list[LispVal])->LispVal:
        if len(values) != 1:
            raise NumArgs(1, values)

        match (s, values[0]):
            case ("LString", LString(_)):
                return LBoolean(True)
            case ("LBoolean", LBoolean(_)):
                return LBoolean(True)
            case ("LNumber", LNumber(_)):
                return LBoolean(True)
            case ("LAtom", LAtom(_)):
                return LBoolean(True)
            case _:
                print(s, values)
                return LBoolean(False)

    return _inner

PRIMITIVES = {
        "+": apply_recursive(caliculate(lambda a, b: a + b)),
        "-": apply_recursive(caliculate(lambda a, b: a - b)),
        "*": apply_recursive(caliculate(lambda a, b: a * b)),
        "/": apply_recursive(caliculate(lambda a, b: a // b)),
        "mod": apply_recursive(caliculate(lambda a, b: a % b)),
        "string?": type_check("LString"),
        "number?": type_check("LNumber"),
        "boolean?": type_check("LBoolean"),
        "atom?": type_check("LAtom"),
        "string=?": type_check("LAtom"),
        }

def apply(name: str, tail: list[LispVal])->LispVal:
    if name in PRIMITIVES:
        fn = PRIMITIVES[name]
        return fn(tail)
    else:
        raise NotFunction(name)
