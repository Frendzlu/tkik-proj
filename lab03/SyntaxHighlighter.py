import sys
from Lexer import Scanner
from Token import Token, TokenType, get_chord_notation_tokens


class SyntaxHighlighter:
    COLOR_MAP = {
        TokenType.MEASURE_DELIMITER: "#007ACC",
        TokenType.CHORD_REPETITION: "#8A2BE2",
        TokenType.CHORD_OVERLAP: "#E74C3C",
        TokenType.PITCH: "#27AE60",
        TokenType.CHANGE_BY_SEMITONE: "#F39C12",
        TokenType.CHORD_ROOT_NODE_MODIFIER: "#A52A2A",
        TokenType.SUBSCRIPT: "#008B8B",
        TokenType.SUPERSCRIPT: "#C71585",
        TokenType.CHORD_QUALITY_MODIFIER: "#FC7F03",
        TokenType.NUMBER: "#FFF35F",
        TokenType.CHORD_COMPONENT_MODIFIER: "#1E90FF",
        TokenType.METRIC_SIGNATURE: "#228B22",
        TokenType.METER_DELIMITER: "#DAA520",
        TokenType.NO_CHORD: "#7F8C8D",
        TokenType.UNKNOWN: "#FF0000",
    }

    def __init__(self, filename):
        self.filename = filename
        self.scanner = Scanner(get_chord_notation_tokens())
        self.scanner.keep_whitespace = True

    def highlight_file(self):
        text = """
                <html><head>
                    <style>
                        body { background-color: #1e1e1e; color: #dcdcdc; font-family: monospace; }
                        pre { white-space: pre-wrap; }
                    </style>
                </head><body style="font-size:2rem;"><pre>"""

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                for line in file:
                    text += self.process_line(line) + "\n"
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found")
            sys.exit(1)

        text += "</pre></body></html>"
        return text

    def process_line(self, line):
        self.scanner.set_text(line.strip())
        highlighted_line = ""

        while True:
            token = self.scanner.next_token()
            if token is None:
                break
            highlighted_line += self.format_token(token) if token.type != TokenType.KEEP_WHITESPACE else " "

        return highlighted_line

    def format_token(self, token):
        color = self.COLOR_MAP.get(token.type, "black")
        return f'<span style="color: {color};">{token.value}</span>'

    def to_html_file(self, filename):
        if ".html" not in filename:
            filename += ".html"

        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.highlight_file())
        print(f"Syntax-highlighted '{self.filename}' file saved as '{filename}'")


if __name__ == "__main__":
    filename = "./chord_code.txt"
    syntax_highlighter = SyntaxHighlighter(filename)
    syntax_highlighter.to_html_file("chord_code_highlighted")

    for err in syntax_highlighter.scanner.errors:
        print(err)
