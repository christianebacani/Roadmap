# Question: Write out expression!
# Categories: 7 Kyu

def expression_out(expression: str) -> str:
    OPERATORS = {
        '+': 'Plus',
        '-': 'Minus',
        '*': 'Times',
        '/': 'Divided By',
        '**': 'To The Power Of',
        '=': 'Equals',
        '!=': 'Does Not Equal'
    }
    NUMBERS = {
        '1': 'One',
        '2': 'Two',
        '3': 'Three',
        '4': 'Four',
        '5': 'Five',
        '6': 'Six',
        '7': 'Seven',
        '8': 'Eight',
        '9': 'Nine',
        '10': 'Ten'
    }
    first_number = expression.split()[0]
    operator = expression.split()[1]
    second_number = expression.split()[2]

    try:
        result = NUMBERS[first_number] + ' ' + OPERATORS[operator] + ' ' + NUMBERS[second_number]
        return result
    
    except KeyError:
        return 'That\'s not an operator!'