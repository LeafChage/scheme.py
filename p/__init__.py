from p.digit_parser import DigitParser
from p.many1_parser import Many1Parser
from p.parser import *
from p.take_parser import TakeParser
from p.parser_exception import ParserException
from p.any_parser import AnyParser
from p.string_parser import StringParser
from p.and_parser import AndParser
from p.or_parser import OrParser
from p.choice_parser import ChoiceParser
from p.many_parser import ManyParser
from p.skip_parser import SkipParser
from p.letter_parser import LetterParser
from p.eof_parser import EofParser
from p.one_of_parser import OneOfParser
from p.until_parser import UntilParser
from p.attempt_parser import AttemptParser

def take(n: int) -> IParser[str]:
    return TakeParser(n)

def any() -> IParser[str]:
    return AnyParser()

def string(v: str) -> IParser[str]:
    return StringParser(v)

def digit() -> IParser[str]:
    return DigitParser()

def letter() -> IParser[str]:
    return LetterParser()

def many[T](p: IParser[T]) -> IParser[list[T]]:
    return ManyParser(p)

def many1[T](p: IParser[T]) -> IParser[list[T]]:
    return Many1Parser(p)

def skip[T](p: IParser[T]) -> IParser[None]:
    return SkipParser(p)

def choice[T](*ps: IParser[T]) -> IParser[T]:
    return ChoiceParser(*ps)

def one_of(targets: str) -> IParser[str]:
    return OneOfParser(targets)

def eof() -> IParser[None]:
    return EofParser()

def until[T](p: IParser[T]) -> IParser[str]:
    return UntilParser(p)

def attempt[T](p: IParser[T]) -> IParser[str]:
    return AttemptParser(p)


