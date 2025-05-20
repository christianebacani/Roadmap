# Question: Pyramid Array
# Categories: 6 Kyu

def pyramid(n: int) -> list[list[int]]:
    if n == 0:
        return []
    
    result = []

    for i in range(1, n + 1):
        row = []

        for _ in range(i):
            row.append(1)
        
        result.append(row)
    
    return result