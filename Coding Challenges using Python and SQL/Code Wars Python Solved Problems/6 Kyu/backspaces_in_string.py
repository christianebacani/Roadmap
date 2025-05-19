# Question: Backspaces in string
# Categories: 6 Kyu

def clean_string(characters: str) -> str:
    result = []

    for i in range(len(characters)):
        if characters[i] == '#':
            result = result[:-1]
        
        else:
            result.append(characters[i])
    
    return ''.join(result)