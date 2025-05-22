# Question: Decoding a message
# Categories: 7 Kyu

def decode(message: str) -> str:
    decoded_characters = {
        'a': 'z',
        'b': 'y',
        'c': 'x',
        'd': 'w',
        'e': 'v',
        'f': 'u',
        'g': 't',
        'h': 's',
        'i': 'r',
        'j': 'q',
        'k': 'p',
        'l': 'o',
        'm': 'n',
        'n': 'm',
        'o': 'l',
        'p': 'k',
        'q': 'j',
        'r': 'i',
        's': 'h',
        't': 'g',
        'u': 'f',
        'v': 'e',
        'w': 'd',
        'x': 'c',
        'y': 'b',
        'z': 'a'
    }
    decoded_message = []

    for i in range(len(message)):
        if not message[i].isalpha():
            decoded_message.append(message[i])
        
        else:
            decoded_message.append(decoded_characters[message[i]])
    
    return ''.join(decoded_message)