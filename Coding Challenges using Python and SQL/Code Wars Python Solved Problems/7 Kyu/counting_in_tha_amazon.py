# Question: Counting in the Amazon
# Categories: 7 Kyu

def count_arara(number: int) -> str:
    number_and_arara = {
        1: 'anane',
        2: 'adak',
        3: 'adak anane',
        4:  'adak adak',
        5: 'adak adak anane',
        6: 'adak adak adak',
        7: 'adak adak adak anane',
        8: 'adak adak adak adak'
    }
    
    if number <= 8:
        return number_and_arara[number]
    
    result = []

    while number != 0:
        if number > 8:
            result.append(number_and_arara[8])
            number -= 8

        else:
            result.append(number_and_arara[number])
            number = 0
    
    return ' '.join(result)