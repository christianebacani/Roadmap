# Question: Pull your words together, man!
# Categories: 7 Kyu

def sentencify(words: list[str]) -> str:
    for i in range(len(words)):
        if i != 0:
            break
        
        if words[i].isupper():
            continue

        words[i] = words[i].capitalize()
    
    words = ' '.join(words) + '.'
    return words