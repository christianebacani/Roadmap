# Question: Grouped by commas
# Categories: 6 Kyu

def group_by_commas(n: int) -> str:
    numbers = str(n)[::-1]
    result = []
    
    while len(numbers) != 0:
        result.append(numbers[:3])
        result.append(',')
        numbers = numbers[3:]
    
    result = ''.join(result)[::-1]

    if result[0] == ',':
        result = result[1:]
    
    return result