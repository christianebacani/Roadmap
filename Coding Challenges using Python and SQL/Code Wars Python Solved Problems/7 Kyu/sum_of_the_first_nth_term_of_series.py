# Question: Sum of the first nth term of Series
# Categories: 7 Kyu

def series_sum(n: int) -> str:
    if n == 0:
        return '0.00'

    total = 0

    for index, denominator in enumerate(range(1, 1001, 3)):
        total += (1 / denominator)
        index += 1

        if index == n:
            break
    
    return f'{total:.2f}'