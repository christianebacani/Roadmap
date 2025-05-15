# Question: Sum of two lowest positive integers
# Categories: 7 Kyu

def sum_two_smallest_numbers(numbers: list[int]) -> int:
    numbers = sorted(numbers)
    
    return numbers[0] + numbers[1]