# Question: Complete The Pattern #6 - Odd Ladder
# Categories: 7 Kyu

def pattern(n: int) -> str:
    result = []

    for i in range(1, n + 1):
        if i % 2 == 0:
            continue

        result.append(str(i) * i)
    
    result = '\n'.join(result)
    return result