import flytrap as P
from flytrap import IParser
from scheme.lisp_value import LAtom, LBoolean, LList, LNumber, LString, LispVal

def symbol() -> IParser[str, str]:
    return P.one_of("!#$%&|*+-/:<=>?@^_~")

def spaces() -> IParser[str, str]:
    return P.one_of(" \n\r\t")

def number() -> IParser[str, LispVal]:
    return P.many1(P.digit()).map(lambda nums: LNumber(int(''.join(nums))))

def string() -> IParser[str, LispVal]:
    return P.string("\"").with_(
            P.until(P.string("\""))
        ).skip(
            P.string("\"")
        ).map(lambda v : LString("".join(v)))

def atom() -> IParser[str, LispVal]:
    def _inner_concat_list(a: tuple[str, list[str]]) -> str:
        (first, rest) = a
        return "".join([first] + rest)

    def _inner_change_to_lispvalue(a: str) -> LispVal:
        match(a):
            case "#t": return LBoolean(True)
            case "#f": return LBoolean(False)
            case atom: return LAtom(atom)

    return P.letter().or_(
                symbol()
            ).and_(
                P.many(P.choice(P.letter(), P.digit(), symbol()))
            ).map(
                _inner_concat_list
            ).map(
                _inner_change_to_lispvalue
            )

def plist() -> IParser[str, LispVal]:
    return P.many1(lisp().skip(P.attempt(spaces()))).map(lambda l : LList(l))

# def dotted_list() -> IParser[LispVal]:
#     P.many1(plist())
#     raise ParserException()

def s_expression() -> IParser[str, LispVal]:
    return P.string("(").with_(plist()).skip(P.string(")"))

def quoted() -> IParser[str, LispVal]:
    def _inner(a: tuple[str, LispVal])->LispVal:
        (_, lisp) = a
        return LList([LAtom("quote"), lisp])

    return P.string("'").and_(lisp()).map(_inner)

def lisp() -> IParser[str, LispVal]:
    return P.choice(atom(),
                    string(),
                    number(),
                    P.lazy(quoted),
                    P.lazy(s_expression)
                    )

def parser(value: str) -> LispVal:
    (result, _) = lisp().parse(value)
    return result



