from __future__ import annotations
from typing import Optional

from .lexer import Lexer, Token, TokenType


class Parser:

    def __init__(self, lexer: Lexer) -> None:
        self.lexer = lexer
        self.lookahead = lexer.next_token()

    def parse(self) -> None:
        while self.lookahead.token_type != TokenType.EOF:
            pass

    def consume(self) -> None:
        self.lookahead = self.lexer.next_token()

    def error(self, string: str) -> None:
        raise SyntaxError(f"Expected {string} found {self.lookahead} on "
                          f"line {self.lexer.line_num}.")

    def match(self, token_type: TokenType) -> Optional[Token]:
        if self.lookahead.token_type == token_type:
            old_token = self.lookahead
            self.consume()
            return old_token
        self.error(TokenType[token_type.name])
