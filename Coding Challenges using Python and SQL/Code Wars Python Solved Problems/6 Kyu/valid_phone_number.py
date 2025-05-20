# Question: Valid Phone Number
# Categories: 6 Kyu
import re

def valid_phone_number(phone_number: str) -> bool:
    if re.search(r'^\(\d{3}\)\s\d{3}\-\d{4}$', phone_number):
        return True
    
    return False