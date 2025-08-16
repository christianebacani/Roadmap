# Question: Odder Than the Rest
# Categories: 7 Kyu

def odd_one(arr: list[int]) -> int:
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            return i
    
    return -1