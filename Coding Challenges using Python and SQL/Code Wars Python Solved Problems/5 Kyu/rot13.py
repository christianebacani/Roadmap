# Question: ROT13
# Categories: 5 Kyu

def rot13(message: str) -> str:
    rot13_decryption = {
        'a':'n', 'b': 'o', 'c': 'p',
        'd': 'q', 'e': 'r', 'f': 's',
        'g': 't', 'h': 'u', 'i': 'v',
        'j': 'w', 'k': 'x', 'l': 'y',
        'm': 'z', 'n': 'a', 'o': 'b',
        'p': 'c', 'q': 'd', 'r': 'e',
        's': 'f', 't': 'g', 'u': 'h',
        'v': 'i', 'w': 'j', 'x': 'k',
        'y': 'l', 'z': 'm'
    }
    descrypted_message = ''

    for i in range(len(message)):
        if not message[i].isalpha():
            descrypted_message += message[i]
            continue

        if message[i].isupper():
            descrypted_message += rot13_decryption[message[i].lower()].upper()
        
        else:
            descrypted_message += rot13_decryption[message[i]]
    
    return descrypted_message