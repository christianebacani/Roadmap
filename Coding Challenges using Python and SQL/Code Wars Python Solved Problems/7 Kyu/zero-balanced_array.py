# Question: zero-balanced Array
# Categories: 7 Kyu

def is_zero_balanced(arr: list[int]) -> bool:
    if sum(arr) != 0 or arr == []:
        return False
    
    for i in range(len(arr)):
        if arr[i] == 0:
            continue

        if arr[i] * -1 not in arr:
            return False

    return True