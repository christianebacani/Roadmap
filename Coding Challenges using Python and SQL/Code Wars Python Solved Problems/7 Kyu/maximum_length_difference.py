# Question: Maximum Length Difference
# Categories: 7 Kyu

def mxdiflg(a1: list[str], a2: list[str]) -> int:
    if a1 == [] or a2 == []:
        return -1
    
    absolute_differences = []

    for i in range(len(a1)):
        for j in range(len(a2)):
            absolute_differences.append(abs(len(a1[i]) - len(a2[j])))
    
    return max(absolute_differences)