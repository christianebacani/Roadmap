# Question: Nice Array
# Categories: 7 Kyu

def is_nice(arr: list[int]) -> bool:
    if arr == []:
        return False

    for i in range(len(arr)):
        if arr[i] - 1 not in arr and arr[i] + 1 not in arr:
            return False
    
    return True