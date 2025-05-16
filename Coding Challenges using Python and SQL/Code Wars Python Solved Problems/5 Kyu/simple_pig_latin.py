# Question: Simple Pig Latin
# Categories: 5 Kyu

def pig_it(text: str) -> str:
    text = text.split()

    for i in range(len(text)):
        if not text[i].isalpha():
            continue

        text[i] = text[i][1:] + text[i][0] + 'ay'

    text = ' '.join(text)

    return text