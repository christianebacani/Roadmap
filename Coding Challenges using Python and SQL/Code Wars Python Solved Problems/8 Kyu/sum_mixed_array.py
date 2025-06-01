# Question: Sum Mixed Array
# Categories: 8 Kyu

def sum_mix(arr: list[int | str]) -> int:
    return sum([int(num) for num in arr])