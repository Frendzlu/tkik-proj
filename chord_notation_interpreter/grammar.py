from utils import reader
from lark import Lark
from error_handler import handle_errors

if __name__ == "__main__":
    grammar = reader("./grammar.txt")
    chord_code = reader("./invalid_cc.txt")

    # chord code parser
    ccp = Lark(rf"{grammar}", start="start", parser='lalr')

    # abstract syntax tree
    ast = ccp.parse(chord_code,  on_error=handle_errors)
    for tree in ast.children:
        print(f"\n\n=============== {tree.data} ================")
        print(tree.pretty())
    # print(ast.pretty())
