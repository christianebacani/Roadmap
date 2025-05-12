# Write a function to calculate the sum of all digits in a given number
# Categories: Easy

def sum_of_digits(n: int) -> int:
    n = str(n)
    sum = 0

    for i in range(len(n)):
        sum += int(n[i])
    
    return sum