# Question: Figurate Numbers #2 - Pronic Number
# Categories: 7 Kyu

def is_pronic(n: int) -> bool:
    if n < 0:
        return False
    
    if n == 0:
        return True
    
    for number in range(n + 1):
        if (number * (number + 1)) == n:
            return True

        if (number * (number - 1))  == n:
            return True
    
    return False