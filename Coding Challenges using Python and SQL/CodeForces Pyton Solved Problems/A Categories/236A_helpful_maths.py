# 236A - Helpful Maths

numbers_and_operations = input().strip()

if '+' in numbers_and_operations:
    numbers_and_operations = numbers_and_operations.split('+')
    
    for i in range(len(numbers_and_operations)):
        numbers_and_operations[i] = int(numbers_and_operations[i])
    
    numbers_and_operations = sorted(numbers_and_operations)

    for i in range(len(numbers_and_operations)):
        numbers_and_operations[i] = str(numbers_and_operations[i])
    
    numbers_and_operations = '+'.join(numbers_and_operations)

print(numbers_and_operations)