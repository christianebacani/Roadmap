# Question: Find the capitals
# Categories: 7 Kyu

def capitals(word: str) -> list[int]:
    result = []

    for i in range(len(word)):
        if word[i].isupper():
            result.append(i)
    
    return result