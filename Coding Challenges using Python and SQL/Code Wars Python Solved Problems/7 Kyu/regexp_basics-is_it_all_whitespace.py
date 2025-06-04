# Question: Regexp Basics - is it all whitespace?
# Categories: 7 Kyu

import re

def whitespace(string: str) -> bool:
    if re.search(r'^\s*$', string):
        return True
    
    return False