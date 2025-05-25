# Question: Return a string's even characters.
# Categories: 7 Kyu

def even_chars(st: str) -> list[str] | str: 
    if len(st) < 2 or len(st) > 100:
        return 'invalid string'
    
    result = []

    for index, char in enumerate(st):
        index += 1

        if index % 2 == 0:
            result.append(char)

    return result