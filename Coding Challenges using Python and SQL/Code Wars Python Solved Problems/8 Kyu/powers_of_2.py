# Question: Powers of 2
# Categories: 8 Kyu

def powers_of_two(n: int) -> list[int]:
    result = []

    for exponent in range(n + 1):
        result.append(2 ** exponent)
    
    return result