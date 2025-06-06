# Question: Find the divisors!
# Categories: 7 Kyu

def divisors(integer: int) -> list[int] | str:
    number_is_prime = True

    for i in range(2, integer):
        if integer % i == 0:
            number_is_prime = False
            break
    
    if number_is_prime:
        return f'{integer} is prime'
    
    return [num for num in range(2, integer) if integer % num == 0]