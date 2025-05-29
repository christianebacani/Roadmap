# Question: Calculate average
# Categories: 8 Kyu

def find_average(numbers: list[int]) -> int | float:
    try:
        return sum(numbers) / len(numbers)
    
    except ZeroDivisionError:
        return 0