# Question: Decipher this!
# Categories: 6 Kyu

def decipher_this(text: str) -> str:
    decrypted_text = []
    text = text.split()

    for i in range(len(text)):
        word = text[i]

        decrypted_word = []
        unicode_value = []
        character_value = []

        for j in range(len(word)):
            if word[j].isnumeric():
                unicode_value.append(word[j])
            
            else:
                character_value.append(word[j])

        unicode_value = int(''.join(unicode_value))
        unicode_value = chr(unicode_value)
        decrypted_word.append(unicode_value)

        for j in range(len(character_value)):
            if j == 0:
                decrypted_word.append(character_value[-1])
            
            elif j == len(character_value) - 1:
                decrypted_word.append(character_value[0])
            
            else:
                decrypted_word.append(character_value[j])

        decrypted_text.append(''.join(decrypted_word))
    
    return ' '.join(decrypted_text)