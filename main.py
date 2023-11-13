import sys
from p.parser_exception import ParserException
from scheme import parse

def main():
    args = sys.argv
    # try:
    (result, _) = parse().parse(" ".join(args[1:]))
    print(result.show())
    # except ParserException as e:
    #     print("error", e)

main()
