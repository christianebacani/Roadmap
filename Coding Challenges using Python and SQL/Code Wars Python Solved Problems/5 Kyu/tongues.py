# Question: Tongues
# Categories: 5 Kyu

def tongues(code: str) -> str:
    vowels = 'aiyeou'
    consonants = 'bkxznhdcwgpvjqtsrlmf'
    decode = []

    for i in range(len(code)):
        if not code[i].isalpha():
            decode.append(code[i])
            continue

        if code[i].isupper():
            vowels = vowels.upper()
            consonants = consonants.upper()
        
        else:
            vowels = vowels.lower()
            consonants = consonants.lower()

        if code[i] in vowels and vowels.index(code[i]) + 3 > len(vowels) - 1:
            decode.append(vowels[(vowels.index(code[i]) + 3) - len(vowels)])
        
        elif code[i] in vowels and vowels.index(code[i]) + 3 <= len(vowels) - 1:
            decode.append(vowels[vowels.index(code[i]) + 3])
        
        elif code[i] in consonants and consonants.index(code[i]) + 10 > len(consonants) - 1:
            decode.append(consonants[(consonants.index(code[i]) + 10) - len(consonants)])
        
        else:
            decode.append(consonants[consonants.index(code[i]) + 10])
    
    return ''.join(decode)