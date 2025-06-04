# Question: Find the position!
# Categories: 8 Kyu

def position(letter: str) -> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = 'Position of alphabet: ' + str(alphabet.index(letter) + 1)

    return result