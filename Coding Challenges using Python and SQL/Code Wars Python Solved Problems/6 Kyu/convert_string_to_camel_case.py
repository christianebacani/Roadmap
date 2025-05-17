# Question: Convert string to camel case
# Categories: 6 Kyu

def to_camel_case(text: str) -> str:
    delimiters = '-_'
    
    for i in range(len(delimiters)):
        text = text.replace(delimiters[i], ' ')
    
    text = text.split()

    for i in range(len(text)):
        if (i != 0) or (text[i][0].isupper()):
            text[i] = text[i].capitalize()
    
    text = ''.join(text)

    return text