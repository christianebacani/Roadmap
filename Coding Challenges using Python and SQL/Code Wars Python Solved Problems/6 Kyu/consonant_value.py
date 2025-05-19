# Question: Consonant value
# Categories: 6 Kyu

def solve(characters: str) -> int:
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiou'

    for i in range(len(vowels)):
        characters = characters.replace(vowels[i], ' ')
    
    characters = characters.split()
    consonant_values = []

    for i in range(len(characters)):
        word = characters[i]
        
        consonant_value = 0

        for j in range(len(word)):
            consonant_value+= (alphabets.index(word[j]) + 1)

        consonant_values.append(consonant_value)

    return max(consonant_values)