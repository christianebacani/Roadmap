# Question: Factorial
# Categories: 7 Kyu

def factorial(n: int) -> int:
    if n < 0 or n > 12:
        raise ValueError

    total = 1
    
    for i in range(n, 0, -1):
        total *= i

    return total