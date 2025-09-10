# Question: Complete The Pattern #4
# Categories: 7 Kyu

def pattern(n: int) -> str:
    result = []
    
    for i in range(1, n + 1):
        answer = ''

        for j in range(i, n + 1):
            answer += str(j)

        result.append(answer)

    result = '\n'.join(result)
    return result