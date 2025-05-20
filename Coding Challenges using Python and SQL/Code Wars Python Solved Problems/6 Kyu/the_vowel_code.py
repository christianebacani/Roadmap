# Question: The Vowel Code
# Categories: 6 Kyu

def encode(characters: str) -> str:
    encoded_characters = {
        'a': '1',
        'e': '2',
        'i': '3',
        'o': '4',
        'u': '5'
    }
    
    for character, encoded_character in encoded_characters.items():
        characters = characters.replace(character, encoded_character)

    return characters

def decode(encrypted_text: str) -> str:
    decoded_characters = {
        '1': 'a',
        '2': 'e',
        '3': 'i',
        '4': 'o',
        '5': 'u'
    }

    for character, decoded_character in decoded_characters.items():
        encrypted_text = encrypted_text.replace(character, decoded_character)
    
    return encrypted_text