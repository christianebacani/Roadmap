# Question: Find all non-consecutive numbers
# Categories: 7 Kyu

def all_non_consecutive(arr: list[int]) -> list[dict[str, int]]:
    result = []
    
    for i in range(len(arr)):
        if i == 0:
            continue

        if arr[i] - arr[i - 1] != 1:
            result.append({'i': i, 'n': arr[i]})
    
    return result