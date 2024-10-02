from enum import Enum

class Errors(Enum):
    Syntax = 'SyntaxError'
    Expectation = 'ExpectationError'
    Console = 'ConsoleError'
    UnknownVariable = 'UnknownVariableError'

def raise_error(name: Errors, content: str, index: int | None = None) -> None:
    if index is not None:
        print(f'{name}: {content}: at {index} line')
    else:
        print(f'{name}: {content}')
    exit(1)