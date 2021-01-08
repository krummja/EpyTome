from __future__ import annotations

from parser.token import Token, TokenType


class Lexer:

    def __init__(self, input_stream: str) -> None:
        self.input_stream = input_stream
        self.pos: int = 0
        self.line_num: int = 1
        self.char_num: int = 1
        if len(input_stream) != 0:
            self.char: str = self.input_stream[self.pos]
        else:
            self.char: str = TokenType.EOF

    def next_token(self) -> Token:
        pass

    def consume(self) -> None:
        pass

    def error(self) -> None:
        raise SyntaxError(f"Invalid character {self.char} at "
                          f"[{self.line_num}:{self.char_num}].")
