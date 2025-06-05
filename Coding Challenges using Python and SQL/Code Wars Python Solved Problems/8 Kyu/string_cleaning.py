# Question: String cleaning
# Categories: 8 Kyu

def string_clean(s: str) -> str:
    """
    Function will return the cleaned string
    """
    result = ''

    for i in range(len(s)):
        if not s[i].isdigit():
            result += s[i]
    
    return result