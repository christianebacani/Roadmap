# Question: Lario and Muigi Pipe Problem
# Categories: 8 Kyu

def pipe_fix(arr: list[int]) -> list[int]:
    return [num for num in range(min(arr), max(arr) + 1)]