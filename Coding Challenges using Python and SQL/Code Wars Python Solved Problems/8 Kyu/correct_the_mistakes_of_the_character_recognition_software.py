# Question: Correct the mistakes of the character recognition software
# Categories: 8 Kyu

def correct(s: str) -> str:
    misinterpreted_characters = {
        '5': 'S',
        '0': 'O',
        '1': 'I'
    }

    for misinterpreted_char, interpreted_char in misinterpreted_characters.items():
        s = s.replace(misinterpreted_char, interpreted_char)

    return s