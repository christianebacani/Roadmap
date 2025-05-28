# Question: Search for letters
# Categories: 7 Kyu

def change(st: str) -> str:
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    for i in range(len(alphabets)):
        if alphabets[i].lower() in st or alphabets[i].upper() in st:
            result += '1'
        
        else:
            result += '0'
    
    return result