# Question: WeIrD StRiNg CaSe
# Categories: 6 Kyu

def to_weird_case(words: str) -> str:
    words = words.split()
    
    for i in range(len(words)):
        word = list(words[i])

        for j in range(len(word)):
            if j % 2 == 0:
                word[j] = word[j].upper()
            
            else:
                word[j] = word[j].lower()
        
        words[i] = ''.join(word)
    
    return ' '.join(words)