# Question: Check for prime numbers
# Categories: 7 Kyu

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True