# 1678.) Goal Parser Interpretation
# Categories: String

class Solution:
    def interpret(self, command: str) -> str:
        parsers = {
            'G' : 'G',
            '()' : 'o',
            '(al)' : 'al'
        }
    
        for parser in list(parsers.keys()):
            command = command.replace(parser, parsers[parser])
        
        return command