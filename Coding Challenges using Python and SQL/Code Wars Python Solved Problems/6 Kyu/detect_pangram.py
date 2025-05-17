# Question: Detect Pangram
# Categories: 6 Kyu

def is_pangram(st: str) -> bool:
    alphabets = [
        'a', 'b', 'c', 'd',
        'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p',
        'q', 'r', 's', 't',
        'u', 'v', 'w', 'x',
        'y', 'z'
    ]
    st = list(st.lower())

    for i in range(len(alphabets)):
        if alphabets[i] not in st:
            return False

    return True