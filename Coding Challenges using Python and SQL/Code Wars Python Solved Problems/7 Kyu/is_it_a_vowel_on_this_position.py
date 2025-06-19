# Question: Is it a vowel on this position?
# Categories: 7 Kyu

def check_vowel(strng: str, position: int) -> bool:
    if (position < 0) or (position > len(strng) - 1):
        return False
    
    if strng[position].lower() in 'aeiou':
        return True
    
    return False