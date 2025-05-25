from chord_notation_interpreter.Transformer import EvalExpressions
from utils import reader
from lark import Lark, Token
from error_handler import handle_errors

if __name__ == "__main__":
    grammar = reader("./grammar.txt")
    chord_code = reader("./cc.txt")

    # chord code parser
    ccp = Lark(rf"{grammar}", start="start", parser='lalr')

    # abstract syntax tree
    ast = ccp.parse(chord_code,  on_error=handle_errors)
    ast2 = ast.copy()
    print(ast2.pretty())
    print(EvalExpressions().transform(ast2).pretty())




