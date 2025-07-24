# Question: Sum of Minimums!
# Categories: 7 Kyu

def sum_of_minimums(numbers: list[list[int]]) -> int:
    total = 0

    for i in range(len(numbers)):
        total += min(numbers[i], default=0)

    return total