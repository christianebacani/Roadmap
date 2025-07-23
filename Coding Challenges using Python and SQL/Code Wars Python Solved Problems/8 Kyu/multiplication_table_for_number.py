# Question: Multiplication table for number
# Categories: 8 Kyu

def multi_table(number: int) -> str:
    result = ''

    for i in range(1, 11):
        if i != 10:
            result += f'{i} * {number} = {i * number}\n'
        
        else:
            result += f'{i} * {number} = {i * number}'

    return result