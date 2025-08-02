# Question: Sum of Cubes
# Categories: 7 Kyu

def sum_cubes(n: int) -> int:
    total = 0
    
    for i in range(1, n + 1):
        total += (i ** 3)

    return total