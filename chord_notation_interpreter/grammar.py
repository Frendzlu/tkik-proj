from utils import reader
from lark import Lark


if __name__ == "__main__":
    grammar = reader("./grammar.txt")
    chord_code = reader("./test.txt")

    # chord code parser
    ccp = Lark(rf"{grammar}", start="start")

    # abstract syntax tree
    ast = ccp.parse(chord_code)
    print(ast.pretty())
