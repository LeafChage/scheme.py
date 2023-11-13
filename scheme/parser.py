import p as P
from p import IParser
from scheme.lisp_value import LAtom, LBoolean, LList, LNumber, LString, LispVal

def symbol() -> IParser[str]:
    return P.one_of("!#$%&|*+-/:<=>?@^_~")

def spaces() -> IParser[str]:
    return P.one_of(" \n\r\t")

def number() -> IParser[LispVal]:
    return P.many1(P.digit()).map(lambda nums: LNumber(int(''.join(nums))))

def string() -> IParser[LispVal]:
    def _inner(a: tuple[tuple[str, str], str]) -> LispVal:
        ((_, target), _) = a
        return LString(target)

    return P.string("\"").and_(
            P.until(P.string("\""))
        ).and_(
            P.string("\"")
        ).map(_inner)

def atom() -> IParser[LispVal]:
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

def plist() -> IParser[LispVal]:
    def _inner(a: list[tuple[LispVal, None]])-> LispVal:
        def fn(t: tuple[LispVal, None])->LispVal:
            (v, _) = t
            return v
        return LList(list(map(fn, a)))

    return P.many1(
            parse().and_(
                P.attempt( P.eof().or_( spaces().map(lambda _: None)))
            )
        ).map(_inner)

# def dotted_list() -> IParser[LispVal]:
#     P.many1(plist())
#     raise ParserException()
#
def s_expression() -> IParser[LispVal]:
    def _inner(a: tuple[tuple[str, LispVal], str])->LispVal:
        ((_, val), _) = a
        return val

    return P.string("(").debug().and_(
            plist()
        ).and_(P.string(")")).map(_inner)

def quoted() -> IParser[LispVal]:
    def _inner(a: tuple[str, LispVal])->LispVal:
        (_, lisp) = a
        return LList([LAtom("quote"), lisp])

    return P.string("'").and_(parse().debug()).map(_inner)

def parse() -> IParser[LispVal]:
    return P.choice(atom(),
                    string(),
                    number(),
                    # quoted(),
                    # s_expression()
                    )
