import pprint
from Token import Token, TokenType, generate_token_types

class Scanner:
    keep_whitespace = False
    index = 0
    text = ""
    token_dict = {}
    errors = []

    def __init__(self, token_dict, keep_whitespace=False):        
        self.token_dict = generate_token_types(token_dict)
        self.keep_whitespace = keep_whitespace

    def set_text(self, text):
        self.text = text if self.keep_whitespace else self.strip_whitespace(text)
        self.index = 0

    def parse_file(self, filename):
        pass
    
    def next_token(self):
        if self.index >= len(self.text):
            return None
        
        char = self.text[self.index]
        token_type = self.token_dict.get(char, TokenType.UNKNOWN)
        token = None
        if token_type == TokenType.DIGIT:
            token = self.parse_number()
        elif token_type == TokenType.IDENTIFIER:
            token = self.parse_identifier()
        else:
            token = Token(token_type, char, self.index)
            self.index += 1  
        
        if token.type == TokenType.UNKNOWN:
            self.errors.append(f"TOKENIZATION ERROR ON INDEX: {self.index-1} - UNEXPECTED TOKEN TYPE\n{token}")
        return token

    def parse_number(self):
        start_index = self.index
        number = ""
        while self.index < len(self.text) and self.token_dict.get(self.text[self.index]) == TokenType.DIGIT:
            number += self.text[self.index]
            self.index += 1
        return  Token(TokenType.DIGIT, number, start_index)
        
    def parse_identifier(self):
        start_index = self.index
        identifier = ""
        while self.index < len(self.text) and self.token_dict.get(self.text[self.index]) == TokenType.IDENTIFIER:
            identifier += self.text[self.index]
            self.index += 1
        return Token(TokenType.IDENTIFIER, identifier, start_index)


    def strip_whitespace(self, text):
        return text.replace(' ', '').replace('\n', '').replace('\r', '').replace('\t', '')


if __name__ == "__main__":
    tokens = {
        TokenType.DIGIT: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
        TokenType.OPERATOR: ['+', '/', '-', '*'],
        TokenType.BRACKET_LEFT: ['('],
        TokenType.BRACKET_RIGHT: [')'],
        TokenType.IDENTIFIER: list("abcdefghijklmnopqrstuwxyz")
    }

    sc = Scanner(tokens)
    sc.set_text("3+3*(25-43)         costamcostam26+252")
    pprint.pprint(sc.token_dict)

    while True:
        token = sc.next_token()
        if token is None:
            break
        print(token)
    
    print("\n\n\n\n")
    for err in sc.errors:
        print(err)

    print(sc.token_dict)