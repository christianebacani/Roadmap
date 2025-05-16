# Question: Duplicate Encoder
# Categories: 6 Kyu

def duplicate_encode(word: str) -> str:
    word = word.lower()
    encoded_word = ''

    for i in range(len(word)):
        if word.count(word[i]) == 1:
            encoded_word += '('
        
        else:
            encoded_word += ')'

    return encoded_word