# Question: V A P O R C O D E
# Categories: 7 Kyu

def vaporcode(s: str) -> str:
    result = []

    for i in range(len(s)):
        if s[i] != ' ':
            result.append(s[i].upper())
    
    result = '  '.join(result)
    return result