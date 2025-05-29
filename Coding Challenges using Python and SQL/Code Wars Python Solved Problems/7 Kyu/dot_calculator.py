# Question: Dot Calculator
# Categories: 7 Kyu

def calculator(txt: str) -> str:
    if '+' in txt:
        first_operand = txt.split('+')[0].count('.')
        operator = '+'
        second_operand = txt.split('+')[1].count('.')
    
    elif '-' in txt:
        first_operand = txt.split('-')[0].count('.')
        operator = '-'
        second_operand = txt.split('-')[1].count('.')
    
    elif '*' in txt:
        first_operand = txt.split('*')[0].count('.')
        operator = '*'
        second_operand = txt.split('*')[1].count('.')
        
    else:
        first_operand = txt.split('//')[0].count('.')
        operator = '//'
        second_operand = txt.split('//')[1].count('.')
    
    operator_and_answer = {
        '+': first_operand + second_operand,
        '-': first_operand - second_operand,
        '*': first_operand * second_operand,
        '//': first_operand // second_operand
    }

    return operator_and_answer[operator] * '.'