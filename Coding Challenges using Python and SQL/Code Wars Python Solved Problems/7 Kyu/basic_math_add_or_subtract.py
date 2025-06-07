# Question: Basic Math (Add or Subtract)
# Categories: 7 Kyu

def calculate(s: str) -> str:    
    numbers = s
    operations = ['plus', 'minus']

    for operation in operations:
        numbers = numbers.replace(operation, ' ')

    numbers = numbers.split()
    available_operations = s
    new_available_operations = ''

    for i in range(len(available_operations)):
        if available_operations[i].isalpha():
            new_available_operations += available_operations[i]

        else:
            new_available_operations += ' '

    available_operations = new_available_operations.split()

    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    
    if available_operations[0] == 'plus':
        result = numbers[0] + numbers[1]
    
    else:
        result = numbers[0] - numbers[1]
    
    numbers = numbers[2:]
    available_operations = available_operations[1:]
    
    while len(numbers) != 0:
        if available_operations[0] == 'plus':
            result = result + numbers[0]
        
        else:
            result = result - numbers[0]
        
        numbers = numbers[1:]
        available_operations = available_operations[1:]

    return str(result)