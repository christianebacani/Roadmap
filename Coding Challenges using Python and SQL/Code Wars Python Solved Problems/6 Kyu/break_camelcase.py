# Question: Break camelCase
# Categories: 6 Kyu

def solution(s: str) -> str:
    result = ''

    for i in range(len(s)):
        if s[i].isupper():
            result += ' '
            result += s[i]
        
        else:
            result += s[i]
    
    return result