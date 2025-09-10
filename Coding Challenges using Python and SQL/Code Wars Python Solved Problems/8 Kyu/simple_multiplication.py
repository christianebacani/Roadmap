# Question: Simple multiplication
# Categories: 8 Kyu

def simple_multiplication(number: int) -> int:
    if number % 2 == 0:
        return number * 8

    return number * 9