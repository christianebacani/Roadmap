# Question: Is it a letter?
# Categories: 7 Kyu

def is_it_letter(s: str) -> bool:
    letters = 'abcdefghijklmnopqrstuvwxyz'
    
    return s.lower() in letters