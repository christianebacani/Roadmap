# Question: Simple Fun #20: First Reverse Try
# Categories: 7 Kyu

def first_reverse_try(arr: list[int]) -> list[int]:
    if arr == []:
        return []

    first_element = arr[0]
    last_element = arr[-1]
    arr[0] = last_element
    arr[-1] = first_element

    return arr