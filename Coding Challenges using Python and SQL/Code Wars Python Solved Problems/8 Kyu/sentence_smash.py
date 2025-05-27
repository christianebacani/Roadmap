# Question: Sentence Smash
# Categories: 8 Kyu

def smash(words: list[str]) -> str:
    if words == []:
        return ''

    return ' '.join(words)