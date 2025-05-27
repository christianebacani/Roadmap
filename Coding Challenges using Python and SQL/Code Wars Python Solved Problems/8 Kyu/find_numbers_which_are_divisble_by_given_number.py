# Question: Find numbers which are divisible by given number
# Categories: 8 Kyu

def divisible_by(numbers: list[int], divisor: int) -> list[int]:
    return [num for num in numbers if num % divisor == 0]