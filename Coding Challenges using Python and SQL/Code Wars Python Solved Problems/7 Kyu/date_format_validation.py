# Question: Date Format Validation
# Categories: 7 Kyu
import re

def date_checker(date: str) -> bool:
    if re.search(r'^\d{2}\-\d{2}\-\d{4}\s\d{2}\:\d{2}$', date):
        return True
    
    return False