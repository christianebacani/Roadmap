# Question: Remove Unnecesasary Characters from Items in List
# Categories: 7 Kyu

def remove_char(array: list[str]) -> list[str]:
    for i in range(len(array)):
        result = ''

        for j in range(len(array[i])):
            if array[i][j].isdigit():
                result += array[i][j]
        
        result = list(result)
        result.insert(0, '$')
        result.insert(-2, '.')
        result = ''.join(result)

        array[i] = result
    
    return array