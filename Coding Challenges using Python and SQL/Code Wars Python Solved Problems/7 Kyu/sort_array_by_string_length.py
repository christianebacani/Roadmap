# Question: Sort array by string length
# Categories: 7 Kyu

def sort_by_length(arr: list[str]) -> list[str]:
    characters_and_length = {}

    for i in range(len(arr)):
        characters_and_length[arr[i]] = len(arr[i])
    
    sorted_length = sorted(list(characters_and_length.values()))
    result = []

    for i in range(len(sorted_length)):
        for characters, length in characters_and_length.items():
            if sorted_length[i] == length:
                result.append(characters)
    
    return result