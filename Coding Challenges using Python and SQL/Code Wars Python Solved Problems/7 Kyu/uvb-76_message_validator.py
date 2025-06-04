# Question: UVB-76 Message Validator
# Categories: 7 Kyu

import re

def validate(message: str) -> bool:
    if re.search(r'^(MDZHB){1}\s\d{2}\s\d{3}\s[A-Z]+\s\d{2}\s\d{2}\s\d{2}\s\d{2}$', message):
        return True
    
    return False