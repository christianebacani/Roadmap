# Question: Largest Elements
# Categories: 7 Kyu

def largest(n: int, xs: list[int]) -> list[int]:
    xs.sort()
    xs.reverse()
    result = xs[:n]
    result.reverse()

    return result