# Question: Shortest Word
# Categories: 7 Kyu

def find_short(s: str) -> int:
    s = s.split()
    list_of_word_length = []

    for i in range(len(s)):
        list_of_word_length.append(len(s[i]))

    return min(list_of_word_length, default=0)