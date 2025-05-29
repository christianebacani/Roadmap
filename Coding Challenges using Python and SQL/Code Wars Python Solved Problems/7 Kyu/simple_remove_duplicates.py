# Question: Simple remove duplicates
# Categories: 7 Kyu

def solve(arr: list[int]) -> list[int]: 
    arr = arr[::-1]
    result = []

    for i in range(len(arr)):
        if arr[i] not in result:
            result.append(arr[i])
    
    return result[::-1]