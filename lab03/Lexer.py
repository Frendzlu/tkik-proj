import pprint
from Token import Token, TokenType, generate_token_types, get_chord_notation_tokens


class Scanner:
    keep_whitespace = False
    index = 0
    text = ""
    token_dict = {}
    tokens_by_length = []
    errors = []

    def __init__(self, token_dict, keep_whitespace=False):
        self.token_dict = generate_token_types(token_dict)
        self.tokens_by_length = sorted(self.token_dict.keys(), key=len, reverse=True)
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

        match token_type:
            case TokenType.NUMBER:
                token = self.match_number()
            case _:
                token = self.match_rest()

        if token.type == TokenType.UNKNOWN:
            self.errors.append(f"TOKENIZATION ERROR ON INDEX: {self.index-1} - UNEXPECTED TOKEN TYPE\n{token}")
        return token

    def match_number(self):
        start_index = self.index
        number = ""
        while self.index < len(self.text) and self.token_dict.get(self.text[self.index]) == TokenType.NUMBER:
            number += self.text[self.index]
            self.index += 1
        return Token(TokenType.NUMBER, number, start_index)

    def match_rest(self):
        start_index = self.index
        char = self.text[self.index]
        for value in self.tokens_by_length:
            if self.text[self.index :].startswith(value):
                self.index += len(value)
                return Token(self.token_dict[value], value, start_index)

        self.index += 1
        return Token(TokenType.UNKNOWN, char, start_index)

    def strip_whitespace(self, text):
        return text.replace(" ", "").replace("\n", "").replace("\r", "").replace("\t", "")


if __name__ == "__main__":
    tokens = get_chord_notation_tokens()
    sc = Scanner(tokens)

    sc.set_text("|  8  <4:4>  N.C.  Gm(7)/D  Gm(7)/D  Gm(7)/D  Gm(7)/D  \  Gm(7)/D  \\ |")
    pprint.pprint(sc.token_dict)

    while True:
        token = sc.next_token()
        if token is None:
            break
        print(token)

    print("\n\n\n\n")
    for err in sc.errors:
        print(err)
