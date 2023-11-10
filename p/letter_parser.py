from p.parser import IParser
from p.parser_exception import ParserException
from util.string import String

letter = [
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

class LetterParser(IParser[str]):
    def __init__(self) -> None:
        pass

    def parse(self, stream: str) -> tuple[str, str]:
        (v, s)  = String.split(stream, 1)
        if v in letter:
            return (v,s)
        else:
            raise ParserException()



