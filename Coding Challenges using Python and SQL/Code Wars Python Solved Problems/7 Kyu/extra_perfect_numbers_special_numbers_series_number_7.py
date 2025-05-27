# Question: Extract Perfect Numbers (Special Numbers Series #7)
# Categories: 7 Kyu

def extra_perfect(n: int) -> list[int]:
    return [num for num in range(1, n + 1) if bin(num)[2:][0] == '1' and bin(num)[2:][-1] == '1']