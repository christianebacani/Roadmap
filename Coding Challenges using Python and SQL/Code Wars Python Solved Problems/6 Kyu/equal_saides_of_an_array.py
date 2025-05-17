# Question: Equal Sides of An Array
# Categories: 6 Kyu

def find_even_index(arr: list[int]) -> int:
    for i in range(len(arr)):
        left_side_sum = sum(arr[:i])
        right_side_sum = sum(arr[i + 1:])

        if left_side_sum == right_side_sum:
            return i
    
    return -1