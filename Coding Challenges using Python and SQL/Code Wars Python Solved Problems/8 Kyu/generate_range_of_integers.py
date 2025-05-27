# Question: Generate range of integers
# Categories: 8 Kyu

def generate_range(start: int, stop: int, step: int) -> list[int]:
    return [num for num in range(start, stop + 1, step)]