# Question: Ones and Zeros
# Categories: 7 Kyu

def binary_array_to_number(arr: list[int]) -> int:
    arr = [str(num) for num in arr]
    binary_value = ''.join(arr)
    return int(binary_value, base=2)