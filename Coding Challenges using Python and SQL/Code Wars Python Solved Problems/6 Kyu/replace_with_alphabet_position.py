# Question: Replace With Alphabet Position
# Categories: 6 Kyu

def alphabet_position(text: str) -> str:
    result = []
    alphabets = 'abcdefghijklmnopqrstuvwxyz'

    for i in range(len(text)):
        if text[i].lower() not in alphabets:
            continue

        result.append(str(alphabets.index(text[i].lower()) + 1))

    result = ' '.join(result)

    return result