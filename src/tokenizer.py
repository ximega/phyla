from enum import Enum, auto
from typing import Literal, Self

class Keywords(Enum):
    Using = 'using'
    Collection = 'collection'
    Input = 'input'
    Arrow = auto() # ->
    Reference = auto() # ~, for referencing part of library
    Any = auto() # any keyword for any type
    Separator = auto() # ::, when pointing input values
    Redefiner = auto() # ::, when redefining name for return
    Scope = 'scope'
    To = '[to]'
    Local = 'local'
    Function = 'function'
    Public = 'public'
    Private = 'private'

def is_available_scope(scope: str) -> bool:
    available_chars = list('abcd')
    if len(scope) != 2: 
        return False
    if scope[0] not in available_chars or scope[1] not in available_chars:
        return False
    else:
        return True

class Token:
    def __init__(
        self,
        pub_or_pri: Literal['public', 'private'],
        starting_keyword: Keywords,
        values: list[tuple[str | Keywords | tuple[str | Keywords | tuple]]],
        subtoken: None | Self
    ) -> None:
        self.pub_or_pri = pub_or_pri
        self.starting_keyword = starting_keyword
        self.values = values
        self.subtoken = subtoken

class Tokenizer:
    def __init__(self, code: str) -> None:
        self.code = code
        self.lines = code.split('\n')
        
    def tokenize(self) -> list[Token]: # type: ignore
        pass # type: ignore