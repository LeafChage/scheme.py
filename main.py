import sys
from p.parser_exception import ParserException
import scheme

def main():
    args = sys.argv
    try:
        (result, _) = scheme.parser().parse(" ".join(args[1:]))
        print(result.show())
    except ParserException as e:
        print("error", e)

main()
