# Question: Change it up
# Categories: 6 Kyu

def changer(s: str) -> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiou'
    result = ''
    
    for i in range(len(s)):
        if not s[i].isalpha():
            result += s[i]
            continue

        target_index = alphabet.index(s[i].lower()) + 1
        
        if target_index <= 25:
            target_letter = alphabet[target_index]

        else:
            target_letter = alphabet[(target_index % 25) - 1]
        
        if target_letter.lower() in vowels:
            result += target_letter.upper()
        
        else:
            result += target_letter.lower()
    
    return result