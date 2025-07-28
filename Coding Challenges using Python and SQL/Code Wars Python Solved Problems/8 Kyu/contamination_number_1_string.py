# Question: Contamination #1 -String-
# Categories: 8 Kyu

def contamination(text: str, char: str) -> str:
    if text == '' or char == '':
        return ''

    result = ''

    for _ in range(len(text)):
        result += char
    
    return result