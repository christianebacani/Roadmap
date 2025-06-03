# Question: Regexp basics - parsing prices
# Categories: 7 Kyu

import re

def to_cents(amount: str) -> int | bool:
    if re.search(r'^.*\n.*$', amount):
        return None
    
    if re.search(r'^\$\d{1,}\.\d{2}$', amount):
        amount = amount.replace('$', '')
        amount = amount.replace('.', '')
        return int(amount)

    return None