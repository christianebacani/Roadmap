# Question: Find Maximum and Minimum Values of a List
# Categories: 8 Kyu

def minimum(arr: list[int]) -> int:
    return min(arr, default=0)

def maximum(arr: list[int]) -> int:
    return max(arr, default=0)