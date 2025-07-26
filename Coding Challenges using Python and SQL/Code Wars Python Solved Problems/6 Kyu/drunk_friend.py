# Question: Drunk friend
# Categories: 6 Kyu

def decode(string_: str | int | float | bool) -> str:
    if not isinstance(string_, str):
        return 'Input is not a string'
    
    result = ''
    # A  B  C  D  E  F  G  H  I  J  K  L  M
    # Z  Y  X  W  V  U  T  S  R  Q  P  O  N
    
    decoded_characters = {
        'A': 'Z',
        'B': 'Y',
        'C': 'X',
        'D': 'W',
        'E': 'V',
        'F': 'U',
        'G': 'T',
        'H': 'S',
        'I': 'R',
        'J': 'Q',
        'K': 'P',
        'L': 'O',
        'M': 'N',
        'N': 'M', 
        'O': 'L',
        'P': 'K',
        'Q': 'J',
        'R': 'I',
        'S': 'H',
        'T': 'G',
        'U': 'F',
        'V': 'E',
        'W': 'D',
        'X': 'C',
        'Y': 'B',
        'Z': 'A'
    }

    for i in range(len(string_)):
        if not string_[i].isalpha():
            result += string_[i]
            continue

        if string_[i].islower():
            result += decoded_characters[string_[i].upper()].lower()

        else:
            result += decoded_characters[string_[i]]

    return result