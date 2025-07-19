# Question: Merge two sorted arrays into one
# Categories: 8 Kyu

def merge_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    answer = arr1 + arr2
    answer = list(set(answer))
    answer.sort()

    return answer