# Question: Ordered Count of Characters
# Categories: 7 Kyu

def ordered_count(inp: str) -> str:
    char_frequencies = {}

    for i in range(len(inp)):
        if inp[i] in char_frequencies:
            continue

        char_frequencies[inp[i]] = inp.count(inp[i])
    
    result = []

    for key, value in char_frequencies.items():
        result.append(tuple([key, value]))
    
    return result