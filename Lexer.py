import pprint
import sys


class Scanner:
    keepWhitespace = False
    pos = 0
    line = 0
    tokenDict = {}

    def __init__(self, tokenDict, keepWhitespace=False):
        for key in tokenDict:
            for token in tokenDict[key]:
                self.tokenDict[token] = key
        self.keepWhitespace = keepWhitespace

    def parse_file(self, filename):
        pass

    def parse_line(self, text):
        if not self.keepWhitespace:
            text = self.strip_whitespace(text)
        scanning_result = []
        errors = []
        for char in text:
            if char in self.tokenDict:
                scanning_result.append((self.tokenDict[char], char))
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


