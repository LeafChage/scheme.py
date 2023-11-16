from p.parser_exception import ParserException
import scheme

def repl():
    while True:
        data = input("lisp> ")
        if data.upper() == "EXIT":
            break
        try:
            result = scheme.parser(data)
            print(scheme.lisp(result).show())
        except ParserException as e:
            print(e.msg())

def main():
    repl()

main()
