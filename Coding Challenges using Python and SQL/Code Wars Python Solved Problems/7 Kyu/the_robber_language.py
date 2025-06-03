# Question: The Robber Language
# Categories: 7 Kyu

def robber_encode(sentence: str) -> str:
    vowels = 'aeiou'
    result = ''

    for i in range(len(sentence)):
        if sentence[i].lower() in vowels or not sentence[i].isalpha():
            result += sentence[i]
            continue

        letter_o = 'o'

        if sentence[i].isupper():
            letter_o = letter_o.upper()
        
        result += (sentence[i] + letter_o + sentence[i])

    return result