# Question: Sum of Multiples
# Categories: 8 Kyu

def sum_mul(n: int, m: int) -> int | str:
    if n <= 0 or m <= 0:
        return 'INVALID'

    list_of_multiples_of_n = []

    for number in range(1, m):
        if number % n == 0:
            list_of_multiples_of_n.append(number)

    return sum(list_of_multiples_of_n)