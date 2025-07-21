# Question: Love vs friendship
# Categories: 7 Kyu

def words_to_marks(s: str) -> int:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    total_value = 0

    for i in range(len(s)):
        total_value += (alphabet.index(s[i]) + 1)

    return total_value