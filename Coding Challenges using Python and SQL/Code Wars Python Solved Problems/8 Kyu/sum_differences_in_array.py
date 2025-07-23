# Question: Sum of differences in array
# Categories: 8 Kyu

def sum_of_differences(arr: list[int]) -> int | None:
    arr.sort()
    arr.reverse()

    if arr == [] or len(arr) == 1:
        return 0

    differences = []

    for i in range(len(arr)):
        if i == len(arr) - 1:
            continue

        differences.append(arr[i] - arr[i + 1])
    
    return sum(differences)