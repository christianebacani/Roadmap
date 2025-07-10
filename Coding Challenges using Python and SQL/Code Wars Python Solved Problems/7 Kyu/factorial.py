# Question: Factorial
# Categories: 7 Kyu

def factorial(n: int) -> int:
    total = 1

    for i in range(1, n + 1):
        total *= i
    
    return total