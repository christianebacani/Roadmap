# Question: Nth Smallest Element (Array Series #4)
# Categories: 7 Kyu

def nth_smallest(arr: list[int], position: int) -> int:
    arr.sort()
    return arr[position - 1]