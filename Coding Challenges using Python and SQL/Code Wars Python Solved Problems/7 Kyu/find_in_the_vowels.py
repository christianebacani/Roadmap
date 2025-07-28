# Question: Find the vowels
# Categories: 7 Kyu

def vowel_indices(word: str) -> list[int]:
    result = []
    vowels = 'aeiouy'

    for i in range(len(word)):
        if word[i].lower() in vowels:
            result.append(i + 1)
    
    return result