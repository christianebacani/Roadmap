# Question: Digits explosion
# Categories: 7 Kyu

def explode(s: str) -> str:
    result = ''

    for i in range(len(s)):
        if s[i] == '0':
            continue

        result += (s[i] * int(s[i]))
    
    return result