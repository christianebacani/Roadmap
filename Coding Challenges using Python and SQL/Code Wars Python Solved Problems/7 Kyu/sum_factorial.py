# Question: Sum Factorial
# Categories: 7 Kyu

def sum_factorial(lst: list[int]) -> int:
    factorial = []

    for i in range(len(lst)):
        number = lst[i]
        total = 1

        for j in range(1, number + 1):
            total *= j
        
        factorial.append(total)
    
    return sum(factorial)