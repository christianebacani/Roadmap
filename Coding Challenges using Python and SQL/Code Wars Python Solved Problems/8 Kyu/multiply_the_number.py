# Question: Multiply the number
# Categories: 8 Kyu

def multiply(n: int) -> int:
    return n * (5 ** len(str(n).replace('-', '')))