# Question: Palindromes Here and There
# Categories: 7 Kyu

def convert_palindromes(numbers: list[int]) -> list[int]:
    return [1 if str(num) == str(num)[::-1] else 0 for num in numbers]