from lark import  Token
from lark.exceptions import UnexpectedCharacters, UnexpectedToken

def handle_errors(e):
    if isinstance(e, UnexpectedCharacters):
        # count = 0
        # while isinstance(e, UnexpectedCharacters):
        # e.interactive_parser.resume_parse()
        # print(e)
        print(e)
        # print(f'{count} unexpected characters found in a row')
        return True
    
    if isinstance(e, UnexpectedToken):
        print(f'skipping token: {e.token}')
        return True
    print(e.token)
    return False