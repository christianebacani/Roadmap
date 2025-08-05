# Question: Sort by Last Char
# Categories: 7 Kyu

def last(s: str) -> list[str]:
    s = s.split()
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    result = []

    for i in range(len(alphabets)):
        for j in range(len(s)):
            if alphabets[i] == s[j][-1]:
                result.append(s[j])

    return result