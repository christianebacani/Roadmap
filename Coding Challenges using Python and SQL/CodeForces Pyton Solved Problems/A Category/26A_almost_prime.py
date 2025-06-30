# 26A - Almost Prime

def is_number_almost_prime(number: int) -> bool:
    divisors = []

    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    
    total_prime_divisors = 0

    for i in range(len(divisors)):
        if divisors[i] == 1:
            continue

        if divisors[i] == 2:
            total_prime_divisors += 1
            continue
        
        is_prime = True

        for j in range(2, divisors[i]):
            if divisors[i] % j == 0:
                is_prime = False
                break

        if is_prime:
            total_prime_divisors += 1

    return total_prime_divisors == 2
        
n = int(input().strip())
total = 0

for i in range(1, n + 1):
    if is_number_almost_prime(i) is True:
        total += 1

print(total)