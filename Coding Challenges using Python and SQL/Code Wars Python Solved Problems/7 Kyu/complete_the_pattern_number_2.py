# Question: Complete The Pattern #2
# Categories: 7 Kyu

def pattern(n: int) -> str:
    if n <= 0:
        return ''

    answer = []
    
    for i in range(1, n + 1):
        result = ''

        for j in range(i, n + 1):
            result = str(j) + result
        
        answer.append(result)
    
    answer = '\n'.join(answer)
    return answer