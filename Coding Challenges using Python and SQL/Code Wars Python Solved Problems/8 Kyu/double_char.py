# Question: Double Char
# Categories: 8 Kyu

def double_char(s: str) -> str:
    result = ''

    for i in range(len(s)):
        result += (s[i] * 2)
    
    return result