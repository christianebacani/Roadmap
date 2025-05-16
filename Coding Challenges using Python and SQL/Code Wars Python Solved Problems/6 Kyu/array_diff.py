# Question: Array.diff
# Categories: 6 Kyu

def array_diff(a: list[int], b: list[int]) -> list[int]:
    answer = []

    for i in range(len(a)):
        if a[i] in b:
            continue

        answer.append(a[i])
    
    return answer