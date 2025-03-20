import pprint


class Scanner:
    keep_whitespace = False
    pos = 0
    line = 0
    token_dict = {}

    def __init__(self, token_dict, keep_whitespace=False):
        for key in token_dict:
            for token in token_dict[key]:
                self.token_dict[token] = key
        self.keep_whitespace = keep_whitespace

    def parse_file(self, filename):
        pass

    def parse_line(self, text):
        if not self.keep_whitespace:
            text = self.strip_whitespace(text)
        scanning_result = []
        errors = []
        for char in text:
            if char in self.token_dict:
                scanning_result.append((self.token_dict[char], char))
            else:
                errors.append("Unknown token at position {}".format(self.pos))
            self.pos += 1
        if errors:
            return [], errors
        return scanning_result, errors

    def strip_whitespace(self, text):
        return text.replace(' ', '').replace('\n', '').replace('\r', '').replace('\t', '')


if __name__ == "__main__":
    sc = Scanner({
        "digit": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
        "operation": ['+', '/', '-', '*'],
        "bracket_left": ['('],
        "bracket_right": [')'],
        "identity": list("abcdefghijklmnopqrstuwxyz")
    })
    scres, err = sc.parse_line("3+3*(25-43)         costamcostam26+252")
    pprint.pprint(scres)
    pprint.pprint(err)
