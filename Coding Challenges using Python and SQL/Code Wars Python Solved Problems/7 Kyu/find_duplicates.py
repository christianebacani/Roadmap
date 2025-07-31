# Question: Find Duplicates
# Categories: 7 Kyu

def duplicates(arr: list[int] | str) -> list[int | str]:
    result = []

    for i in range(len(arr)):
        if arr.count(arr[i]) == 1:
            continue

        if arr[i] in arr[:i] and arr[i] not in result:
            result.append(arr[i])
    
    return result