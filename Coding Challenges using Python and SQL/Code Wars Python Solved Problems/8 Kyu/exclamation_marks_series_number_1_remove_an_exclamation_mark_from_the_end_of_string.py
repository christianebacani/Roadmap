# Question: Exclamation marks series #1: Remove an exclamation mark from the end of string
# Categories: 8 Kyu

def remove(word: str) -> str:
    try:
        if word[-1] == '!':
            return word[:-1]

        return word
    
    except:
        return word