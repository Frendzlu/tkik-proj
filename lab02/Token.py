from enum import Enum


class TokenType(Enum):
    DIGIT = 0
    OPERATOR = 1
    BRACKET_LEFT = 2
    BRACKET_RIGHT = 3
    IDENTIFIER = 4
    UNKNOWN = 5


class Token:
    def __init__(self, type_: TokenType, value: str, position: int):
        self.type = type_
        self.value = value
        self.position = position

    def __repr__(self):
        return f"Token(type={self.type}, value='{self.value}', position={self.position})"


def generate_token_types(token_name_val_dict: dict):
    token_dict = {}
    for name, value in token_name_val_dict.items():
        print(name, value)
        for v in value:
            token_dict[v] = name

    return token_dict