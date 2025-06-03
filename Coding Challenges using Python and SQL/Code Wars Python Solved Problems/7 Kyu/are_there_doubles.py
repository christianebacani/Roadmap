# Question: Are there doubles?
# Categories: 7 Kyu

def double_check(strng: str) -> bool:
    for i in range(1, len(strng)):
        if strng[i - 1].lower() == strng[i].lower():
            return True
    
    return False