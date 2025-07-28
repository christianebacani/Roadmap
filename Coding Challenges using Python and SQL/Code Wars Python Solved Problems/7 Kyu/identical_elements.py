# Question: Identical Elements
# Categories: 7 Kyu

def duplicate_elements(m: list[int], n: list[int]) -> bool:
    for i in range(len(m)):
        if m[i] in n:
            return True
    
    return False