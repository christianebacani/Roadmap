# Question: Count characters in your string
# Categories: 6 Kyu

def count(s: str) -> dict[str, int]:
    char_and_frequencies = {}

    for i in range(len(s)):
        char_and_frequencies[s[i]] = s.count(s[i])

    return char_and_frequencies