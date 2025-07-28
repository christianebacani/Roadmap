# Question: Is valid identifier?
# Categories: 7 Kyu
import re

def is_valid(idn: str) -> bool:
    if re.search(r'^([A-Za-z\_\$])[A-Za-z0-9\_\$]*$', idn):
        return True
    
    return False