# Question: Magic Sums of 3s
# Categories: 7 Kyu

def magic_sum(arr: list[int]) -> int:
    total = 0

    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            continue

        if '3' in str(arr[i]):
            total += arr[i]
    
    return total