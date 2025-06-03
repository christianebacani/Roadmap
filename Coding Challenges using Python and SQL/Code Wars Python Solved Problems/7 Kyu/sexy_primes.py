# Question: Sexy Primes <3
# Categories: 7 Kyu

def is_prime(number : int) -> bool:
    if number == 1:
        return False
    
    elif number == 2:
        return True
    
    else:
        pass

    for i in range(2, number):
        if number % i == 0:
            return False
    
    return True

def sexy_prime(x: int, y: int) -> bool:
    if is_prime(x) and is_prime(y) and abs(x - y) == 6:
        return True
    
    return False