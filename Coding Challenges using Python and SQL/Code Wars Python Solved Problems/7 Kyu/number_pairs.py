# Question: Number Pairs
# Categories: 7 Kyu

def get_larger_numbers(a: list[int], b: list[int]) -> list[int]:
    return [max([a[i], b[i]]) for i in range(len(a))]