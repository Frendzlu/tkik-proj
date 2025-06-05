from lark import  Token
from lark.exceptions import UnexpectedCharacters, UnexpectedToken

class ErrorHandler:
    es = []

    def handle_errors(self, e):
        if isinstance(e, UnexpectedCharacters):
            emsg = f"Line {e.line}, column {e.column}: Unexpected character"
            self.es.append(emsg)
            print(emsg)
            # print(f'{count} unexpected characters found in a row')
            return True

        if isinstance(e, UnexpectedToken):
            emsg = f"Line {e.line}, column {e.column}: Unexpected token {e.token}"
            self.es.append(emsg)
            print(emsg)
            return True

        print(e.token)
        return False