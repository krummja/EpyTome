from __future__ import annotations

from typing import Hashable
from enum import auto, Enum


class TokenType(Enum):
    """Enum representing all token types."""
    EOF = auto()
    SEMICOLON = auto()
    COLON = auto()
    COMMA = auto()
    AMPERSAND = auto()
    LPAREN = auto()
    RPAREN = auto()
    PERIOD = auto()
    QUOTE = auto()
    AUTHOR = auto()
    LNAME = auto()
    FNAME = auto()
    YEAR = auto()
    TITLE = auto()
    PUBLICATION = auto()
    ADDRESS = auto()
    ID = auto()
    NUMBER = auto()


class Token:

    def __init__(self, token_type: int, text: str) -> None:
        self.token_type = token_type
        self.text = text

    def __str__(self) -> str:
        return f"{self.text}, {TokenType(self.token_type).name}"

    def __hash__(self) -> Hashable:
        return hash((self.token_type, self.text))

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Token):
            return (self.token_type == other.token_type,
                    self.text == other.text)
        else:
            raise TypeError(f"Expected Token. Got {type(other)}.")


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
