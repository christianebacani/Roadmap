# Question: Thinkful - List and Loop Drills: Inverse Slicer
# Categories: 7 Kyu

def inverse_slice(items: list[int], a: int, b: int) -> list[int]:
    result = items[:a] + items[b:]

    return result