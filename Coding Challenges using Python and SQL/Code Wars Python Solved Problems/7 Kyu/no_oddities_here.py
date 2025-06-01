# Question: No oddities here
# Categories: 7 Kyu

def no_odds(values: list[int]) -> list[int]:
    return [num for num in values if num % 2 == 0]