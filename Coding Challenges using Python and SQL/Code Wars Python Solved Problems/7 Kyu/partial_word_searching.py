# Question: Partial Word Searching
# Categories: 7 Kyu

def word_search(query: str, sequence: list[str]) -> list[str]:
    result = []

    for i in range(len(sequence)):
        if query.lower() in sequence[i].lower():
            result.append(sequence[i])
    
    if result == []:
        return ['None']

    return result