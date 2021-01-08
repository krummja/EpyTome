from __future__ import annotations
from typing import Hashable
from enum import Enum


class TokenType(Enum):
    """Enum representing all token types."""
    EOF = 0
    SEMICOLON = 1
    COLON = 2
    LPAREN = 3
    RPAREN = 4
    PERIOD = 5
    QUOTE = 6
    AUTHOR = 7
    YEAR = 8
    TITLE = 9
    PUBLICATION = 10


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
