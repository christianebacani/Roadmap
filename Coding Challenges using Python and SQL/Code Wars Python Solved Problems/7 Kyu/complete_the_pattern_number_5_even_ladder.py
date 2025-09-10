# Question: Complete The Pattern #5 - Even Ladder
# Categories: 7 Kyu

def pattern(n: int) -> str:
    if n == 0:
        return ''
    
    result = []

    for i in range(1, n + 1):
        if i % 2 != 0:
            continue

        result.append(str(i) * i)
    
    result = '\n'.join(result)
    return result