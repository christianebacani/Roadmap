# Question: Sort and Star
# Categories: 8 Kyu

def two_sort(arr: list[str]) -> str:
    first_value = sorted(arr)[0]
    result = []
    
    for i in range(len(first_value)):
        result.append(first_value[i])
    
    return '***'.join(result)