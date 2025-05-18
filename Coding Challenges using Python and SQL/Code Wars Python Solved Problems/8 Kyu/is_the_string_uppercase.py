# Question: Is the string uppercase?
# Categories: 8 Kyu

def is_uppercase(words: str) -> bool:
    for i in range(len(words)):
        if words[i].islower():
            return False
    
    return True