# Question: Beginner - Reduce but Grow
# Categories: 8 Kyu

def grow(arr: list[int]) -> int:
    product = 1

    for i in range(len(arr)):
        product *= arr[i]

    return product