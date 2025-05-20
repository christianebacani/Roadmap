# Question: Vowel Shifting
# Categories: 6 Kyu

def extracting_vowels_and_shifting(characters: str, shift: int) -> str:
    vowels = ''

    for i in range(len(characters)):
        if characters[i].lower() in ['a', 'e', 'i', 'o', 'u']:
            vowels += characters[i]
    
    if vowels == '':
        return vowels

    if shift < 0:
        shift = abs(shift)
        initial_shift = 0

        while initial_shift < shift:
            vowels = vowels[1:] + vowels[0]
            initial_shift += 1
    
    else:
        initial_shift = 0

        while initial_shift < shift:
            vowels = vowels[-1] + vowels[:-1]
            initial_shift += 1
    
    return vowels

def vowel_shift(text: str, number_of_shifts: int) -> str | None:
    if text is None:
        return None
    
    if text == '':
        return ''
    
    if number_of_shifts == 0:
        return text
    
    vowels_shifted = extracting_vowels_and_shifting(text, number_of_shifts)
    
    if vowels_shifted == '':
        return text

    text = list(text)

    for i in range(len(text)):
        if text[i].lower() in ['a', 'e', 'i', 'o', 'u']:
            text[i] = vowels_shifted[0]
            vowels_shifted = vowels_shifted[1:]
    
    return ''.join(text)