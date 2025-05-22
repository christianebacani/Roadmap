# Question: Collatz Conjecture (3n+1)
# Categories: 8 Kyu

def hotpo(n: int) -> int:
    steps = 0

    while n != 1:
        steps += 1
        
        if n % 2 == 0:
            n = n // 2
        
        else:
            n = (3 * n) + 1

    return steps