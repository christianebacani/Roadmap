# Question: Square(n) Sum
# Categories: 8 Kyu

def square_sum(numbers: list[int]) -> int:
    total = 0

    for i in range(len(numbers)):
        total += (numbers[i] ** 2)
    
    return total