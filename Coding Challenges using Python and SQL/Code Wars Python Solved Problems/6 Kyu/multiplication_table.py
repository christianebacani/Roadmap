# Question: Multiplication table
# Categories: 6 Kyu

def multiplication_table(size: int) -> list[list[int]]:
    results = []

    for i in range(1, size + 1):
        result = []

        for j in range(1, size + 1):
            result.append(i * j)
        
        results.append(result)

    return results