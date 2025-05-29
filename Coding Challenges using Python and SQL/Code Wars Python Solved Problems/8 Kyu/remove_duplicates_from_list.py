# Question: Remove duplicates from list
# Categories: 8 Kyu

def distinct(sequence: list[int]) -> list[int]:
    result = []
    
    for i in range(len(sequence)):
        if sequence[i] not in result:
            result.append(sequence[i])
    
    return result