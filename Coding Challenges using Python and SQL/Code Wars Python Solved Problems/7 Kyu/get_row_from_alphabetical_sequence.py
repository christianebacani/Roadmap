# Question: Get row from alphabetical sequence
# Categories: 7 Kyu

def get_row(n: int) -> str:
    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_sequence = []

    for i in range(len(alphabets)):
        current_letter = alphabets[i]
        next_letters = alphabets[i + 1:]

        alphabet_sequence.append((current_letter * (i + 1)) + next_letters)
    
    if n <= 26:
        return alphabet_sequence[n - 1]

    else:
        return alphabet_sequence[(n % 26) - 1]