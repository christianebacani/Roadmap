# Question: Merging sorted integer arrays (without duplicates)
# Categories: 8 Kyu

def merge_arrays(first: list[int], second: list[int]) -> list[int]: 
    result = first + second
    new_result = []

    for i in range(len(result)):
        if isinstance(result[i], int):
            new_result.append(result[i])
    
    result = list(set(new_result))
    result.sort()

    return result