from enum import Enum, auto


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
    Call = auto() # parenthesis called together near to function/method - ()
    TypeAssignment = auto()
    VarsCalculation = auto()
    VarReference = auto()
    
PUBLICITY_ASSIGNABLE = (Keywords.Function, Keywords.Collection)


def is_available_scope(scope: str) -> bool:
    available_chars = list('abcd')
    if len(scope) != 2: 
        return False
    if scope[0] not in available_chars or scope[1] not in available_chars:
        return False
    else:
        return True
    

MODULES = {
    'Cmd': [
        'prompt'
    ],
    'Std': [
        'm'
    ],
    'Dim': [
        'squared'
    ]
}