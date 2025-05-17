# Question: Count the number of divisors of a positive integer n
# Categories: 7 Kyu

def divisors(n: int) -> int:
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    
    return count