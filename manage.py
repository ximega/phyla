import os, sys
from src.errors import raise_error, Errors
from src.tokenizer import Tokenizer

if __name__ == '__main__':
    try:
        filepath = sys.argv[1]
        
        with open(filepath, 'r') as f:
            contents = f.read()
            
            tokens = Tokenizer(contents).tokenize().tokens
            
            print(tokens)
        
        if len(sys.argv) > 2:
            raise_error(Errors.Console, f"Can't specify any additional arguments than filepath")
    except IndexError:
        raise_error(Errors.Console, f"File to execute is not specified")