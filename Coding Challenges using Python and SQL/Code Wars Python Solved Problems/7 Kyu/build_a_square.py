# Question: Build a square
# Categories: 7 Kyu

def generate_shape(n: int) -> str:
    result = ''

    for i in range(1, n + 1):
        result += ('+' * n)

        if i != n:
            result += '\n'

    return result