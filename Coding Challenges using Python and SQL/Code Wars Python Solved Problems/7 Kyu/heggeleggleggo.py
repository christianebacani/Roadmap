# Question: heggeleggleggo
# Categories: 7 Kyu

def heggeleggleggo(word: str) -> str:
    consonants = 'bcdfghjklmnpqrstvwxyz'
    result = ''
    
    for i in range(len(word)):
        if word[i].lower() in consonants:
            result += (word[i] + 'egg')
        
        else:
            result += word[i]
    
    return result