# Question: Valid number to 2 decimal places
# Categories: 7 Kyu
import re

def valid_number(n: str) -> bool:
    if re.search(r'^[\d\+\-]{0,}\.\d{2}$', n):
        return True
    
    return False