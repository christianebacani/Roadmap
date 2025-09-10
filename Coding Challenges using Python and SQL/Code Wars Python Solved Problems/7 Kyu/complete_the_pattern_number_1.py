# Question: Complete The Pattern #1
# Categories: 7 Kyu

def pattern(n: int) -> str:
    result = []

    for i in range(1, n + 1):
        result.append(str(i) * i)

    result = '\n'.join(result)
    return result