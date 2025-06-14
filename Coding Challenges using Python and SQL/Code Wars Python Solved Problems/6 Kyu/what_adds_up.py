# Question: What adds up
# Categories: 6 Kyu

def addsup(a1: list[int], a2: list[int], a3: list[int]) -> list[list[int]]:
    result = []

    for i in range(len(a1)):
        for j in range(len(a2)):
            if a1[i] + a2[j] in a3:
                result.append([a1[i], a2[j], a1[i] + a2[j]])
    
    return result