# Question: Sum of prime-indexed elements
# Categories: 6 Kyu

def total(arr: list[int]) -> int:
    elements_with_prime_indices = []

    for i in range(len(arr)):
        if i <= 1:
            continue
        
        if i == 2:
            elements_with_prime_indices.append(arr[i])
            continue

        prime = True

        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
        
        if prime:
            elements_with_prime_indices.append(arr[i])
    
    return sum(elements_with_prime_indices)