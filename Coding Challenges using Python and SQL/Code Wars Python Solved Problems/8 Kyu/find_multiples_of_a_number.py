# Question: Find Multiples of a Number
# Categories: 8 Kyu

def find_multiples(integer: int, limit: int) -> list[int]:
    return [i for i in range(integer, limit + 1) if i % integer == 0]