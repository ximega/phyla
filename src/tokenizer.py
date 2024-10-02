from typing import Literal, Self
from src.errors import Errors, raise_error
from src.scopes import *


class Token:
    def __init__(
        self,
        pub_or_pri: Literal['public', 'private', 'null'],
        starting_keyword: Keywords,
        values: list[tuple[str | Keywords | tuple[str | Keywords | tuple]]] | str,
        subtoken: Self | None = None
    ) -> None:
        self.pub_or_pri = pub_or_pri
        self.starting_keyword = starting_keyword
        self.values = values
        self.subtoken = subtoken

class Tokenizer:
    def __init__(self, code: str) -> None:
        self.code = code
        self.lines = code.split('\n')
        self.tokens: list[Token] = []
        
    def tokenize(self) -> Self: 
        for index, line in enumerate(self.lines, 1):
            splitted = line.strip().split(' ')
            
            splitted[-1] = splitted[-1][:-1]
            splitted.append(';')

            # for skipping empty lines
            if splitted[0] in ('', ';'):
                continue
            for word in splitted:                
                if word in ('', ' '):
                    raise_error(Errors.Syntax, f"Too much space between code blocks", index)
            
            if splitted[0] in [Keywords.Private, Keywords.Public]:
                try:
                    if splitted[1] not in PUBLICITY_ASSIGNABLE:
                        raise_error(Errors.Syntax, f"You are not allowed to make {splitted[1]} {splitted[0]}", index)
                except IndexError:
                    raise_error(Errors.Expectation, f"Expected code block after {splitted[1]}", index)
            
            match splitted[0]:
                case 'public': pass
                    #self.tokens.append(Token('public', ))
                case 'private': pass
                    #self.tokens.append(Token('private'))
                case 'using':
                    try:
                        if splitted[1] not in MODULES:
                            raise_error(Errors.UnknownVariable, f"Unknown module {splitted[1]} was used", index)
                        
                        self.tokens.append(Token('null', Keywords.Using, splitted[1]))
                    except IndexError:
                        raise_error(Errors.Expectation, f"Was expecting scope for using", index)
                    
        return self