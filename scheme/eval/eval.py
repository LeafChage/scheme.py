from collections.abc import Callable
from functools import reduce
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
            return apply(v, *tail)
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

def caliculate(f: Callable[[int, int], int])->Callable[[list[LispVal]], LispVal]:
    return lambda nums: LNumber(reduce(f, map(unpack_num,nums)))

# def type_check(c: type[LispVal])->Callable[[LispVal], LispVal]:
#     def _inner(v: LispVal)->LispVal:
#         return LBoolean(type(v) is c)
#
#     return _inner

PRIMITIVES = {
        "+": caliculate(lambda a, b: a + b),
        "-": caliculate(lambda a, b: a - b),
        "*": caliculate(lambda a, b: a * b),
        "/": caliculate(lambda a, b: a // b),
        "mod": caliculate(lambda a, b: a % b),
        # "string?": type_check(LString),
        }

def apply(name: str, *tail: LispVal)->LispVal:
    fn = PRIMITIVES[name]
    return fn(list(tail))
