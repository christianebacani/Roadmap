# Question: Find twins
# Categories: 8 Kyu

def elimination(arr: list[int]) -> int | None:
    if arr == []:
        return None
    
    for i in range(len(arr)):
        if arr.count(arr[i]) == 2:
            return arr[i]

    return None