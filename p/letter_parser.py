from p.parser import IParser
from p.parser_exception import ParserException

_letter = [
        "a","b","c","d","e",
        "f","g","h","i","j",
        "k","l","m","n","o",
        "p","q","r","s","t",
        "u","v","w","x","y","z",
        "A","B","C","D","E",
        "F","G","H","I","J",
        "K","L","M","N","O",
        "P","Q","R","S","T",
        "U","V","W","X","Y","Z",
        ]

class LetterParser(IParser[str, str]):
    def __init__(self) -> None:
        pass

    def expect(self) -> list[str]:
        return _letter

    def parse(self, stream: str) -> tuple[str, str]:
        try:
            v = stream[0]
        except IndexError:
            raise ParserException(_letter, actual="EOF")
        else:
            if v in _letter:
                return (v,stream[1:])
            else:
                raise ParserException(_letter,actual=v)


def letter():
    return LetterParser()
