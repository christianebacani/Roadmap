# Question: Are we alternate?
# Categories: 6 Kyu

def is_alt(word: str) -> bool:
    vowels = 'aeiou'

    for i in range(1, len(word)):
        previous_char = word[i - 1]
        current_char = word[i]

        if previous_char.lower() not in vowels and current_char.lower() not in vowels:
            return False
        
        if previous_char.lower() in vowels and current_char.lower() in vowels:
            return False
    
    return True