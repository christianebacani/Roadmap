# Question: If you can't sleep, just count sheep!!
# Categories: 8 Kyu

def count_sheep(number: int) -> str:
    if number == 0:
        return ''
    
    result = ''

    for i in range(1, number + 1):
        result += f'{i} sheep...'
    
    return result